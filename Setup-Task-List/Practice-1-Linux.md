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

### ➕ Additional Exercises (Simple & Fast)

These short tasks reinforce basics — each one takes ~3–10 minutes.

1) Quick create & list  
- Goal: make folder and file, check it exists.  
```bash
mkdir -p ~/lab/projects
cd ~/lab/projects
touch notes.txt
ls -la
```

2) Write and read text  
- Goal: add text and view it.  
```bash
echo "Hello Linux" > notes.txt
cat notes.txt
```

3) Move, copy, delete  
- Goal: practice mv, cp, rm.  
```bash
mkdir backup
cp notes.txt backup/
mv backup/notes.txt backup/final.txt
rm backup/final.txt
```

4) Permissions & symlink (safe demo)  
- Goal: see file permissions and create a link.  
```bash
chmod 644 notes.txt
ln -s notes.txt notes-link.txt
ls -l
```

5) Find and search text  
- Goal: locate files and search inside them.  
```bash
find . -name "*.txt"
grep -n "Hello" -R .
```

6) Small script (automation)  
- Goal: create a runnable script that shows date and free space.  
```bash
cat > ~/lab/report.sh <<'EOF'
#!/bin/bash
date
df -h ~
EOF
chmod +x ~/lab/report.sh
~/lab/report.sh
```

7) Networking check (basic)  
- Goal: display interfaces and test connectivity.  
```bash
ip a
ping -c 3 8.8.8.8
```

---

### 🏁 Challenges for Students

Each challenge has a clear goal, a few hints/commands, and an estimated time. Encourage students to try without looking at hints first.

1) Beginner — "My Notes Organizer" (10–15 min)  
- Goal: create a folder structure and move files into categories.  
- Task: create ~/lab/notes with subfolders work, personal; create three text files and move them into correct folders.  
- Hints:
  ```bash
  mkdir -p ~/lab/notes/{work,personal}
  touch ~/lab/notes/work/task1.txt ~/lab/notes/personal/todo.txt
  mv ~/lab/notes/*.txt ~/lab/notes/work/   # example move
  ls -R ~/lab/notes
  ```
- Expected: two subfolders with files inside.

2) Beginner — "Quick Search" (10 min)  
- Goal: find where a word appears in your notes.  
- Task: add different lines to files, then find the word "TODO" across the directory.  
- Hint:
  ```bash
  grep -n "TODO" -R ~/lab/notes
  ```
- Expected: paths and line numbers where "TODO" appears.

3) Intermediate — "Permission Fixer" (15 min)  
- Goal: learn chmod and who can access files.  
- Task: create a script that sets files in ~/lab/notes to 640 and makes a public copy with 644.  
- Hints:
  ```bash
  chmod 640 ~/lab/notes/work/*.txt
  cp ~/lab/notes/work/task1.txt ~/lab/notes/public_task.txt
  chmod 644 ~/lab/notes/public_task.txt
  ls -l ~/lab/notes
  ```
- Expected: correct permission bits shown by ls -l.

4) Intermediate — "Simple Backup Script" (20–30 min)  
- Goal: write a small bash script that tars a directory with a timestamp and keeps only the last 3 backups.  
- Task: script should create /tmp/lab-backups and rotate backups.  
- Hints:
  - Use date +"%Y%m%d-%H%M" for timestamp.  
  - Use ls -1t and tail to remove old files.  
- Example steps:
  ```bash
  mkdir -p /tmp/lab-backups
  # create script ~/lab/backup.sh that creates a tar and prunes older than 3
  chmod +x ~/lab/backup.sh
  ~/lab/backup.sh
  ls -l /tmp/lab-backups
  ```
- Expected: backup files present and limited to 3.

5) Intermediate — "Process Watcher" (15 min)  
- Goal: practice ps, grep, and kill (safe demo).  
- Task: start a background sleep process, find it, and stop it.  
- Hints:
  ```bash
  sleep 300 &    # starts background job
  ps aux | grep sleep
  kill <PID>
  ```
- Expected: process appears then stops after kill.

6) Advanced — "Find & Replace" (20–30 min)  
- Goal: use find + sed to replace a string in multiple files.  
- Task: change the word "Hello" to "Hi" in all .txt files under ~/lab. Test on copies first.  
- Hints:
  ```bash
  find ~/lab -type f -name "*.txt" -exec sed -i.bak 's/Hello/Hi/g' {} +
  ```
- Expected: .txt files updated and .bak backups created.

7) Advanced — "Network Troubleshoot Mini-Lab" (20–30 min)  
- Goal: combine ip, ss, ping and traceroute to inspect connectivity.  
- Task: check your VM/network interface, list listening ports, ping google DNS, traceroute to example.com.  
- Hints:
  ```bash
  ip a
  ss -tuln
  ping -c 3 8.8.8.8
  traceroute example.com   # may need sudo or install traceroute
  ```
- Expected: students can read outputs and explain any failures.

8) Creative Bonus — "Small Utility" (30–40 min)  
- Goal: make a small tool that counts lines in .txt files and prints the top 3 largest files.  
- Task: write a script ~/lab/top_files.sh that prints "filename — lines".  
- Hints:
  ```bash
  find ~/lab -type f -name "*.txt" -exec wc -l {} + | sort -nr | head -n 3
  ```
- Expected: script prints top 3 by line count.

---

Tips for instructors:
- Ask students to describe what each command does before running it.  
- Encourage using --help and man pages (e.g., man grep).  
- Use small checkpoints: run one command, verify output, then proceed.

---


