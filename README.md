# Æther-Bound: Generador de Personajes Multiagente

**Æther-Bound** es un sistema inteligente de creación de personajes para un mundo de fantasía oscura y alquimia. Utiliza un equipo de agentes de IA coordinados para transformar una idea simple en una ficha de personaje completa y coherente.

## Arquitectura del Sistema
El proyecto se basa en **Agentic AI** utilizando el framework **CrewAI** y modelos locales a través de **Ollama**.

### Los Agentes
1.  **Narrador de Æther-Bound**: Se encarga de la coherencia narrativa, el nombre y el trasfondo trágico.
2.  **El Croupier del Destino**: Gestiona el azar. Utiliza una herramienta de Python (`roll_dice`) para lanzar dados reales y determinar rasgos únicos del personaje.
3.  **Maestro de Reglas**: Traduce la historia y el azar en estadísticas (Vigor, Astucia, Esencia) y genera el documento final.

### Flujo de Trabajo
1.  **Entrada**: El usuario introduce una descripción breve.
2.  **Proceso**: Los agentes colaboran de forma secuencial. El resultado de un agente sirve de contexto para el siguiente.
3.  **Salida**: Se genera una ficha técnica en formato Markdown.

## 🛠️ Instalación y Requisitos

### 1. Ollama
Descarga e instala Ollama desde [ollama.com](https://ollama.com). Una vez instalado, descarga el modelo necesario:
```bash
ollama pull llama3
```

### 2. Entorno Python
Crea un entorno virtual e instala las dependencias:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Uso
Ejecuta el script principal:
```bash
python main.py
```
Sigue las instrucciones en pantalla e introduce tu idea. Los agentes empezarán a "forjar" tu personaje.

## 💾 Guardado de Resultados
Al finalizar la ejecución, el sistema:
1.  Muestra la ficha en la terminal.
2.  **Auto-guarda** un archivo `.md` con un nombre basado en tu idea y una marca de tiempo (ej: `ficha_Guerrero_Oscuro_20231027_1200.md`). Esto te permite tener un historial de todos tus personajes creados.

---
*Este proyecto fue desarrollado con fines didácticos para explorar NLP, Transformers y Sistemas Multiagente.*
