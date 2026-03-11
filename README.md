# Æther-Bound: Generador de Personajes Multiagente

Este proyecto es un sistema didáctico de creación de personajes para el juego de rol **Æther-Bound**. Utiliza **CrewAI** para la orquestación de agentes y **Ollama** como motor de lenguaje local.

## Objetivo
Demostrar cómo varios agentes de IA pueden colaborar para:
1. Traducir deseos del usuario a mecánicas de juego.
2. Validar la coherencia narrativa.
3. Generar azar mediante herramientas (dados).
4. Producir una ficha de personaje estructurada.

## Requisitos
- Python 3.10+
- Ollama (con el modelo `llama3` o similar cargado)
- CrewAI

## Ejecución
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar: `python main.py`
