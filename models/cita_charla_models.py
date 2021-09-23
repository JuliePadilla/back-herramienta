from pydantic import BaseModel

class Cita_CharlaInAdd(BaseModel):
    id_rol: str
    texto_charla: str
    personas_charla: int
    modalidad_charla: str
    tema_charla: str
    otro_tema_charla: str
    fecha_charla: str
    correo_charla: str


class Cita_CharlaOut(BaseModel):
    id_rol: str
    texto_charla: str
    personas_charla: int
    modalidad_charla: str
    tema_charla: str
    otro_tema_charla: str
    fecha_charla: str
    correo_charla: str

    class Config:
        orm_mode = True