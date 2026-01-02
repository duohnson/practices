import class_ as cl
import save_load as sl

# Modulo 3 = # Outpots y Inputs

def registrar(): # registrar en ram
        ide = input("Introduce la identificación:\n")
        nom = input("Introduce el nombre:\n")
        apell = input("Introduce el apellido:\n")
        ed = int(input("Introduce tu edad:\n"))

        ya_registrado = cl.Personal(ide, nom, apell, ed) # decimos que ya_registrados es la variable con los atributos de la clase personal constructor INIT
        sl.registros[ya_registrado.identidad] = ya_registrado.__dict__ # aca decimos que, registros es igual a clave identidad, con valores ya registrado, convertido a dict
        
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
                sl.guardar()
            case 2:
                busqueda = sl.cargar_json(input("Por favor introduce la identificación a buscar:\n"))
                print(busqueda)
            case 3:
                print("Muchas gracias por usar el simulador, vuelva pronto.")
                break
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    inicio()
