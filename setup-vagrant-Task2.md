## 🖥 **Step-by-Step: Vagrant Setup with VirtualBox**



### **1. Install Vagrant**

* Download from: [https://developer.hashicorp.com/vagrant/downloads](https://developer.hashicorp.com/vagrant/downloads)
* select windows and click on AMD64


* <img width="598" height="200" alt="image" src="https://github.com/user-attachments/assets/2d958be5-14ad-4355-b0a0-e96c9dbd3265" />
* Install it like any normal app.

* <img width="493" height="388" alt="image" src="https://github.com/user-attachments/assets/fbdd528c-26b7-4603-8686-5277d2e304db" />

* **Check installation** in terminal or command prompt:


```bash
vagrant --version
```

You should see something like:

```
Vagrant 2.x.x
```

---

### **3. Create a Project Folder**

```bash
mkdir vagrant_demo
cd vagrant_demo
```

---

### **4. Initialize a Vagrant Box**

* Example: Ubuntu 22.04 LTS

```bash
vagrant init bento/ubuntu-22.04
```

This creates a `Vagrantfile` in your folder.

---

### **5. Start the VM**

```bash
vagrant up
```

* Vagrant will:

  * Download the **box** (pre-built VM image) from HashiCorp.
  * Create and start it in VirtualBox automatically.

---

### **6. Connect to the VM**

```bash
vagrant ssh
```

* You’re now **inside** the VM’s terminal.
* Run:

```bash
lsb_release -a
```

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

* Destroy the VM (remove completely):

```bash
vagrant destroy
```

---
