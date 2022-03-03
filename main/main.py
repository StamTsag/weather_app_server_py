import json
from fastapi import FastAPI
from typing import List

from temp import Temp
from db import Db

app = FastAPI()
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

@app.get("/last_days/{d}")
async def last_days(d: int):
    return db.last_days(d)
