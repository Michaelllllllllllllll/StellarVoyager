import numpy as np
def afficher_ihm(obtenir_entier, obtenir_flottant, Vaisseau, Planete):
    """Affiche l'interface utilisateur

    Input : aucune

    Output : dictionnaire avec les données d'entrée du problème"""
    mission = {}
    print("Voici les planètes du système solaire :\n1 - Mercure\n2 - Vénus\n3 - Terre\n4 - Mars\n5 - Jupiter\n6 - Saturne\n7 - Uranus\n8 - Neptune\n9 - Pluton")

    mission['numero_planete_depart'] = obtenir_entier("Veuillez entrer le numéro de la planète de départ de votre voyage : ", 1, 9) - 1
    mission['numero_planete_arrivee'] = obtenir_entier("Veuillez entrer le numéro de la planète d'arrivée de votre voyage : ", 1, 9) - 1
    mission['planete_depart'] = Planete(mission['numero_planete_depart'])
    mission['planete_arrivee'] = Planete(mission['numero_planete_arrivee'])
    mission['vaisseau'] = Vaisseau(obtenir_flottant)

    jour = obtenir_entier("Veuillez entrer le numéro du jour de départ au plus tôt : ", 1, 31)
    mois = obtenir_entier("Veuillez entrer le numéro du mois de départ au plus tôt : ", 1, 12)
    annee = obtenir_entier("Veuillez entrer le numéro de l'année de départ au plus tôt : ", 1600, 2200 - 1)
    print("\nTéléchargement des éphémérides 1/2 :\n")
    mission['planete_depart'].coordonnees_planete(jour, mois, annee)
    print("\nTéléchargement des éphémérides 2/2 :\n")
    mission['planete_arrivee'].coordonnees_planete(jour, mois, annee)

    return mission

def retour_utilisateur(mission):

    if mission['mission_trop_longue'] == 'oui':
        print("\nErreur, la mission est trop longue, elle dépasse l'année maximale permise par nos données d'éphéméride.")
    else:
        print(f"\nVous souhaitez partir de la planète {mission['planete_depart'].nom_planete_affichage} pour aller vers {mission['planete_arrivee'].nom_planete_affichage}.\nCe code vous montrera toutes les données indispensables au trajet.")
        print(f"En considérant votre charge utile de {mission['vaisseau'].masse_charge_utile} kg, le vaisseau aura une masse (sans carburant) de {mission['vaisseau'].masse_initiale} kg, soit environ {mission['vaisseau'].masse_initiale / 1000} tonnes.")

        print(f"\nLa durée du voyage sera de {int(mission['duree_transfert'])} jours, soit environ {round(mission['duree_transfert'] / 30, 2)} mois, ou {round(mission['duree_transfert'] / (30 * 12), 2)} ans.")

        print(f"La date de départ optimal de {mission['planete_depart'].nom_planete_affichage} sera le {int(mission['jour_depart'])}/{int(mission['mois_depart'])}/{int(mission['annee_depart'])}.")

        print(f"Si vous partez à cette date, la date d'arrivée sur {mission['planete_arrivee'].nom_planete_affichage} sera le {int(mission['jour_arrivee_planete'])}/{int(mission['mois_arrivee_planete'])}/{int(mission['annee_arrivee_planete'])}.")

        print(f"\nAu départ, à une hauteur d'environ {int(mission['planete_depart'].rayon_orbite - mission['planete_depart'].rayon)} km, le vaisseau se déplacera à une vitesse de {mission['vitesse_orbite_depart']} km/s")

        print(f"Le vaisseau devra se déplacer à une vitesse de {mission['vitesse_liberation']} km/s pour sortir de l'attraction de la planète {mission['planete_depart'].nom_planete_affichage}, Il faudra accélerer.")

        print(f"Ce qui correspond à variation de vitesse de {mission['delta_v_orbite_depart']} km/s pour partir vers {mission['planete_arrivee'].nom_planete_affichage}.")

        print(f"\nA l'arrivée, le vaisseau sera à une hauteur de {int(mission['planete_arrivee'].rayon_orbite - mission['planete_arrivee'].rayon)} km, le vaisseau devra se déplacer à une vitesse de {mission['vitesse_orbite_arrivee']} km/s")
        print(f"Ce qui correspond à une variation de vitesse de {mission['delta_v_orbite_arrivee']} km/s, il va falloir freiner.")

        print(f"\nLa masse de carburant pour la phase de départ de l'orbite vers la planète {mission['planete_arrivee'].nom_planete_affichage} sera de {int(mission['carburant_sortie_orbite_init'])} kg.")

        print(f"La masse de carburant pour la phase de freinage afin d'atteindre l'orbite de la planète {mission['planete_arrivee'].nom_planete_affichage} sera de {int(mission['carburant_entree_orbite_arrivee'])} kg.")

        print(f"\nUne fois sur place, vous devrez attendre {int(mission['duree_sur_planete_arrivee'])} jours pour avoir la meilleure fenetre de tir, soit environ {round(mission['duree_sur_planete_arrivee'] / 30, 2)} mois, ou {round(mission['duree_sur_planete_arrivee'] / (30 * 12), 2)} ans.")

        print(f"Le jour de depart sur {mission['planete_arrivee'].nom_planete_affichage} serait le {int(mission['jour_depart_planete'])}/{int(mission['mois_depart_planete'])}/{int(mission['annee_depart_planete'])}, si vous souhaitez revenir.")

        print(f"\nPour aller sur la planète {mission['planete_arrivee'].nom_planete_affichage}, il faudra {int(mission['carburant_sortie_orbite_init']) + int(mission['carburant_entree_orbite_arrivee'])} kg de carburant.")
        print(f"Une fois en orbite autour de la planète {mission['planete_depart'].nom_planete_affichage}, votre vaisseau devra peser au total {int(mission['poids_vaisseau'])} kg, soit {int(mission['poids_vaisseau'] / 1000)} tonnes")

        if mission['retour_oui_non'] == 'oui' :
            print(f"\nVous comptez revenir sur la planète initiale. La période totale de la mission sera alors de {int(mission['duree'])} jours, soit environ {round(mission['duree'] / 30, 2)} mois, ou {round(mission['duree'] / (30 * 12), 2)} ans.")
            print(f"La date de retour sur {mission['planete_depart'].nom_planete_affichage} sera le {int(mission['jour_retour_mission'])}/{int(mission['mois_retour_mission'])}/{int(mission['annee_retour_mission'])}.")
            print(f"N'oubliez pas de ravitailler votre vaisseau !")

        elif mission['retour_oui_non'] == 'non' :
            print(f"\nVous comptez rester sur la planète initiale. La période totale de la mission sera de {int(mission['duree'])} jours, soit environ {round(mission['duree'] / 30, 2)} mois, ou {round(mission['duree'] / (30 * 12), 2)} ans.")
            print(f"La date de fin de mission sur {mission['planete_arrivee'].nom_planete_affichage} sera le {int(mission['jour_arrivee_planete'])}/{int(mission['mois_arrivee_planete'])}/{int(mission['annee_arrivee_planete'])}.")