USE_ROUNDED_COORDS = False
OPENWEATHER_API = "29c33489ae12ea696d0e3ce965213b4e"  # paste API token here
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
