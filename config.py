from langchain_ollama import ChatOllama

# Usamos phi4 por ser más ligero y rápido que llama3
def get_llm():
    return ChatOllama(
        model="phi4",
        base_url="http://localhost:11434"
    )
