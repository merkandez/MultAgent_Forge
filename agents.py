from crewai import Agent, LLM
from config import get_llm
from tools import roll_dice

# Configuramos el LLM explícitamente para CrewAI para usar phi4
llm_ollama = LLM(model="ollama/phi4", base_url="http://localhost:11434")

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
    goal='Usar la herramienta de dados para decidir el destino. ES OBLIGATORIO RESPONDER EN ESPAÑOL.',
    backstory='Eres la personificación del azar. Tu única misión es usar la herramienta de dados y decidir el rasgo según el resultado. Si ya tienes el resultado, entrega la RESPUESTA FINAL.',
    llm=llm_ollama,
    tools=[roll_dice],
    max_iter=5,  # Damos un poco más de margen
    allow_delegation=False,
    verbose=True
)
