from pydantic import BaseModel

class CapacitacionInAdd(BaseModel):
    id_usuario: str
    contador_capacitacion: int

class CapacitacionOut(BaseModel):
    id:int
    id_usuario: str
    contador_capacitacion: int

    class Config:
        orm_mode = True