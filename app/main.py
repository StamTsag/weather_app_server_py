from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from temp import Temp
from db import Db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Db()

@app.post("/add_temp")
async def add_temp(temp: Temp):
    db.add_temp(temp)
    db.add_last_temp(temp)
    return {"msg": "ok"}

@app.post("/add_last_temp")
async def add_last_temp(temp: Temp):
    db.add_last_temp(temp)
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
