"""
copy_local_to_github.py

This script copies files from a local folder to a cloned GitHub repository,
then commits and pushes the changes.

Prerequisites:
1) Git installed and authenticated (SSH or token already set up)
2) Repository already cloned locally
3) Python 3.x

Usage:
- Update the CONFIG section
- Run: python copy_local_to_github.py
"""

import shutil
import os
from git import Repo

# ========== CONFIG ==========
LOCAL_SOURCE_DIR = r"D:\\local_files"     # Folder to copy FROM
GITHUB_REPO_DIR = r"D:\\github_repo"      # Local cloned repo path
COMMIT_MESSAGE = "Copied files from local folder"
# ============================

def copy_files(src_dir, dst_dir):
    for item in os.listdir(src_dir):
        src = os.path.join(src_dir, item)
        dst = os.path.join(dst_dir, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

def git_push(repo_dir, message):
    repo = Repo(repo_dir)
    repo.git.add(all=True)
    repo.index.commit(message)
    repo.remote(name="origin").push()

if __name__ == "__main__":
    copy_files(LOCAL_SOURCE_DIR, GITHUB_REPO_DIR)
    print("Files copied successfully")

    git_push(GITHUB_REPO_DIR, COMMIT_MESSAGE)
    print("Changes committed and pushed to GitHub")

git commit -m "Removed copy_local_to_github.py script"


import tarfile

with tarfile.open("backup.tar", "w") as tar:
    tar.add("file1.txt")

print("Tar file created")





