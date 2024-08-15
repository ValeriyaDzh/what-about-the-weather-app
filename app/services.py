import logging

import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

from app.exeptions import NotFoundException, UnprocessableEntityException

logger = logging.getLogger("weater_app")


async def get_coordinate(city: str) -> tuple[float]:
    geolocator = Nominatim(user_agent="GetLog")
    try:
        location = geolocator.geocode(city)
        if location is not None:
            logger.info(f"Get from {city}: {location.raw}")
            if location.raw["addresstype"] in ("town", "city", "country", "county"):
                return location.latitude, location.longitude
            else:
                raise UnprocessableEntityException(
                    "You must enter the name of the: town, city, county, country "
                )
        else:
            logger.info(f"Not found {city}")
            raise NotFoundException(
                f"Oops...nothing was found. Check the entered data: {city}"
            )
    except GeocoderTimedOut:
        ...


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
        data = response.json()
        return f'{data["current_weather"]["temperature"]}{data["hourly_units"]["temperature_2m"]}'
