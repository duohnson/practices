import base as bs

def registrar():
    print("-- REGISTRANDO UN USUARIO --\n")

    # Actualmente sin uso:
    # ids_aleatorio = str(uuid.uuid4().hex[:5]) # Creamos la variable para generar id aleatorios, anteriormente exportamos el uuid, entonces (uuid.uuid4()) 
    # nos permite garantizar que el id sea unico, ademas de hex[:] nos permite decidir que tan largo sera este id.

    # Abajo guardaremos los datos en variables para luego convertirlas en la clase y usar las funciones de carga y guardar 
    # basicamente, aca introduciremos los parametros a guardar
    
    ids = input("Introduce tu cédula:\n")
    nombre = input("Introduce el nombre:\n")
    apellidos = input("Introduce los apellidos:\n")
    edad = int(input("Introduce la edad:\n"))
    ciudad = input("Introduce la ciudad:\n")

    nuevo_id = bs.Usuario(ids, nombre, apellidos, edad, ciudad) # Aca logramos convertir la informacion ingresada a una clase,
    # Usando el uuid_aleatorio para generar un id que no se repetira
    
    bs.Usuario.guardar_en_json(nuevo_id) # Llamamos a la funcion guardar en json el nuevo usuario, y iniciamos los procesos de funciones para guardar y cargar

    print(f"Registro exitoso!\n")
    print(f"Se ingreso a {nombre.capitalize()} {apellidos.capitalize()} con la cédula {ids}.")
