# Local RAG for Summary & Q&A Assistant

A production-ready RAG (Retrieval-Augmented Generation) pipeline designed for document analysis. This system allows users to upload (PDF/DOCX) and perform semantic queries against them using a fully local LLM stack.

## Key Features

* **Local & Private:** Powered by **Ollama (Mistral)** and **HuggingFace Embeddings**. So that no data leaves your machine.
* **Modular Architecture:** Built with the 2026 LangChain v0.3 standard using specialized partner packages.
* **Legal Guardrails:** Semantic similarity checks to ensure queries remain relevant to the uploaded file.

---

## Prerequisites

Before starting, ensure you have the following installed on your machine:

1. **Ollama:** [Download here](https://ollama.com/download)
```bash
    # or use pip to install it
    pip install ollama
    # to download the model
    ollama pull mistral
```
2. **Conda (Miniforge recommended):** `brew install miniforge`
3. **Mistral Model:** Run `ollama run mistral` in your terminal.

---

## Installation & Setup

Follow these steps exactly to replicate the environment:

### 1. Environment Creation

```bash
# Create a dedicated Python 3.12 environment
conda create -n smart_qna python=3.12 -y
conda activate smart_qna

# Optional: Clear any previous build caches
pip cache purge

```

### 2. Dependency Installation
```bash
pip install -r requirements.txt
```
or manually Install the specific modular packages required:

```bash
# Core LangChain & Classic Bridge
pip install langchain-core langchain-community langchain-text-splitters langchain-classic

# Hardware Specifics & Vector DB
pip install langchain-ollama langchain-chroma langchain-huggingface sentence-transformers

# API & Frontend
pip install fastapi uvicorn pypdf docx2txt gradio

```

---

## Project Structure

* `app.py`: FastAPI backend handling uploads and the RAG logic.
* `ui.py`: Gradio-based web interface (Chat & Upload tabs).
* `ingestion.py`: Logic for parsing PDF/DOCX and recursive chunking.
* `vector_store.py`: Manages the ChromaDB vector database and HuggingFace embeddings.
* `rag_chain.py`: The retrieval logic using the `langchain_classic` bridge.
* `llm_setup.py`: Configuration for the local Ollama/Mistral connection.

---

## How to Run

You will need **three** terminal windows open:

### Step 1: Start Ollama

Ensure the Mistral model is served:

```bash
ollama serve

```

### Step 2: Start the Backend (FastAPI)

```bash
conda activate smart_qna
uvicorn app:app --reload --port 8000

```

### Step 3: Start the Frontend (Gradio)

```bash
conda activate smart_qna
python ui.py

```

Open your browser to `http://localhost:7860`.