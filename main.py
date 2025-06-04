from git import Repo
from pathlib import Path
from splitter import chunk_code
from vector_store import create_documents_from_chunks, store_in_vector_db
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
    print(f"\nFound {len(code_files)} Python files.")

    code_chunks = chunk_code(code_files)
    print(f"\nTotal chunks created: {len(code_chunks)}")

    # Convert your code chunks to documents
    docs = create_documents_from_chunks(code_chunks)

    # Store documents in local vector DB
    store_in_vector_db(docs)

    # Preview original files
    for file in code_files[:3]:
        print(f"\n--- {file['file']} ---\n{file['content'][:300]}...\n")

    # Preview chunked content
    for chunk in code_chunks[:3]:
        file_name = chunk['file'].split('/')[-1].split('\\')[-1]
        print(f"\n--- {chunk['chunk_id']} from {file_name} ---\n{chunk['content'][:300]}...\n")
