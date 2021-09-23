from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.cita_charla_db import Cita_CharlaInDB
from models.cita_charla_models import Cita_CharlaInAdd, Cita_CharlaOut

router = APIRouter()

@router.post("/charla/create/",response_model=Cita_CharlaOut)
async def register_cita_charla(new_request: Cita_CharlaInAdd, db: Session = Depends(get_db)):
    cita_charla_in_db = Cita_CharlaInDB(**new_request.dict())
    db.add(cita_charla_in_db)
    db.commit()
    db.refresh(cita_charla_in_db)
    return cita_charla_in_db