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
        "1. Usa la herramienta 'roll_dice' con sides='6'. "
        "2. Según el resultado: 1-2='Vínculo Débil', 3-4='Sangre Alquímica', 5-6='Ojo del Abismo'. "
        "3. Explica brevemente el rasgo en ESPAÑOL."
    ),
    expected_output="El resultado del dado y el nombre del rasgo obtenido en español.",
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
