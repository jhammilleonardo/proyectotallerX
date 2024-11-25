def dar_me_gusta(conexion, tweet_id, usuario_id):
    cursor = conexion.cursor()
    try:
        query = """
        INSERT INTO likes (tweet_id, usuario_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (tweet_id, usuario_id))
        conexion.commit()
        print("❤️ Me gusta registrado con éxito.")
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("❌ Ya has dado me gusta a este tweet.")
        else:
            print(f"❌ Error al dar me gusta: {err}")
    finally:
        cursor.close()

def agregar_comentario(conexion, tweet_id, usuario_id, contenido):
    cursor = conexion.cursor()
    try:
        query = """
        INSERT INTO comentarios (tweet_id, usuario_id, contenido)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (tweet_id, usuario_id, contenido))
        conexion.commit()
        print("💬 Comentario agregado con éxito.")
    except mysql.connector.Error as err:
        print(f"❌ Error al agregar comentario: {err}")
    finally:
        cursor.close()

def ver_comentarios(conexion, tweet_id):
    cursor = conexion.cursor()
    try:
        query = """
        SELECT c.id, u.username, c.contenido, c.fecha_hora
        FROM comentarios c
        JOIN usuarios u ON c.usuario_id = u.id
        WHERE c.tweet_id = %s
        ORDER BY c.fecha_hora ASC
        """
        cursor.execute(query, (tweet_id,))
        resultados = cursor.fetchall()
        if resultados:
            print("\n=== Comentarios ===")
            for comentario in resultados:
                print(f"ID: {comentario[0]}, Usuario: @{comentario[1]}")
                print(f"Publicado: {comentario[3]}")
                print(f"Comentario: {comentario[2]}")
                print("-" * 40)
        else:
            print("❌ No hay comentarios en este tweet.")
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar comentarios: {err}")
    finally:
        cursor.close()
