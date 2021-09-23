from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.cita_reunion_db import Cita_ReunionInDB
from models.cita_reunion_models import Cita_ReunionInAdd, Cita_ReunionOut

router = APIRouter()

@router.post("/meeting/create/",response_model=Cita_ReunionOut)
async def register_cita_reunion(new_request: Cita_ReunionInAdd, db: Session = Depends(get_db)):
    cita_reunion_in_db = Cita_ReunionInDB(**new_request.dict())
    db.add(cita_reunion_in_db)
    db.commit()
    db.refresh(cita_reunion_in_db)
    return cita_reunion_in_db