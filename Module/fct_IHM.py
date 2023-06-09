from fct_simple import obtenir_flottant

def afficher_ihm():
    """Affiche l'interface utilisateur

    Input : aucune

    Output : dictionnaire avec les données d'entrées du problème"""
    mission = {}
    print("Voici les planètes du système solaire :\n1 - Mercure\n2 - Vénus\n3 - Terre\n4 - Mars\n5 - Jupiter\n6 - Saturne\n7 - Uranus\n8 - Neptune\n9 - Pluton")
    print('hello1')
    mission['planete_depart'] = obtenir_flottant("Veuillez entrer le numéro de la planète de départ de votre voyage : ")
    print('hello2')