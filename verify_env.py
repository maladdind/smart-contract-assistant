# the sole purpose of this file is to verify that the modular LangChain packages are correctly installed in 
# this conda environment. If you see the success message below,
# you're good to go! If not, follow the error message tips to resolve any issues.
import sys

def verify_setup():
    print("Starting Verification...\n")
    
    # Track missing packages
    missing = []
    
    # 1. Check Core & Classic Bridge
    try:
        from langchain_classic.chains import RetrievalQA
        print("Classic Bridge: OK")
    except ImportError:
        missing.append("langchain-classic")

    # 2. Check Ollama Integration
    try:
        from langchain_ollama import ChatOllama
        print("Ollama Integration: OK")
    except ImportError:
        missing.append("langchain-ollama")

    # 3. Check Vector DB & Embeddings
    try:
        from langchain_chroma import Chroma
        from langchain_huggingface import HuggingFaceEmbeddings
        import sentence_transformers
        print("Vector DB & Embeddings: OK")
    except ImportError as e:
        missing.append(f"langchain-chroma/huggingface (Error: {e})")

    # 4. Check Document Parsing
    try:
        import pypdf
        import docx2txt
        print("Document Parsers: OK")
    except ImportError:
        missing.append("pypdf / docx2txt")

    # 5. Check API & UI Frameworks
    try:
        import fastapi
        import uvicorn
        import gradio
        print("API & UI Frameworks: OK")
    except ImportError:
        missing.append("fastapi / uvicorn / gradio")

    print("\n" + "="*40)
    if not missing:
        print("SUCCESS: All systems go! Your Machine is ready.")
        print(f"Python Version: {sys.version.split()[0]}")
    else:
        print("ISSUES DETECTED:")
        for m in missing:
            print(f"   - Missing or broken: {m}")
        print("\nTip: Run 'pip install -r requirements.txt' to fix missing packages.")
    print("="*40)

if __name__ == "__main__":
    verify_setup()