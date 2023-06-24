# MGA 802

# Importe notre module contenant toutes nos fonctions
import Module as md

# Début la mission en lançant l'interface homme-machine
mission = md.afficher_ihm(md.obtenir_entier, md.obtenir_flottant, md.Vaisseau, md.Planete)

# Debute les calculs pour la mission
mission = md.appel_fonctions_physique(mission, md.retour_utilisateur)

# Affiche le graphique et les trajectoires associées à la mission effectuée (vaisseau et planètes).
md.afficher_trajectoire(mission)