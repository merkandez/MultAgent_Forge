from crewai import Agent
from config import get_llm

llm = get_llm()

# Agente encargado de la parte creativa y narrativa
narrador = Agent(
    role='Narrador de Æther-Bound',
    goal='Transformar las ideas del usuario en un concepto de personaje profundo y coherente con el mundo.',
    backstory='Eres un experto escritor de fantasía oscura. Sabes cómo dar profundidad a pasados trágicos y poderes misteriosos.',
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# Agente encargado de las estadísticas y reglas
mecanico = Agent(
    role='Maestro de Reglas',
    goal='Asignar atributos (Vigor, Astucia, Esencia) y validar las mecánicas del personaje.',
    backstory='Eres un calculador nato. Te aseguras de que el personaje sea jugable y equilibrado según las reglas de Æther-Bound.',
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# Agente encargado del azar
azar = Agent(
    role='El Croupier del Destino',
    goal='Aportar elementos aleatorios y tirar dados para definir rasgos únicos.',
    backstory='Eres la personificación del azar. Tu palabra es ley cuando los dados dictan el destino.',
    llm=llm,
    allow_delegation=False,
    verbose=True
)
