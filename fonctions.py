import json

#Definition d'une classe pokemon 
class Pokemon:
    def __init__(self,nom,type_pokemon,hp,attaque,defense):
        self.nom=nom
        self.type_pokemon=type_pokemon
        self.hp=hp
        self.attaque=attaque
        self.defense=defense
    
      # Fonction pour afficher les informations d'un Pokemon
    def __str__(self):
         return f"Nom: {self.nom}, Type: {self.type_pokemon}, HP: {self.hp}, Attaque: {self.attaque}, Defense: {self.defense}"

# Liste pour stocker les Pokemon crees
pokemon_list = [] 

# Fonction pour creer un Pokemon
def creerPokemon():
    nom = input("Entrez le nom du Pokemon : ")
    #Verifie si le pokemon existe dejà avec le nom
    for pokemon in pokemon_list:
        # Verifie si le pokemon existe
        if pokemon.nom.lower() == nom.lower():
            print(f"Pokemon {nom} existe deja.")
            return None   
    type_pokemon = input("Entrez le type du Pokemon : ")
    hp = int(input("Entrez le nombre de HP : "))
    attaque = int(input("Entrez le type d'attaque : "))
    defense = int(input("Entrez le type de defense : "))
    pokemon = Pokemon(nom,type_pokemon,hp,attaque,defense)
    return pokemon


#Cree un fichier json pour sauvegarder les pokemon
def saveList(filename="pokemonData.json"):
    try:
        with open(filename, "w") as file:
            jsonList = [pokemon.__dict__ for pokemon in pokemon_list]
            json.dump(jsonList, file)
            print(f"Pokemon sauvegardes {filename}.")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde: {e}")

#Affiche les pokemon du json 
def loadList(filename="pokemonData.json"):
    try:
        with open(filename, "r") as file:
            jsonList = json.load(file)
            for p in jsonList:
                pokemon = Pokemon(p["nom"], p["type_pokemon"], p["hp"], p["attaque"], p["defense"])
                pokemon_list.append(pokemon)
            print(f"Liste de pokemon cahrgee depuis {filename}.")
    except FileNotFoundError:
        print(f" Le fichier {filename} n'a pas etait trouver.")
    except json.JSONDecodeError:
        print(f"Erreur lors du decodage du fichier {filename}.")

# Fonction pour afficher les informations d'un Pokemon
def afficherPokemon(pokemon):
    print(f"Nom: {pokemon.nom}")
    print(f"Type: {pokemon.type_pokemon}")
    print(f"HP: {pokemon.hp}")
    print(f"Attaque: {pokemon.attaque}")
    print(f"Defense: {pokemon.defense}\n")