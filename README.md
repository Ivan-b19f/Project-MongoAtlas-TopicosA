# Project-MongoAtlas-TopicosA

Proyecto básico para conectar Python a MongoDB Atlas en Tópicos en Inteligencia de Negocios.

## Requisitos
- Python 3.8+
- Cuenta en MongoDB Atlas (cluster gratuito).

## Instalación
1. Clona el repo: `git clone https://github.com/Ivan-b19f/Project-MongoAtlas-TopicosA.git`
2. Crea entorno virtual: `python -m venv myenv`
3. Activa: `myenv\Scripts\activate` (Windows) o `source myenv/bin/activate` (Linux/Mac)
4. Instala: `pip install -r requirements.txt`
5. Copia `.env.example` a `.env` y llena con tu URI de Atlas.

## Ejecución
- Prueba conexión: `python notebook/connect.py`
- Output esperado: "Conexión exitosa a Atlas" + lista de colecciones (ej. ['movies', 'comments']).

## Estructura
- `notebook/`: Scripts de conexión.
- Para BI: Usa pandas en notebooks para queries y análisis.

## Notas
- Configura Network Access en Atlas (IP 0.0.0.0/0 para pruebas).
- Basado en sample_mflix dataset.
