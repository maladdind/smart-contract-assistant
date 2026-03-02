from fastapi import FastAPI, UploadFile, File
import shutil
import os
from ingestion import load_document, split_documents
from vector_store import create_vector_store
from rag_chain import build_qa_chain
from llm_setup import get_llm

app = FastAPI(title="Smart Contract Assistant")
vectordb = None
llm = get_llm()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global vectordb
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Process the document: load, split, and create vector store
    docs = load_document(temp_path)
    chunks = split_documents(docs)
    vectordb = create_vector_store(chunks)
    
    os.remove(temp_path)
    return {"message": "Success", "chunks_indexed": len(chunks)}

@app.post("/ask")
async def ask_question(question: str):
    if vectordb is None:
        return {"answer": "Please upload a document first."}
    
    chain = build_qa_chain(llm, vectordb)
    # The result contains 'answer' and 'context' (source docs)
    result = chain.invoke({"input": question})
    
    return {
        "answer": result["answer"],
        "sources": [doc.metadata.get('source', 'unknown') for doc in result["context"]]
    }
