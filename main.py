from git import Repo
from pathlib import Path
import os

def clone_repo(repo_url, save_path="cloned_repo"):
    if not os.path.exists(save_path):
        print(f"Cloning {repo_url}...")
        Repo.clone_from(repo_url, save_path)
        print("Cloned successfully.")
    else:
        print(f"{save_path} already exists. Skipping clone.")

    return Path(save_path)

def read_python_files(repo_path):
    code_contents = []
    for file_path in repo_path.rglob("*.py"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code_contents.append({
                "file": str(file_path),
                "content": f.read()
            })
    return code_contents

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repo URL: ")
    repo_path = clone_repo(repo_url)
    code_files = read_python_files(repo_path)
    print(f"Found {len(code_files)} Python files.")
    for file in code_files[:3]:
        print(f"\n--- {file['file']} ---\n{file['content'][:300]}...\n")
