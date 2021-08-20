from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.fortalecimiento_db import FortalecimientoInDB
from models.fortalecimiento_models import FortalecimientoInAdd, FortalecimientoOut

router = APIRouter()

@router.post("/request/fortalecimiento/",response_model=FortalecimientoOut)
async def register_fortalecimiento(new_request: FortalecimientoInAdd, db: Session = Depends(get_db)):
    fortalecimiento_in_db = FortalecimientoInDB(**new_request.dict())
    db.add(fortalecimiento_in_db)
    db.commit()
    db.refresh(fortalecimiento_in_db)
    return fortalecimiento_in_db