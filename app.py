import requests
import os
from dotenv import load_dotenv

class OpenWeatherMapWrapper:
    def __init__(self, api_key, latitude, longitude):
        if api_key is None or latitude is None or longitude is None:
            raise ValueError("Les variables d'environnement API_KEY, LATITUDE et LONGITUDE doivent être définies.")
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        
        # Appel à l'API OpenWeatherMap pour récupérer les données météorologiques
        url = f"{self.base_url}lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"
        self.response = requests.get(url).json()

        if self.response["cod"] != "404":
            self.main = self.response["main"]
            self.temperature = self.main["temp"]
            self.pressure = self.main["pressure"]
            self.humidity = self.main["humidity"]
            self.celsius, self.fahrenheit = self.kelvin_to_celsius_fahrenheit(self.temperature)


    def get_weather(self):
        weather_description = f"Il fait actuellement {self.celsius:.1f} degrés Celsius ({self.fahrenheit:.1f} degrés Fahrenheit). La pression atmosphérique est de {self.pressure} hPa et l'humidité est de {self.humidity}%."
        return weather_description
    
    def kelvin_to_celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32
        return celsius, fahrenheit

if __name__ == "__main__":
    load_dotenv()
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