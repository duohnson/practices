import json
import os

# Modulo 1 = # Clases #

class Personal():
    def __init__(self, identidad, nombre, apellidos, edad):
        self.identidad = str(identidad).strip()
        self.nombre = str(nombre).strip()
        self.apellidos = str(apellidos).strip()
        self.edad = str(edad).strip()

    def mostrar(self):
        print(f"{self.identidad}:   {self.nombre}, {self.apellidos}, {self.edad}")

# Modulo 2 = # Globales para RAM #

registros = {}
BASE_DATOS = "json/registros.json"

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

# Modulo 3 = # Outpots y Inputs

def registrar(): # registrar en ram
        ide = "011"
        nom = "Jane"
        apell = "Hopper"
        ed = "?"

        ya_registrado = Personal(ide, nom, apell, ed) # decimos que ya_registrados es la variable con los atributos de la clase personal constructor INIT
        registros[ya_registrado.identidad] = ya_registrado.__dict__ # aca decimos que, registros es igual a clave identidad, con valores ya registrado, convertido a dict
        

# 1 #
registrar()
guardar()
imprimir = cargar_json("011")
print(imprimir)
# 1 #

# 2 #
iden = "70xx"
nomb = "Daniel"
apells = "Uohnson"
eda = "27"
prueba = Personal(iden,nomb,apells,eda)
registros[prueba.identidad] = prueba.__dict__
guardar()
imprimir_prueba = cargar_json("70xx")
print(imprimir_prueba)
# 2 #