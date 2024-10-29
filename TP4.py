import json
#Suite du TP1, en ajoutant la saisie du nombre de pokemon par l'utilisateur et vérifier si le pokemon existe déjà dans la liste

# Liste pour stocker les Pokémon créés
pokemon_list = []

 # Fonction pour créer un Pokémon
def creer_pokemon():
    nom = input("Entrez le nom du Pokémon : ")
    #Vérifie si le pokemon existe déjà avec le nom
    for pokemon in pokemon_list:
        # Check if the Pokemon already exists
        if pokemon['nom'].lower() == nom.lower():
            print(f"Pokemon {nom} already exists.")
            return None
    type_pokemon = input("Entrez le type du Pokémon : ")
    hp = int(input("Entrez le nombre de HP : "))
    attaque = int(input("Entrez le type d'attaque : "))
    defense = int(input("Entrez le type de défense : "))
    pokemon = {
        "nom": nom,
        "type_pokemon": type_pokemon,
        "hp": hp,
        "attaque": attaque,
        "defense": defense
    }
    return pokemon

exit = False
while exit != True:
# Call newPokemon for interact with user and create pokemon
    new = creer_pokemon()
    if new:
        pokemon_list.append(new) 
    choice = input("Do you want to create another Pokemon? (y/n): ")
    if choice.lower() != "y":
        exit = True


# Fonction pour afficher les informations d'un Pokémon
def afficher_pokemon(pokemon):
    print(f"Nom: {pokemon['nom']}")
    print(f"Type: {pokemon['type_pokemon']}")
    print(f"HP: {pokemon['hp']}")
    print(f"Attaque: {pokemon['attaque']}")
    print(f"Défense: {pokemon['defense']}\n")



exit = False
while exit != True:
# Call newPokemon for interact with user and create pokemon
    new = creer_pokemon()
    if new:
        pokemon_list.append(new) 
    choice = input("Do you want to create another Pokemon? (y/n): ")
    if choice.lower() != "y":
        exit = True

# Afficher les informations des pokemon en parcourant la liste
print("\n--- Informations des Pokémon créés ---")
for pokemon in pokemon_list:
    afficher_pokemon(pokemon)

#Créer un fichier json pour sauvegarder les pokemon 
with open("file.json","a") as pokemon_file:
    print(pokemon_file.write(str(pokemon_list).replace("\'", "\"")))
    


