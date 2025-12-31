class Calculadora:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def suma(self):
        return self.n1 + self.n2
    
    def resta(self):
        return self.n1 - self.n2
    
    def multiplicar(self):
        return self.n1 * self.n2
    
    def division(self):
        if self.n2 == 0:
            return "No se puede divivir por 0"
        return self.n1 / self.n2
     
def menu():
    print("Bienvenido a la Calculadora Basica.")
    print("Seleccione un valor según lo que necesite:")
    print("(1) Sumar\n(2) Restar\n(3) Multiplicar\n(4) Division\n(5) Salir")

def seleccion():
    return int(input("¿Cual tipo de operación desea usar?\n"))

def inicio():
    while True:
        menu()
        try:
            seleccion_usada = seleccion()
            if seleccion_usada == 5:
                print("Tenga un buen día.")
                break
            if seleccion_usada not in (1,2,3,4):
                print("Valor incorrecto, debe usar un número entre el 1 o 5 segun la opcion a usar.\n")
                continue
            resultado = Calculadora(float(input("¿Cual sería el primer valor?\n")),float(input("¿Cual sería el segundo valor?\n")))
            if seleccion_usada == 1:
                print(resultado.suma())
            elif seleccion_usada == 2:
                print(resultado.resta())
            elif seleccion_usada == 3:
                print(resultado.multiplicar())
            elif seleccion_usada == 4:
                print(resultado.division())
        except (ValueError, SyntaxError):
            print("Valor utilizado incorrecto, se reiniciará la calculadora, seleccione un valor entre 1 o 5.")

inicio()

