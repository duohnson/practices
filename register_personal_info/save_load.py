import json
import os

# Modulo 2 = # Globales para RAM #

registros = {}
BASE_DATOS = "personal/registros.json"

def guardar(): # guardar el registro de ram a json
    try:
        with open(BASE_DATOS, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(registros)

    with open(BASE_DATOS, "w") as f:
        json.dump(data, f, indent=4)

def cargar_json(identidad: str):
 
    if not os.path.exists(BASE_DATOS): # si no existe la base de datos, imprime que no existe
        print("No existe en la base de datos aún.")
        return
    
    try:
        with open(BASE_DATOS, "r", encoding="utf-8") as f: # abre base de datos en modo lectura
            data = json.load(f) # guarda la informacion de la carga en la variable data
        if identidad in data: # si identidad(la key) esta en data
            return data[identidad] # imprime la informacion de esa identidad (key)
        else:
            print("Sin registros encontrados") # si no encontro resultados, imprime
            return
    except json.JSONDecodeError:
        print("Json corrupto y con errores") # si encontro errores, imprime
        return
