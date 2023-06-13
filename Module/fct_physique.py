import numpy as np

# e = 0, nous considérons que les orbites sont circulaires
# On considère que le vaisseau est deja en orbite a basse alttitude avec une vitesse initiale non nulle

param_gravitation_soleil = 132712440018	 # km3/s2
masse_soleil = 1.989 * 10**30 #kg

def determiner_instant_depart(mission):
    """Détermine le moment où le vaisseau doit partir pour consommer le moins de carburant possible et entamer l'orbite de Hohmann

    Input :
        planete_depart (ndarray): Tableau NumPy contenant les angles de la planète de départ (2 lignes : temps et angles).
        planete_arrivee (ndarray): Tableau NumPy contenant les angles de la planète d'arrivée (2 lignes : temps et angles).

    Output :
        Angle optimal pour entamer l'orbite et l'instant de départ (jour, minute, seconde)."""

    difference_angles = abs(mission['planete_depart'].temps_pos_planete[3]-mission['planete_arrivee'].temps_pos_planete[3])

    indices_minimum = np.where(difference_angles == np.min(difference_angles))[0]

    premier_indice_minimum = indices_minimum[0]

    # Afficher la valeur de l'angle correspondant au premier minimum
    premier_minimum = difference_angles[premier_indice_minimum]

    # Afficher le temps correspondant au premier minimum
    instant_depart = mission['planete_arrivee'].temps_pos_planete[0][premier_indice_minimum]
    print(premier_minimum)
    print(instant_depart)

    return premier_minimum, instant_depart


def calculer_delta_v(mission):
    """Calcule la variation de vitesse (delta-v) nécessaire pour passer d'une orbite autour du Soleil à une autre,
        en tenant compte des vitesses initiales et finales du vaisseau.

        Input :
            param_gravitation_soleil (float): Paramètre gravitationnel du Soleil.
            distance_soleil_depart (float): Distance entre le Soleil et le point de départ.
            distance_soleil_arrivee (float): Distance entre le Soleil et le point d'arrivée.
            vitesse_initiale_vaisseau (float): Vitesse initiale du vaisseau avant le changement d'orbite.
            vitesse_arrivee_vaisseau (float): Vitesse à l'arrivée du vaisseau après le changement d'orbite.

        Output :
            variation de vitesse delta-v requise au départ et à l'arrivée.
        """

    # Calcul de la vitesse de libération au départ
    vitesse_liberation_depart = abs(np.sqrt(((2 * param_gravitation_soleil) / (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)) * (mission['planete_arrivee'].distance_soleil / mission['planete_depart'].distance_soleil)))

    # Calcul de la vitesse à l'arrivée
    vitesse_arrivee = abs(np.sqrt(((2 * param_gravitation_soleil) / (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)) * (mission['planete_depart'].distance_soleil / mission['planete_arrivee'].distance_soleil)))

    # Calcul de la variation de vitesse delta-v au départ et à l'arrivée
    delta_v1 = abs(round(vitesse_liberation_depart - (mission['planete_depart'].vitesse / 3600), 2))
    delta_v2 = abs(round((mission['planete_arrivee'].vitesse / 3600) - vitesse_arrivee, 2))

    print(f"delta_v1 = {delta_v1} km/s")
    print(f"delta_v2 = {delta_v2} km/s")
    print("je dois commenter tous les deltav")

    return delta_v1

def calculer_influence_planete(mission):
    distance_influence = round(mission['planete_depart'].distance_soleil * (mission['planete_depart'].masse / masse_soleil)**(2/5), 2)
    print(f"influence : {distance_influence} km")
    return distance_influence
def calculer_vitesse_orbite_depart(mission, delta_v1, distance_influence):
    """
    :param mission:
    :return:
    """

    vitesse_orbite = round(np.sqrt(mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite), 2)
    print(f"Vitesse orbite : {vitesse_orbite} km/s")
    energie_orbitale_planete_depart = ((delta_v1)**2 / 2) - (mission['planete_depart'].parametre_gravitationnel / distance_influence)
    vitesse_liberation = round(np.sqrt(2 * (energie_orbitale_planete_depart + (mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite))), 2)
    print(f"vitesse de liberation : {vitesse_liberation} km/s.")
    delta_v_orbite_planete_arrivee = round(vitesse_liberation - vitesse_orbite, 2)
    print(f"delta_v_mars = {delta_v_orbite_planete_arrivee} km/s")


def calculer_duree_transfert(mission):
    """Calcule la durée estimée du transfert entre deux orbites autour du Soleil.

    Input :
        param_gravitation_soleil (float): Paramètre gravitationnel du Soleil.
        distance_soleil_depart (float): Distance entre le Soleil et le point de départ.
        distance_soleil_arrivee (float): Distance entre le Soleil et le point d'arrivée.

    Output :
        La durée estimée du transfert en ***.
    """
    # Calcul de la durée estimée du transfert
    duree_transfert = abs((np.pi / 2) * np.sqrt((mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)**3 / (2 * param_gravitation_soleil)))
    duree_transfert /= (3600 * 24)
    print(f"La durée du voyage sera de {int(duree_transfert)} jours, soit environ {round(duree_transfert/30, 2)} mois.")

    return duree_transfert


def calculer_periode_synodique(mission):
    """Calcule la période synodique entre deux planètes.

    Input :
        periode_planete_depart (float): Période orbitale de la planète de départ.
        periode_planete_arrivee (float): Période orbitale de la planète d'arrivée.

    Output :
        La période synodique entre les deux planètes en jour.
    """

    # Calcul de la période synodique
    periode_synodique = abs(round(1 / ((1 / mission['planete_depart'].periode_revolution) - (1 / mission['planete_arrivee'].periode_revolution)), 0))

    print(f"Il faut en moyenne attendre {int(periode_synodique)} jours pour avoir la meilleure fenetre de lancement, ne loupez pas le coche.")



def calculer_duree_mission(duree_transfert, mission):
    """Calcule la durée totale de la mission en fonction de la durée de transfert et de la durée une fois sur place.

    Input :
        duree_transfert (float): Durée estimée du transfert entre deux orbites.
        periode_synodique (float): Période synodique entre les deux planètes.

    Output :

    """
    omega_depart = 360 / mission['planete_depart'].periode_revolution
    omega_arrivee = 360 / mission['planete_arrivee'].periode_revolution

    delta_omega = omega_depart - omega_arrivee

    phi = 360 + 180 - (omega_depart*duree_transfert) - (omega_depart*duree_transfert - 180)

    duree_sur_planete_arrivee = abs(phi / delta_omega)
    print(f"Une fois sur place, vous devrez attendre {int(duree_sur_planete_arrivee)} jours, soit environ {round(duree_sur_planete_arrivee / 30, 2)} mois.")

    # Demande à l'utilisateur s'il souhaite revenir sur la planète de départ
    question_utilisateur = input("Souhaitez-vous revenir sur la planète de départ (oui ou non) ?")

    if question_utilisateur == 'oui':
        # Calcule la durée totale de la mission si l'utilisateur souhaite revenir sur la planète de départ
        duree = abs(duree_transfert + duree_sur_planete_arrivee + duree_transfert)
        print(f"Vous comptez revenir sur la planète initiale. La période totale de la mission sera alors de {int(duree)} jours, soit environ {round(duree/30, 2)} mois.")
    elif question_utilisateur == 'non':
        # Calcule la durée totale de la mission si l'utilisateur ne souhaite pas revenir sur la planète de départ
        duree = abs(duree_transfert)
        print(f"Vous comptez rester sur la planète initiale. La période totale de la mission sera de {int(duree)} jours, soit environ {round(duree/30, 2)} mois.")

def appel_fonctions_physique(mission):
    """a faire"""
    determiner_instant_depart(mission)
    delta_v1 = calculer_delta_v(mission)
    distance_influence = calculer_influence_planete(mission)
    calculer_vitesse_orbite_depart(mission, delta_v1, distance_influence)
    duree_transfert = calculer_duree_transfert(mission)
    calculer_periode_synodique(mission)
    calculer_duree_mission(duree_transfert, mission)