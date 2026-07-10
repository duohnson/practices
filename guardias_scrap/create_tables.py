import pymysql
import manage as B  


def crear_tablas():

    connection = pymysql.connect(
        host=B.DB,
        user=B.DB_USER,
        password=B.DB_PASSWORD,
        database=B.DB_NAME,
        port=B.Port
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personal (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    crear_tablas()

print("Tablas creadas exitosamente.")
