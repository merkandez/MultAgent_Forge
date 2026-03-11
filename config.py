from langchain_community.chat_models import ChatOllama

# Configuración del modelo local usando Ollama
# Asegúrate de tener Ollama corriendo y el modelo descargado: ollama pull llama3
def get_llm():
    return ChatOllama(
        model="llama3",
        base_url="http://localhost:11434"
    )
