from flask import Flask, request, jsonify
from app import OpenWeatherMapWrapper
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Créez une instance de la classe OpenWeatherMapWrapper avec votre clé API
load_dotenv()
api_key = os.environ.get("API_KEY")

# Route pour récupérer les données météorologiques en fonction de la latitude et de la longitude
@app.route('/weather')
def weather():
    # Récupérer les paramètres de la requête (latitude et longitude)
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    weather_wrapper = OpenWeatherMapWrapper(api_key, latitude, longitude)

    # Vérifier si les paramètres sont présents
    if latitude is None or longitude is None:
        return jsonify({"error": "Latitude and longitude parameters are required."}), 400

    # Construire la réponse JSON
    if weather_wrapper:
        response = {
            "weather": {
                "temperature": {
                    "celsius": weather_wrapper.celsius,
                    "fahrenheit": weather_wrapper.fahrenheit
                },
                "pressure": weather_wrapper.pressure,
                "humidity": weather_wrapper.humidity
            }
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Failed to retrieve weather data."}), 500

if __name__ == '__main__':
    # Démarrez le serveur Flask en écoutant sur le port 80 sur toutes les adresses disponibles
    app.run(debug=True , host='0.0.0.0',port=80)

