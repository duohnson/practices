pedido = []
pizza = []

def bienvenida():
    print("-- Bienvenido a Pizzeria Uohnson --")
    print("Es un gusto atenderlo, tenemos 3 Pizzas distintas de las cuales puede escoger.")
    print("(1) Pizza de Jamón y Queso\n(2) Pizza Hawaiana\n(3) Pizza Pepperoni\n(4) No deseo ordenar\n")
    opcion = str(input("¿Cual Pizza desea?\n"))
    if opcion == "1":
        pizza.append("Jamón y Queso")
        return menu()
    elif opcion == "2":
        pizza.append("Hawaiana")
        return menu()
    elif opcion == "3":
        pizza.append("Pepperoni")
        return menu()
    elif opcion == "4":
        pizza.append("Sin ordenar")
        print("Muchas gracias por su visita, vuelva pronto.")
        return salir()
    else:
        print("Usaste un valor incorrecto, por favor vuelva a seleccionar una opción entre 1 o 3.\n")
        return bienvenida()

def menu():
    while True:
        seleccion = str(input("¿Desea agregar algun ingrediente?\n(1) Si, deseo agregar.\n(2) No, no deseo agregar.\n"))
        if seleccion == "1":
            print("Ingredientes que puede añadir:\n(1) Salsa de Tomate\n(2) Queso Mozzarella\n(3) Queso Parmesano\n(4) Queso cheddar\n(5) Orégano\n(6) Aceite de Oliva")
            complementos = str(input("¿Que desea añadir?\n"))
            try:
                if complementos == "1":
                    pedido.append("Salsa de Tomate")
                    return menu()
                elif complementos == "2":
                    pedido.append("Queso Mozzarella")
                    return menu()
                elif complementos == "3":
                    pedido.append("Queso Parmesano")
                    return menu()
                elif complementos == "4":
                    pedido.append("Queso cheddar")
                    return menu()
                elif complementos == "5":
                    pedido.append("Orégano")
                    return menu()
                elif complementos == "6":
                    pedido.append("Aceite de Oliva")
                    return menu()
                else:
                    print("Usaste un valor incorrecto, utiliza una selección de 1 a 7.")
                    return menu()
            except ValueError:
                print("Usaste un valor incorrecto, utiliza una selección de 1 a 7.")
                return menu()
        elif seleccion == "2":
            print("Con mucho gusto, procederemos con el pedido..")
            return
        else:
            print("Valor introducido incorrecto, debe ser una seleccion entre 1 y 2.")
            return menu()
        
def salir():
    while True:
        break

bienvenida()
print(f'{" ".join(pizza)} con {", ".join(pedido)}')