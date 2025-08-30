

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

```bash
docker stop <container_id>
```
<img width="695" height="91" alt="image" src="https://github.com/user-attachments/assets/c629c170-6222-404d-8c57-4bd23ed02061" />

```bash
docker start <container_id>
```
<img width="351" height="33" alt="image" src="https://github.com/user-attachments/assets/c30804b4-1244-4a8d-9453-a8043897a8f1" />

```bash
docker rm <container_id>
```
<img width="333" height="31" alt="image" src="https://github.com/user-attachments/assets/e853dc2d-705b-48e2-8f89-ffe9a1aa2a57" />

---

## 🔹 **4. Inspect & Logs**

```bash
docker logs <container_id>
```
<img width="692" height="177" alt="image" src="https://github.com/user-attachments/assets/fe7fc24f-82b4-4c0b-8a1a-d2247be532a8" />

```bash
docker inspect <container_id>
```
<img width="711" height="158" alt="image" src="https://github.com/user-attachments/assets/619bb752-ae38-4002-a5c1-83d48dafab22" />

---

## 🔹 **5. Cleanup**

```bash
docker container prune
```
<img width="462" height="269" alt="image" src="https://github.com/user-attachments/assets/5c99fa4e-a25c-43fa-bc80-acd62d8f82c7" />


```bash
docker image prune -a
```
<img width="663" height="271" alt="image" src="https://github.com/user-attachments/assets/d58e558f-2923-4223-b8b1-9d4c220d6ef8" />

```bash
docker system prune -a
```
<img width="465" height="190" alt="image" src="https://github.com/user-attachments/assets/89b2262d-26a2-4813-8ee1-9c426f9bf5aa" />

---


