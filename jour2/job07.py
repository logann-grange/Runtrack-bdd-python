import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Entreprise"
)

cursor = mydb.cursor()

# affichage des employé au salaire supérieur à 3000
cursor.execute("SELECT * FROM employe WHERE salaire >= 3000;")
result = cursor.fetchall()
print(result)

# affichage des employés et leurs services
cursor.execute("SELECT * FROM employe LEFT JOIN service ON employe.id_service = service.id;")
result = cursor.fetchall()
print(result)



class Employe() :
    def __init__(self, id):
        self.id = id
        self.data = self.return_employe()
        self.nom = self.data[1]
        self.prenom = self.data[2]
        self.salaire = self.data[3]
        self.id_service =  self.data[5]
        self.id_service = self.data[6]

    def refresh(self) :
        cursor.execute(f"SELECT * FROM employe LEFT JOIN service ON employe.id_service = service.id WHERE employe.id = {self.id};")
        self.data = cursor.fetchone()
        self.nom = self.data[1]
        self.prenom = self.data[2]
        self.salaire = self.data[3]
        self.id_service =  self.data[5]
        self.id_service = self.data[6]


    def return_employe(self) :
        for employe in result :
            if employe[0] == self.id :
                return employe
            
    def change_salaire(self, salaire) :
        cursor.execute(f"UPDATE employe SET salaire = {salaire} WHERE id = {self.id};")
        mydb.commit()
        self.refresh()

    def change_service(self, id_service) :
        cursor.execute(f"UPDATE employe SET id_service = {id_service} WHERE id = {self.id};")
        mydb.commit()
        self.refresh()




e1 = Employe(1)
print(e1.salaire)
e1.change_salaire(e1.salaire + 100)
print(e1.salaire)

cursor.close()
mydb.close()