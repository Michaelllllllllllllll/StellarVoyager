def afficher_ihm(obtenir_entier, obtenir_flottant, Vaisseau, Planete):
    """Affiche l'interface utilisateur

    Input : aucune

    Output : dictionnaire avec les données d'entrées du problème"""
    mission = {}
    print("Voici les planètes du système solaire :\n1 - Mercure\n2 - Vénus\n3 - Terre\n4 - Mars\n5 - Jupiter\n6 - Saturne\n7 - Uranus\n8 - Neptune\n9 - Pluton")
    mission['numero_planete_depart'] = obtenir_entier("Veuillez entrer le numéro de la planète de départ de votre voyage : ") - 1
    mission['numero_planete_arrivee'] = obtenir_entier("Veuillez entrer le numéro de la planète d'arrivée de votre voyage : ") - 1
    mission['planete_depart'] = Planete(mission['numero_planete_depart'])
    mission['planete_arrivee'] = Planete(mission['numero_planete_arrivee'])
    mission['vaisseau'] = Vaisseau(obtenir_flottant)
    return mission