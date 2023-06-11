import skyfield

class Planete:
    def __init__(self, nom_planete):
        self.nom_planete = nom_planete
        self.periode = 6
        self.rayon = 7
        self.masse = 5
        self.vitesse = 5
        self.excentricite = 0
        self.cst_gravitation = 6.7 *10**11 # m3 kg–1 s–2
        self.parametre_gravitationnel = self.masse * self.cst_gravitation
        #distance planete soleil
        #influance planete de la gravitation

    def coordonnées_debut(self):
        """Calculates the buoyant force acting on the balloon at the given altitude."""
        return 4*6
    def coordonnées_fin(self):
        """Calculates the buoyant force acting on the balloon at the given altitude."""
        return 4*6