from pydantic import BaseModel

class AcompanamientoInAdd(BaseModel):
    id_usuario: str
    contador_acompanamiento: int

class AcompanamientoOut(BaseModel):
    id:int
    id_usuario: str
    contador_acompanamiento: int

    class Config:
        orm_mode = True