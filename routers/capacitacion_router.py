from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.capacitacion_db import CapacitacionInDB
from models.capacitacion_models import CapacitacionInAdd, CapacitacionOut

router = APIRouter()

@router.post("/request/capacitacion/",response_model=CapacitacionOut)
async def register_capacitacion(new_request: CapacitacionInAdd, db: Session = Depends(get_db)):
    capacitacion_in_db = CapacitacionInDB(**new_request.dict())
    db.add(capacitacion_in_db)
    db.commit()
    db.refresh(capacitacion_in_db)
    return capacitacion_in_db