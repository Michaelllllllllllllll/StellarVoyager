def obtenir_flottant(question):
    """Vérifie que l'entrée de l'utilisateur est un nombre flottant.

    :param question: Une chaîne de caractères contenant la question posée à l'utilisateur.
    :type question: str

    :return: Le nombre flottant entré par l'utilisateur.
    :rtype: float"""
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