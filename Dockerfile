# Utiliser une image Python officielle en tant qu'image de base
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /TP1

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances Python à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel l'application Flask fonctionne
EXPOSE 8081

# Définir les variables d'environnement pour la latitude, la longitude et la clé API
ENV LAT=""
ENV LONG=""
ENV API_KEY=""

# Commande par défaut à exécuter lorsque le conteneur est lancé
CMD ["python", "weather_api.py"]
