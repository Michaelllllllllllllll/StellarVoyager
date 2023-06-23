class Vaisseau:
    """Classe représent un vaisseau spatial et ses caractéristiques.

    :ivar float masse_vide: La masse à vide du vaisseau en kg.
    :ivar float masse_reactive: La masse de carburant réactif en kg.

    :classmethod: __init__(self, obtenir_flottant): Initialise un objet Vaisseau.
    """
    def __init__(self, obtenir_flottant):
        """Le constructeur.

        :param fct obtenir_flottant: Vérifie que l'entrée de l'utilisateur est un nombre flottant.
        """
        self.masse_charge_utile = obtenir_flottant('Entrer la masse de charge utile que vous voulez emmener avec vous en kg : ')
        self.masse_initiale = 15 * self.masse_charge_utile

        pass