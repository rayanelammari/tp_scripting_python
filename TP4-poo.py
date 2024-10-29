class Pokemon:
    def __init__(self,nom,type_pokemon,hp,attaque,defense):
        self.nom=nom
        self.type_pokemon=type_pokemon
        self.hp=hp
        self.attaque=attaque
        self.defense=defense

    # Fonction pour afficher les informations d'un Pokémon
    def afficher_pokemon(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type_pokemon}")
        print(f"HP: {self.hp}")
        print(f"Attaque: {self.attaque}")
        print(f"Défense: {self.defense}\n")


myPokemon = Pokemon("Pikachu","Eclair",145,100,85) #Instanciation d'un objet de la classe Pokemon
myPokemon.afficher_pokemon() #Appel de la fonction d'affichage
myPokemon.hp=100 #Modification d'un attribut de l'objet
myPokemon.afficher_pokemon() #Affiche l'objet avec le nouveau hp