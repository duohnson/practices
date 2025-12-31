# Como usar bien los diccionarios.

registros = {}

identificador = 701010101
nombre = "Daniel"
apellido = "Uohnson"

registros[identificador] = {
    "nombre":nombre,
    "apellido":apellido
}

# Este diccionario se convierte en
#   {"identificador": {"nombre":"kenneth","apellido":"uohnson"}
#}
# KEY:VALUE donde por estar encerrados en {} el nombre se convierte en la key del valor kenneth, y lo mismo con apellido.
# asi que si, los diccionarios poseen keys y values externos e internos

# ids = PAR 1 (keys) y datos = PAR 2 (values)
for ids, datos in registros.items(): # items, hace que el diccionario se fraccione por pares, par 1 KEYS y par 2 VALUES
    print(f"La key es el {ids} y el nombre es {datos['nombre']} {datos['apellido']}")