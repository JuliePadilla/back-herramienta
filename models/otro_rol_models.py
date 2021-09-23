from pydantic import BaseModel

class OtroRolInAdd(BaseModel):
    id_rol: str
    nombre_rol: str

class OtroRolOut(BaseModel):
    id_rol: str
    nombre_rol: str

    class Config:
        orm_mode = True