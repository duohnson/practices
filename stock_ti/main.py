import save_load as sl

def mostrar_todas():
    try:
        with open(sl.BASE, "r") as f:
            contenido = f.read()
        print("Todas las órdenes registradas:")
        print(contenido)
    except FileNotFoundError:
        print("No se encontró el archivo de órdenes.")

def modificar_orden():
    try:
        modificar = int(input("Ingrese el número de orden a modificar:\n"))
    except ValueError:
        print("Número de orden inválido.")
        return
    if modificar in sl.ordenes:
        print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
        nombre = input(f"Nombre ({sl.ordenes[modificar]['nombre']}):\n") or sl.ordenes[modificar]['nombre']
        cedula = input(f"Cédula ({sl.ordenes[modificar]['cedula']}):\n") or sl.ordenes[modificar]['cedula']
        modelo = input(f"Modelo ({sl.ordenes[modificar]['modelo']}):\n") or sl.ordenes[modificar]['modelo']
        serie = input(f"Serie ({sl.ordenes[modificar]['serie']}):\n") or sl.ordenes[modificar]['serie']
        fecha = input(f"Fecha ({sl.ordenes[modificar]['fecha']}):\n") or sl.ordenes[modificar]['fecha']
        sl.ordenes[modificar] = {
            "nombre": nombre,
            "cedula": cedula,
            "modelo": modelo,
            "serie": serie,
            "fecha": fecha
        }
        sl.guardar()
        print("Orden modificada con éxito.")
    else:
        print("Orden no encontrada.")

def inicio():
    while True:
        print("Seleccione una opción:")
        print("1. Registrar nueva orden")
        print("2. Consultar orden existente")
        print("3. Mostrar todas las órdenes")
        print("4. Modificar orden existente")
        print("5. Buscar orden por cédula")
        print("6. Salir")
        opcion = input()
        if opcion == "1":
            sl.registrar()
            sl.guardar()
        elif opcion == "2":
            sl.cargar()
        elif opcion == "3":
            mostrar_todas()
        elif opcion == "4":
            modificar_orden()
        elif opcion == "5":
            cedula = input("Ingrese la cédula para buscar su orden:\n")
            resultado = sl.buscar_cedula(cedula)
            if resultado == "No se encontró ninguna orden con esa cédula.":
                print(resultado)
            else:
                orden, info = resultado
                print(f"Orden encontrada: {orden}")
                print(f"Nombre: {info['nombre']}")
                print(f"Cédula: {info['cedula']}")
                print(f"Modelo: {info['modelo']}")
                print(f"Serie: {info['serie']}")
                print(f"Fecha: {info['fecha']}")
        elif opcion == "6":
            print("Gracias por usar el sistema de gestión de órdenes.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    sl.cargar_base()
    inicio()

