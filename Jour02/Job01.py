import mysql.connector


host = "localhost"
user = "root"
password = "mansour13"
database = "LaPlateforme"  


connection = None

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connecté à la base de données")

  
        query = "SELECT * FROM etudiant"
        cursor = connection.cursor()
        cursor.execute(query)
        students = cursor.fetchall()

        for student in students:
            print(student)

except mysql.connector.Error as err:
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur d'accès: Nom d'utilisateur ou mot de passe incorrect")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Erreur de base de données: La base de données spécifiée n'existe pas")
    else:
        print(f"Erreur inattendue: {err}")


finally:
  
    if connection is not None and connection.is_connected():
        connection.close()
        print("Connexion à la base de données fermée")
