import pytest
import os
from app import OpenWeatherMapWrapper

api_key = "69a51c15ef27c400261980ddf6c2e60c"
latitude = 48.8534
longitude = 2.3488

def test_kelvin_to_celsius_fahrenheit():
    weather_wrapper = OpenWeatherMapWrapper(api_key, latitude, longitude)
    celsius, fahrenheit = weather_wrapper.kelvin_to_celsius_fahrenheit(288.15)
    assert celsius == pytest.approx(15.0, abs=0.1)
    assert fahrenheit == pytest.approx(59.0, abs=0.1)

def test_get_weather():
    weather_wrapper = OpenWeatherMapWrapper(api_key, latitude, longitude)
    weather_description = weather_wrapper.get_weather()

    assert weather_description is not None
    assert "Il fait actuellement" in weather_description
    assert "degrés Celsius" in weather_description
    assert "degrés Fahrenheit" in weather_description
    assert "La pression atmosphérique est de" in weather_description
    assert "l'humidité est de" in weather_description