import numpy as np
from skyfield.api import load, utc
from datetime import timedelta

# e = 0, nous considérons que les orbites sont circulaires
# Nous considérons que le vaisseau est déjà en orbite à basse altitude avec une vitesse initiale non nulle

# Données du soleil utiles (constantes)
param_gravitation_soleil = 132712440018	 #km^3/s^2
masse_soleil = 1.989 * 10**30 #kg

def determiner_instant_depart(mission):
    """Cette fonction détermine le moment où le vaisseau doit partir pour consommer le moins de carburant possible et entamer l'orbite de Hohmann. Pour cela, il cherche la date où l'angle entre la planète de départ et d'arrivée est adapté pour commencer le transfert.

    :param dict mission: Contient tous les paramètres utiles de la mission.
    :Formules utilisées:
    :math:`\\Phi = \\pi - \\Delta T~\\omega`

    :math:`\\Delta T` est le temps de trajet entre la planète de départ et d'arrivée.

    :math:`\\Phi` est l'angle entre la planète de départ et la planète d'arrivée au moment où le vaisseau doit partir.

    :math:`\\omega` est la vitesse angulaire de la planète d'arrivée autour du soleil.

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Création d'un tableau contenant les angles entre la planète de départ et d'arrivée au cours du temps
    difference_angles = abs(mission['planete_depart'].temps_pos_planete[3] - mission['planete_arrivee'].temps_pos_planete[3])

    #Calcul de l'angle qui permet le départ du vaisseau
    angle_objectif = np.pi - 2 * np.pi / mission['planete_arrivee'].periode_revolution * mission['duree_transfert']

    #Soustraction de l'angle recherché au tableau des angles pour chercher le zéro
    minimalisation = angle_objectif - difference_angles

    #Parcours le tableau des angles jusqu'au premier zéro
    for indice in range(1, len(minimalisation)):
        if (minimalisation[indice] > 0 and minimalisation[indice-1] < 0) or (minimalisation[indice] < 0 and minimalisation[indice-1] > 0):
            break

    #Récupère l'indice de l'instant de départ
    mission['indice'] = indice
    #Mémorise l'angle de la planète au moment du départ
    mission['angle_depart'] = mission['planete_depart'].temps_pos_planete[3,indice]
    #Mémorise la date au moment du départ
    mission['jour_depart'] = mission['planete_depart'].temps_pos_planete[0, indice]
    mission['mois_depart'] = mission['planete_depart'].temps_pos_planete[1, indice]
    mission['annee_depart'] = mission['planete_depart'].temps_pos_planete[2, indice]

    #Calcul de la date d'arrivée sur la planète d'arrivée
    ts = load.timescale()
    date_arrivee_planete = ts.utc(mission['annee_depart'], mission['mois_depart'], mission['jour_depart'])
    date_arrivee_planete = date_arrivee_planete + timedelta(days=int(mission['duree_transfert']))
    #Mémorise la date au moment d'arrivée
    mission['jour_arrivee_planete'] = date_arrivee_planete.utc_datetime().day
    mission['mois_arrivee_planete'] = date_arrivee_planete.utc_datetime().month
    mission['annee_arrivee_planete'] = date_arrivee_planete.utc_datetime().year

    #Calcul de l'indice dans le tableau du moment d'arrivée sur la planète d'arrivée
    mission['indice'] += int(mission['duree_transfert'])

    return mission

def calculer_energie_orbitale(mission):
    """Cette fonction calcule l'énergie orbitale qui est utilisée pour calculer la vitesse de libération du vaisseau.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :Formules utilisées:

    :math:`v_{périgée} = \\sqrt{\\frac{2\\mu_{soleil}}{d_{planète~initiale/soleil}+d_{planète~finale/soleil}}\\times \\frac{d_{planète~finale/soleil}}{d_{planète~initiale/soleil}}}`

    :math:`\\Delta v1 = v_{périgée} - v_{planète~initiale}`

    :math:`\\epsilon = \\frac{\\Delta v1^2}{2} - \\frac{\\mu_{planète~initiale}}{SOI}`

    :math:`\\epsilon` est l'énergie orbitale pour initier l'orbite de transfert vers la planète finale

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul de la vitesse de libération au départ
    vitesse_perigee = abs(np.sqrt(((2 * param_gravitation_soleil) / (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)) * (mission['planete_arrivee'].distance_soleil / mission['planete_depart'].distance_soleil)))
    #Calcul de la différence de vitesse
    mission['delta_v1'] = abs(round(vitesse_perigee - (mission['planete_depart'].vitesse / 3600), 2))
    #Calcul de l'énergie orbitale de la planète de départ
    mission["energie_orbitale_planete_depart"] = ((mission['delta_v1']) ** 2 / 2) - (mission['planete_depart'].parametre_gravitationnel / mission['distance_influence'])

    return mission

def calculer_influence_planete(mission):
    """Cette fonction calcule la distance maximale à laquelle la planète a toujours une influence sur le vaisseau.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul la distance maximale à laquelle la planète a toujours une influence sur le vaisseau
    mission['distance_influence'] = round(mission['planete_depart'].distance_soleil * (mission['planete_depart'].masse / masse_soleil)**(2/5), 2)

    return mission

def calculer_vitesse_orbite(mission):
    """Cette fonction calcule les vitesses en orbite des planètes de départ et d'arrivée.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :Formules utilisées:
    :math:`v_{orbite} = \\frac{\\mu_{planète}}{Rayon~orbite~planète}`

    :math:`v_{libération} = \\sqrt{2(\\epsilon _{planète} + \\frac{\\mu_{planète}}{Rayon~orbite~planète})}`

    :math:`\\Delta v_{départ} = v_{libération} - v_{orbite~départ}`

    :math:`\\Delta v_{arrivée} =  v_{orbite~arrivée} - v_{libération}`

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul la vitesse en orbite autour de la planète de départ
    mission['vitesse_orbite_depart'] = round(np.sqrt(mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite), 2)
    #Calcul la vitesse en orbite autour de la planète d'arrivée
    mission['vitesse_orbite_arrivee'] = round(np.sqrt(mission['planete_arrivee'].parametre_gravitationnel / mission['planete_arrivee'].rayon_orbite), 2)
    #Calcul la vitesse de libération
    mission['vitesse_liberation'] = round(np.sqrt(2 * (mission["energie_orbitale_planete_depart"] + (mission['planete_depart'].parametre_gravitationnel / mission['planete_depart'].rayon_orbite))), 2)

    #Calcul l'accélération au départ
    mission['delta_v_orbite_depart'] = round(mission['vitesse_liberation'] - mission['vitesse_orbite_depart'], 2)
    #Calcul la décélération à l'arrivée
    mission['delta_v_orbite_arrivee'] = round(mission['vitesse_orbite_arrivee'] - mission['vitesse_liberation'], 2)

    return mission

def calculer_duree_transfert(mission):
    """Cette fonction calcule la durée estimée du transfert entre deux planètes.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :Formules utilisées:
    :math:`\\frac{\\pi}{2}\\times\\sqrt{\\frac{(d_{planète~initiale/soleil}+d_{planète~finale/soleil})^3}{2\\mu _{soleil}}}`

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul de la durée estimée du transfert
    mission['duree_transfert'] = abs((np.pi / 2) * np.sqrt((mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil)**3 / (2 * param_gravitation_soleil)))
    #Conversion des secondes en jour
    mission['duree_transfert'] /= (3600 * 24)

    return mission

def calculer_masse_carburant(mission):
    """Cette fonction calcule la masse du carburant à emporter pour réaliser le trajet.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :Formules utilisées:

    De l'équation de Tsiolkovski découle :
    :math:`\\Delta v = v_{initiale}\\ln(\\frac{m_{initiale}}{m_{finale}})`

    Avec :math:`v_{initiale}` qui correspond à la vitesse avant d'entamer l'actionnement des moteurs.
    Elle correspond à la vitesse du vaisseau en orbite avant la phase d'accélération
    et à la vitesse de libération (vitesse de déplacement du vaisseau durant le voyage) avant le freinage.

    On a en développant:

    :math:`m_{carburant} = m_{initiale}(1-e^{-\\frac{\\Delta v}{v_{orbite}}} - m_{charge~utile})`

    :math:`m_{poids~vaisseau} = m_{charge~utile} + m_{initiale} + m_{carburant}`

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul la masse de carburant utilisé pour l'accélération
    mission['carburant_sortie_orbite_init'] = mission['vaisseau'].masse_initiale * (1 - np.exp(-((abs(mission['delta_v_orbite_depart'])) / mission['vitesse_orbite_depart']))) - mission['vaisseau'].masse_charge_utile

    #Calcul la masse de carburant utilisé pour la décélération
    mission['carburant_entree_orbite_arrivee'] = (mission['vaisseau'].masse_initiale - mission['carburant_sortie_orbite_init']) * (1 - np.exp(-((abs(mission['delta_v_orbite_arrivee'])) / mission['vitesse_orbite_arrivee']))) - mission['vaisseau'].masse_charge_utile

    #Calcul de la masse total du vaisseau
    mission['poids_vaisseau'] = mission['vaisseau'].masse_charge_utile + mission['vaisseau'].masse_initiale + mission['carburant_sortie_orbite_init'] + mission['carburant_entree_orbite_arrivee']
    return mission

def calculer_duree_mission(mission):
    """Cette fonction calcule la durée totale de la mission en fonction de la durée de transfert et de la durée de séjour sur place.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    formules utilisées :

    :math:`\\omega = \\frac{360\\pi}{T} (degrés/jour)`

    :math:`\\delta_{\\omega} = \omega_{planète~initiale}-\omega_{planète~finale}`

    Pour le reste des angles, nous avons expliqué directement via les commentaires du code.

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict
    """
    #Calcul des vitesses de rotation des planètes
    omega_planete_depart = 360 / mission['planete_depart'].periode_revolution
    omega_planete_arrivee = 360 / mission['planete_arrivee'].periode_revolution

    # Calcul la vitesse de rotation relative entre les deux planètes
    delta_omega = omega_planete_depart - omega_planete_arrivee

    #Pour la suite, on prend la convention suivante pour tous les angles :
    #p1i : position initiale de la planète de départ
    #p1f : position finale de la planète de départ
    #p2i : position initiale de la planète d'arrivée
    #p2f : position finale de la planète d'arrivée

    #Angle entre la position initiale de la planète de départ et la position finale de la planète de départ
    angle_p1i_p1f = omega_planete_depart * mission['duree_transfert']

    #Angle entre la position finale de la planète de départ et la position finale de la planète d'arrivée
    angle_p1f_p2f = angle_p1i_p1f - 180

    #angle de phasage
    phi = 180 - angle_p1i_p1f

    #Calcul de la durée d'attente sur la planète d'arrivée une fois sur place
    angle_duree_totale = 360 + phi - angle_p1f_p2f
    mission['duree_sur_planete_arrivee'] = abs(angle_duree_totale / delta_omega)

    #Calcul de la date de départ du vaisseau de la planète d'arrivée
    ts = load.timescale()
    date_depart_planete = ts.utc(mission['annee_arrivee_planete'], mission['mois_arrivee_planete'], mission['jour_arrivee_planete'])
    date_depart_planete = date_depart_planete + timedelta(days=int(mission["duree_sur_planete_arrivee"]))

    #Mémorisation de la date de départ du vaisseau de la planète d'arrivée
    mission['jour_depart_planete'] = date_depart_planete.utc_datetime().day
    mission['mois_depart_planete'] = date_depart_planete.utc_datetime().month
    mission['annee_depart_planete'] = date_depart_planete.utc_datetime().year

    #Calcul de l'indice dans le tableau du moment de départ de la planète d'arrivée
    mission['indice'] += int(mission["duree_sur_planete_arrivee"])
    #Gestion d'erreur du dépassement de tableau si la mission est trop longue
    try:
        #Mémorisation de l'angle de la planète d'arrivée au moment du départ vers la planète de départ
        mission['angle_depart_planete'] = mission['planete_depart'].temps_pos_planete[3, mission['indice']]
        #Variable pour savoir s'il y a eu une erreur
        mission['mission_trop_longue'] = 'non'
    except IndexError:
        #Variable pour savoir s'il y a eu une erreur
        mission['mission_trop_longue'] = 'oui'
        mission['retour_oui_non'] = 'non'
        #Fin de la fonction
        return mission

    # Demande à l'utilisateur s'il souhaite revenir sur la planète de départ
    question_utilisateur = input("Souhaitez-vous revenir sur la planète de départ (oui ou non) : ")

    if question_utilisateur == 'oui' or question_utilisateur == 'OUI' or question_utilisateur == 'o' or question_utilisateur == 'O':
        #Mémorisation de la réponse de l'utilisateur
        mission['retour_oui_non'] = 'oui'

        #Calcule la durée totale de la mission si l'utilisateur souhaite revenir sur la planète de départ
        mission['duree'] = abs(mission['duree_transfert'] + mission["duree_sur_planete_arrivee"] + mission['duree_transfert'])

        #Affichage de la date d'arrivée du vaisseau sur la planète de départ
        ts = load.timescale()
        date_retour_mission = ts.utc(mission['annee_depart_planete'], mission['mois_depart_planete'], mission['jour_depart_planete'])
        date_retour_mission = date_retour_mission + timedelta(days=int(mission['duree_transfert']))
        #Mémorisation de la date d'arrivée du vaisseau sur la planète de départ
        mission['jour_retour_mission'] = date_retour_mission.utc_datetime().day
        mission['mois_retour_mission'] = date_retour_mission.utc_datetime().month
        mission['annee_retour_mission'] = date_retour_mission.utc_datetime().year

    elif question_utilisateur == 'non' or question_utilisateur == 'NON' or question_utilisateur == 'n' or question_utilisateur == 'N':
        #Mémorisation de la réponse de l'utilisateur
        mission['retour_oui_non'] = 'non'

        # Calcule la durée totale de la mission si l'utilisateur ne souhaite pas revenir sur la planète de départ
        mission['duree'] = abs(mission['duree_transfert'])

    return mission

def appel_fonctions_physique(mission):
    """Cette fonction appel les fonctions qui effectuent les calculs physiques pour la mission spatiale demandé.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :return: Tous les paramètres utiles de la mission.
    :rtype: dict

    Remarque :
        Cette fonction effectue plusieurs étapes de calcul physique pour préparer les données de mission. Les calculs incluent la durée de transfert, l'instant de départ, le delta-v, l'influence planétaire, la vitesse orbitale, la masse de carburant, et la durée totale de la mission.
    """
    mission = calculer_duree_transfert(mission)
    mission = determiner_instant_depart(mission)
    mission = calculer_influence_planete(mission)
    mission = calculer_energie_orbitale(mission)
    mission = calculer_vitesse_orbite(mission)
    mission = calculer_masse_carburant(mission)
    mission = calculer_duree_mission(mission)

    return mission