## 🔹 **1. Docker Basics**

Open git Bash from Search Window

<img width="1155" height="977" alt="image" src="https://github.com/user-attachments/assets/fed9149d-1331-4d3e-89bb-a09e18243166" />

Change the directory to 

demo changes
sdfd

```
cd vagrant-ansible-terrafom-docker
```
Run Vagrant Up

```
vagrant provision --provision-with docker

```
ssh to Vagrant

```
vagrant ssh

```

## Check docker version

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
<img width="567" height="105" alt="image" src="https://github.com/user-attachments/assets/da4ce395-98cc-4d60-bca0-3bad29d9de41" />

```bash
docker run -d --name mynginx nginx
```
<img width="417" height="64" alt="image" src="https://github.com/user-attachments/assets/788ba84e-36d9-4ca9-8554-745c84bfe266" />

```bash
docker ps
```
<img width="760" height="86" alt="image" src="https://github.com/user-attachments/assets/534b6519-f2b7-4459-8096-66893c05c943" />

```bash
docker ps -a
```
<img width="899" height="138" alt="image" src="https://github.com/user-attachments/assets/c7a30ad7-2047-43a8-bba3-74a0ef1cd50c" />

--

### ➕ Additional Tasks (Easy, hands-on)

1) Inspect a container  
- Goal: see how Docker describes a running container.  
```bash
docker ps            # get CONTAINER ID
docker inspect <CONTAINER_ID>
```
- Expected: JSON output with network, mounts, and config. Time: 3 min

2) Stop, start, and remove a container  
- Goal: practice lifecycle commands.  
```bash
docker stop mynginx
docker start mynginx
docker rm -f mynginx
```
- Expected: container stops, restarts, then removed. Time: 4 min

3) Expose a container port and test with curl  
- Goal: run nginx on host port and verify HTTP response.  
```bash
docker run -d --name web -p 8080:80 nginx
curl -I http://localhost:8080
```
- Expected: HTTP 200/302 headers returned. Time: 5 min

4) Use a bind mount to edit files from host  
- Goal: mount a host folder into a container for live edits.  
```bash
mkdir -p ~/docker-demo/www
echo "Hello from host" > ~/docker-demo/www/index.html
docker run -d --name web-dev -p 8081:80 -v ~/docker-demo/www:/usr/share/nginx/html:ro nginx
# open http://localhost:8081
```
- Expected: page served from host file. Time: 8 min

5) Build a simple image from a Dockerfile  
- Goal: learn Dockerfile -> build -> run.  
```bash
cat > ./Dockerfile <<'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python","-m","http.server","5000"]
EOF
docker build -t student-http .
docker run -d -p 5000:5000 student-http
```
- Expected: simple HTTP server reachable at localhost:5000. Time: 12–15 min

---

### 🎯 Challenge Tasks (Apply what you learned)

Challenge A — Compose a web + Redis stack (15–25 min)  
- Goal: use docker-compose to run two services together.  
- Task: create docker-compose.yml to run nginx (or simple web app) and redis, then start and check both services.  
- Example:
```yaml
version: '3.8'
services:
  web:
    image: nginx
    ports: ["8080:80"]
  redis:
    image: redis:alpine
```
- Commands:
```bash
docker-compose up -d
docker-compose ps
docker-compose logs web
```
- Expected: both services running and reachable. Hint: use docker-compose down to stop.

Challenge B — Build, tag, and run a custom image (20–30 min)  
- Goal: create a tiny app image, tag it, and run with a volume.  
- Task: write a Dockerfile for a static site or small Python app, build it, tag as local: student-app, and run with mounted config.  
- Hints:
```bash
docker build -t student-app .
docker tag student-app student-app:lab1
docker run -d --name student-app -p 9000:5000 student-app
```
- Expected: app serves content; inspect with docker logs and docker exec.

Challenge C — Troubleshoot & fix a broken image (20–30 min)  
- Goal: use logs, inspect, and history to find and fix an image that fails to start.  
- Task: run a deliberately broken container (wrong CMD), inspect logs, fix Dockerfile, rebuild, and confirm it runs.  
- Hints:
```bash
docker run --name broken sample-image
docker logs broken
docker inspect broken
docker history sample-image
# edit Dockerfile, rebuild, retest
```
- Expected: student identifies error from logs, updates Dockerfile, and gets container running.



