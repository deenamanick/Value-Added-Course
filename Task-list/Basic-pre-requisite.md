
## 🖥 **Step-by-Step: Dev Environment Setup for Virtualization & Vagrant**

### **1. Install Visual Studio Code**

* Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
* Install it on your system.
* VS Code will help you edit your `Vagrantfile` and other scripts with syntax highlighting.

  <img width="1188" height="683" alt="image" src="https://github.com/user-attachments/assets/5831f17b-3ce7-40eb-9234-3131df765b01" />


---

### **2. Install Git Bash** (Windows Users)

* Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)
* Install it, and choose **Git Bash** from the terminal options during installation.
* Check installation:

```bash
git --version
```

<img width="1234" height="634" alt="image" src="https://github.com/user-attachments/assets/2d093916-e169-4c01-b882-d31944f3829e" />


### **5. Install Terraform (Windows)**

1. Download Terraform from: [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)

   <img width="616" height="242" alt="image" src="https://github.com/user-attachments/assets/3cf5684d-2050-4746-b4f7-fc4a1e108c20" />

2. Extract the downloaded ZIP file.
3. Move the `terraform.exe` file to a folder (e.g., `C:\terraform`).
4. Add that folder to your **PATH**:

   * Press `Win + R`, and type **sysdm.cpl**, and look for **Advanced setting**, click **Environment Variable**. or search for **Environment Variables** in windows search, and open it.
   * 
    <img width="398" height="201" alt="image" src="https://github.com/user-attachments/assets/373df2c8-cd37-4fdc-9cb4-5d9b08f0ffd9" />

   <img width="413" height="464" alt="image" src="https://github.com/user-attachments/assets/b1bb21a4-1de1-4876-ad90-7ce6af278465" />
  * 
   * Edit **System Variables** → Find `Path` → Click **Edit** → Add `C:\terraform`.
6. Verify installation:

```bash
terraform -version
```




