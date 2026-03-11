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
    print(f"\n[SISTEMA] Iniciando la forja de almas para: {user_input}\n")
    # Ejecución del flujo con el input del usuario
    resultado = crew.kickoff(inputs={'user_input': user_input})
    return resultado

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   🎨 BIENVENIDO A LA FORJA DE ÆTHER-BOUND 🎨   ")
    print("="*50 + "\n")
    
    print("Describe el personaje que imaginas.")
    print("Ejemplos:")
    print("- 'Un alquimista ciego que ve a través de los vapores.'")
    print("- 'Una guerrera sigilosa con un brazo de plata.'\n")
    
    user_idea = input("➤ TU IDEA: ")
    
    if user_idea.strip():
        ficha_final = generar_personaje(user_idea)
        
        print("\n" + "="*30)
        print("📜 FICHA FINAL GENERADA")
        print("="*30 + "\n")
        print(ficha_final)
    else:
        print("\n[!] No has introducido ninguna idea. La forja se apaga...")
