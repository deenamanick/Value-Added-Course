

---

## 🧪 **Linux Hands-On Exercise for Students**

### 🔹 **Step-by-Step Task Flow**

---

### ✅ **Step 1: Open the Terminal**

No command needed — just open your terminal emulator (e.g., GNOME Terminal, Konsole, or terminal in your VM).

---

### ✅ **Step 2: Create a New Directory**

```bash
mkdir my_practice
```

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

Moves `notes.txt` into the `projects` folder.

---

### ✅ **Step 7: Navigate to the Subdirectory**

```bash
cd projects
```

---

### ✅ **Step 8: Add Text to the File**

```bash
echo "This is my first Linux file." > notes.txt
```

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

