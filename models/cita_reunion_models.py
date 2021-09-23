from pydantic import BaseModel

class Cita_ReunionInAdd(BaseModel):
    id_rol: str
    texto_reunion: str
    tema_reunion: str
    fecha_reunion: str
    hora_reunion: str
    correo_reunion: str


class Cita_ReunionOut(BaseModel):
    id_rol: str
    texto_reunion: str
    tema_reunion: str
    fecha_reunion: str
    hora_reunion: str
    correo_reunion: str

    class Config:
        orm_mode = True