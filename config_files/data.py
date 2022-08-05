from dataclasses import dataclass
from config_files.config import get_OWMapi_key

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + get_OWMapi_key() + "&lang=ru&"
    "units=metric"
)


@dataclass(frozen=True, slots = True)
class Coordinates():
    latitube: float
    longitube: float
