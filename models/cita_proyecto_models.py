from pydantic import BaseModel

class Cita_ProyectoInAdd(BaseModel):
    id_rol: str
    texto_proyecto: str
    tema_proyecto: str
    otro_tema_proyecto: str
    correo_proyecto: str


class Cita_ProyectoOut(BaseModel):
    id_rol: str
    texto_proyecto: str
    tema_proyecto: str
    otro_tema_proyecto: str
    correo_proyecto: str

    class Config:
        orm_mode = True