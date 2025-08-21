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


chown -R vagrant:vagrant /home/vagrant/terraform-docker