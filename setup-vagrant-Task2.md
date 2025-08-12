## 🖥 **Step-by-Step: Vagrant Setup with VirtualBox**



### **1. Install Vagrant**

* Download from: [https://developer.hashicorp.com/vagrant/downloads](https://developer.hashicorp.com/vagrant/downloads)
* Install it like any normal app.
* **Check installation** in terminal or command prompt:

```bash
vagrant --version
```

You should see something like:

```
Vagrant 2.x.x
```

---

### **3. Create a Project Folder**

```bash
mkdir vagrant_demo
cd vagrant_demo
```

---

### **4. Initialize a Vagrant Box**

* Example: Ubuntu 22.04 LTS

```bash
vagrant init ubuntu/jammy64
```

This creates a `Vagrantfile` in your folder.

---

### **5. Start the VM**

```bash
vagrant up
```

* Vagrant will:

  * Download the **box** (pre-built VM image) from HashiCorp.
  * Create and start it in VirtualBox automatically.

---

### **6. Connect to the VM**

```bash
vagrant ssh
```

* You’re now **inside** the VM’s terminal.
* Run:

```bash
lsb_release -a
```

to confirm the OS version.

---

### **7. Exit the VM**

```bash
exit
```

---

### **8. Stop or Destroy the VM**

* Stop the VM (saves state):

```bash
vagrant halt
```

* Destroy the VM (remove completely):

```bash
vagrant destroy
```

---

### **Extra Tip for Class Demo**

* Use `ubuntu/focal64` (Ubuntu 20.04) or `centos/8` for variety.
* Edit `Vagrantfile` to change RAM, CPUs:

```ruby
config.vm.provider "virtualbox" do |vb|
  vb.memory = "2048"
  vb.cpus = 2
end
```

---

If you want, I can prepare a **ready-to-use Vagrantfile** with:

* **Ubuntu 22.04**
* Pre-installed tools (Git, Curl, Docker)
* 2GB RAM, 2 CPUs

That way your students can run `vagrant up` and have a full environment instantly.
Do you want me to create that?
