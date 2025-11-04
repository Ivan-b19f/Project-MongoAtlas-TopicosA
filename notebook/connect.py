from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
dotenv_path = '.env'
load_dotenv(dotenv_path)

mongo_uri = os.getenv("MONGODB_URI_ATLAS")
db_name = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(mongo_uri)
    db = client[db_name]
    print("Conexión exitosa a Atlas")
    colecciones = db.list_collection_names()
    print('Conectado Mongo DB Atlas: Base de Datos', db_name)
    print('Colecciones: ', colecciones)
except errors.ServerSelectionTimeoutError as e:
    print("No se pudo conectar al servidor", e)
except errors.OperationFailure as e:
    print("Error de autenticación", e)
except Exception as e:
    print('No sé qué pasó', e)
