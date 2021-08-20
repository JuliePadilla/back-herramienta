from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.acompanamiento_db import AcompanamientoInDB
from models.acompanamiento_models import AcompanamientoInAdd, AcompanamientoOut

router = APIRouter()

@router.post("/request/acompanamiento/",response_model=AcompanamientoOut)
async def register_acompanamiento(new_request: AcompanamientoInAdd, db: Session = Depends(get_db)):
    acompanamiento_in_db = AcompanamientoInDB(**new_request.dict())
    db.add(acompanamiento_in_db)
    db.commit()
    db.refresh(acompanamiento_in_db)
    return acompanamiento_in_db