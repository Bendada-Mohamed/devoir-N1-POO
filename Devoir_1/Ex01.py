from abc import ABC, abstractmethod
import json
# Classe Animal avec methode abstraite
class Animal(ABC):
    def __init__(self,code, nom_scientifique, espece, nombre_de_pieds, pays_dorigine):
        self.__code = int(code)
        self.__nom_scientifique = str(nom_scientifique)
        self.__espece = str(espece)
        self.__nombre_de_pieds = int(nombre_de_pieds)
        self.__pays_dorigine = str(pays_dorigine)
# Selecteurs
    def get_code(self):
        return self.__code
    def get_nom_scientifique(self):
        return self.__nom_scientifique
    def get_espece(self):
        return self.__espece
    def get_nombre_de_pieds(self):
        return self.__nombre_de_pieds
    def get_pays_dorigine(self):
        return self.__pays_dorigine
# Mutateurs
    def set_code(self, code):
        self.__code = code
    def set_nom_scientifique(self, nom_scientifique):
        self.__nom_scientifique = nom_scientifique
    def set_espece(self, espece):
        self.__espece = espece
    def set_nombre_de_pieds(self, nombre_de_pieds):
        self.__nombre_de_pieds = nombre_de_pieds
    def set_pays_dorigine(self, pays_dorigine):
        self.__pays_dorigine = pays_dorigine
# Methode Afficher les informations de l'animal
    def afficher_info(self):
        return (f" Code :{self.get_code()},"
                f" Nom scientifique :{self.get_nom_scientifique()},"
                f" Espece :{self.get_espece()},"
                f" Nombre de pieds :{self.get_nombre_de_pieds()},"
                f" Pays dorigine:{self.get_pays_dorigine()}")
    # Methode abstraite se deplacer
    @abstractmethod
    def se_deplacer(self):
        pass
# les classes filles
# Chien
class Chien(Animal):
    def afficher_info(self):
        return f"{super().afficher_info()} | Se deplace : {self.se_deplacer()}"
    def se_deplacer(self):
            return f"{self.get_espece()} se deplace sur {self.get_nombre_de_pieds()} pieds."
# Chat
class Chat(Animal):
    def se_deplacer(self):
        return f"{self.get_espece()} se deplace sur {self.get_nombre_de_pieds()} pieds."
    def afficher_info(self):
        return f"{super().afficher_info()} | Se deplace : {self.se_deplacer()}"
# Poulet
class Poulet(Animal):
    def se_deplacer(self):
            return f"{self.get_espece()} se deplace sur {self.get_nombre_de_pieds()} pieds."
    def afficher_info(self):
        return f"{super().afficher_info()} | se deplace : {self.se_deplacer()}"
# Vache
class Vache(Animal):
    def se_deplacer(self):
            return f"{self.get_espece()} se deplace sur {self.get_nombre_de_pieds()} pieds."
    def afficher_info(self):
        return f"{super().afficher_info()} | se deplace : {self.se_deplacer()}"

# Classe Zoo
class Zoo:
    def __init__(self, nom, superficie):
        self.nom = nom
        self.superficie = superficie
        self.tableaux_danimaux = []
# Methode Ajouter Animal
    def ajouter_animal(self, nouveau_animal):
        self.tableaux_danimaux.append(nouveau_animal)
        print(f"animal ajoute : {nouveau_animal.afficher_info()}")
# Methode Supprimer Animal
    def supprimer_animal(self, code):
        for i in self.tableaux_danimaux:
            if i.get_code() == code:
                self.tableaux_danimaux.remove(i)
                print(f"animal supprime : {i.afficher_info()}")
                return
        print("aucun animal avec ce code na ete trouve.")

# Methode Update Animal
    def update_animal(self, code, **kwargs):
        for i in self.tableaux_danimaux:
            if i.get_code() == code:
                if 'nom_scientifique' in kwargs:
                    i.set_nom_scientifique(kwargs['nom_scientifique'])
                if 'espece' in kwargs:
                    i.set_espece(kwargs['espece'])
                if 'nombre_de_pieds' in kwargs:
                    i.set_nombre_de_pieds(kwargs['nombre_de_pieds'])
                if 'pays_dorigine' in kwargs:
                    i.set_pays_dorigine(kwargs['pays_dorigine'])
                print(f"Animal mise a jour : {i.afficher_info()}")
                return
        print("aucun animal avec ce code na ete trouve")
# Methode Chercher Animal
    def chercher_animal(self, espece):
        animaux_trouves = []
        for animal in self.tableaux_danimaux:
                if animal.get_espece() == espece:
                    animaux_trouves.append(animal)
        if animaux_trouves:
            print(f"Animaux trouve pour lespece '{espece}'")
            for animal in animaux_trouves:
                print(animal.afficher_info())
        else:
            print(f"aucun animal trouve pour l'espece '{espece}'")
# Methode Nombre Animal
    def nombre_animal(self, nom_scientifique):
        count = sum(1 for animal in self.tableaux_danimaux if animal.get_nom_scientifique() == nom_scientifique)
        return f"le nombre animal sous le nom : '{nom_scientifique}' est :{count} animal"

#Methode Tri Animal
    def tri_animal(self):
        def get_animal_code(animal):
            return animal.get_code()
        self.tableaux_danimaux.sort(key = get_animal_code)
        print("animaux tries par code")
# Methode Afficher Animal
    def afficher_animal(self):
        print(f"les animaux qui exist dans zoo de {self.nom} sont :")
        for animal in self.tableaux_danimaux:
            print(animal.afficher_info())
# Methode Enregistrer animal
    def enregistrer_animal(self):
        with open('animals.txt','w') as fichier:
            for animal in self.tableaux_danimaux:
                fichier.write(f"{animal.afficher_info()}\n")
# Methode Load Animals from JSON
    def load_json(self, nomficher):
        animaux = []
        with open(nomficher, "r") as file:
            contenu = json.load(file)
        for dictionair in contenu:
            espece = dictionair['espece']
            if espece == 'Chien':
                animal = Chien(dictionair['code'], dictionair['nom_scientifique'], dictionair['espece'], dictionair['nombre_de_pieds'], dictionair['pays_dorigine'])
            elif espece == 'Chat':
                animal = Chat(dictionair['code'], dictionair['nom_scientifique'], dictionair['espece'], dictionair['nombre_de_pieds'], dictionair['pays_dorigine'])
            elif espece == 'Poulet':
                animal = Poulet(dictionair['code'], dictionair['nom_scientifique'], dictionair['espece'], dictionair['nombre_de_pieds'], dictionair['pays_dorigine'])
            elif espece == 'Vache':
                animal = Vache(dictionair['code'], dictionair['nom_scientifique'], dictionair['espece'], dictionair['nombre_de_pieds'], dictionair['pays_dorigine'])
            else:
                class GenericAnimal(Animal):
                    def se_deplacer(self):
                        return f"{espece} marche avec ses {dictionair['nombre_de_pieds']} pieds."
                    def afficher_info(self):
                        return f"{super().afficher_info()} | se deplace : {self.se_deplacer()}"
                animal = GenericAnimal(dictionair["code"], dictionair["nom_scientifique"], espece, dictionair["nombre_de_pieds"], dictionair["pays_dorigine"])
            animaux.append(animal)
        print("les animaux importer de jsonfile homa hado")
        for animal in animaux:
            print(animal.afficher_info())


chien = Chien(1, "Canis lupus", "Chien", 4, "France")
chat = Chat(2, "Felis catus", "Chat", 4, "Allemagne")
poulet = Poulet(3, "Gallus gallus", "Poulet", 2, "Tamesna")
vache = Vache(4, "Bos taurus", "Vache", 4, "Maroc")

# Exemple de test avec le zoo
zoo_tamesna = Zoo("Tamesna", 500)


# Ajouter des animaux
zoo_tamesna.ajouter_animal(Chien(3, "Canis lupus", "Chien", 4, "France"))
zoo_tamesna.ajouter_animal(Chat(2, "Felis catus", "Chat", 4, "Allemagne"))
zoo_tamesna.ajouter_animal(Poulet(1, "Gallus gallus", "Poulet", 2, "Tamesna"))
# zoo_tamesna.afficher_animal()
zoo_tamesna.tri_animal()
zoo_tamesna.afficher_animal()
# zoo_tamesna.load_json('animals.json')
# print(zoo_tamesna.nombre_animal("Canis lupus"))

# Mettre à jour un animal
# zoo_tamesna.update_animal(2, nom_scientifique="Felis silvestris", pays_dorigine="Italie")
# zoo_tamesna.afficher_animal()
# Supprimer un animal
# zoo_tamesna.supprimer_animal(3)
# zoo_tamesna.afficher_animal()
# zoo_tamesna.enregistrer_animal()


