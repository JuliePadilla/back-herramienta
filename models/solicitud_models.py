from pydantic import BaseModel

class SolicitudInAdd(BaseModel):
    id_rol: str
    lineamientos: int
    socializacion: int
    acompanamiento: int
    fortalecimiento: int
    medicion: int
    proyecto: int
    charla: int
    capacitacion: int
    reunion: int

class SolicitudOut(BaseModel):
    id:int
    id_rol: str
    lineamientos: int
    socializacion: int
    acompanamiento: int
    fortalecimiento: int
    medicion: int
    proyecto: int
    charla: int
    capacitacion: int
    reunion: int

    class Config:
        orm_mode = True
   



