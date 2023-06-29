def StellarVoyager():
    """Cette fonction lance notre programme. Pour cela, elle importe toutes les fonctions néccéssaires et les exécute dans le bon ordre.
    """
    # Importe notre module contenant toutes nos fonctions
    import voyage as vy

    # Début la mission en lançant l'interface homme-machine
    mission = vy.afficher_ihm(vy.obtenir_entier, vy.obtenir_flottant, vy.Vaisseau, vy.Planete)

    # Debute les calculs pour la mission
    mission = vy.appel_fonctions_physique(mission)

    # Affiche un texte qui explique les paramètres de la mission à l'utilisateur
    vy.retour_utilisateur(mission)

    # Débute les calculs pour la mission
    mission = vy.appel_fonctions_physique(mission)

    # Affiche le graphique et les trajectoires associées à la mission effectuée (vaisseau et planètes)
    vy.afficher_trajectoire(mission)