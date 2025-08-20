

## 🔹 **1. Docker Basics**

```bash
docker --version
```

```bash
docker info
```
<img width="450" height="206" alt="image" src="https://github.com/user-attachments/assets/c9284cc9-9f5a-4182-ae9c-d473eaafdca2" />


---

## 🔹 **2. Images**

```bash
docker search ubuntu
```
<img width="595" height="331" alt="image" src="https://github.com/user-attachments/assets/170c23fb-1344-4d3f-a61b-420fa74c699f" />

```bash
docker pull ubuntu
```
<img width="568" height="127" alt="image" src="https://github.com/user-attachments/assets/c2bbce0a-bad4-4b08-ae8b-f394e5d74ce4" />

```bash
docker images
```
<img width="426" height="83" alt="image" src="https://github.com/user-attachments/assets/22c38330-6ae8-4618-ac50-8d94049cec04" />

```bash
docker rmi ubuntu
```
<img width="637" height="94" alt="image" src="https://github.com/user-attachments/assets/46e67568-1153-4a99-ac9d-6d76d3d40ed4" />

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


