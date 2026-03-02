try:
    from langchain_classic.chains import RetrievalQA
    from langchain_ollama import ChatOllama
    from langchain_chroma import Chroma
    print("✅ SUCCESS: Modular LangChain and Conda are correctly configured.")
except ModuleNotFoundError as e:
    print(f"❌ ERROR: {e}")
    print("Tip: Ensure you ran 'pip install langchain-classic' in this env.")