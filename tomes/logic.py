# Tomes

class Registro():

# Donde usamos str como metodo strings para la lectura csv, y 
# .strip() para eliminar caracteres como espacios al inicio y al final.

    def __init__(self, identificacion, bolsa_de_ingreso, bolsa_de_salida, fecha, hora, estado):
        self.identificacion = str(identificacion).strip()
        self.bolsa_de_ingreso = str(bolsa_de_ingreso).strip()
        self.bolsa_de_salida = str(bolsa_de_salida).strip()
        self.fecha = str(fecha).strip()
        self.hora = str(hora).strip()
        self.estado = str(estado).strip()

    def es_valido():
        pass