from git import Repo
from pathlib import Path
import os
import shutil

def clone_repo(repo_url, save_path="cloned_repo"):
    if os.path.exists(save_path):
      print(f"Removing old {save_path} folder...")
      try:
          shutil.rmtree(save_path)
      except Exception as e:
          print(f"❌ Failed to remove folder: {e}")
          exit(1)
    print(f"Cloning {repo_url}...")
    Repo.clone_from(repo_url, save_path)
    print("✅ Cloned Successfully")
    return Path(save_path)
    
    

def read_python_files(repo_path):
    code_contents = []
    for file_path in repo_path.rglob("*.py"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
            code_contents.append((str(file_path), code))
    return code_contents

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repo URL: ")
    repo_path = clone_repo(repo_url)
    code_files = read_python_files(repo_path)
    print(f"Found {len(code_files)} Python files.")
    for path, content in code_files[:3]:  # Show first 3 files for preview
        print(f"\n--- {path} ---\n{content[:300]}...\n")
