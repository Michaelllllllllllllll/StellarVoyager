# MGA 802

import Module as md

mission = md.afficher_ihm(md.obtenir_entier, md.obtenir_flottant, md.Vaisseau, md.Planete)

mission = md.appel_fonctions_physique(mission, md.retour_utilisateur)

md.afficher_trajectoire(mission)