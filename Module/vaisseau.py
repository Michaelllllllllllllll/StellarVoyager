class Vaisseau:
    def __init__(self, masse_vide, masse_reactive):
        """Classe Vaisseau
        :param float masse_vide: La masse du vaisseau à vide.
        :param float masse_reactive: La masse reactive du carburant.
        """
        self.masse_vide = masse_vide
        self.masse_reactive = masse_reactive
