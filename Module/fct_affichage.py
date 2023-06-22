import matplotlib.pyplot as plt
import numpy as np

# Fonction qui affiche la trajectoire du vaisseau ainsi que celle des planètes
def afficher_trajectoire(mission):
    """
    :param mission:
    :return:
    """

    # Liste des distances des planètes par rapport au soleil en km.
    distance_au_soleil = [57910000, 108200000, 149600000, 227940000, 778330000, 1429400000, 2870990000, 4498250000, 5906380000]
    # Liste les noms des planètes.
    nom_planete_affichage = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']

    # Tableau contenant 200 angles de pi à 2 pi
    angle_planete = np.linspace(0, 2 * np.pi, 200)

    # Définit la figure 1
    plt.figure(1)

    # Affiche les orbites des 9 planètes
    for i in range(9):

        # Position en x et y des points pour tracer l'orbite de chaque planètes
        x = distance_au_soleil[i] * np.cos(angle_planete)
        y = distance_au_soleil[i] * np.sin(angle_planete)

        # Affiche les points et les relies en pointillés avec le nom des planètes en légende
        plt.plot(x, y, label = nom_planete_affichage[i], linestyle='dashed')

    ## Trajet aller
    # Récupère l'anglais de départ de la mission
    angle_depart = mission['angle_depart']
    # Tableau des angles de la trajectoire commençant à l'angle de départ jusqu'à l'angle de départ + pi (orbite de Hohman)
    angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
    # Calcule le rayon du trajet
    rayon_trajet = (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil) / 2
    # Calcule les coordonnées x et y du centre du trajet (récupère le position du soleil et le décale du rayon du trajet)
    centre_trajet_x = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
    centre_trajet_y = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
    # Calcul des tableaux des coordonnées du points x & y effectuant la trajectoire du vaisseau
    x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
    y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
    # Affiche la trajectoire allée du vaisseau
    plt.plot(x, y, label = 'Trajet aller')

    ## Trajet retour
    # S'effectue seulement si l'utilisateur indique qu'il
    if mission['retour_oui_non'] == 'oui':
        # Récupère l'angle initial du retour
        angle_depart = mission['angle_depart_planete']
        # Calcule le rayon du trajet
        angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
        # Calcule le rayon du trajet
        rayon_trajet = (mission['planete_arrivee'].distance_soleil + mission['planete_depart'].distance_soleil) / 2
        # Calcule les coordonnées x et y du centre du trajet (récupère le position du soleil et le décale du rayon du trajet)
        centre_trajet_x = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
        centre_trajet_y = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
        # Calcul des tableaux des coordonnées du points x & y effectuant la trajectoire du vaisseau
        x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
        y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
        # Affiche la trajectoire retour du vaisseau
        plt.plot(x, y, label = 'Trajet retour')

    # Définit le libellé de l'axe des abscisses
    plt.xlabel('Position x en km ')
    # Définit le libellé de l'axe des ordonnées
    plt.ylabel('Position y en km')
    # Définit le titre du graphique
    plt.title('Affichage de la mission en référenciel héliocentrique')
    # Affiche la légende
    plt.legend()
    # Conserve les proportions du graphique
    plt.axis('equal')
    # Affiche une grille
    plt.grid()
    # Affiche le graphique
    plt.show()