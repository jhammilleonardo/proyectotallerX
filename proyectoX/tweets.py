def publicar_tweet(conexion, usuario_id, contenido):
    cursor = conexion.cursor()
    try:
        query = """
        INSERT INTO tweets (usuario_id, contenido)
        VALUES (%s, %s)
        """
        cursor.execute(query, (usuario_id, contenido))
        conexion.commit()
        print("✅ Tweet publicado con éxito.")
    except mysql.connector.Error as err:
        print(f"❌ Error al publicar tweet: {err}")
    finally:
        cursor.close()

def ver_tweets_usuario(conexion, usuario_id):
    cursor = conexion.cursor()
    try:
        query = """
        SELECT t.id, t.contenido, t.fecha_hora, 
               (SELECT COUNT(*) FROM likes WHERE tweet_id = t.id) AS likes,
               (SELECT COUNT(*) FROM comentarios WHERE tweet_id = t.id) AS comentarios
        FROM tweets t
        WHERE t.usuario_id = %s
        ORDER BY t.fecha_hora DESC
        """
        cursor.execute(query, (usuario_id,))
        resultados = cursor.fetchall()
        if resultados:
            print("\n=== Tus Tweets ===")
            for tweet in resultados:
                print(f"ID: {tweet[0]}, Likes: {tweet[3]}, Comentarios: {tweet[4]}")
                print(f"Publicado: {tweet[2]}")
                print(f"Contenido: {tweet[1]}")
                print("-" * 40)
        else:
            print("❌ No tienes tweets publicados.")
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar tweets: {err}")
    finally:
        cursor.close()
