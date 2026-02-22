
## 🖥 **Step-by-Step: Dev Environment Setup for Virtualization & Vagrant**

### **1. Install Visual Studio Code**

* Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
* Install it on your system.
* VS Code will help you edit your `Vagrantfile` and other scripts with syntax highlighting.

  <img width="1188" height="683" alt="image" src="https://github.com/user-attachments/assets/5831f17b-3ce7-40eb-9234-3131df765b01" />


---

### **2. Install Git Bash** (Windows Users)

* Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)
  
<img width="1148" height="660" alt="image" src="https://github.com/user-attachments/assets/651f2e8a-04d8-4bfd-b71a-4c3fca3a51f6" />

* Select visual studio code editor

<img width="612" height="501" alt="image" src="https://github.com/user-attachments/assets/514fa4f7-48f2-4a8e-902a-747526579b53" />


* Install it, and choose **Git Bash** from the terminal options during installation.
* Check installation:

* Uncheck version and select Git Bash

* <img width="596" height="487" alt="image" src="https://github.com/user-attachments/assets/f41b48fe-80af-433e-8462-bbf1475ba330" />


```bash
git --version
```

<img width="1234" height="634" alt="image" src="https://github.com/user-attachments/assets/2d093916-e169-4c01-b882-d31944f3829e" />

---







<img width="734" height="421" alt="image" src="https://github.com/user-attachments/assets/a32595c0-1c3a-4d79-a09c-6cf5c0cbdc19" />

username: jeevi, password: jeevi

This will:

* Enable required features 
* Install **Ubuntu** by default.
* Restart the computer.

---

### ✅ Step 4: Set Up Linux

* After restart, **Ubuntu terminal** will open automatically the first time.
* Students need to:

  * Enter a **username** - jeevi
  * Enter a **password** - jeevi

---

### ✅ Step 5: Update Linux Packages

Inside the Ubuntu terminal, run:

```bash
sudo apt update && sudo apt upgrade -y
```

---

### ✅ Step 6: Accessing Files

* Windows files are available inside Linux at `/mnt/c/` (for C: drive).
* Example: `cd /mnt/c/Users/YourName/Documents`

---

### ✅ Step 7: Recommended Setup

Install basic tools:

```bash
sudo apt install -y git curl wget build-essential
```

---

### 🚀 Usage Tips

* Open WSL by searching **Ubuntu** in the Start menu.









