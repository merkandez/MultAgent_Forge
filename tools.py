import random
from langchain.tools import tool

class DiceTools:
    @tool("roll_dice")
    def roll_dice(sides: str):
        """Lanza un dado del número de caras especificado (ej: '6'). Devuelve un número entero."""
        try:
            n_sides = int(sides)
            result = random.randint(1, n_sides)
            return f"Resultado del dado (1d{sides}): {result}"
        except ValueError:
            return "Error: Indica un número válido de caras."
