# This module defines the RAG (Retrieval-Augmented Generation) chain,
#  which combines a retriever (vector store) with a question-answering chain to provide accurate responses based on the uploaded documents.
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def build_qa_chain(llm, vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    
    # Precise system prompt for uploaded documents
    system_prompt = (
        "You are a Legal Assistant specializing in smart contracts. "
        "Use the following pieces of context to answer the question. "
        "If the answer is not in the context, say you don't know. "
        "Keep answers professional and concise.\n\n"
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # chain construction
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)
