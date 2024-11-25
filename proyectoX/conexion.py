import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="red_social_x"
        )
        print("✅ Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar a la base de datos: {err}")
        return None
