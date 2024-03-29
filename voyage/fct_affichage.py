import matplotlib.pyplot as plt
import numpy as np

# Fonction qui affiche la trajectoire du vaisseau ainsi que celle des planètes
def afficher_trajectoire(mission):
    """Cette fonction affiche un graphique de la trajectoire du vaisseau ainsi que celle des planètes de notre système solaire. Elle affiche aussi les dates importantes de la mission.

    :param dict mission: Contient tous les paramètres utiles de la mission.

    :return: Aucun
    """
    # Liste de la distance de chacune des planètes par rapport au soleil en km
    distance_au_soleil = [57910000, 108200000, 149600000, 227940000, 778330000, 1429400000, 2870990000, 4498250000, 5906380000] #km
    # Liste les noms des planètes
    nom_planete_affichage = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']

    # Tableau contenant 200 angles de 0 à 2 pi
    angle_planete = np.linspace(0, 2 * np.pi, 200) #rad

    # Définit la figure
    plt.figure(1)

    # Affichage du soleil
    plt.scatter(0, 0, label='Soleil', color='gold')

    # Affiche les orbites des 9 planètes
    for i in range(9):

        # Position en x et y des points pour tracer l'orbite de chaque planète
        x = distance_au_soleil[i] * np.cos(angle_planete)
        y = distance_au_soleil[i] * np.sin(angle_planete)

        # Affiche les points et les relient en pointillés avec le nom des planètes en légende
        # La conversion est faite de km à unité astronomique (1 km = 6.68*10^-9 UA)
        # Pour rappel, 1 UA = 150 millions de km : distance entre la Terre et le Soleil en moyenne
        plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = nom_planete_affichage[i], linestyle='dashed')

    ## Trajet aller
    # Récupère l'angle de départ de la mission
    angle_depart = mission['angle_depart']
    # Tableau des angles de la trajectoire commençant à l'angle de départ jusqu'à l'angle de départ + pi (orbite de Hohmann)
    angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
    # Calcule le rayon du trajet
    rayon_trajet = (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil) / 2
    # Calcule les coordonnées x et y du centre du demi-cercle du trajet
    centre_trajet_x = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
    centre_trajet_y = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
    # Calcul des tableaux contenant les coordonnées des points x et y de la trajectoire du vaisseau
    x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
    y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)

    # Affiche la trajectoire aller du vaisseau
    plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = 'Trajet aller', color='blue')

    # Affiche les dates de départ d'arrivée du trajet aller
    plt.scatter(x[0] * 6.68459e-9, y[0] * 6.68459e-9)
    plt.text(x[0] * 6.68459e-9, y[0] * 6.68459e-9, f"{int(mission['jour_depart'])}/{int(mission['mois_depart'])}/{int(mission['annee_depart'])}")
    plt.scatter(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9)
    plt.text(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9, f"{int(mission['jour_arrivee_planete'])}/{int(mission['mois_arrivee_planete'])}/{int(mission['annee_arrivee_planete'])}")

    ## Trajet retour
    # S'effectue seulement si l'utilisateur indique qu'il veut revenir (voir fct_physique)
    if mission['retour_oui_non'] == 'oui':
        # Récupère l'angle initial du retour
        angle_depart = mission['angle_depart_planete']
        # Tableau des angles de la trajectoire commençant à l'angle de départ jusqu'à l'angle de départ + pi (orbite de Hohmann)
        angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
        # Calcule le rayon du trajet
        rayon_trajet = (mission['planete_arrivee'].distance_soleil + mission['planete_depart'].distance_soleil) / 2
        # Calcule les coordonnées x et y du centre du demi-cercle du trajet
        centre_trajet_x = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
        centre_trajet_y = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
        # Calcul des tableaux des coordonnées des points x et y de la trajectoire du vaisseau
        x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
        y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)

        # Affiche la trajectoire retour du vaisseau
        plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = 'Trajet retour', color='red')

        # Affiche les dates de départ d'arrivée du trajet retour
        plt.scatter(x[0] * 6.68459e-9, y[0] * 6.68459e-9)
        plt.text(x[0] * 6.68459e-9, y[0] * 6.68459e-9, f"{int(mission['jour_depart_planete'])}/{int(mission['mois_depart_planete'])}/{int(mission['annee_depart_planete'])}")
        plt.scatter(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9)
        plt.text(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9, f"{int(mission['jour_retour_mission'])}/{int(mission['mois_retour_mission'])}/{int(mission['annee_retour_mission'])}")

    # Définit le libellé de l'axe des abscisses
    plt.xlabel('Position x en unité astronomique')
    # Définit le libellé de l'axe des ordonnées
    plt.ylabel('Position y en unité astronomique')
    # Définit le titre du graphique
    plt.title(f"Affichage de la mission de la planète {mission['planete_depart'].nom_planete_affichage} à la planète {mission['planete_arrivee'].nom_planete_affichage} en référenciel héliocentrique")
    # Affiche la légende
    plt.legend()
    # Conserve les proportions du graphique
    plt.axis('equal')
    # Affiche une grille
    plt.grid()
    # Affiche le graphique
    plt.show()