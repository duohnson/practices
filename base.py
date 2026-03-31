import sqlite3

DB = "data/database.sqlite"

def obtener():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (username TEXT PRIMARY KEY, nombre TEXT, apellido TEXT, edad INTEGER)")
    conn.commit()
    conn.close()
    
def agregar_usuario(username, nombre, apellido, edad):
    # Asegurar que la tabla existe
    obtener()
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, nombre, apellido, edad) VALUES (?, ?, ?, ?)", (username, nombre, apellido, edad))
    conn.commit()
    conn.close()

def editar_usuario(username, nombre=None, apellido=None, edad=None):
    """Edita los campos proporcionados para el usuario `username`.
    Devuelve True si se actualizó al menos una fila, False en caso contrario o si no se pasan campos.
    """
    obtener()
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    fields = []
    params = []
    if nombre is not None:
        fields.append("nombre = ?")
        params.append(nombre)
    if apellido is not None:
        fields.append("apellido = ?")
        params.append(apellido)
    if edad is not None:
        fields.append("edad = ?")
        params.append(edad)
    if not fields:
        conn.close()
        return False
    params.append(username)
    query = "UPDATE usuarios SET " + ", ".join(fields) + " WHERE username = ?"
    cursor.execute(query, params)
    conn.commit()
    changed = cursor.rowcount
    conn.close()
    return changed > 0

def eliminar_usuario(username):
    """Elimina el usuario con `username`. Devuelve True si se eliminó, False si no existía."""
    obtener()
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0

