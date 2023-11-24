# UE-AD-A1-REST

Dans ce tp, nous avons développé 4 API : une en REST, une en GRAPHQL et deux en gRPC. Elles sont toutes en relation entre elles.
C'est uniquement sur l'API User que les utilisateurs pourront effectuer des requêtes.
L'API User (REST) aura, elle, accès à Movie (graphql) et Booking (gRPC). Enfin, Booking est également en relation avec Showtimes (gRPC).
Pour avoir le détail de chacune des routes disponibles, un fichier YAML est disponible dans le dossier user. Pour les autres API, nous avons conservé les mêmes routes que pour le tp REST, vous pouvez donc vous référer aux fichiers YAML du TP REST.

# Table des Matières
1. [Description](#description)
   - 1.1 [API User](#api-user)
   - 1.2 [API Movie](#api-movie)
   - 1.3 [API Booking](#api-booking)
   - 1.4 [API Showtime](#api-showtime)
2. [Déploiement](#déploiement)
   - 2.1 [Installation de virtualenv (si ce n'est pas déjà fait)](#installation-de-virtualenv-si-ce-nest-pas-déjà-fait)
   - 2.2 [Création d'un environnement virtuel](#création-dun-environnement-virtuel)
   - 2.3 [Activation de l'environnement virtuel](#activation-de-lenvironnement-virtuel)
   - 2.4 [Installation des dépendances du projet](#installation-des-dépendances-du-projet)
   - 2.5 [Lancement des API REST](#lancement-des-api-rest)
3. [Tests](#tests)
   - 3.1 [API User](#api-user-1)
4. [Pour finir](#pour-finir)
5. [Auteurs](#auteurs)
6. [Licence](#licence)
7. [Contact](#contact)

## Description

### API User

Cette API propose un accès à toutes les données relatives aux utilisateurs. Les données de la base sont de la forme :
- un identifiant
- un nom (Nom et Prénom)
- un indicateur de la dernière fois qu'il était actif

### API Movie

Cette API propose un accès à toutes les données relatives aux films dans la base de données. Les données sont de la forme :
 - identifiant d'un film
 - titre d'un film
 - nom du directeur d'un film
 - note donnée à un film

### API Booking

Cette API propose un accès à toutes les données relatives à la réservation de séances par les utilisateurs. Les données sont de la forme :
- l'identifiant d'un utilisateur
- une liste "dates" composée à la fois :
    - d'une date 
    - d'une liste de séances de films réservées pour date

### API Showtime

Cette API propose un accès à toutes les données relatives aux dates de projection des films. Les données sont de la forme :
- l'identifiant d'un utilisateur
- une liste "dates" composée à la fois :
    - d'une date 
    - d'une liste de séances de films réservées pour date

## Déploiement 

Nous allons démarrer chacun des services afin de pouvoir effectuer des requêtes sur chacun d'entre eux.

Pour assurer un environnement de développement isolé, nous allons avoir recours à l'utilisation d'un environnement virtuel (venv). Suivez ces étapes pour configurer et activer votre venv sur windows :

### Installation de virtualenv (si ce n'est pas déjà fait)

```
pip install virtualenv
```

### Création d'un environnement virtuel

L'installation peut prendre plusieurs dizaines de secondes.

```
# Assurez-vous d'être dans le répertoire de votre projet
cd chemin/vers/votre/projet

# Créez un environnement virtuel (que l'on nommera ici 'venv')
python -m venv venv
```

### Activation de l'environnement virtuel

Pour activer l'environnement virtuel, il faut vous assurer que votre ExecutionPolicy autorise l'exécution du fichier d'activation du venv.

tapez cette commande pour vérifier la valeur de l'ExecutionPolicy (souvent par défaut à 'Restricted')
```
Get-ExecutionPolicy
```

Pour pouvoir activer l'environnement virtuel, il faudra la passer en Bypass.

```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass
```

```
# Activez l'environnement virtuel
venv\Scripts\Activate
```

Une fois l'activation réussie, vous devriez voir à gauche de votre terminal l'indication (venv) précéder la ligne.

### Installation des dépendances du projet

Cette action peut prendre plusieurs secondes, le temps de télécharger toutes les librairies nécessaires pour faire tourner les API.

```
# Installez les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt
```

### Lancement des API REST

Lancez chacune des API du projet (spécifiées ci-dessus) Il faut toutes les lancer à la suite avant de commencer à effectuer des requêtes, car elles sont interconnectées sur certaines requêtes.

Déplacez-vous dans le dossier de l'API que vous souhaitez démarrer, puis lancez le fichier python correspondant. Exemple pour User :

``` 
cd user # pour se déplacer dans le dossier voulu
python user.py # on lance l'API
```

Il faudra démarrer 3 onglets supplémentaires dans votre terminal, vous déplacer à la racine du projet (voir commande ci-dessus) et ne pas oublier d'activer l'environnement virtuel (voir commande ci-dessus).
Ensuite, vous pourrez taper les deux commandes juste au-dessus en remplaçant 'user' par :
- 'movie' la première fois
- 'showtime' la deuxième
- 'booking' dans le dernier onglet

Après ces étapes, les API devraient être accessibles pour effectuer des requêtes.

## Tests

Nous avons détaillé les tests uniquement pour l'API User. Pour tester cette API REST, suivez les étapes ci-dessous :

### API User

#### Route 1 : `/`
- **Description** : Route pour la page d'accueil
- **Méthode** : GET
- **URL Postman** : [http://localhost:3203/](http://localhost:3203/)
- **Réponse attendue** : ```<h1 style='color:blue'>Welcome to the User service!</h1> ```


#### Route 2 : `/users/<userId>/bookings`
- **Description** : Route pour obtenir les réservations d'un utilisateur
- **Méthode** : GET
- **URL Postman** : [http://localhost:3203/users/chris_rivers/bookings](http://localhost:3203/users/chris_rivers/bookings)
- **Réponse attendue** : 
```
[
    {
        "dates": [
            {
                "date": "20151201",
                "movies": [
                    "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
                ]
            }
        ],
        "userid": "chris_rivers"
    }
]
```


#### Route 3 : `/users/<userId>/bookings/movies`
- **Description** : Route pour obtenir les films réservés par un utilisateur
- **Méthode** : GET
- **URL Postman** : [http://localhost:3203/users/dwight_schrute/bookings/movies](http://localhost:3203/users/dwight_schrute/bookings/movies)
- **Réponse attendue** : 
```
[
    {
        "director": "Paul McGuigan",
        "id": "7daf7208-be4d-4944-a3ae-c1c2f516f3e6",
        "rating": 6.4,
        "title": "Victor Frankenstein"
    },
    {
        "director": "Ryan Coogler",
        "id": "267eedb8-0f5d-42d5-8f43-72426b9fb3e6",
        "rating": 8.8,
        "title": "Creed"
    },
    {
        "director": "Ridley Scott",
        "id": "a8034f44-aee4-44cf-b32c-74cf452aaaae",
        "rating": 8.2,
        "title": "The Martian"
    },
    {
        "director": "Tom Hooper",
        "id": "276c79ec-a26a-40a6-b3d3-fb242a5947b6",
        "rating": 5.3,
        "title": "The Danish Girl"
    }
]
```


#### Route 4 : `/users/<userId>/bookings/add`
- **Description** : Route pour ajouter une réservation pour un utilisateur
- **Méthode** : POST
- **URL Postman** : [http://localhost:3203/users/peter_curley/bookings/add](http://localhost:3203/users/peter_curley/bookings/add)
- **Body à passer à la requête** :
```
{
  "date": "20151205",
  "movieid": "a8034f44-aee4-44cf-b32c-74cf452aaaae"
}
```
- **Réponse attendue** : 
```
{
    "date": "20151205",
    "movieid": "a8034f44-aee4-44cf-b32c-74cf452aaaae"
}
```

## Pour finir

A la fin de l'utilisation des API, n'oubliez pas de vous déconnecter de l'environnement virtuel en tapant la commande :
```deactivate```

ainsi que de rétablir votre ExecutionPolicy par défaut : 

```Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Default```

Vous pouvez vérifier sa valeur si vous le souhaitez en tapant :
```Get-ExecutionPolicy```

## Auteurs
- BLEUET Matthis
- CHALEKH Zineddine

## Licence
License: [GNU General Public License v3 (GPL-3)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Contact
Pour toute question, veuillez nous contacter à zineddine.chalekh@imt-atlantique.net ou matthis.bleuet@imt-atlantique.net .
