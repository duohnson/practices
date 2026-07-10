import pymysql

import manage as B

def test():
    try:
        connection = pymysql.connect(
            host=B.DB,
            user=B.DB_USER,
            password=B.DB_PASSWORD,
            database=B.DB_NAME,
            port=B.Port
        )
        print("Conexion exitosa!")
        connection.close()
    except Exception as e:
        print(f"Error al conectar: {e}")

if __name__ == "__main__":
    test()
