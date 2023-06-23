def obtenir_flottant(question):
    """Vérifie que l'entrée de l'utilisateur est un nombre flottant.

    :param question: Contient la question posée à l'utilisateur.
    :type question: str

    :return: Le nombre entré par l'utilisateur.
    :rtype: float
    """
    while True:
        # Vérifiez constamment si une valeur a été saisie suivie de "Try"
        try:
            # Mettre la valeur entrée par l'utilisateur dans "entree"
            entree = input(question)
            # Essayez de le transformer en nombre flottant, s'il ne peut pas, nous passons à "except"
            valeur = float(entree)
            return valeur
        except ValueError:
            # Si l'entree n'est pas un nombre flottant, nous avons une erreur
            print("Entrée invalide, un flottant est attendu, veuillez réessayer.")

def obtenir_entier(question, minimum, maximum):
    """Vérifie que l'entrée de l'utilisateur est un nombre entier.

    :param question: Contient la question posée à l'utilisateur.
    :type question: str

    :return: Le nombre entré par l'utilisateur.
    :rtype: int
    """
    while True:
        # Vérifiez constamment si une valeur a été saisie suivie de "Try"
        try:
            # Mettre la valeur entrée par l'utilisateur dans "entree"
            entree = input(question)
            # Essayez de le transformer en nombre flottant, s'il ne peut pas, nous passons à "except"
            valeur = float(entree)
            if valeur % 1 != 0 or valeur > maximum or valeur < minimum :
                valeur = ''
            valeur = int(valeur)
            return valeur
        except ValueError:
            # Si l'entree n'est pas un nombre flottant, nous avons une erreur
            print(f"Entrée invalide, un entier entre {minimum} et {maximum} est attendu, veuillez réessayer.")