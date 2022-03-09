from pydantic import BaseModel

class TempReq(BaseModel):
    y: int
    m: int
    d: int
    h: int
    averageTemp: str

class Temp:
    def __init__(self, y: int, m: int, d: int, h: int, averageTemp: str):
        self.y = y
        self.m = m
        self.d = d
        self.h = h
        self.averageTemp = averageTemp
