def registrar_usuario(conexion, username, email, password, nombre_completo=None):
    cursor = conexion.cursor()
    try:
        query = """
        INSERT INTO usuarios (username, email, password, nombre_completo)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (username, email, password, nombre_completo))
        conexion.commit()
        print("✅ Usuario registrado con éxito.")
    except mysql.connector.Error as err:
        print(f"❌ Error al registrar usuario: {err}")
    finally:
        cursor.close()
