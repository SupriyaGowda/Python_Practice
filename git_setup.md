🚀 COMPLETE FLOW: Local Project ➜ GitHub
🟢 PART 1 — One Time Setup (Only Once Per System)
✅ 1️⃣ Install Git

Check:

git --version

✅ 2️⃣ Configure Git (Very Important — Only Once)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"


Check configuration:

git config --list

🟢 PART 2 — Upload New Local Project to GitHub
✅ Step 1 — Keep Project Outside OneDrive

Example:

C:\Projects\Python_Practice


Avoid:

OneDrive

✅ Step 2 — Open Folder in VS Code

File → Open Folder → Select your project folder

✅ Step 3 — Initialize Git

Inside terminal:

git init


Check:

dir /a


You must see:

.git

✅ Step 4 — Add All Files
git add .

✅ Step 5 — Commit Files
git commit -m "Initial commit"

✅ Step 6 — Create Repository on GitHub

Go to GitHub

Click ➕ → New repository

Name it

⚠️ IMPORTANT: DO NOT tick "Add README"

Click Create

✅ Step 7 — Connect Local to GitHub

Copy repo URL from GitHub.

Then run:

git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git branch -M main
git push -u origin main

🟢 PART 3 — If You Get “remote contains work” Error

Run:

git pull origin main --allow-unrelated-histories
git push

🟢 PART 4 — Normal Daily Workflow (After Setup)

Whenever you modify code:

git add .
git commit -m "Describe your change"
git push


That’s it ✅

🟢 PART 5 — Clone Repo to Another System

If you want to download from GitHub:

git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

🟢 PART 6 — Common Problems & Quick Fix
Problem	Fix
not a git repository	Run git init
pip not recognized	Use python -m pip
jupyter not recognized	Use python -m notebook
remote rejected	Run git pull first
>> in terminal	Press Ctrl + C
🧠 Simple Memory Formula
First Time:
init → add → commit → remote add → push

Daily:
add → commit → push

🎯 Bonus Professional Tip

Before pushing, check status:

git status


See commit history:

git log


See remote link:

git remote -v

💎 You Now Know

✔ Git setup
✔ Local to GitHub flow
✔ Clone flow
✔ Error handling
✔ Daily workflow
