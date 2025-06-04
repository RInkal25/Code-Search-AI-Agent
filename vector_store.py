# vector_store.py

import os
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from dotenv import load_dotenv

embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# Load your OpenAI key from .env
load_dotenv()

def create_documents_from_chunks(chunks):
    """
    Converts a list of chunks into LangChain Document objects.
    Each document contains content and metadata (file name, chunk ID).
    """
    docs = []
    for chunk in chunks:
        docs.append(Document(
            page_content=chunk["content"],
            metadata={
                "file": chunk["file"],
                "chunk_id": chunk["chunk_id"]
            }
        ))
    return docs

def store_in_vector_db(documents, persist_dir="./chroma_db"):
    """
    Takes documents, converts them into embeddings, and stores them in Chroma DB.
    """
    # embedding_fn = OpenAIEmbeddings()  # Turns text into embeddings (vectors)
    vectordb = Chroma.from_documents(
        documents,
        embedding=embedding_fn,
        persist_directory=persist_dir
    )
    vectordb.persist()  # Saves the vector DB to disk
    print(f"✅ Stored {len(documents)} chunks in vector DB at '{persist_dir}'")
