# **StellarVoyager**, calculateur de trajectoire orbitale

## Description
Le but du projet est de calculer la trajectoire entre deux planètes la moins consommatrice de carburant.
Il introduit **l'orbite de Hohmann** qui illustre la technique. 
Le principe est de partir au moment optimum pour profiter du mouvement de l'orbite initiale.
Les moteurs sont alors utilisés deux fois, la première fois pour **accélerer et sortir de l'attraction** de la planète initiale, et la seconde fois pour **freiner et rentrer dans l'orbite** de la planète visée.

## Utilisation
Une fois que vous avez installé le nécessaire __(voir rubrique **installation**)__, vous devez éxecuter le programme depuis le fichier **main*

Dans l'ordre, vous devez :
   * Choisir une planète de départ.
   * Choisir une planète d'arrivée.
   * Choisir la charge utile que vous voulez emmener avec vous dans l'espace.

Ensuite, vous devez indiquer le moment au plus tot, auquel vous voulez partir, de la façon suivante :
   * Le jour
   * Le mois
   * L'année
         __Vous devrez patienter quelques instants, le temps que le programme calcule les données des planètes.__
   * Indiquer si vous voulez revenir ou non sur la planète initiale

Vous aurez alors en sortie les données importantes pour votre voyage, soit :
   * La masse du vaisseau et du carburant en fonction de votre charge utile.
   * Les vitesses associées pour réaliser les manoeuvres.
   * Le processus de durée (date de départ, d'arrivée et de retour).
   * Un graphique montrant le déplacement du vaisseau entre les deux planètes dans le système solaire.

## Structure du projet


## Installation


## Exemples
Pour vous aider à utiliser le programme, nous allons vous introduire l'exemple d'une mission habitée de la Terre vers Mars.
Mettez-vous dans l'ambiance : 
__Nous sommes dans un monde ou les hommes ont colonisés Mars et nous voulons ravitaillé la planète en matière première et en équipage.
Vous êtes la personne en charge du départ et vous convertissez tous les élements indiqués en unité de masse, soit :__
   __- 10 personnes d'environ 75 kg, soit 750 kg.__
   __- 5000 kg de matière première pour ravitailler la planète__
__Vous voulez partir à partir du mois de Juin 2035 et vous voulez connaitre la quantité de carburant, et quand vous serez de retour auprès de votre famille.__

Voici ce que vous rentrez pour la mission, vous pouvez le voir **en gras** :
* Veuillez entrer le numéro de la planète de départ de votre voyage : **3** __Terre__
* Veuillez entrer le numéro de la planète d'arrivée de votre voyage : **4** __Mars__
* Entrer la masse de charge utile que vous voulez emmener avec vous en kg : **5750** __Kg__
* Veuillez entrer le numéro du jour de départ au plus tôt : **1** __Jour__
* Veuillez entrer le numéro du mois de départ au plus tôt : **6** __Juin__
* Veuillez entrer le numéro de l'année de départ au plus tôt : **2035** __Année__
* Souhaitez-vous revenir sur la planète de départ (oui ou non) : **oui**

Les résultats sont : 
Vous souhaitez partir de la planète **Terre** pour aller vers **Mars**.
Ce code vous montrera toutes les données indispensables au trajet.
En considérant votre charge utile de **5750.0 kg**, le vaisseau aura une masse (sans carburant) de **86250.0** kg, soit environ **86.25** tonnes.

La durée du voyage sera de **258 jours**, soit environ **8.63 mois**, ou **0.72 ans**.
La date de départ optimal de Terre sera le **24/9/2035.**
Si vous partez à cette date, la date d'arrivée sur Mars sera le **8/6/2036.**

Au départ, à une hauteur d'environ **318 km**, le vaisseau se déplacera à une vitesse de **7.72 km/s**
Le vaisseau devra se déplacer à une vitesse de **11.5 km/s** pour sortir de l'attraction de la planète Terre, **Il faudra accélerer.**
Ce qui correspond à variation de vitesse de **3.78 km/s** pour partir vers Mars.

A l'arrivée, le vaisseau sera à une hauteur de **169 km**, le vaisseau devra se déplacer à une vitesse de **3.47 km/s**
Ce qui correspond à une variation de vitesse de **-8.03 km/s, il va falloir freiner.**

La masse de carburant pour la phase de départ de l'orbite vers la planète Mars sera de **27641 kg**.
La masse de carburant pour la phase de freinage afin d'atteindre l'orbite de la planète Mars sera de **47064 kg.**

Une fois sur place, vous devrez attendre **454 jours** pour avoir la meilleure fenetre de tir, soit environ **15.15 mois**, ou **1.26 ans.**
Le jour de depart sur Mars serait le **5/9/2037**, si vous souhaitez revenir.

Pour aller sur la planète Mars, il faudra **74705 kg** de carburant.
Une fois en orbite autour de la planète Terre, **votre vaisseau devra peser au total 166706 kg, soit 166 tonnes**

Vous comptez revenir sur la planète initiale. La période totale de la mission sera alors de **972 jours**, soit environ **32.4 mois**, ou **2.7 ans.**
La date de retour sur Terre sera le **21/5/2038.**
__N'oubliez pas de ravitailler votre vaisseau !__

Voici le graphique de l'itinéraire de votre voyage : 
![Voyage Terre Mars](C:\Users\romai\PycharmProjects\StellarVoyager\StellarVoyager\voyage_terre_mars.png)

## Contributions
Nous acceptons tout type de contribution dans notre projet.

## Licence
GNU

## Auteurs
GRANAL Laétitia - ROBILLARD Romain - ROQUEJOFRE Michaël

## Statut du projet
Le projet est **terminé**