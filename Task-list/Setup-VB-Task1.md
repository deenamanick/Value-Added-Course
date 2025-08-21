
## 🖥 **Setting up VirtualBox – Demo Steps**

### **1. Download and Install VirtualBox**

* Go to: https://download.virtualbox.org/virtualbox/7.1.0/
* Choose your operating system (Windows, macOS, or Linux).
* Download and install VirtualBox using the installer.

---

#### Click on Windows Hosts

<img width="1212" height="624" alt="image" src="https://github.com/user-attachments/assets/e44e2a83-d767-4ec0-8af0-f70b611d02cc" />



After the download is complete, go to the downloaded folder, then click and start the installation.

<img width="503" height="395" alt="image" src="https://github.com/user-attachments/assets/a99dc0e6-15da-4a8c-87bc-c5976a3eb967" />


#### Note

The installer for VirtualBox 7.0.10 will likely not proceed until it detects that the Microsoft Visual C++ 2019 Redistributable is installed.

To fix this, you need to:

**Download** : Get the redistributable package directly from the official Microsoft website. https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

<img width="935" height="162" alt="image" src="https://github.com/user-attachments/assets/48260091-02f9-4a84-af47-1e96e5f315f6" />


**Install** : Run the installer.

**Rerun**: Start the VirtualBox installation again. It should now proceed without the error.

**Reboot**

 Complete the installation. If a restart is required, please reboot your computer before launching VirtualBox. This is necessary to finalize the installation of the new system drivers.

**Enable Virtualization**

The specific name for the virtualization option can vary depending on the motherboard manufacturer and CPU brand, but here are the most common names you'll find in the BIOS/UEFI settings:

* **For Intel CPUs:**
    * **Intel Virtualization Technology**
    * **Intel VT-x**
    * **Virtualization Technology (VTx)**
* **For AMD CPUs:**
    * **SVM Mode** (Secure Virtual Machine Mode)
    * **AMD-V**
    * **Virtualization**
 
 <img width="541" height="245" alt="image" src="https://github.com/user-attachments/assets/e1748e41-658c-46df-a720-cf7f2815e09b" />


### How to Find and Enable the Option

1.  **Enter the BIOS/UEFI:** Restart your computer and press the designated key (commonly F2, F10, F12, or Del) to enter the BIOS or UEFI setup.
2.  **Locate the Setting:** Navigate to the **Advanced**, **CPU Configuration**, or a similar-sounding menu.
3.  **Enable:** Find the setting with one of the names listed above and change its value from `Disabled` to `Enabled`.
4.  **Save and Exit:** Save your changes and exit the BIOS/UEFI. The computer will restart, and the feature will be active.
