class Vaisseau:
    """Classe représentant un vaisseau.

    :ivar masse_vide: La masse du vaisseau à vide.
    :vartype masse_vide: float
    :ivar masse_reactive: La masse réactive du carburant.
    :vartype masse_reactive: float"""

    def __init__(self):
        """Initialise un objet Vaisseau.

        :param float masse_vide: La masse du vaisseau à vide.
        :param float masse_reactive: La masse réactive du carburant."""
        self.masse_vide = obtenir_flottant('Entrer la masse à vide du vaisseau : ')
        self.masse_reactive = obtenir_flottant('Entrer la masse de carburant réactif : ')

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
