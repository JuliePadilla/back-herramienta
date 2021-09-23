from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.cita_capacitacion_db import Cita_CapacitacionInDB
from models.cita_capacitacion_models import Cita_CapacitacionInAdd, Cita_CapacitacionOut

router = APIRouter()

@router.post("/capacitacion/create/",response_model=Cita_CapacitacionOut)
async def register_cita_capacitacion(new_request: Cita_CapacitacionInAdd, db: Session = Depends(get_db)):
    cita_capacitacion_in_db = Cita_CapacitacionInDB(**new_request.dict())
    db.add(cita_capacitacion_in_db)
    db.commit()
    db.refresh(cita_capacitacion_in_db)
    return cita_capacitacion_in_db