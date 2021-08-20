from pydantic import BaseModel

class CharlaInAdd(BaseModel):
    id_usuario: str
    contador_charla: int

class CharlaOut(BaseModel):
    id:int
    id_usuario: str
    contador_charla: int

    class Config:
        orm_mode = True
