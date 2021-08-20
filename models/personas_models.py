from pydantic import BaseModel

class EntidadInAdd(BaseModel):
    id_rol: str
    nombre_entidad: str
    departamento: str
    municipio: str


class EntidadOut(BaseModel):
    id_rol: str
    nombre_entidad: str
    departamento: str
    municipio: str

    class Config:
        orm_mode = True