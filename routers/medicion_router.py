from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.medicion_db import MedicionInDB
from models.medicion_models import MedicionInAdd, MedicionOut

router = APIRouter()

@router.post("/request/medicion/",response_model=MedicionOut)
async def register_medicion(new_request: MedicionInAdd, db: Session = Depends(get_db)):
    medicion_in_db = MedicionInDB(**new_request.dict())
    db.add(medicion_in_db)
    db.commit()
    db.refresh(medicion_in_db)
    return medicion_in_db