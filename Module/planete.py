from skyfield.api import load, utc
import datetime
from datetime import timedelta
import numpy as np

class Planete:
    """
        Classe représentant une planète du système solaire et ses caractéristiques utiles au projet.

        Attributs :
            nom_planete (chaine de caractères) : Nom de la planète en Anglais reconnue par les données éphémérides.
            nom_planete_affichage (chaine de caractères) : Nom de la planète en Français.
            masse (flottant) : Masse de la planète en kilogrammes.
            periode_revolution (flottant) : Période de révolution de la planète en jours.
            rayon (flottant) : Rayon de la planète en kilomètres.
            rayon_orbite (flottant) : Rayon de l'orbite de la planète en kilomètres.
            vitesse (flottant) : Vitesse de la planète en kilomètres par heure.
            distance_soleil (flottant) : Distance de la planète par rapport au Soleil en kilomètres.
            parametre_gravitationnel (flottant) : Paramètre gravitationnel standard de la planète en km^3/s^2.
            nombre_annee (entier) : Nombre d'années utilisées pour les coordonnées des planètes.
            ephemeris : Données éphémérides pour toutes les planètes.

        Méthodes :
            __init__(self, numero_planete): Initialise une instance de la classe Planete.
            coordonnees_planete(self, jour, mois, annee): Récupère les coordonnées des planètes à la date indiquée
        """
    def __init__(self, numero_planete):
        """
            Initialise une instance de la classe Planete.

            Input :
            numero_planete (entier): Numéro de la planète indiquée par l'utilisateur.

            Output :
            Aucune.
        """

        # Liste des noms des planetes utilisées dans Skyfield afin de récupérer les données associées
        nom_planete_ordre = ['mercury barycenter', 'venus barycenter', 'earth barycenter', 'mars barycenter', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter', 'pluto barycenter']
        # Récupère le nom de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.nom_planete = nom_planete_ordre[numero_planete]

        # Liste des noms des planètes en français pour l'affichage
        nom_planete_affichage_ordre = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']
        # Récupère le nom en français de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.nom_planete_affichage = nom_planete_affichage_ordre[numero_planete]

        # Liste des masses des planètes dans le même ordre que leurs noms
        masse_planete_ordre = [3.3011e+23, 4.8675e+24, 5.9724e+24, 6.4171e+23, 1.8982e+27, 5.6834e+26, 8.6813e+25, 1.0241e+26, 1.303e+22] #kg
        # Récupère la masse de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.masse = masse_planete_ordre[numero_planete] #kg

        # Liste des périodes des planètes dans le même ordre que leur noms
        periode_planete_ordre = [87.97, 224.7, 365.26, 686.98, 4332.71, 10759.5, 30685.0, 60190.0, 90560.0] #jours
        # Récupère la période de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.periode_revolution = periode_planete_ordre[numero_planete] #jours

        # Liste des rayons des planètes dans le même ordre que leur noms
        rayon_planete_ordre = [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0, 1188.3] #km
        # Récupère le rayon de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.rayon = rayon_planete_ordre[numero_planete] #km

        # Calcule la distance entre le centre de la planète de départ/ d'arrivée et la position du vaisseau au départ/ à l'arrivée
        self.rayon_orbite = self.rayon * 1.05 #km

        # Liste des vitesse des planètes dans le même ordre que leur noms
        vitesse_planete_ordre = [172800, 126000, 104400, 86400, 46800, 36000, 25200, 18000, 18000] #km/h
        # Récupère la vitesse de la planète avec le numéro de la planète entrée par l'utilisateur.
        self.vitesse = vitesse_planete_ordre[numero_planete] #km/h

        # Liste des distance des planètes parrapport au soleil dans le même ordre que leur noms
        distance_au_soleil = [57910000, 108200000, 149600000, 227940000, 778330000, 1429400000, 2870990000, 4498250000, 5906380000] #km/h
        # Récupère la distance de la planète par rapport au soleil avec le numéro de la planète entrée par l'utilisateur.
        self.distance_soleil = distance_au_soleil[numero_planete] #km

        # Le paramètre gravitationnel standard est obtenu en multipliant la masse de l'astre par la constante gravitationnelle
        # (paramètre gravitationnel standard = M * G)
        # Calcule le paramètre gravitationel associé à l'astre entré
        self.parametre_gravitationnel = self.masse * 6.67 * 10**-20 #km^3/s^2

        self.nombre_annee = 20

        # Charger les données éphémérides pour toutes les planètes
        # Ephemeries comprises entre 1900 et 2050
        #self.ephemeris = load('de421.bsp')
        # Ephemeries comprises entre 1600 et 2200
        self.ephemeris = load('de405.bsp')

    def coordonnees_planete(self, jour, mois, annee):
        """
        Calcule les coordonnées de la planète à une date donnée.

        Input :
            jour (entier): Le jour de la date d'observation.
            mois (entier): Le mois de la date d'observation.
            annee (entier): L'année de la date d'observation.

        Output :
            Aucune.
        """

        # Date précise à laquelle vous souhaitez observer la planète
        date_observation = datetime.datetime(annee, mois, jour)

        # tableau des coordonnées sur 10 ans
        self.temps_pos_planete = np.zeros([4, self.nombre_annee * 365])

        ## Calcul de la position relative de la planète cible en fonction du soleil
        # Récupère les données associées à la planète cible
        planete_cible = self.ephemeris[self.nom_planete]
        # Récupère les données du soleil
        sun = self.ephemeris['sun']
        position_relative = planete_cible - sun

        ## Obtention de la position de la planète à la date d'observation
        # Charger une échelle de temps par défaut.
        ts = load.timescale()
        # Converti la date donnée en entrée par l'utilisateur en date UTC
        date = ts.utc(date_observation.year, date_observation.month, date_observation.day)

        # Boucle qui donne la date en fonction de la position de la planète.
        for jour in range(self.nombre_annee * 365):
            # Récupère la position relative à la date entrée
            astrometric = position_relative.at(date)
            # Conversion en coordonnées astrométriques
            ra, dec, distance = astrometric.radec()

            ## Temps (format jour/mois/année)
            # Récupère le jour
            self.temps_pos_planete[0, jour] = date.utc_datetime().day
            # Récupère le mois
            self.temps_pos_planete[1, jour] = date.utc_datetime().month
            # Récupère l'année
            self.temps_pos_planete[2, jour] = date.utc_datetime().year

            # Données astrométriques
            self.temps_pos_planete[3, jour] = ra.radians

            # Ajoute une journée à la date actuelle
            date = date + timedelta(days = 1)