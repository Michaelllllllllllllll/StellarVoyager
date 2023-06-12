class Vaisseau:
    """Classe représentant un vaisseau.

    :ivar masse_vide: La masse du vaisseau à vide.
    :vartype masse_vide: float
    :ivar masse_reactive: La masse réactive du carburant.
    :vartype masse_reactive: float"""

    def __init__(self, obtenir_flottant):

        """Initialise un objet Vaisseau.

        :param obtenir_flottant: Une fonction qui permet d'obtenir un nombre flottant de l'utilisateur.
        :type obtenir_flottant: function"""
        self.masse_vide = obtenir_flottant('Entrer la masse à vide du vaisseau en kg : ')
        self.masse_reactive = obtenir_flottant('Entrer la masse de carburant réactif en kg : ')