from pydantic import BaseModel

class SocializacionInAdd(BaseModel):
    id_usuario: str
    contador_socializacion: int

class SocializacionOut(BaseModel):
    id:int
    id_usuario: str
    contador_socializacion: int

    class Config:
        orm_mode = True