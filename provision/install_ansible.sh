#!/usr/bin/env bash
set -e

# Add Ansible PPA
sudo apt-get update -y
sudo add-apt-repository --yes --update ppa:ansible/ansible

# Install Ansible
sudo apt-get install -y ansible

# SSH key for Ansible
sudo -u vagrant ssh-keygen -t rsa -b 2048 -N "" -f /home/vagrant/.ssh/id_rsa || true

# Create sample inventory and config
mkdir -p /home/vagrant/ansible

cat <<EOF | sudo tee /home/vagrant/ansible/inventory.ini
[workers]
worker1 ansible_host=172.20.0.11 ansible_user=root
worker2 ansible_host=172.20.0.12 ansible_user=root

[all:vars]
ansible_python_interpreter=/usr/bin/python3
EOF

cat <<EOF | sudo tee /home/vagrant/ansible/ansible.cfg
[defaults]
inventory = ./inventory.ini
remote_user = root
host_key_checking = False
deprecation_warnings = False
interpreter_python = auto_silent

[privilege_escalation]
become = false
EOF

# Fix permissions
sudo chown -R vagrant:vagrant /home/vagrant/ansible
