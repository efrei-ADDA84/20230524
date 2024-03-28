import requests
import os

class OpenWeatherMapWrapper:
    def __init__(self, api_key, latitude, longitude):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"

        # Vérifier que les variables d'environnement sont définies
        if api_key is None or latitude is None or longitude is None:
            raise ValueError("Les variables d'environnement API_KEY, LATITUDE et LONGITUDE doivent être définies.")

    def get_weather(self):
        url = f"{self.base_url}lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"
        response = requests.get(url).json()

        if response["cod"] != "404":
            main = response["main"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            celsius, fahrenheit = self.kelvin_to_celsius_fahrenheit(temperature)
            weather_description = f"Il fait actuellement {celsius:.1f} degrés Celsius ({fahrenheit:.1f} degrés Fahrenheit). La pression atmosphérique est de {pressure} hPa et l'humidité est de {humidity}%."
            return weather_description
        else:
            return None

    def kelvin_to_celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32
        return celsius, fahrenheit

if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    latitude = os.getenv("LAT")
    longitude = os.getenv("LONG")

    weather_wrapper = OpenWeatherMapWrapper(api_key, latitude, longitude)
    weather_description = weather_wrapper.get_weather()

    if weather_description:
        print("Météo actuelle à la position géographique (latitude: {}, longitude: {}):".format(latitude, longitude))
        print(weather_description)
    else:
        print("Impossible de récupérer les données météorologiques.")
