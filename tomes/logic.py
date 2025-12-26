# Tomes
from datetime import datetime, date

class Registro():

# Donde usamos str como metodo strings para la lectura csv, y 
# .strip() para eliminar caracteres como espacios al inicio y al final.

    def __init__(self, id=None, bolsa_de_ingreso=None, bolsa_de_salida=None, fecha=None, hora=None, estado=None):
        self.id = str(id).strip()
        self.bolsa_de_ingreso = str(bolsa_de_ingreso).strip()
        self.bolsa_de_salida = str(bolsa_de_salida).strip()
        self.fecha = str(fecha).strip()
        self.hora = str(hora).strip()
        self.estado = estado

    def registrar(self):
        self.id = input("¿Cual es la cédula a guardar?.\n")
        self.bolsa_de_ingreso = input("Introduzca etiqueta de bolsa entrante.\n")
        self.bolsa_de_salida = input("Introduzca etiqueta de bolsa saliente.\n")
        self.fecha = date.today()
        self.hora = datetime.now().strftime("%I:%M:%p")
        print("Si el estado fue Correcto seleccione (1).\nDe lo contrario, seleccione (2).")
        self.estado = int(input("¿Cual es el estado?\n"))

    def resultados(self):

        while True:
            if registros.estado == 1:
                return "Correcto"
            elif registros.estado == 2:
                return "Erroneo"
            else:
                print("Valor incorrecto, solo 1 o 2.")


registros = Registro()
registros.registrar()
registros.resultados()

print(f"Donde decimos que la identificación es {registros.id}\nCon bolsa entrante {registros.bolsa_de_ingreso} y bolsa de salida {registros.bolsa_de_salida}.\n")
print(f"Esto se realizo en la fecha {registros.fecha} con hora {registros.hora}.\nPor lo cual el proceso concluye como {registros.resultados()}.")