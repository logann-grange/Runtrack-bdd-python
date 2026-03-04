import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
cursor.execute("SELECT nom, capacite FROM salle;") #requete

result = cursor.fetchall() # retourne toutes les lignes de la requettes

#result = cursor.fetchone() # retourne la 1ere ligne de la requete

print(result)

cursor.close()
mydb.close()