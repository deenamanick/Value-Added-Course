## 🔹 **1. Docker Basics**

```bash
docker --version       # Check Docker version
docker info            # Get system info
```

---

## 🔹 **2. Images**

```bash
docker search ubuntu   # Search image on Docker Hub
docker pull ubuntu     # Download an image
docker images          # List images
docker rmi ubuntu      # Remove image
```

---

## 🔹 **3. Containers**

```bash
docker run -it ubuntu /bin/bash   # Run container interactively
docker run -d --name mynginx nginx  # Run container in background

docker ps              # List running containers
docker ps -a           # List all containers
docker stop <id>       # Stop a container
docker start <id>      # Start a stopped container
docker rm <id>         # Remove a container
```

---

## 🔹 **4. Inspect & Logs**

```bash
docker logs <id>       # Show logs
docker inspect <id>    # Inspect details
```

---

## 🔹 **5. Cleanup**

```bash
docker container prune # Remove stopped containers
docker image prune -a  # Remove unused images
docker system prune -a # Clean everything unused
```
