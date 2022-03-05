import json
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from temp import Temp
from db import Db

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Db()

temps: List[Temp] = []

@app.get("/add/{temp}")
async def add_temp(temp: str):
    temp = Temp(temp)
    temps.append(temp)
    return {"msg": "ok"}

@app.get("/temps/{m}/{d}")
async def search_temps(m: int, d: int):
    return db.get_temps(m, d)

@app.get("/last_temp")
async def last_temp():
    return db.last_temp()

@app.get("/last_days/{d}")
async def last_days(d: int):
    if d == 0 or d > 29:
        return {"msg": "day cannot be 0 or larger than 29"}
    return db.last_days(d)
