from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.charla_db import CharlaInDB
from models.charla_models import CharlaInAdd, CharlaOut

router = APIRouter()

@router.post("/request/charla/",response_model=CharlaOut)
async def register_charla(new_request: CharlaInAdd, db: Session = Depends(get_db)):
    charla_in_db = CharlaInDB(**new_request.dict())
    db.add(charla_in_db)
    db.commit()
    db.refresh(charla_in_db)
    return charla_in_db