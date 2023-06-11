def afficher_ihm():
    """Affiche l'interface utilisateur

    Input : aucune

    Output : dictionnaire avec les données d'entrées du problème"""
    mission = {}
    print("Voici les planètes du système solaire :\n1 - Mercure\n2 - Vénus\n3 - Terre\n4 - Mars\n5 - Jupiter\n6 - Saturne\n7 - Uranus\n8 - Neptune\n9 - Pluton")
    mission['planete_depart'] = obtenir_entier("Veuillez entrer le numéro de la planète de départ de votre voyage : ")
    vaisseau = Vaisseau()
    planete = ['Mercure', 'Vénus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']


def obtenir_entier(question):
    """Vérifie que l'entrée de l'utilisateur est un nombre entier.

    :param question: Une chaîne de caractères contenant la question posée à l'utilisateur.
    :type question: str

    :return: Le nombre entier entré par l'utilisateur.
    :rtype: int"""
    while True:
        # Vérifiez constamment si une valeur a été saisie suivie de "Try"
        try:
            # Mettre la valeur entrée par l'utilisateur dans "entree"
            entree = input(question)
            # Essayez de le transformer en nombre flottant, s'il ne peut pas, nous passons à "except"
            valeur = float(entree)
            if valeur % 1 != 0:
                valeur = ''
            valeur = int(valeur)
            return valeur
        except ValueError:
            # Si l'entree n'est pas un nombre flottant, nous avons une erreur
            print("Entrée invalide, un entier est attendu, veuillez réessayer.")