#!/usr/bin/env python3.10.5
import ssl 
import json
from json import JSONDecodeError
from dataclasses import dataclass
from typing import TypeAlias,Literal
from enum import Enum
import urllib.request
from urllib.error import URLError
from datetime import datetime


from config_files.config import Coordinates,OPENWEATHER_URL

Celsius: TypeAlias = float
Wind: TypeAlias = float
GustWind: TypeAlias = float


class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots= True, frozen = True)
class Weather():
    temperature: Celsius 
    wind: float
    gust_wind: float
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str
    weather_icon: str

    



def get_weather(coordinates: Coordinates) -> str:
    open_weather_response = _get_open_weather_response(longitube=coordinates.longitube,
                                                        latitube = coordinates.latitube)
    weather = _parse_weather_response(open_weather_response)
    return _format_weather(weather)

def _get_open_weather_response(latitube: float, longitube: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = OPENWEATHER_URL.format(
        latitude=latitube, longitude=longitube)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise 


def _parse_weather_response(open_weather_response: str) -> Weather:
    try:
        openweather_dict = json.loads(open_weather_response)
    except JSONDecodeError:
        raise 
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        wind = _parse_wind_speed(openweather_dict),
        gust_wind = _parse_gust_wind(openweather_dict),
        weather_type =_parse_weather_type(openweather_dict),
        sunrise =_parse_sun_time(openweather_dict, "sunrise"),
        sunset =_parse_sun_time(openweather_dict, "sunset"),
        city =_parse_city(openweather_dict),
        weather_icon= _parse_weather_icon(openweather_dict)
    )

def _parse_weather_icon(openweather_dict: dict) -> str :
    id = openweather_dict["weather"][0]["icon"]
    icon = f"http://openweathermap.org/img/wn/{id}@4x.png"
    return icon 
    
def _parse_wind_speed(openweather_dict: dict) -> Wind:
    return round(openweather_dict["wind"]["speed"])

def _parse_gust_wind(openweather_dict: dict) -> GustWind:
    return round(openweather_dict["wind"]["gust"])

def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])

def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise 

def _parse_sun_time(
        openweather_dict: dict,
        time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])

def _parse_city(openweather_dict: dict) -> str:
    try:
        return openweather_dict["name"]
    except KeyError:
        raise



def _format_weather(weather: Weather) -> str:
    return (f"{weather.city}, температура {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"Скорость ветра {weather.wind} м/с \nc порывами до {weather.gust_wind} м/с\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n"
            f"{weather.weather_icon}"
            )


if __name__ == "__main__":
    print(get_weather(Coordinates(latitube=55.7, longitube=36.7)))    
