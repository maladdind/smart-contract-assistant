from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Centralized vector store management for document embeddings. This module handles both creation and
# loading of the Chroma vector store, ensuring consistent embedding generation with HuggingFace models.
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(documents, persist_directory="./chroma_db"):
    """Creates a Chroma vector store. Persistence is now automatic."""
    return Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
# 
def load_vector_store(persist_directory="./chroma_db"):
    """Loads an existing store from disk."""
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )