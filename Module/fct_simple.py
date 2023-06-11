def obtenir_flottant(question):
    """Vérifie que l'entrée de l'utilisateur est un nombre flottant.

    Input : Chaine de caractères avec la question posée à l'utilisateur

    Output : Nombre flottant entré par l'utilisateur"""
    while True:
        # Vérifiez constamment si une valeur a été saisie suivie de "Try"
        try:
            # Mettre la valeur entrée par l'utilisateur dans "entree"
            entree = input(question)
            # Essayez de le transformer en nombre flottant, s'il ne peut pas, nous passons à "except"
            valeur = float(entree)
            break
        except ValueError:
            # Si l'entree n'est pas un nombre flottant, nous avons une erreur
            print("Entrée invalide, un flottant est attendu, veuillez réessayer.")
    return valeur

def obtenir_entier(question):
    """Vérifie que l'entrée de l'utilisateur est un nombre entier.

    Input : Chaine de caractères avec la question posée à l'utilisateur

    Output : Nombre entier entré par l'utilisateur"""
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
            break
        except ValueError:
            # Si l'entree n'est pas un nombre flottant, nous avons une erreur
            print("Entrée invalide, un entier est attendu, veuillez réessayer.")
    return valeur