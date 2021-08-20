from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.proyecto_db import ProyectoInDB
from models.proyecto_models import ProyectoInAdd, ProyectoOut

router = APIRouter()

@router.post("/request/proyecto/",response_model=ProyectoOut)
async def register_proyecto(new_request: ProyectoInAdd, db: Session = Depends(get_db)):
    proyecto_in_db = ProyectoInDB(**new_request.dict())
    db.add(proyecto_in_db)
    db.commit()
    db.refresh(proyecto_in_db)
    return proyecto_in_db