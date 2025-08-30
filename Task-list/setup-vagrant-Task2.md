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

```bash
mkdir Ubuntu-Linux
```

```bash
cd Ubuntu-Linux
```

<img width="601" height="391" alt="image" src="https://github.com/user-attachments/assets/593ed296-b2e2-436f-bf7b-4c5aede9c617" />

---

### **4. Initialize a Vagrant Box**

* Example: Ubuntu 22.04 LTS

```bash
vagrant init bento/ubuntu-22.04
```
<img width="598" height="381" alt="image" src="https://github.com/user-attachments/assets/4afb302c-266f-4799-a7db-16b0f39815b5" />

This creates a `Vagrantfile` in your folder.


---

### **5. Start the VM**

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
