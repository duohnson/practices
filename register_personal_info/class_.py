# Modulo 1 = # Clases #

class Personal():
    def __init__(self, identidad, nombre, apellidos, edad):
        self.identidad = str(identidad).strip()
        self.nombre = str(nombre).strip()
        self.apellidos = str(apellidos).strip()
        self.edad = int(edad)

    def mostrar(self):
        print(f"{self.identidad}:   {self.nombre}, {self.apellidos}, {self.edad}")
