from crewai import Crew, Process
from agents import narrador, azar, mecanico
from tasks import tarea_concepcion, tarea_azar, tarea_ficha

# Instancia del equipo de agentes
crew = Crew(
    agents=[narrador, azar, mecanico],
    tasks=[tarea_concepcion, tarea_azar, tarea_ficha],
    process=Process.sequential,
    verbose=True
)

def generar_personaje(user_input):
    print(f"\n--- Iniciando creación para: {user_input} ---\n")
    # Ejecución del flujo con el input del usuario
    resultado = crew.kickoff(inputs={'user_input': user_input})
    return resultado

if __name__ == "__main__":
    # Ejemplo de uso
    entrada = "Quiero un personaje sigiloso, con un pasado trágico y poderes raros."
    ficha_final = generar_personaje(entrada)
    
    print("\n" + "="*30)
    print("FICHA FINAL GENERADA")
    print("="*30 + "\n")
    print(ficha_final)
