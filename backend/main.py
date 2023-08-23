from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import aiohttp

import api
import secret as s
from orm import Base

app = FastAPI()

db_engine = create_async_engine(
    f"postgresql+asyncpg://{s.DB_NAME}:{s.DB_PASS}@{s.DB_HOST}/{s.DB_NAME}",
    echo=True
)

db_session_maker = async_sessionmaker(db_engine, expire_on_commit=False)

@app.get("/data/{lat}/{lng}")
async def get_data(lat: float, lng: float):
    async with aiohttp.ClientSession() as s:
        data = await api.get_scores(lat, lng, s, db_session_maker)
        return {
            "overall": data.overall_score(),
            "scores": data
        }

@app.on_event("startup")
async def startup():
    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
@app.on_event("shutdown")
async def shutdown():
    await db_engine.dispose()
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)