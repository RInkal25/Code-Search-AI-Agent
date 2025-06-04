from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_code(code_files, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    all_chunks = []
    for file in code_files:
        file_path = file["file"]
        file_name = file_path.split("/")[-1].split("\\")[-1].replace(".py", "")  # Extract file name only (no path or extension)

        chunks = splitter.split_text(file["content"])

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "file": file_path,
                "chunk_id": f"{file_name}_{i}",
                "content": chunk
            })

        print(f"✅ Chunked {file_path} into {len(chunks)} chunks")

    return all_chunks
