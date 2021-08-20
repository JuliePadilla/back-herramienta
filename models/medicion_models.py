from pydantic import BaseModel

class MedicionInAdd(BaseModel):
    id_usuario: str
    contador_medicion: int

class MedicionOut(BaseModel):
    id:int
    id_usuario: str
    contador_medicion: int

    class Config:
        orm_mode = True