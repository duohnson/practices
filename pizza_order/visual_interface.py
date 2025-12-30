import logic as lg
import random as rd

def seleccionar_pizzas():
    print("Es un gusto atenderlo, tenemos 3 Pizzas distintas de las cuales puede escoger.")
    print(f"(1) Pizza de Jamón y Queso - Precio ${lg.jamonyq}\n(2) Pizza Hawaiana - Precio ${lg.hawiana}\n(3) Pizza Pepperoni - Precio ${lg.peperonni}\n(4) Regresar\n")
    lg.opcion = str(input("¿Cual Pizza desea?\n"))
    if lg.opcion == "1":
        lg.pizza.append("Jamón y Queso")
        lg.carrito = lg.jamonyq + lg.carrito
        return menu_ingredientes()
    elif lg.opcion == "2":
        lg.pizza.append("Hawaiana")
        lg.carrito = lg.hawiana + lg.carrito
        return menu_ingredientes()
    elif lg.opcion == "3":
        lg.pizza.append("Pepperoni")
        lg.carrito = lg.peperonni + lg.carrito
        return menu_ingredientes()
    elif lg.opcion == "4":
        return
    else:
        print("Usaste un valor incorrecto, por favor vuelva a seleccionar una opción entre 1 o 3.\n")
        return seleccionar_pizzas()

def menu_ingredientes():
    print(f"Orden: ${lg.carrito}")
    seleccion = str(input(f"¿Desea agregar algun ingrediente extra?\n(1) Si, deseo agregar.\n(2) No, no deseo agregar.\n"))
    if seleccion == "1":
        print(f"Ingredientes que puede añadir:\n(1) Salsa de Tomate - Extra ${lg.salsa_de_tomate}\n(2) Queso Mozzarella - Extra ${lg.queso_mozzarella}\n(3) Queso Parmesano - Extra ${lg.queso_parmesano}\n(4) Queso cheddar - Extra ${lg.queso_cheddar}\n(5) Orégano - Extra ${lg.oregano}\n(6) Aceite de Oliva - Extra ${lg.aceite_de_oliva}\n(7) Regresar")
        complementos = str(input("¿Que desea añadir?\n"))
        try:
            if complementos == "1":
                lg.pedido.append("Salsa de Tomate")
                lg.carrito = lg.carrito + lg.salsa_de_tomate
                return menu_ingredientes()
            elif complementos == "2":
                lg.pedido.append("Queso Mozzarella")
                lg.carrito = lg.carrito + lg.queso_mozzarella
                return menu_ingredientes()
            elif complementos == "3":
                lg.pedido.append("Queso Parmesano")
                lg.carrito = lg.carrito + lg.queso_parmesano
                return menu_ingredientes()
            elif complementos == "4":
                lg.pedido.append("Queso cheddar")
                lg.carrito = lg.carrito + lg.queso_cheddar
                return menu_ingredientes()
            elif complementos == "5":
                lg.pedido.append("Orégano")
                lg.carrito = lg.carrito + lg.oregano
                return menu_ingredientes()
            elif complementos == "6":
                lg.pedido.append("Aceite de Oliva")
                lg.carrito = lg.carrito + lg.aceite_de_oliva
                return menu_ingredientes()
            elif complementos == "7":
                return menu_ingredientes()
            else:
                print("Usaste un valor incorrecto, utiliza una selección de 1 a 7.")
                return menu_ingredientes()
        except ValueError:
            print("Usaste un valor incorrecto, utiliza una selección de 1 a 7.")
            return menu_ingredientes()
    elif seleccion == "2":
        print("Con mucho gusto, procederemos con el pedido..")
        return
    else:
        print("Valor introducido incorrecto, debe ser una seleccion entre 1 y 2.")
        return menu_ingredientes()

def pago():
    lg.cancelar = float(input(f"¿Con cuanto desea cancelar el monto?\n"))
    vuelto = lg.cancelar - lg.carrito
    vuelto = round(vuelto, 2)
    numero_orden = rd.randint(1, 100)
    if lg.cancelar >= lg.carrito:
        print(f"El pedido se canceló correctamente, en unos minutos se le llamará con el pedido número {numero_orden}.\nSu vuelto sería {vuelto}\n\n")
        lg.algo_mas = str(input("¿Podemos ayudarle en algo más?\n(1) Si, deseo ordenar otra Pizza\n(2) No, sería todo.\n"))
        if lg.algo_mas == "1":
            return saludo()
        elif lg.algo_mas == "2":
            print("Muchas gracias por su visita, vuelva pronto.")
            return salir()
    else:
        print(f"Que pena, no le alcanza, le estarían faltando ${vuelto}")
        return

def pedido_listo():
    if not lg.pedido and lg.pizza: # si no pedido (si pedido no es True, recordemos que todas las lists, duples, dict, set, sin valores son False)
        print(f'En ese caso usted ordenó una Pizza {" ".join(lg.pizza)} sin ingredientes extra, sería un total de ${lg.carrito}.')
        return pago()
    elif lg.pedido and lg.pizza:
        print(f'En este caso usted ordenó una Pizza {" ".join(lg.pizza)} con extras de {", ".join(lg.pedido)}, sería un total de ${lg.carrito}.')
        return pago()

def saludo():
    print("-- Bienvenido a Pizzeria Uohnson --")
    print("Será un gusto atenderlo, ¿desea ordenar?\n")
    decision = str(input("(1) ORDENAR.\n(2) CERRAR.\n"))
    if decision == "1":
        seleccionar_pizzas()
        pedido_listo()
    elif decision == "2":
        print("Muchas gracias por su visita, vuelva pronto.")
        return salir()
    else:
        print("Caracter invalido, debe escoger entre 1 o 2.")

def salir():
    while True:
        break

saludo()