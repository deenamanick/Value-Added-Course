
## 🖥 **Setting up VirtualBox – Demo Steps**

### **1. Download and Install VirtualBox**

* Go to: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
* Choose your operating system (Windows, macOS, or Linux).
* Download and install VirtualBox using the installer.

---

#### Click on Windows Hosts

<img width="1765" height="908" alt="image" src="https://github.com/user-attachments/assets/79029a59-0303-46c2-98c7-e49a0e27597a" />

After the download is complete, go to the downloaded folder, then click and start the installation.

#### Note

The installer for VirtualBox 7.0.10 will likely not proceed until it detects that the Microsoft Visual C++ 2019 Redistributable is installed.

To fix this, you need to:

**Download** : Get the redistributable package directly from the official Microsoft website. https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

<img width="910" height="518" alt="image" src="https://github.com/user-attachments/assets/2be31d56-3305-4919-9428-cbc20e63e6fd" />


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
