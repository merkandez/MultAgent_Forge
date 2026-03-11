import random
from crewai.tools import tool

@tool("roll_dice")
def roll_dice(caras: str):
    """Lanza un dado. Entrada: Un string con el número de caras, ej: '6'."""
    try:
        n = int(caras)
        return str(random.randint(1, n))
    except:
        return "3"
