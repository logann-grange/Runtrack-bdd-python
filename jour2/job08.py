import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Zoo"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM animal;")

result = cursor.fetchall()

class Animal() :

    def __init__(self, id, nom, race, id_cage, date_naissance,pays):
        self.id = id
        self.nom = nom
        self.race = race
        self.id_cage = id_cage
        self.date_naissance = date_naissance
        self.pays = pays
        
    def return_data(self) :
        for animal in result :
            if animal[0] == self.id :
                return animal
            
    def add_to_bdd(self) :
        cursor.execute(f"INSERT INTO animal (nom, race, id_cage, date_naissance, pays) VALUES ('{self.nom}', '{self.race}', {self.id_cage}, '{self.date_naissance}', '{self.pays}');")
        mydb.commit()

    def delete_on_bdd(self) :
        cursor.execute(f"DELETE FROM animal WHERE id = {self.id};")
        mydb.commit()
    
    def change_name(self, name) :
        self.name = name
        cursor.execute(f"UPDATE animal SET nom = '{name}' WHERE id = {self.id};")
        mydb.commit()

    def change_race(self, race) :
        self.race = race
        cursor.execute(f"UPDATE animal SET race = '{race}' WHERE id = {self.id};")
        mydb.commit()

    def change_cage_id(self, cage_id) :
        self.id_cage = cage_id
        cursor.execute(f"UPDATE animal SET id_cage = {cage_id} WHERE id = {self.id};")
        mydb.commit()

    def change_pays(self, pays) :
        self.pays = pays
        cursor.execute(f"UPDATE animal SET pays = '{pays}' WHERE id = {self.id};")
        mydb.commit()

    def change_date(self, date) :
        self.date_naissance = date
        cursor.execute(f"UPDATE animal SET date_naissance = '{date}' WHERE id = {self.id};")
        mydb.commit()


class Cage() :

    def __init__(self, id, superficie, capacite):
        self.id = id
        self.superficie = superficie
        self.capacite = capacite

    def add_to_bdd(self) :
        cursor.execute(f"INSERT INTO cage (superficie, capacite) VALUES ({self.superficie}, {self.capacite});")
        mydb.commit()

    def delete_on_bdd(self) :
        cursor.execute(f"DELETE FROM cage WHERE id = {self.id};")
        mydb.commit()

    def change_superficie(self, superficie) :
        self.superficie = superficie
        cursor.execute(f"UPDATE cage SET superficie = {superficie} WHERE id = {self.id};")
        mydb.commit()

    def change_capacite(self, capacite) :
        self.capacite = capacite
        cursor.execute(f"UPDATE cage SET capacite = {capacite} WHERE id = {self.id};")
        mydb.commit()


class Zoo() :

    def __init__(self, animaux, cages):
        self.animaux = animaux
        self.cages = cages
        self.add_to_bdd()

    def print_animal_cage(self):
        for cage in self.cages :
            animal_in_cage = []
            print(f"cage {cage.id} :")
            for animal in self.animaux :
                if cage.id == animal.id_cage :
                    animal_in_cage.append(animal)
                    print(f"    {animal.id}, {animal.nom}, {animal.race}, {animal.date_naissance}, {animal.pays}")

    def print_all_animals(self) :
        for animal in self.animaux :
            print(f"    {animal.id}, {animal.nom}, {animal.race}, {animal.id_cage}, {animal.date_naissance}, {animal.pays}")

    def superficie_total(self) :
        total = 0
        for cage in self.cages :
            total += cage.superficie
        return total
    
    def add_to_bdd(self) :
        for animal in self.animaux :
            animal.add_to_bdd()

        for cage in self.cages : 
            cage.add_to_bdd()


list_animaux = [
    Animal(1, "Tigre", "", 1, "04/06/2015", "quelque part"),
    Animal(2, "Singe", "", 2, "04/08/2014", "quelque part"),
    Animal(3, "Rat", "", 3, "04/08/2024", "quelque part"),
    Animal(4, "Lion", "", 1, "04/08/2024", "quelque part")
]

list_cage = [
    Cage(1, 50, 3),
    Cage(2, 25, 4),
    Cage(3, 20, 10)
]

zoo = Zoo(list_animaux, list_cage)

cursor.close()
mydb.close()