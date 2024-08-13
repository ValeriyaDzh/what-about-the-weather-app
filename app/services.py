import requests
from geopy.geocoders import Nominatim


async def get_coordinate(city: str) -> tuple[float]:
    geolocator = Nominatim(user_agent="GetLog")
    location = geolocator.geocode(city)
    print(location.latitude, location.longitude)
    return location.latitude, location.longitude


async def get_weater_today(city: str):
    coordinats = await get_coordinate(city)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coordinats[0],
        "longitude": coordinats[1],
        "hourly": "temperature_2m,precipitation",
        "current_weather": True,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        # return response.json()
        data = response.json()
        return f'{data["current_weather"]["temperature"]}{data["hourly_units"]["temperature_2m"]}'


# добавить ограничение по названию города
