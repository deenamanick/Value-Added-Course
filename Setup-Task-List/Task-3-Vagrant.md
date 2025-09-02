## 🖥 **Step-by-Step: Vagrant Setup with VirtualBox**



### **1. Install Vagrant**

* Download from: [https://developer.hashicorp.com/vagrant/downloads](https://developer.hashicorp.com/vagrant/downloads)
* select windows and click based on processor type you have.
 For **AMD** choose - **AMD64**  ---
 For **Intel** choose - **I686**

* <img width="598" height="200" alt="image" src="https://github.com/user-attachments/assets/2d958be5-14ad-4355-b0a0-e96c9dbd3265" />

* Install it like any normal app.

* <img width="493" height="388" alt="image" src="https://github.com/user-attachments/assets/fbdd528c-26b7-4603-8686-5277d2e304db" />

**Note** It will ask for reboot. Go ahead and reboot the laptop.

* **Check installation** in terminal or command prompt:


```bash
vagrant --version
```

You should see something like:

```
Vagrant 2.x.x
```
if you dont see the version of vagrant, close gitbash window and try the same command.

<img width="593" height="407" alt="image" src="https://github.com/user-attachments/assets/a41c075b-bc46-4b7f-a822-f2b1f85ca62f" />

<img width="598" height="397" alt="image" src="https://github.com/user-attachments/assets/c6174c9d-f8e5-4576-9c10-2294e05c53dd" />

---

### **3. Create a Project Folder**

Fork the repository

Login to github first. If you dont have the account, create the one by clicking on Sign up Button.

https://github.com/

<img width="985" height="371" alt="image" src="https://github.com/user-attachments/assets/71a4c39a-8c38-40c2-98f9-24755edb4073" />

Next step is 

Fork this repo: 👉 https://github.com/deenamanick/vagrant-ansible-terrafom-docker.git

<img width="1740" height="966" alt="image" src="https://github.com/user-attachments/assets/b56f12fa-57c7-44b9-a673-3854a32bed0a" />

Once the fork is done, go to your github home page, and clone the repo, copy the repo path.

<img width="1558" height="955" alt="image" src="https://github.com/user-attachments/assets/459bbad4-ed76-4099-96da-efba8fc75ea8" />

Open the git Bash and path clone URL, and press enter


<img width="740" height="452" alt="image" src="https://github.com/user-attachments/assets/2e88e6db-0a6d-4016-87c2-fc2800acedc7" />

if it is successfull, you should the screen as below

<img width="751" height="447" alt="image" src="https://github.com/user-attachments/assets/1c51dd6a-a563-4786-8e3c-379e4bebfeb0" />

run the following command in Git Bash

```
cd vagrant-ansible-terrafom-docker/

```

You should see this folder structure

<img width="707" height="107" alt="image" src="https://github.com/user-attachments/assets/19353b39-c70e-4c06-9ee6-1888e3c4e619" />


---

### *4. Start the VM**

```bash
vagrant up
```

* Vagrant will:

  * Download the **box** (pre-built VM image) from HashiCorp.
  * Create and start it in VirtualBox automatically.
 
    <img width="1044" height="576" alt="image" src="https://github.com/user-attachments/assets/18231479-d127-49a1-b3b2-c840a4140444" />


---

### **6. Connect to the VM**

```bash
vagrant ssh
```
<img width="585" height="396" alt="image" src="https://github.com/user-attachments/assets/9db4e839-5c82-4828-bac5-9d5261a0e6eb" />


* You’re now **inside** the VM’s terminal.
* Run:

```bash
lsb_release -a
```
<img width="823" height="596" alt="image" src="https://github.com/user-attachments/assets/4d9a2c02-df3e-473c-a5cc-3e0adceb9241" />

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


---
