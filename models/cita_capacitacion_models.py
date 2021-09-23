from pydantic import BaseModel

class Cita_CapacitacionInAdd(BaseModel):
    id_rol: str
    texto_capacitacion: str
    personas_capacitacion: int
    modalidad_capacitacion: str
    tema_capacitacion: str
    otro_tema_capacitacion: str
    fecha_capacitacion: str
    correo_capacitacion: str


class Cita_CapacitacionOut(BaseModel):
    id_rol: str
    texto_capacitacion: str
    personas_capacitacion: int
    modalidad_capacitacion: str
    tema_capacitacion: str
    otro_tema_capacitacion: str
    fecha_capacitacion: str
    correo_capacitacion: str

    class Config:
        orm_mode = True