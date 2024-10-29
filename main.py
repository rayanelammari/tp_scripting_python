import sys
from fonctions import creerPokemon,afficherPokemon,pokemon_list, saveList,loadList

#Charge le fichier au démarrage
loadList()
#verifie si le nom du pokemon est dans l'argument
if len(sys.argv) > 1:
    choice = sys.argv[1]
    # Cherche le nom du pokemon
    for pokemon in pokemon_list:
        if pokemon.nom.lower() == choice.lower():
            print(f"Choisir Pokemon : {pokemon}")
            sys.exit(0)

    print(f"Pokemon {choice} non trouve.")
    
else:
    exit = False
    while exit != True:
        #Appel de la fonction pour creer un pokemon à ajoute dans la liste
        new = creerPokemon()
        if new:
            pokemon_list.append(new) 
        choice = input("Voulez-vous creer un autre pokemon ? (y/n): ")
        if choice.lower() != "y":
            exit = True


# Afficher les informations des pokemon en parcourant la liste
print("\n--- Informations des Pokemon crees ---")
for pokemon in pokemon_list:
    afficherPokemon(pokemon)

#Enregistre
saveList()