'''
prueba = int(input("escriban\n"))

match prueba:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("valor erroneo, solo de 1 a 3")
'''
registro = {
    1: {"campo": "nombre", "valor": "kenneth"},
    2: {"campo": "apellido", "valor": "uohnson"}
}

print(registro[1]["valor"])