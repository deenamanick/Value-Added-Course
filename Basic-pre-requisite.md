
## 🖥 **Step-by-Step: Dev Environment Setup for Virtualization & Vagrant**

### **1. Install Visual Studio Code**

* Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
* Install it on your system.
* VS Code will help you edit your `Vagrantfile` and other scripts with syntax highlighting.

---

### **2. Install Git Bash** (Windows Users)

* Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* Install it, and choose **Git Bash** from the terminal options during installation.
* Check installation:

```bash
git --version
```

### **5. Install Terraform (Windows)**

1. Download Terraform from: [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)
2. Extract the downloaded ZIP file.
3. Move the `terraform.exe` file to a folder (e.g., `C:\terraform`).
4. Add that folder to your **PATH**:

   * Press `Win + S`, search for **Environment Variables**, and open it.
   * Edit **System Variables** → Find `Path` → Click **Edit** → Add `C:\terraform`.
5. Verify installation:

```bash
terraform -version
```




