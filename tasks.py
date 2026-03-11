from crewai import Task
from agents import narrador, mecanico, azar

# Tarea 1: Crear la base narrativa
tarea_concepcion = Task(
    description=(
        "Analiza la petición del usuario: '{user_input}'. "
        "Crea un nombre para el personaje, un trasfondo trágico y describe su apariencia "
        "en el mundo de Æther-Bound."
    ),
    expected_output="Un párrafo con el nombre, trasfondo y descripción visual del personaje.",
    agent=narrador
)

# Tarea 2: Determinar un rasgo por azar
tarea_azar = Task(
    description=(
        "Usa la herramienta roll_dice para lanzar 1d6. "
        "Si el resultado es 1-2: Rasgo 'Vínculo Débil'. "
        "Si es 3-4: Rasgo 'Sangre Alquímica'. "
        "Si es 5-6: Rasgo 'Ojo del Abismo'. "
        "Explica qué significa este rasgo para el personaje."
    ),
    expected_output="El resultado del dado y la descripción del rasgo obtenido.",
    agent=azar
)

# Tarea 3: Generar la ficha técnica final
tarea_ficha = Task(
    description=(
        "Basándote en la narrativa y el rasgo aleatorio, asigna 10 puntos entre Vigor, Astucia y Esencia. "
        "Genera una ficha de personaje clara y profesional en formato Markdown."
    ),
    expected_output="Una ficha de personaje completa en Markdown con Secciones: Nombre, Trasfondo, Rasgo, Atributos.",
    agent=mecanico
)
