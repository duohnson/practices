import json
import uuid # en caso de sustituir cédulas por ids que se generen aleatoriamente

class Usuario(): # Creamos una clase para definir los parametros automaticos 

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

    def guardar_en_json(ids_objeto): # en json guarda, donde uuid_objeto sera el id a guardar
        nombre_del_archivo = "pruebas.json" # guarda todo en json, la cual usara como almacen el argumento nombre_de_archivo

        try: # intenta
            with open(nombre_del_archivo, "r") as archivo: # abrir el archivo nombre_de_archivo como "r" lectura y su abreviatura será archivo
                datos_conv = json.load(archivo) # declaramos que datos_conv es la conversion de la carga de json load sobre el archivo (lo carga)
        except (FileNotFoundError, json.JSONDecodeError): # esto nos permite que si el archivo no existe se cree, y si esta vacio, lo lea como un directorio vacio
                datos_conv = {} # lo convierte en directorio vacio si esta vacio o nuevo
            
        datos_conv[ids_objeto.ids] = ids_objeto.__dict__ # usamos el uuid del usuario como llave y __dict__ lo que hace es que todos los objetos
# tienen un diccionario interno con sus datos y se preparan para formato json
            
        with open(nombre_del_archivo, "w") as archivo: # # abrir el archivo nombre_de_archivo como "w" escritura y su abreviatura será archivo
            json.dump(datos_conv, archivo, indent=4) # dump significa vaciar, toma el objeto de python (el diccionario datos_conv que posee todo el usuario)
         # y lo convierte en diccionario para lograr cargarlo a json
         # datos_conv es el ORIGEN, es el diccionario con la informacion del id, nombre apellido y demas
         # archivo es el DESTINO, donde se debe guardar todo el diccionario, el .json
         # indentamos o sangrias 4 por cada bloque
    @staticmethod
    def cargar_desde_json(ids_buscado): # creamos una funcion para cargar los datos, y el uuid que buscaremos
        try:
            with open("pruebas.json", "r") as archivo: # nuevamente, abrimos el json en modo lectura y lo renombramos archivo para no tener que escribir todo el bloque
                datos =  json.load(archivo) # datos es el almacen del resultado de la carga .load del json que se llamara archivo

                if ids_buscado in datos: # si el id buscado esta en datos entonces:
                    info = datos[ids_buscado] # haremos que info sea igual al diccionario guardado en json, tomando el id del usuario para traer todo el dict
                    return Usuario(info['ids'], info['nombre'], info['apellidos'], info['edad'], info['ciudad'])
          # este return devuelve a info la conversion del diccionario a una clase nuevamente, y llama al instructor de class Usuario() nuevamente
          # recordar que en python los diccionarios no poseen metodos, por eso se deben convertir de objeto clase a diccionario al guardar, y en objeto clase nuevamente al cargar
                else:
                    return None # si no encuentras nada, solo di no encontre nada pero no des error
              
        except FileNotFoundError:
            return None # si no encuentras nada, solo di no encontre nada pero no des error

def registrar():
    print("-- REGISTRANDO UN USUARIO --\n")

    # actualmente sin uso ids_aleatorio
    ids_aleatorio = str(uuid.uuid4().hex[:5]) # creamos la variable para generar id aleatorios, anteriormente exportamos el uuid, entonces (uuid.uuid4()) 
    # nos permite garantizar que el id sea unico, ademas de hex[:] nos permite decidir que tan largo sera este id.

    '''
    abajo guardaremos los datos en variables para luego convertirlas en la clase y usar las funciones de carga y guardar 
    basicamente, aca introduciremos los parametros a guardar
    '''
    ids = input("Introduce tu cédula:\n")
    nombre = input("Introduce el nombre:\n")
    apellidos = input("Introduce los apellidos:\n")
    edad = int(input("Introduce la edad:\n"))
    ciudad = input("Introduce la ciudad:\n")

    nuevo_id = Usuario(ids, nombre, apellidos, edad, ciudad) # aca logramos convertir la informacion ingresada a una clase,
    # usando el uuid_aleatorio para generar un id que no se repetira
    
    Usuario.guardar_en_json(nuevo_id) # llamamos a la funcion guardar en json el nuevo usuario, y iniciamos los procesos de funciones para guardar y cargar

    print(f"Registro exitoso!\n")
    print(f"Se ingreso a {nombre.capitalize()} {apellidos.capitalize()} con la cédula {ids}.")

'''
usuario1 = Usuario(input("¿Cual será tu usuario?:\n"),input("Introduce tu nombre:\n"),input("Introduce tu apellido:\n"),int(input("Introduce tu edad:\n")),input("Introduce tu ciudad\n"))
print(usuario1.ver_datos())


while True: # verdadero usa
    registrar() #registrar
    continuar = input("Quieres registrar a una persona? (s/n):\n") # texto a elegir
    if continuar.lower() != 's': # si es diferente a s, rompe con break el codigo
        break
        
'''

def menu():

    print("-------* PERSONAL *-------\n")
    print("Registro de personal con los datos.\n", "(1) Selecciona para registrar.\n", "(2) Selecciona para ver datos.\n", "(3) Salir del registro.")
    seleccion = input("¿En que podemos ayudarle?\n")
    return seleccion
    
while True:
    
    opcion = menu()

    try:
        seleccion = int(opcion)
        if seleccion == 1:
            print("Ingresando...\n")
            registrar()
            
        elif seleccion == 2:
            ids_buscar = input("¿Cual es la cédula?\n")
            usuario_encontrado = Usuario.cargar_desde_json(ids_buscar)
            print("Mostrando información...\n")
            if usuario_encontrado:
                usuario_encontrado.ver_datos()
            else:
                print("Usuario no encontrado.")
        elif seleccion == 3:
            print("Saliendo...\n")
            break
        else:
            print("Usaste un número incorrecto, debes escoger entre (1) ó (2).")

    except ValueError:
        print("Usaste un valor incorrecto, debes escoger entre (1) ó (2).")