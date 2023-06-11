from skyfield.api import load, utc
import datetime
from datetime import timedelta
import numpy as np
#import math

class Planete:
    def __init__(self, numero_planete):

        nom_planete_ordre = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
        self.nom_planete = nom_planete_ordre[numero_planete]

        masse_planete_ordre = [3.3011e+23, 4.8675e+24, 5.9724e+24, 6.4171e+23, 1.8982e+27, 5.6834e+26, 8.6813e+25, 1.0241e+26, 1.303e+22] #kg
        self.masse = masse_planete_ordre[numero_planete]

        periode_planete_ordre = [87.97, 224.7, 365.26, 686.98, 4332.71, 10759.5, 30685.0, 60190.0, 90560.0] #jour
        self.periode_revolution = periode_planete_ordre[numero_planete]

        rayon_planete_ordre = [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0, 1188.3] #km
        self.rayon = rayon_planete_ordre[numero_planete]

        self.rayon_orbite = self.rayon + 300

        vitesse_planete_ordre = [172800, 126000, 104400, 86400, 46800, 36000, 25200, 18000, 18000] #km/h
        self.vitesse = vitesse_planete_ordre[numero_planete]

        self.parametre_gravitationnel = self.masse * 6.67 *10**-11

        self.nombre_annee = 10

        # Charger les données éphémérides pour toutes les planètes
        self.ephemeris = load('de421.bsp')

    def coordonnees_planete(self, jour, mois, annee):

        # Date précise à laquelle vous souhaitez observer la planète
        date_observation = datetime.datetime(annee, mois, jour)

        #tableau coordonnées sur 10 ans
        temps_pos_planete = np.zeros([4, self.nombre_annee * 365])

        planete_cible = self.ephemeris[self.nom_planete]
        sun = self.ephemeris['sun']
        position_relative = planete_cible - sun

        # Obtention de la position de la planète à la date d'observation
        ts = load.timescale()
        date = ts.utc(date_observation.year, date_observation.month, date_observation.day)

        for jour in range(self.nombre_annee * 365):
            astrometric = position_relative.at(date)
            # Conversion en coordonnées astrométriques
            ra, dec, distance = astrometric.radec()

            temps_pos_planete[0,jour] = date.utc_datetime().day
            temps_pos_planete[1,jour] = date.utc_datetime().month
            temps_pos_planete[2,jour] = date.utc_datetime().year
            temps_pos_planete[3,jour] = ra.radians

            date = date + timedelta(days = 1)

        return temps_pos_planete