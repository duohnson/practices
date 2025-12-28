import base as bs
import register as rg

'''
*------ > LINEAS DE CODIGO USADAS SOLO PARA PEQUEÑAS PRUEBAS < ------*

usuario1 = Usuario(input("¿Cual será tu usuario?:\n"),input("Introduce tu nombre:\n"),input("Introduce tu apellido:\n"),int(input("Introduce tu edad:\n")),input("Introduce tu ciudad\n"))
print(usuario1.ver_datos())
while True: # verdadero usa
    registrar() #registrar
    continuar = input("Quieres registrar a una persona? (s/n):\n") # texto a elegir
    if continuar.lower() != 's': # si es diferente a s, rompe con break el codigo
        break      
'''

def menu():

# Pequeño menú de navegación
    
    print("-------* PERSONAL *-------\n")
    print("Registro de personal con los datos.\n", "(1) Selecciona para registrar.\n", "(2) Selecciona para ver datos.\n", "(3) Salir del registro.")
    seleccion = input("¿En que podemos ayudarle?\n")
    return seleccion # Devolvera la seleccion 1 2 o 3

# Aca iniciamos la interaccion para navegar entre los metodos de la clase, usando un while = mientras.

while True:
    
    opcion = menu() # Entonces opcion es igual al menu() el cual devolvia la seleccion

    try:
        seleccion = int(opcion) # Intentamos retomar la seleccion de menu()
        if seleccion == 1:
            print("Ingresando...\n")
            rg.registrar() # Al seleccionar 1 llamamos al metodo para registrar informacion.
            
        elif seleccion == 2:
            ids_buscar = input("¿Cual es la cédula?\n") # Acá le definimos la cédula que buscaremos a la variable ids_buscar (esta si es variable por estar fuera de una clase/funcion
            usuario_encontrado = bs.Usuario.cargar_desde_json(ids_buscar) # Aca definimos que, el usuario encontrado es la variable del resultado de, en la clase usuario, llamamos al metodo cargar datos, para 
            # buscar la cedula con la cedula que necesitamos, es como un comparativo ok? decimos la variable "usuario_encontrado" sera la busqueda en la base del valor "ids_buscar".
            print("Mostrando información...\n")
            if usuario_encontrado:
                usuario_encontrado.ver_datos() # Si encontro la cedula o bien al usuario, 
            else:
                print("Usuario no encontrado.\n") # Si no encontro el registro
        elif seleccion == 3:
            print("Saliendo...\n") 
            break # Para salir de sistema
        else:
            print("Usaste un número incorrecto, debes escoger entre (1) ó (2).")

    except ValueError:
        print("Usaste un valor incorrecto, debes escoger entre (1) ó (2).")
