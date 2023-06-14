import matplotlib.pyplot as plt
import numpy as np

def afficher_trajectoire(mission):

    distance_au_soleil = [57910000, 108200000, 149600000, 227940000, 778330000, 1429400000, 2870990000, 4498250000, 5906380000]
    nom_planete_affichage = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']

    angle_planete = np.linspace(0, 2 * np.pi, 200)

    plt.figure(1)

    for i in range(9):

        x = distance_au_soleil[i] * np.cos(angle_planete)
        y = distance_au_soleil[i] * np.sin(angle_planete)
        plt.plot(x, y, label = nom_planete_affichage[i], linestyle='dashed')

    #trajet aller
    angle_depart = mission['angle_depart']
    angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
    rayon_trajet = (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil) / 2
    centre_trajet_x = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
    centre_trajet_y = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
    x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
    y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
    plt.plot(x, y, label = 'Trajet aller')

    #trajet retour
    if mission['retour_oui_non'] == 'oui':
        angle_depart = mission['angle_depart_planete']
        angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
        rayon_trajet = (mission['planete_arrivee'].distance_soleil + mission['planete_depart'].distance_soleil) / 2
        centre_trajet_x = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
        centre_trajet_y = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
        x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
        y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
        plt.plot(x, y, label = 'Trajet retour')

    plt.xlabel('Position x en km ')
    plt.ylabel('Position y en km')
    plt.title('Affichage de la mission en référenciel héliocentrique')
    plt.legend()
    plt.axis('equal')  # Pour conserver les proportions
    plt.grid()
    plt.show()