# Pequeña practica realizada, donde vemos un poquito como funciona guardar y cargar listas en JSON

# This project implements a Personal Records System using Object-Oriented Programming (OOP) and persistent storage. 
# It features a User class that manages individual profiles and handles the conversion between Python Objects and JSON format. 
# By using a dictionary-based storage logic, the system can save data to a local file and "re-hydrate" it back into class instances for later use. 
# The application includes a validated main loop that allows users to register new entries or retrieve existing ones by ID, ensuring data persistence and basic error handling.
# I built this app in Spanish since it's my native tongue and I'm using it for practice

import json # Para este caso al ser una practica, solo usaremos json.
import uuid # En caso de sustituir cédulas por ids que se generen aleatoriamente.

class Usuario(): # Creamos una clase para definir los argumentos del objeto.

    def __init__(self, ids, nombre, apellidos, edad, ciudad):
        self.ids = ids
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.ciudad = ciudad

    def ver_datos(self):
        print("-------- PERFIL --------\n")
        print(f"Personal, {self.nombre.capitalize()} {self.apellidos.capitalize()}")
        print("La cédula es:", self.ids)
        print(f"Actualmente tiene {self.edad} años.")
        print(f"Vive en {self.ciudad.capitalize()}.\n")

    def guardar_en_json(ids_objeto): # En json guarda, donde uuid_objeto sera el id a guardar.
        nombre_del_archivo = "pruebas.json" # Guarda todo en json, la cual usara como almacen el argumento nombre_de_archivo.

        try: # Intenta
            with open(nombre_del_archivo, "r") as archivo: # Abrir el archivo nombre_de_archivo como "r" lectura y su abreviatura será archivo
                datos_conv = json.load(archivo) # Declaramos que datos_conv es la conversion de la carga de json load sobre el archivo (lo carga)
        except (FileNotFoundError, json.JSONDecodeError): # Esto nos permite que si el archivo no existe se cree, y si esta vacio, lo lea como un directorio vacio
                datos_conv = {} # Lo convierte en directorio vacio si esta vacio o nuevo
            
        datos_conv[ids_objeto.ids] = ids_objeto.__dict__ # Usamos el uuid del usuario como llave y __dict__ lo que hace es que todos los objetos
# tienen un diccionario interno con sus datos y se preparan para formato json
            
        with open(nombre_del_archivo, "w") as archivo: # Abrir el archivo nombre_de_archivo como "w" escritura y su abreviatura será archivo
            json.dump(datos_conv, archivo, indent=4) # dump significa vaciar, toma el objeto de python (el diccionario datos_conv que posee todo el usuario)
         # y lo convierte en diccionario para lograr cargarlo a json
         # datos_conv es el ORIGEN, es el diccionario con la informacion del id, nombre apellido y demas
         # archivo es el DESTINO, donde se debe guardar todo el diccionario, el .json
         # Indentamos o sangrias 4 por cada bloque
    @staticmethod
    def cargar_desde_json(ids_buscado): # Creamos una funcion para cargar los datos, y el uuid que buscaremos.
        try:
            with open("pruebas.json", "r") as archivo: # Nuevamente, abrimos el json en modo lectura y lo renombramos archivo para no tener que escribir todo el bloque
                datos =  json.load(archivo) # datos es el almacen del resultado de la carga .load del json que se llamara archivo

                if ids_buscado in datos: # Si el id buscado esta en datos entonces:
                    info = datos[ids_buscado] # Haremos que info sea igual al diccionario guardado en json, tomando el id del usuario para traer todo el dict
                    return Usuario(info['ids'], info['nombre'], info['apellidos'], info['edad'], info['ciudad'])
          # Este return devuelve a info la conversion del diccionario a una clase nuevamente, y llama al instructor de class Usuario() nuevamente
          # Recordar que en python los diccionarios no poseen metodos, por eso se deben convertir de objeto clase a diccionario al guardar, y en objeto clase nuevamente al cargar
                else:
                    return None # Si no encuentras nada, solo di no encontre nada pero no des error
              
        except FileNotFoundError:
            return None # Si no encuentras nada, solo di no encontre nada pero no des error

