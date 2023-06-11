# MGA 802

import Module as md

from importlib import reload
reload(md)


mission = md.afficher_ihm(md.obtenir_entier, md.obtenir_flottant, md.Vaisseau, md.Planete)
#print(mission)
print(mission['planete_depart'].coordonnees_planete(1, 1, 2025))
print(mission['planete_arrivee'].coordonnees_planete(1, 1, 2025))

vitesse_initiale_vaisseau, vitesse_arrivee_vaisseau = calculer_vitesse_initiale(mission, rayon_orbite_planete_depart, rayon_orbite_planete_arrivee)
