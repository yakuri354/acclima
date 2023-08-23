from aiohttp import ClientSession
from secret import WAQI_TOKEN, OWM_TOKEN

async def waqi_data(lat: float, lng: float, s: ClientSession):
    async with s.get(f"https://api.waqi.info/feed/geo:{lat};{lng}?token={WAQI_TOKEN}") as r:
        return await r.json()

async def owm_data(lat: float, lng: float, s: ClientSession):
    async with s.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lng}&appid={OWM_TOKEN}") as r:
        return await r.json()