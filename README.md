# **StellarVoyager**, calculateur de trajectoire orbitale sur Python

## Description
Le but du projet est de calculer la trajectoire entre deux planètes la moins consommatrice de carburant.
Il introduit **l'orbite de Hohmann** qui illustre la technique. 
Le principe est de partir au moment optimum pour profiter du mouvement de l'orbite initiale.
Les moteurs sont alors utilisés deux fois, la première fois pour **accélerer et sortir de l'attraction** de la planète initiale, et la seconde fois pour **freiner et rentrer dans l'orbite** de la planète visée.

> *La caractéristique clé de la trajectoire de Hohmann est que l'angle entre le point de départ sur l'orbite intérieure et le point d'arrivée sur l'orbite extérieure est de 180 degrés. Cela signifie que l'engin spatial atteindra l'orbite extérieure exactement à l'opposé de son point de départ initial.*
*Cette propriété de 180 degrés entre le départ et l'arrivée est importante pour minimiser la dépense énergétique lors des transferts orbitaux. En exploitant la mécanique orbitale et en choisissant soigneusement les moments des impulsions de propulsion, les missions spatiales peuvent atteindre leur destination en utilisant le moins de carburant possible.*

## Utilisation
Une fois que vous avez installé le nécessaire *(voir rubrique **installation**)*, vous devez éxecuter le programme depuis le fichier *main*

Dans l'ordre, vous devez :
   * Choisir une planète de départ. 
   * Choisir une planète d'arrivée.
   * Choisir la charge utile que vous voulez emmener avec vous dans l'espace.

Ensuite, vous devez indiquer le moment au plus tôt, auquel vous voulez partir, de la façon suivante :
   * Le jour
   * Le mois
   * L'année
         
   *Vous devrez patienter quelques instants, le temps que le programme calcule les données des planètes.*

   * Indiquer si vous voulez revenir ou non sur la planète initiale

Vous aurez alors en sortie les données importantes pour votre voyage, soit :
   * La masse du vaisseau et du carburant en fonction de votre charge utile.
   * Les vitesses associées pour réaliser les manoeuvres.
   * Les dates clés du voyage (date de départ, d'arrivée et de retour).
   * Un graphique montrant le déplacement du vaisseau entre les deux planètes dans le système solaire.

De plus, nous sommes conscients que Pluton n'est plus catégorisée comme une planète mais comme une planète naine. 
Nous l'avons ajouté pour avoir plus de possibilités et par pure curiosité.

## Structure du projet
Le programme est organisé de la façon suivante : 

![Structure du projet](structure.jpg)

Nous avons un module "Voyage" qui comprend toutes les fonctions qui assurent la fonctionnalité du programme.
L'application "StellarVoyager" comprend ce module et tous les autres fichiers qui assurent la documentation, l'installation et le fonctionnement du programme.

## Installation
Pour installer le programme, suivez les étapes suivantes :
* Accéder au terminal.
* Il faut exécuter la commande : **pip install -r requirements.txt** dans le dossier où se trouve requirements.txt dans votre terminal.
* Aller dans le main et exécuter le programme.

De plus, nous avons utilisé les modules suivants qui seront automatiquement installés avec les commandes précédentes :

Données sur les planètes : [Skyfield](https://rhodesmill.org/skyfield/).

Incorporation du temps : [DateTime](https://docs.python.org/3/library/datetime.html).

Librairie pour vectoriser le code : [Numpy](https://numpy.org/).

Librairie pour tracer les figures : [Matplot](https://matplotlib.org/).

Barre de chargement : [tqdm](https://tqdm.github.io/).

## Exemples
### 1) Mission habitée vers Mars
Pour vous aider à utiliser le programme, nous allons vous introduire l'exemple d'une mission habitée de la Terre vers Mars.
Mettez-vous dans l'ambiance : 

*Nous sommes dans un monde où les hommes ont colonisé Mars et nous voulons ravitailler la planète en matière première et en équipage.*
*Vous êtes la personne en charge du départ et vous convertissez tous les éléments indiqués en unité de masse, soit :*
   - 10 personnes d'environ 75 kg, qui représente 750 kg.
   - 5000 kg de matière première pour ravitailler la planète.

*Vous voulez partir dès le mois de juin 2035 et vous voulez connaitre la quantité de carburant à emporter, et quand vous serez de retour auprès de votre famille.*

Voici ce que vous rentrez pour la mission, vous pouvez le voir **en gras** :
* Veuillez entrer le numéro de la planète de départ de votre voyage : **3** *(Terre)*
* Veuillez entrer le numéro de la planète d'arrivée de votre voyage : **4** *(Mars)*
* Entrer la masse de charge utile que vous voulez emmener avec vous en kg : **5750** *(kg)*
* Veuillez entrer le numéro du jour de départ au plus tôt : **1** *(Jour)*
* Veuillez entrer le numéro du mois de départ au plus tôt : **6** *(Mois)*
* Veuillez entrer le numéro de l'année de départ au plus tôt : **2035** *(Année)*
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
*N'oubliez pas de ravitailler votre vaisseau !*

Voici le graphique de l'itinéraire de votre voyage : 

   ![Exemple du voyage Terre Mars en 2035](voyage_terre_mars.png)

### 2) Envoie d'une sonde de Neptune à Pluton
Autre aspect du programme, une mission trop longue.
En effet, pour des questions de performance, nous nous limitons aux données datant de 1600 à 2200 lors du télechargement des éphémeride
La mission indiquée est trop longue pour un départ à l'heure actuelle (~300 ans).

Si vous souhaitez essayer, le résultat sera le suivant :
   * Erreur, la mission est trop longue, elle dépasse l'année maximale permise par nos données d'éphéméride.
Vous n'aurez pas la possibilité de faire le trajet retour.

Vous obtenez le graphique suivant :

   ![Trajet d'une sonde entre Neptune et Pluton](sonde_neptune_pluton.png)

Le but est de quand même ressortir un résultat sans avoir à crasher le programme.

**ATTENTION** : 
*Si vous avez ce message, cela signifie que le trajet est trop long, ou que vous lancez votre vaisseau trop tard.*
*Pour corriger le problème : essayez de lancer votre voyage plus tôt.* 

Maintenant que vous avez vu deux exemples, amusez-vous bien avec **STELLARVOYAGER**.

## Contributions
Nous acceptons tout type de contribution dans notre projet. Dès lors que les modifications simplifient ou améliorent le programme.
*(Voir rubrique **Licence**)*

## Licence
GNU General Public License (GPL)

## Auteurs
GRANAL Laétitia - ROBILLARD Romain - ROQUEJOFRE Michaël

## Statut du projet
**TERMINE**