'''
# Modulo 1 = # Clases #

class Personal():
    def __init__(self, identidad, nombre, apellidos, edad):
        self.identidad = str(identidad).strip()
        self.nombre = str(nombre).strip()
        self.apellidos = str(apellidos).strip()
        self.edad = int(edad)

    def mostrar(self):
        print(f"{self.identidad}:   {self.nombre}, {self.apellidos}, {self.edad}")

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

# Modulo 3 = # Outpots y Inputs

def registrar(): # registrar en ram
        ide = input("Introduce la identificación:\n")
        nom = input("Introduce el nombre:\n")
        apell = input("Introduce el apellido:\n")
        ed = int(input("Introduce tu edad:\n"))

        ya_registrado = Personal(ide, nom, apell, ed) # decimos que ya_registrados es la variable con los atributos de la clase personal constructor INIT
        registros[ya_registrado.identidad] = ya_registrado.__dict__ # aca decimos que, registros es igual a clave identidad, con valores ya registrado, convertido a dict
        
def inicio():
    
    print("#########################################################################")
    print("##    Bienvenido al Simulador de Registros, sistema básico de pruebas  ##")
    print("#########################################################################")
    
    while True:
        print("#########################################################################")
        print("##    Seleccione:                                                      ##")
        print("##        (1) Registrar nuevo personal.                                ##")
        print("##        (2) Ver información de algun personal.                       ##")
        print("##        (3) Salir.                                                   ##")
        print("#########################################################################")

        try:
            opcion = int(input("¿En que podemos ayudarle:?\n"))
        except (ValueError, SyntaxError, TypeError):
            print("Introduciste un valor incorrecto y no apropiado, por favor, seleccione una opción númerica entre 1 y 3.")
            return
        
        match opcion:
            case 1:
                registrar()
                guardar()
            case 2:
                busqueda = cargar_json(input("Por favor introduce la identificación a buscar:\n"))
                print(busqueda)
            case 3:
                print("Muchas gracias por usar el simulador, vuelva pronto.")
                break
            case _:
                print("Opcion invalida")
        
inicio()
'''