
import numpy as np

# e = 0, nous considérons que les orbites sont circulaires
# On considère que le vaisseau est deja en orbite a basse alttitude avec une vitesse initiale non nulle


def calculer_vitesse_initiale(mission):
    """Calcule la vitesse initiale et d'arrivée du vaisseau en fonction de la hauteur de chaque oribite

    Input :
        Paramètre de gravitation standard de la planète de départ, rayon de l'orbite de la planète de départ
        Rayon

    Output :
        Vitesse du vaisseau avant d'entamer son changement d'orbite et vitesse d'arrivee pour etre en orbite à une hauteur donnée"""

    vitesse_initiale_vaisseau = np.sqrt(mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite)
    vitesse_arrivee_vaisseau = np.sqrt(mission['planete_arrivee'].parametre_gravitationnel / mission['planete_arrivee'].rayon_orbite)
    return vitesse_initiale_vaisseau, vitesse_arrivee_vaisseau

def determiner_instant_depart(mission):
    """Détermine le moment où le vaisseau doit partir pour consommer le moins de carburant possible et entamer l'orbite de Hohmann

    Input :
        planete_depart (ndarray): Tableau NumPy contenant les angles de la planète de départ (2 lignes : temps et angles).
        planete_arrivee (ndarray): Tableau NumPy contenant les angles de la planète d'arrivée (2 lignes : temps et angles).

    Output :
        Angle optimal pour entamer l'orbite et l'instant de départ (jour, minute, seconde)."""

    difference_angles = abs(mission['planete_depart'].temps_pos_planete[3]-mission['planete_arrivee'].temps_pos_planete[3])

    indices_minimum = np.where(difference_angles == np.min(difference_angles))[0]

    premier_indice_minimum = indices_minimum[3]

    # Afficher la valeur de l'angle correspondant au premier minimum
    premier_minimum = difference_angles[premier_indice_minimum]

    # Afficher le temps correspondant au premier minimum
    instant_depart = mission['planete_arrivee'].temps_pos_planete[3][premier_indice_minimum]

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
    vitesse_liberation_depart = np.sqrt(((2 * param_gravitation_soleil) / (distance_soleil_depart + distance_soleil_arrivee)) * (distance_soleil_arrivee / distance_soleil_depart))

    # Calcul de la vitesse à l'arrivée
    vitesse_arrivee = np.sqrt(((2 * param_gravitation_soleil) / (distance_soleil_depart + distance_soleil_arrivee)) * (distance_soleil_depart / distance_soleil_arrivee))

    # Calcul de la variation de vitesse delta-v au départ et à l'arrivée
    delta_v1 = vitesse_liberation_depart - vitesse_initiale_vaisseau
    delta_v2 = vitesse_arrivee_vaisseau - vitesse_arrivee

    return delta_v1, delta_v2

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
    duree_transfert = (np.pi / 2) * np.sqrt((distance_soleil_depart + distance_soleil_arrivee)**3 / (2 * param_gravitation_soleil))

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
    periode_synodique = 1 / ((1 / periode_planete_depart) - (1 / periode_planete_arrivee))

    return periode_synodique

def calculer_duree_mission(duree_transfert, periode_synodique):
    """Calcule la durée totale de la mission en fonction de la durée de transfert et de la période synodique.

    Input :
        duree_transfert (float): Durée estimée du transfert entre deux orbites.
        periode_synodique (float): Période synodique entre les deux planètes.

    Output :

    """
    # Demande à l'utilisateur s'il souhaite revenir sur la planète de départ
    question_utilisateur = input("Souhaitez-vous revenir sur la planète de départ (oui ou non) ?")

    if question_utilisateur == 'oui':
        # Calcule la durée totale de la mission si l'utilisateur souhaite revenir sur la planète de départ
        duree = duree_transfert + periode_synodique + duree_transfert
        print(f"Vous comptez revenir sur la planète initiale. La période totale de la mission sera de {duree} jours.")
    elif question_utilisateur == 'non':
        # Calcule la durée totale de la mission si l'utilisateur ne souhaite pas revenir sur la planète de départ
        duree = duree_transfert
        print(f"Vous comptez rester sur la planète initiale. La période totale de la mission sera de {duree} jours.")



