#dinero_cliente = float(input("¿Cuanto dinero desea utilizar?"))



def pedido():
    print("Pedido")

def menu():
    print("--- PIZZERIA UOHNSON ---")
    print("(1) Si desea iniciar un pedido.")
    print("(2) Si desea salir.")

    seleccion = int(input("¿En que le puedo ayudar el día de hoy?\n"))

    while True:
        try: 
            if seleccion == 1:
                return pedido()
            elif seleccion == 2:
                print("Fue un gusto atenderlo, vuelva pronto...")
                break
            else:
                print("Usaste una seleccion erronea, por favor usar 1 o 2.")
                return menu()
        except ValueError:
            print("Caracter invalido, debe ser un valor númerico 1 o 2.")
            return menu()

menu()