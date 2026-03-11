import random
from crewai.tools import tool

@tool("roll_dice")
def roll_dice(sides: str):
    """Lanza un dado. Argumento 'sides' debe ser el número de caras (ej: '6'). Devuelve SOLO el número resultante."""
    try:
        n_sides = int(sides)
        return random.randint(1, n_sides)
    except ValueError:
        return 1
