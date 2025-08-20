

## 🔹 **1. Docker Basics**

```bash
docker --version
```

```bash
docker info
```

---

## 🔹 **2. Images**

```bash
docker search ubuntu
```

```bash
docker pull ubuntu
```

```bash
docker images
```

```bash
docker rmi ubuntu
```

---

## 🔹 **3. Containers**

```bash
docker run -it ubuntu /bin/bash
```

```bash
docker run -d --name mynginx nginx
```

```bash
docker ps
```

```bash
docker ps -a
```

```bash
docker stop <container_id>
```

```bash
docker start <container_id>
```

```bash
docker rm <container_id>
```

---

## 🔹 **4. Inspect & Logs**

```bash
docker logs <container_id>
```

```bash
docker inspect <container_id>
```

---

## 🔹 **5. Cleanup**

```bash
docker container prune
```

```bash
docker image prune -a
```

```bash
docker system prune -a
```

---


