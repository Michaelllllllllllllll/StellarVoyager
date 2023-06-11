def afficher_ihm(obtenir_entier, obtenir_flottant, Vaisseau):
    """Affiche l'interface utilisateur

    Input : aucune

    Output : dictionnaire avec les données d'entrées du problème"""
    mission = {}
    print("Voici les planètes du système solaire :\n1 - Mercure\n2 - Vénus\n3 - Terre\n4 - Mars\n5 - Jupiter\n6 - Saturne\n7 - Uranus\n8 - Neptune\n9 - Pluton")
    mission['planete_depart'] = obtenir_entier("Veuillez entrer le numéro de la planète de départ de votre voyage : ")
    vaisseau = Vaisseau(obtenir_flottant)
    planete = ['Mercure', 'Vénus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']