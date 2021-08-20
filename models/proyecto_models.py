from pydantic import BaseModel

class ProyectoInAdd(BaseModel):
    id_usuario: str
    contador_proyecto: int

class ProyectoOut(BaseModel):
    id:int
    id_usuario: str
    contador_proyecto: int

    class Config:
        orm_mode = True