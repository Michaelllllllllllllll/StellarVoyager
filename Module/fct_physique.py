import numpy as np
from skyfield.api import load, utc
from datetime import timedelta

# e = 0, nous considérons que les orbites sont circulaires
# On considère que le vaisseau est deja en orbite a basse alttitude avec une vitesse initiale non nulle

# Données du soleil utiles
param_gravitation_soleil = 132712440018	 # km3/s2
masse_soleil = 1.989 * 10**30 #kg

def determiner_instant_depart(mission):
    """Détermine le moment où le vaisseau doit partir pour consommer le moins de carburant possible et entamer l'orbite de Hohmann

    Input :
        planete_depart (ndarray): Tableau NumPy contenant les angles de la planète de départ (2 lignes : temps et angles).
        planete_arrivee (ndarray): Tableau NumPy contenant les angles de la planète d'arrivée (2 lignes : temps et angles).

    Output :
        Angle optimal pour entamer l'orbite et l'instant de départ (jour, minute, seconde)."""

    difference_angles = abs(mission['planete_depart'].temps_pos_planete[3] - mission['planete_arrivee'].temps_pos_planete[3])

    angle_objectif = np.pi - 2 * np.pi / mission['planete_arrivee'].periode_revolution * mission['duree_transfert']

    minimalisation = angle_objectif - difference_angles

    for indice in range(1, len(minimalisation)):
        if (minimalisation[indice] > 0 and minimalisation[indice-1] < 0) or (minimalisation[indice] < 0 and minimalisation[indice-1] > 0):
            break

    mission['indice'] = indice
    mission['angle_depart'] = mission['planete_depart'].temps_pos_planete[3,indice]

    mission['jour_depart'] = mission['planete_depart'].temps_pos_planete[0, indice]
    mission['mois_depart'] = mission['planete_depart'].temps_pos_planete[1, indice]
    mission['annee_depart'] = mission['planete_depart'].temps_pos_planete[2, indice]



    #Affichage de la date d'arrivée du vaisseau sur la planète
    ts = load.timescale()
    date_arrivee_planete = ts.utc(mission['annee_depart'], mission['mois_depart'], mission['jour_depart'])
    date_arrivee_planete = date_arrivee_planete + timedelta(days=int(mission['duree_transfert']))
    mission['jour_arrivee_planete'] = date_arrivee_planete.utc_datetime().day
    mission['mois_arrivee_planete'] = date_arrivee_planete.utc_datetime().month
    mission['annee_arrivee_planete'] = date_arrivee_planete.utc_datetime().year

    mission['indice'] += int(mission['duree_transfert'])

    return mission

def calculer_delta_v(mission):

    # Calcul de la vitesse de libération au départ
    vitesse_liberation_depart = abs(np.sqrt(((2 * param_gravitation_soleil) / (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)) * (mission['planete_arrivee'].distance_soleil / mission['planete_depart'].distance_soleil)))
    mission['delta_v1'] = abs(round(vitesse_liberation_depart - (mission['planete_depart'].vitesse / 3600), 2))

    return mission

def calculer_influence_planete(mission):

    mission['distance_influence'] = round(mission['planete_depart'].distance_soleil * (mission['planete_depart'].masse / masse_soleil)**(2/5), 2)
    return mission

def calculer_vitesse_orbite(mission):
    """
    :param mission:
    :return:
    """

    mission['vitesse_orbite_depart'] = round(np.sqrt(mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite), 2)
    mission['vitesse_orbite_arrivee'] = round(np.sqrt(mission['planete_arrivee'].parametre_gravitationnel / mission['planete_arrivee'].rayon_orbite), 2)

    energie_orbitale_planete_depart = ((mission['delta_v1'])**2 / 2) - (mission['planete_depart'].parametre_gravitationnel / mission['distance_influence'])
    mission['vitesse_liberation'] = round(np.sqrt(2 * (energie_orbitale_planete_depart + (mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite))), 2)

    #accélération
    mission['delta_v_orbite_depart'] = round(mission['vitesse_liberation'] - mission['vitesse_orbite_depart'], 2)
    #frein
    mission['delta_v_orbite_arrivee'] = round(mission['vitesse_orbite_arrivee'] - mission['vitesse_liberation'], 2)

    return mission

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
    mission['duree_transfert'] = abs((np.pi / 2) * np.sqrt((mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)**3 / (2 * param_gravitation_soleil)))
    mission['duree_transfert'] /= (3600 * 24)
    # Obtention de la position de la planète à la date d'observation

    return mission
def calculer_masse_carburant(mission):
    mission['carburant_sortie_orbite_init'] = mission['vaisseau'].masse_initiale * (1 - np.exp(-((abs(mission['delta_v_orbite_depart'])) / mission['vitesse_orbite_depart']))) - mission['vaisseau'].masse_charge_utile

    mission['carburant_entree_orbite_arrivee'] = (mission['vaisseau'].masse_initiale - mission['carburant_sortie_orbite_init']) * (1 - np.exp(-((abs(mission['delta_v_orbite_arrivee'])) / mission['vitesse_orbite_arrivee']))) - mission['vaisseau'].masse_charge_utile

    mission['poids_vaisseau'] = mission['vaisseau'].masse_charge_utile + mission['vaisseau'].masse_initiale + mission['carburant_sortie_orbite_init'] + mission['carburant_entree_orbite_arrivee']
    return mission
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

    return mission

def calculer_duree_mission(mission):
    """Calcule la durée totale de la mission en fonction de la durée de transfert et de la durée une fois sur place.

    Input :
        duree_transfert (float): Durée estimée du transfert entre deux orbites.
        periode_synodique (float): Période synodique entre les deux planètes.

    Output :

    """
    omega_depart = 360 / mission['planete_depart'].periode_revolution
    omega_arrivee = 360 / mission['planete_arrivee'].periode_revolution

    delta_omega = omega_depart - omega_arrivee

    phi = 360 + 180 - (omega_depart*mission['duree_transfert']) - (omega_depart*mission['duree_transfert'] - 180)

    mission['duree_sur_planete_arrivee'] = abs(phi / delta_omega)

    # Affichage de la date de départ du vaisseau sur la planète
    ts = load.timescale()
    date_depart_planete = ts.utc(mission['annee_arrivee_planete'], mission['mois_arrivee_planete'], mission['jour_arrivee_planete'])
    date_depart_planete = date_depart_planete + timedelta(days=int(mission["duree_sur_planete_arrivee"]))
    mission['jour_depart_planete'] = date_depart_planete.utc_datetime().day
    mission['mois_depart_planete'] = date_depart_planete.utc_datetime().month
    mission['annee_depart_planete'] = date_depart_planete.utc_datetime().year

    # récupère l'angle de départ du vaisseau

    mission['indice'] += int(mission["duree_sur_planete_arrivee"])
    try:
        mission['angle_depart_planete'] = mission['planete_depart'].temps_pos_planete[3, mission['indice']]
    except IndexError:
        print("\nErreur, la mission est trop longue, elle dépasse l'année maximale permise par nos données d'éphéméride.")
        mission['retour_oui_non'] = 'non'
        return mission

    # Demande à l'utilisateur s'il souhaite revenir sur la planète de départ

    question_utilisateur = input("Souhaitez-vous revenir sur la planète de départ (oui ou non) : ")

    if question_utilisateur == 'oui' or question_utilisateur == 'OUI' or question_utilisateur == 'o' or question_utilisateur == 'O':

        mission['retour_oui_non'] = 'oui'

        # Calcule la durée totale de la mission si l'utilisateur souhaite revenir sur la planète de départ
        mission['duree'] = abs(mission['duree_transfert'] + mission["duree_sur_planete_arrivee"] + mission['duree_transfert'])

        # Affichage de la date de retour du vaisseau sur la planète initiale
        ts = load.timescale()
        date_retour_mission = ts.utc(mission['annee_depart_planete'], mission['mois_depart_planete'], mission['jour_depart_planete'])
        date_retour_mission = date_retour_mission + timedelta(days=int(mission['duree_transfert']))
        mission['jour_retour_mission'] = date_retour_mission.utc_datetime().day
        mission['mois_retour_mission'] = date_retour_mission.utc_datetime().month
        mission['annee_retour_mission'] = date_retour_mission.utc_datetime().year


    elif question_utilisateur == 'non' or question_utilisateur == 'NON' or question_utilisateur == 'n' or question_utilisateur == 'N':

        mission['retour_oui_non'] = 'non'

        # Calcule la durée totale de la mission si l'utilisateur ne souhaite pas revenir sur la planète de départ
        mission['duree'] = abs(mission['duree_transfert'])


    return mission

def appel_fonctions_physique(mission, retour_utilisateur):
    """a faire"""

    mission = calculer_duree_transfert(mission)
    mission = determiner_instant_depart(mission)
    mission = calculer_delta_v(mission)
    mission = calculer_influence_planete(mission)
    mission = calculer_vitesse_orbite(mission)
    mission = calculer_masse_carburant(mission)
    mission = calculer_periode_synodique(mission)
    mission = calculer_duree_mission(mission)
    retour_utilisateur(mission)

    return mission