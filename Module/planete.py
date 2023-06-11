from skyfield.api import load
import datetime
import numpy as np

class Planete:
    def __init__(self, nom_planete):

        self.nom_planete = nom_planete

        # Charger les données éphémérides pour toutes les planètes
        self.planete = load('de421.bsp')
        #récupère toutes les données de la planète ex : earth = planets['earth']
        self.classe_planete = planete['nom_planet']

        self.periode_revolution = 11
        self.rayon = 7
        self.masse = 11
        self.vitesse = 11
        self.excentricite = 0
        self.cst_gravitation = 6.7 *10**11 # m3 kg–1 s–2
        self.parametre_gravitationnel = self.masse * self.cst_gravitation
        #distance planete soleil
        #influance planete de la gravitation

    def coordonnees_planete(self, jour, mois, annee):
        """Calculates the buoyant force acting on the balloon at the given altitude."""
        #date,ra (tous les jour 2ans

        sun = planets['sun']

        # Obtention du temps actuel
        ts = load.timescale()

        # Date précise à laquelle vous souhaitez observer la planète
        date_observation = datetime.datetime(annee, mois, jour)  # Remplacez avec votre date d'observation

        # Obtention de la position de la planète à la date d'observation
        date = ts.utc(date_observation.year, date_observation.month, date_observation.day)
        astrometric = sun.at(date).observe(self.classe_planete)
        # Conversion en coordonnées astrométriques
        ra, dec, distance = astrometric.radec()

        #tableau coordonnées sur 10 ans
        temps_pos_planete = []
        for jour in range(10*365):
            pass


        return temps_pos_planete


