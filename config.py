from langchain_ollama import ChatOllama

# Configuración del modelo usando la librería más reciente
def get_llm():
    return ChatOllama(
        model="llama3",
        base_url="http://localhost:11434"
    )
