class Vaisseau:
    """Classe représentant un vaisseau spatial et ses caractéristiques.

    :ivar float masse_charge_utile: La masse de charge utile que l'utilisateur veut emmener l'incluant pour le voyage (en kg)
    :ivar float masse_initiale: La masse initiale pour le début d'une manoeuvre (sans le carburant) en kg.

    :classmethod: __init__(self, obtenir_flottant): Initialise un objet Vaisseau.
    """
    def __init__(self, obtenir_flottant):
        """Le constructeur de cette classe initialise le vaisseau en demandant à l'utilisateur la charge utile qu'il souhaite embarquer.

        :param fct obtenir_flottant: Vérifie que l'entrée de l'utilisateur est un nombre flottant.

        :return: Aucun
        """
        # Demande à l'utilisateur la masse de charge utile
        self.masse_charge_utile = obtenir_flottant('Entrer la masse de charge utile que vous voulez emmener avec vous en kg : ')
        # Utilise un coefficient empirique pour trouver la masse initiale du vaisseau
        self.masse_initiale = 15 * self.masse_charge_utile
        pass