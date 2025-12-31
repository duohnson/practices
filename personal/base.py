class Personal:
    
    def __init__(self, identidad: str, nombre: str, apellidos: str, edad: int):
        self.identidad = identidad.strip()
        self.nombre = nombre.strip()
        self.apellidos = apellidos.strip()
        self.edad = edad
        
        self.registros = {} # como base de datos


    def guardar(self):
        self.registros[self.identidad] = {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad":self.edad
        }

    def mostrar(self):
        print(self.registros)


def registrar():
    ident = "70261"
    nom = "daniel"
    apell = "uohnson"
    ed = 27

    ya_registrado = Personal(ident, nom, apell, ed)
    ya_registrado.guardar()
    print(ya_registrado.registros)

def menu():
    print("Bienvenido al registro de personal.")
    print("Si desea seleccione (1)\nSi desea salir (2)\n")
    seleccion = int(input("¿Cual sería su opción? 1/2\n"))
    while True:
        try:
            if seleccion == 1:
                return registrar()
            elif seleccion == 2:
                print("Vuelva pronto")
                break
            elif seleccion not in (1,2):
                print("La seleccion debe ser entre 1 o 2.")
                return menu()
        except (ValueError, SyntaxError, TypeError):
            print("Valor incorrecto, regresando al inicio.")
            return menu()

menu()