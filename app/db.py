from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import List
import os
import datetime

from temp import Temp, TempReq

class Db:
    def __init__(self):
        load_dotenv()
        client = MongoClient(os.environ.get("MONGODB_URI"))
        self.db = client["weather-app"]
        self.temps_coll = self.db[os.environ.get("MONGODB_NAME")]
        self.last_temp_coll = self.db["last_temp"]

    def add_temp(self, temp: TempReq):
        self.temps_coll.insert_one(jsonable_encoder(temp))

    def add_last_temp(self, temp: TempReq):
        self.last_temp_coll.replace_one({}, jsonable_encoder(temp))

    def get_temps(self, m: int, d: int) -> List[Temp]:
        search: List[Temp] = []
        for t in self.temps_coll.find({"m": m, "d": d}):
            temp = Temp(t["y"], t["m"], t["d"], t["h"], t["averageTemp"])
            search.append(temp)
        return search

    def last_temp(self) -> Temp:
        t = self.last_temp_coll.find_one()
        return Temp(t["y"], t["m"], t["d"], t["h"], t["averageTemp"])

    def last_days(self, days: int) -> List[Temp]:
        now = datetime.datetime.now()
        before = now - datetime.timedelta(days)
        before_days: List[int] = []
        now_days: List[int] = []
        for i in range(0, days):
            date = now - datetime.timedelta(days=i)
            if date.month == before.month:
                before_days.append(date.day)
            else:
                now_days.append(date.day)
        search: List[Temp] = []
        for t in self.temps_coll.find({"d": {"$in": now_days}, "m": now.month}):
            temp = Temp(t["y"], t["m"], t["d"], t["h"], t["averageTemp"])
            search.append(temp)
        for t in self.temps_coll.find({"d": {"$in": before_days}, "m": before.month}):
            temp = Temp(t["y"], t["m"], t["d"], t["h"], t["averageTemp"])
            search.append(temp)
        return search
