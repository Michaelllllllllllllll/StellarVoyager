import matplotlib.pyplot as plt
import numpy as np

def afficher_trajectoire(mission):

    distance_au_soleil = [57910000, 108200000, 149600000, 227940000, 778330000, 1429400000, 2870990000, 4498250000, 5906380000]
    nom_planete_affichage = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Pluton']

    angle_planete = np.linspace(0, 2 * np.pi, 200)

    plt.figure(1)

    plt.scatter(0, 0, label = 'soleil', color='yellow')

    for i in range(9):

        x = distance_au_soleil[i] * np.cos(angle_planete)
        y = distance_au_soleil[i] * np.sin(angle_planete)
        plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = nom_planete_affichage[i], linestyle='dashed')

    #trajet aller
    angle_depart = mission['angle_depart']
    angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
    rayon_trajet = (mission['planete_depart'].distance_soleil + mission['planete_arrivee'].distance_soleil) / 2
    centre_trajet_x = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
    centre_trajet_y = (mission['planete_depart'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
    x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
    y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
    plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = 'Trajet aller', color='blue')

    plt.scatter(x[0] * 6.68459e-9, y[0] * 6.68459e-9)
    plt.text(x[0] * 6.68459e-9, y[0] * 6.68459e-9, f"{int(mission['jour_depart'])}/{int(mission['mois_depart'])}/{int(mission['annee_depart'])}")
    plt.scatter(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9)
    plt.text(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9, f"{int(mission['jour_arrivee_planete'])}/{int(mission['mois_arrivee_planete'])}/{int(mission['annee_arrivee_planete'])}")

    #trajet retour
    if mission['retour_oui_non'] == 'oui':
        angle_depart = mission['angle_depart_planete']
        angle_trajet = np.linspace(angle_depart, angle_depart + np.pi, 200)
        rayon_trajet = (mission['planete_arrivee'].distance_soleil + mission['planete_depart'].distance_soleil) / 2
        centre_trajet_x = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.cos(angle_depart)
        centre_trajet_y = (mission['planete_arrivee'].distance_soleil - rayon_trajet) * np.sin(angle_depart)
        x = centre_trajet_x + rayon_trajet * np.cos(angle_trajet)
        y = centre_trajet_y + rayon_trajet * np.sin(angle_trajet)
        plt.plot(x * 6.68459e-9, y * 6.68459e-9, label = 'Trajet retour', color='red')

        plt.scatter(x[0] * 6.68459e-9, y[0] * 6.68459e-9)
        plt.text(x[0] * 6.68459e-9, y[0] * 6.68459e-9, f"{int(mission['jour_depart_planete'])}/{int(mission['mois_depart_planete'])}/{int(mission['annee_depart_planete'])}")
        plt.scatter(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9)
        plt.text(x[-1] * 6.68459e-9, y[-1] * 6.68459e-9, f"{int(mission['jour_retour_mission'])}/{int(mission['mois_retour_mission'])}/{int(mission['annee_retour_mission'])}")

    plt.xlabel('Position x en unité astronomique')
    plt.ylabel('Position y en unité astronomique')
    plt.title(f"Affichage de la mission de la planète {mission['planete_depart'].nom_planete_affichage} à la planète {mission['planete_arrivee'].nom_planete_affichage} en référenciel héliocentrique")
    plt.legend()
    plt.axis('equal')  # Pour conserver les proportions
    plt.grid()
    plt.show()