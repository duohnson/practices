import random

BASE = 'stock_ti/stock_ti.txt'
ordenes = {}

def cargar_base():
    try:
        with open(BASE, "r") as f:
            contenido = f.read()
        for bloque in contenido.split("-" * 20):
            if bloque.strip():
                lineas = bloque.strip().split("\n")
                orden = int(lineas[0].split(": ")[1])
                nombre = lineas[1].split(": ")[1]
                cedula = lineas[2].split(": ")[1]
                modelo = lineas[3].split(": ")[1]
                serie = lineas[4].split(": ")[1]
                fecha = lineas[5].split(": ")[1]
                ordenes[orden] = {
                    "nombre": nombre,
                    "cedula": cedula,
                    "modelo": modelo,
                    "serie": serie,
                    "fecha": fecha
                }
    except FileNotFoundError:
        print("Archivo no encontrado, creando uno nuevo.")
        with open(BASE, "w") as f:
            pass
        print("Archivo creado exitosamente.")

def registrar():
    while True:
        orden = random.randint(1000, 9999)
        if orden not in ordenes:
            break
    nombre = input("Ingrese el nombre del cliente:\n")
    cedula = input("Ingrese la cédula del cliente:\n")
    modelo = input("Ingrese el modelo del equipo:\n")
    serie = input("Ingrese el número de serie del equipo:\n")
    fecha = input("Ingrese la fecha de ingreso del equipo (dd/mm/yyyy):\n")
    ordenes[orden] = {
        "nombre": nombre,
        "cedula": cedula,
        "modelo": modelo,
        "serie": serie,
        "fecha": fecha
    }
    print(f"Orden registrada con éxito. Número de orden: {orden}")

def guardar():
    try:
        with open(BASE, "w") as f:
            for orden, info in ordenes.items():
                f.write(f"Orden: {orden}\n")
                f.write(f"Nombre: {info['nombre']}\n")
                f.write(f"Cédula: {info['cedula']}\n")
                f.write(f"Modelo: {info['modelo']}\n")
                f.write(f"Serie: {info['serie']}\n")
                f.write(f"Fecha: {info['fecha']}\n")
                f.write("-" * 20 + "\n")
    except FileNotFoundError:
        print("Archivo no encontrado, creando uno nuevo.")
        with open(BASE, "w") as f:
            pass
        print("Archivo creado exitosamente. Por favor, intente registrar la orden nuevamente.")

def cargar():
    consultar = input("Ingrese el número de orden a consultar:\n")
    try:
        with open(BASE, "r") as f:
            contenido = f.read()
        if f"Orden: {consultar}" in contenido:
            print("Información de la orden:")
            print(contenido.split(f"Orden: {consultar}")[1].split("-" * 20)[0])
        else:
            print("Orden no encontrada.")
    except FileNotFoundError:
        print("No se encontró el archivo de órdenes.")

def buscar_cedula(cedula):
    for orden, info in ordenes.items():
        if info['cedula'] == cedula:
            return orden, info
    return "No se encontró ninguna orden con esa cédula."

