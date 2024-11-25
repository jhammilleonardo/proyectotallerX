from conexion import conectar_db
from usuarios import registrar_usuario
from tweets import publicar_tweet, ver_tweets_usuario
from interacciones import dar_me_gusta, agregar_comentario, ver_comentarios

def menu_principal():
    conexion = conectar_db()
    if not conexion:
        return
    
    usuario_actual = None

    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Publicar un tweet")
        print("4. Ver tus tweets")
        print("5. Dar me gusta a un tweet")
        print("6. Comentar un tweet")
        print("7. Ver comentarios de un tweet")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            username = input("Nombre de usuario: ")
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            nombre_completo = input("Nombre completo (opcional): ")
            registrar_usuario(conexion, username, email, password, nombre_completo)
        elif opcion == "2":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            cursor = conexion.cursor()
            query = "SELECT id FROM usuarios WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            usuario = cursor.fetchone()
            if usuario:
                usuario_actual = usuario[0]
                print(f"\n✅ Bienvenido, @{username}.")
            else:
                print("❌ Usuario o contraseña incorrectos.")
            cursor.close()
        elif opcion == "3":
            if usuario_actual:
                contenido = input("Contenido del tweet (máximo 280 caracteres): ")
                if len(contenido) <= 280:
                    publicar_tweet(conexion, usuario_actual, contenido)
                else:
                    print("❌ El contenido supera los 280 caracteres.")
            else:
                print("❌ Debes iniciar sesión primero.")
        elif opcion == "4":
            if usuario_actual:
                ver_tweets_usuario(conexion, usuario_actual)
            else:
                print("❌ Debes iniciar sesión primero.")
        elif opcion == "5":
            if usuario_actual:
                tweet_id = int(input("ID del tweet: "))
                dar_me_gusta(conexion, tweet_id, usuario_actual)
            else:
                print("❌ Debes iniciar sesión primero.")
        elif opcion == "6":
            if usuario_actual:
                tweet_id = int(input("ID del tweet: "))
                contenido = input("Contenido del comentario (máximo 280 caracteres): ")
                if len(contenido) <= 280:
                    agregar_comentario(conexion, tweet_id, usuario_actual, contenido)
                else:
                    print("❌ El contenido supera los 280 caracteres.")
            else:
                print("❌ Debes iniciar sesión primero.")
        elif opcion == "7":
            tweet_id = int(input("ID del tweet: "))
            ver_comentarios(conexion, tweet_id)
        elif opcion == "8":
            print("¡Gracias por usar la red social X!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
    
    conexion.close()

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()




