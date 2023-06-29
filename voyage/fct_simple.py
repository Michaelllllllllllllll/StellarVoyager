def obtenir_flottant(question):
    """Cette fonction vérifie que l'entrée de l'utilisateur est un nombre flottant. Sinon elle lui demande en boucle d'entrée un nombre flottant.

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
            # Sortie de la fonction
            return valeur
        except ValueError:
            # Si l'entrée n'est pas un nombre flottant, nous avons une erreur
            print("Entrée invalide, un flottant est attendu, veuillez réessayer.")

def obtenir_entier(question, minimum, maximum):
    """Cette fonction vérifie que l'entrée de l'utilisateur est un nombre entier compris entre les bornes fournies en entrée. Sinon elle lui demande en boucle d'entrée un nombre entier et précise les bornes à respecter.

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
            # Vérification que le nombre est un entier et qu'il est compris entre le minimum et le maximum
            if valeur % 1 != 0 or valeur > maximum or valeur < minimum:
                # Création d'une erreur pour passer dans le "except"
                valeur = ''
            # Essayez de le transformer en nombre entier, s'il ne peut pas, nous passons à "except"
            valeur = int(valeur)
            # Sortie de la fonction
            return valeur
        except ValueError:
            # Si l'entree n'est pas un nombre entier entre le minimum et le maximum, nous avons une erreur
            print(f"Entrée invalide, un entier entre {minimum} et {maximum} est attendu, veuillez réessayer.")