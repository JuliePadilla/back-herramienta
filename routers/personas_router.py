from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.personas_db import EntidadInDB
from models.personas_models import EntidadInAdd, EntidadOut

router = APIRouter()

@router.post("/entidad/crear/",response_model=EntidadOut)
async def register_entidades(new_entidad: EntidadInAdd, db: Session = Depends(get_db)):
    entidad_in_db = EntidadInDB(**new_entidad.dict())
    db.add(entidad_in_db)
    db.commit()
    db.refresh(entidad_in_db)
    return entidad_in_db

