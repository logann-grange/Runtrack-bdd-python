import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

cursor = mydb.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage;")

result = cursor.fetchall()

print(f"La superficie de la Plateforme est de {result[0][0]} m²")

cursor.close()
mydb.close()