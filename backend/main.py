from fastapi import FastAPI
import aiohttp

import api

app = FastAPI()

@app.get("/data/{lat}/{lng}")
async def get_data(lat: float, lng: float):
    async with aiohttp.ClientSession() as s:
        data = await api.get_scores(lat, lng, s)
        return {
            "overall": data.overall_score(),
            "scores": data
        }
