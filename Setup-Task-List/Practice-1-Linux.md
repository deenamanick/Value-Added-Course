

---

## 🧪 **Linux Hands-On Exercise**

### 🔹 **Step-by-Step Task Flow**

---

### ✅ **Step 1: Open the Terminal**

Open the GitBash from search window

<img width="1155" height="977" alt="image" src="https://github.com/user-attachments/assets/0e0040c7-e159-4019-9fe6-6967611d1fbd" />



---

### ✅ **Step 2: Create a New Directory**

```bash
mkdir my_practice
```
<img width="595" height="400" alt="image" src="https://github.com/user-attachments/assets/e213684e-3f6e-4350-83a4-ebf9d09ef2e3" />


This creates a folder named `my_practice`.

---

### ✅ **Step 3: Move Into the Directory**

```bash
cd my_practice
```

You're now inside the `my_practice` folder.

---

### ✅ **Step 4: Create a New File**

```bash
touch notes.txt
```

<img width="588" height="390" alt="image" src="https://github.com/user-attachments/assets/5edcff22-7376-490c-9659-f9f1c1f76b17" />


This creates an empty file called `notes.txt`.

---

### ✅ **Step 5: Create a Subdirectory**

```bash
mkdir projects
```

Creates a new folder named `projects` inside `my_practice`.

---

### ✅ **Step 6: Move the File into the Subdirectory**

```bash
mv notes.txt projects/
```
<img width="604" height="374" alt="image" src="https://github.com/user-attachments/assets/58e4271e-7807-4ae5-ad64-698eacca4263" />


Moves `notes.txt` into the `projects` folder.

---

### ✅ **Step 7: Navigate to the Subdirectory**

```bash
cd projects
```
<img width="601" height="383" alt="image" src="https://github.com/user-attachments/assets/29bdb65c-e2f8-46d8-ae11-f10b777c0ad7" />


---

### ✅ **Step 8: Add Text to the File**

```bash
echo "This is my first Linux file." > notes.txt
```
<img width="614" height="96" alt="image" src="https://github.com/user-attachments/assets/b4666fdf-2603-49aa-896c-d5c9912d2813" />

Adds content to the file.

---

### ✅ **Step 9: View the File Content**

```bash
cat notes.txt
```

---

### ✅ **Step 10: Copy the File**

```bash
cp notes.txt backup.txt
```

Creates a copy named `backup.txt`.

---

### ✅ **Step 11: Rename the File**

```bash
mv backup.txt final_notes.txt
```

---

### ✅ **Step 12: Delete One File**

```bash
rm final_notes.txt
```

---

### ✅ **Step 13: Go Back to Parent Directory**

```bash
cd ..
```

---

### ✅ **Step 14: Remove Entire Subdirectory**

```bash
rm -r projects
```

---

### ✅ **Step 15: Exit the Terminal**

```bash
exit
```

---

### 🎓 **Optional Challenge for Students**

* Create 3 text files with different content.
* Move them into separate folders.
* Display file content using `cat`, `less`
* Delete only the second file using `rm`.

---

