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
time = 12
print("Party Time" if time == 12 else "Wait")