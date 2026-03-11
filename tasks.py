from crewai import Task
from agents import narrador, mecanico, azar

# Tarea 1: Crear la base narrativa
tarea_concepcion = Task(
    description=(
        "Analiza la petición: '{user_input}'. "
        "Inventa un nombre evocador, un trasfondo oscuro y describe su apariencia. "
        "Escribe todo el resultado en ESPAÑOL."
    ),
    expected_output="Nombre, trasfondo y descripción visual en español.",
    agent=narrador
)

# Tarea 2: Determinar un rasgo por azar
tarea_azar = Task(
    description=(
        "1. Lanza un dado de 6 caras usando la herramienta 'roll_dice'. "
        "2. IMPORTANTE: El Action Input debe ser exactamente: {\"caras\": \"6\"}. "
        "3. Según el número obtenido, elige el rasgo: 1-2='Vínculo Débil', 3-4='Sangre Alquímica', 5-6='Ojo del Abismo'. "
        "Escribe el resultado final en ESPAÑOL resaltando el rasgo obtenido."
    ),
    expected_output="El nombre del rasgo obtenido y su descripción en español.",
    agent=azar
)

# Tarea 3: Generar la ficha técnica final
tarea_ficha = Task(
    description=(
        "Toma la historia y el rasgo anterior. Reparte 10 puntos en Vigor, Astucia y Esencia. "
        "Crea una ficha en Markdown siguiendo este orden: Nombre, Trasfondo, Rasgo, Atributos. "
        "Todo debe estar en ESPAÑOL."
    ),
    expected_output="Ficha de personaje completa en Markdown y en español.",
    agent=mecanico
)
