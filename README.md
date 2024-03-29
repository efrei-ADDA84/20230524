# OpenWeatherMap Wrapper

Ce projet contient un wrapper Python pour l'API OpenWeatherMap, qui permet de récupérer les données météorologiques d'un lieu donné à partir de ses coordonnées de latitude et de longitude.

## Prérequis

Avant d'utiliser ce wrapper, s'assurer d'avoir les éléments suivants :

- Une clé API OpenWeatherMap valide. Si nécessaire s'inscrire sur [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) pour obtenir une clé API gratuite.
- Les coordonnées de latitude et de longitude du lieu pour lequel on souhaite obtenir les données météorologiques.

## Utilisation

1. Cloner le dépôt Git ou télécharger les fichiers du projet.

2. Définir les variables d'environnement `API_KEY`, `LAT` et `LONG` :

   - `API_KEY`: Clé API OpenWeatherMap.
   - `LAT`: Latitude du lieu pour lequel on souhaite obtenir les données météorologiques.
   - `LONG`: Longitude du lieu pour lequel on souhaite obtenir les données météorologiques.

3. Exécuter le script Python `app.py` :
   ```bash
   python app.py
   ```

## Exécution avec Docker

Il est également possible d'exécuter ce projet en utilisant Docker.

### Prérequis

Avant d'exécuter le projet avec Docker, s'assurer d'avoir Docker installé sur son système.

### Construction de l'image Docker

1. Cloner le dépôt Git ou télécharger les fichiers du projet sur sa machine locale.

2. Accéder au répertoire du projet où se trouve le fichier `Dockerfile`.

3. Ouvrir un terminal dans ce répertoire.

4. Construire l'image Docker en exécutant la commande suivante :
   ```bash
   docker build -t openweathermap_wrapper .
   ```
