from crewai import Crew, Process
from agents import narrador, azar, mecanico
from tasks import tarea_concepcion, tarea_azar, tarea_ficha
import datetime
import re

# Instancia del equipo de agentes
crew = Crew(
    agents=[narrador, azar, mecanico],
    tasks=[tarea_concepcion, tarea_azar, tarea_ficha],
    process=Process.sequential,
    verbose=True
)

def guardar_ficha_md(contenido, nombre_pj):
    # Limpiamos el nombre para que sea un nombre de archivo válido
    nombre_archivo = re.sub(r'[\\/*?:"<>|]', "", nombre_pj).strip().replace(" ", "_")
    if not nombre_archivo:
        nombre_archivo = "personaje_desconocido"
        
    fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ficha_{nombre_archivo}_{fecha}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(contenido))
    
    return filename

def generar_personaje(user_input):
    print(f"\n[SISTEMA] Iniciando la forja de almas para: {user_input}\n")
    # Ejecución del flujo con el input del usuario
    resultado = crew.kickoff(inputs={'user_input': user_input})
    return resultado

if __name__ == "__main__":
    print("\n" + "="*50)
    print("   🎨 BIENVENIDO A LA FORJA DE ÆTHER-BOUND 🎨   ")
    print("="*50 + "\n")
    
    user_idea = input("➤ TU IDEA PARA EL PERSONAJE: ")
    
    if user_idea.strip():
        resultado_crew = generar_personaje(user_idea)
        
        # El resultado de crew.kickoff contiene la ficha final del último agente
        ficha_final = str(resultado_crew)
        
        # Intentamos extraer un nombre para el archivo
        # (Buscamos la primera línea que parezca un nombre o usamos la idea)
        nombre_sugerido = user_idea[:20]
        
        archivo_guardado = guardar_ficha_md(ficha_final, nombre_sugerido)
        
        print("\n" + "="*30)
        print(f"📜 FICHA GENERADA Y GUARDADA: {archivo_guardado}")
        print("="*30 + "\n")
        print(ficha_final)
    else:
        print("\n[!] No has introducido ninguna idea. La forja se apaga...")
