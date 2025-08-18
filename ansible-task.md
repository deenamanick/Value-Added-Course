
# Setting up Ansible Lab with Vagrant, Docker & Ubuntu Workers

## 1. 📌 Prerequisites

Before starting, make sure you have the following installed on your **host machine** (Windows / macOS / Linux):

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (latest stable version)
* [Vagrant](https://developer.hashicorp.com/vagrant/downloads)
* (Optional but useful) [Git](https://git-scm.com/downloads)

This has already been covered in basic-pre-requisite.

---

Verify installation:

```bash
vagrant --version
virtualbox --help | head -n 1
```

---

## 2. 📂 Create Project Directory

Create a folder for the lab environment:

```bash
mkdir ansible-lab
cd ansible-lab
```

---

## 3. 📄 Create the Vagrantfile

Inside the `ansible-lab` folder, create a file named **`Vagrantfile`** with the following content:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"
  config.vm.hostname = "ansible-lab"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.network "forwarded_port", guest: 80, host: 8081, auto_correct: true

  # Disable default synced folder
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provision "shell", inline: <<-SHELL
    # Update base system
    apt-get update -y
    apt-get install -y python3-pip curl gnupg lsb-release apt-transport-https ca-certificates software-properties-common

    # Install Docker
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
      > /etc/apt/sources.list.d/docker.list
    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io
    systemctl enable docker
    systemctl start docker
    usermod -aG docker vagrant

    # Install Ansible
    add-apt-repository --yes --update ppa:ansible/ansible
    apt-get install -y ansible

    # SSH key for Ansible
    sudo -u vagrant ssh-keygen -t rsa -b 2048 -N "" -f /home/vagrant/.ssh/id_rsa || true

    # Setup Docker workers
    docker network create --subnet=172.20.0.0/24 ansible-net || true
    docker pull ubuntu:22.04
    for i in 1 2; do
      cname="worker$i"
      cip="172.20.0.1$i"
      docker rm -f $cname || true
      docker run -d --name $cname --hostname $cname \
        --net ansible-net --ip $cip \
        --privileged ubuntu:22.04 sleep infinity
      docker exec $cname apt-get update
      docker exec $cname apt-get install -y openssh-server python3 sudo
      docker exec $cname mkdir -p /var/run/sshd /root/.ssh
      docker exec $cname bash -c "echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config"
      docker exec $cname service ssh start
      pubkey=$(cat /home/vagrant/.ssh/id_rsa.pub)
      docker exec $cname bash -c "echo '${pubkey}' >> /root/.ssh/authorized_keys"
    done

    # Create Ansible inventory + config
    mkdir -p /home/vagrant/ansible
    cat <<EOF > /home/vagrant/ansible/inventory.ini
[workers]
worker1 ansible_host=172.20.0.11 ansible_user=root
worker2 ansible_host=172.20.0.12 ansible_user=root

[all:vars]
ansible_python_interpreter=/usr/bin/python3
EOF

    cat <<EOF > /home/vagrant/ansible/ansible.cfg
[defaults]
inventory = ./inventory.ini
remote_user = root
host_key_checking = False
deprecation_warnings = False
interpreter_python = auto_silent

[privilege_escalation]
become = false
EOF

    # ---------------------------
    # Drop Lab Exercises
    # ---------------------------
    # Task 1 - Install Apache
    cat <<EOF > /home/vagrant/ansible/install_apache.yml
---
- name: Install Apache on workers
  hosts: workers
  become: yes
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
    - name: Install Apache2
      apt:
        name: apache2
        state: present
    - name: Ensure Apache is running
      service:
        name: apache2
        state: started
        enabled: yes
EOF

    # Task 2 - Create user
    cat <<EOF > /home/vagrant/ansible/user_add.yml
---
- name: Create DevOps user
  hosts: workers
  become: yes
  tasks:
    - name: Ensure user 'devops' exists
      user:
        name: devops
        shell: /bin/bash
        groups: sudo
        state: present
EOF

    # Task 3 - Copy index.html
    cat <<EOF > /home/vagrant/ansible/copy_index.yml
---
- name: Deploy custom index.html
  hosts: workers
  become: yes
  tasks:
    - name: Place index.html
      copy:
        dest: /var/www/html/index.html
        content: |
          <h1>Welcome to Ansible Lab</h1>
          <p>Deployed by Ansible on {{ inventory_hostname }}</p>
EOF

    # Task 4 - Stop Apache
    cat <<EOF > /home/vagrant/ansible/stop_apache.yml
---
- name: Stop Apache on workers
  hosts: workers
  become: yes
  tasks:
    - name: Stop Apache
      service:
        name: apache2
        state: stopped
EOF

    # Fix permissions
    chown -R vagrant:vagrant /home/vagrant/ansible
  SHELL
end

```

---

## 4. ▶ Start the Lab VM

Run:

```bash
vagrant up
```

This will:

* Create the **Ansible controller VM**
* Install Docker + Ansible inside it
* Launch **2 worker containers (worker1 & worker2)**
* Configure SSH keys and inventory

---

## 5. 🔑 Access the Controller VM

SSH into the VM:

```bash
vagrant ssh
```

---

## 6. ✅ Test Ansible Connectivity

Inside the VM, run:

```bash
cd ~/ansible
ansible all -m ping
```

Expected output:

```
worker1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
worker2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---


