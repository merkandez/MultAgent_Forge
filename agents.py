from crewai import Agent, LLM
from config import get_llm
from tools import roll_dice

# Configuramos el LLM explícitamente para CrewAI
llm_ollama = LLM(model="ollama/llama3", base_url="http://localhost:11434")

# Agente encargado de la parte creativa y narrativa
narrador = Agent(
    role='Narrador de Æther-Bound',
    goal='Transformar las ideas del usuario en un concepto de personaje profundo. RESPONDE SIEMPRE EN ESPAÑOL.',
    backstory='Eres un experto escritor de fantasía oscura. Tu tono es solemne y misterioso. IMPORTANTE: Todas tus respuestas y descripciones deben estar en ESPAÑOL.',
    llm=llm_ollama,
    allow_delegation=False,
    verbose=True
)

# Agente encargado de las estadísticas y reglas
mecanico = Agent(
    role='Maestro de Reglas',
    goal='Asignar atributos (Vigor, Astucia, Esencia). RESPONDE SIEMPRE EN ESPAÑOL.',
    backstory='Eres un calculador nato. Te aseguras de que el personaje sea jugable. Generas la ficha final en ESPAÑOL.',
    llm=llm_ollama,
    allow_delegation=False,
    verbose=True
)

# Agente encargado del azar
azar = Agent(
    role='El Croupier del Destino',
    goal='Lanzar dados para decidir rasgos. RESPONDE SIEMPRE EN ESPAÑOL.',
    backstory='Eres la personificación del azar. Tu única misión es usar la herramienta de dados UNA VEZ y decidir el rasgo. Si ya tienes el resultado, NO vuelvas a tirar.',
    llm=llm_ollama,
    tools=[roll_dice],
    max_iter=3,  # Evita bucles infinitos
    allow_delegation=False,
    verbose=True
)
