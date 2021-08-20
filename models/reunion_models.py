from pydantic import BaseModel

class ReunionInAdd(BaseModel):
    id_usuario: str
    contador_reunion: int

class ReunionOut(BaseModel):
    id:int
    id_usuario: str
    contador_reunion: int

    class Config:
        orm_mode = True