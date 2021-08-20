from pydantic import BaseModel
from datetime import datetime

class RolInAdd(BaseModel):
    rol: str
    contador: int

class RolOut(BaseModel):
    id_rol: str
    fecha: datetime
    rol: str
    contador: int

    class Config:
        orm_mode = True