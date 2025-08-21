Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-22.04"
  config.vm.hostname = "devops-lab"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.network "forwarded_port", guest: 5000, host: 5000, auto_correct: true

    # Sync Terraform project & app code
  config.vm.synced_folder "./terraform-docker", "/home/vagrant/terraform-docker"
  config.vm.synced_folder "./k8s-quiz", "/home/vagrant/terraform-docker/k8s-quiz"

  # Provisioners
  config.vm.provision "shell", path: "provision/install_docker.sh"
  config.vm.provision "shell", path: "provision/install_ansible.sh"
  config.vm.provision "shell", path: "provision/install_terraform.sh"
end
