from langchain_ollama import ChatOllama

def get_llm():
    """Returns a ChatOllama instance using the mistral model."""
    return ChatOllama(
        model="mistral",
        temperature=0,
        num_predict=512 # Optimized for concise outptut 
    )
