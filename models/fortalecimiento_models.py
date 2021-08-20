from pydantic import BaseModel

class FortalecimientoInAdd(BaseModel):
    id_usuario: str
    contador_fortalecimiento: int

class FortalecimientoOut(BaseModel):
    id:int
    id_usuario: str
    contador_fortalecimiento: int

    class Config:
        orm_mode = True