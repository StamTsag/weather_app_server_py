from pydantic import BaseModel

class Temp(BaseModel):
    y: int
    m: int
    d: int
    h: int
    averageTemp: str
