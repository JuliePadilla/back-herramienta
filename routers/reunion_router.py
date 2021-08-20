from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.reunion_db import ReunionInDB
from models.reunion_models import ReunionInAdd, ReunionOut

router = APIRouter()

@router.post("/request/reunion/",response_model=ReunionOut)
async def register_reunion(new_request: ReunionInAdd, db: Session = Depends(get_db)):
    reunion_in_db = ReunionInDB(**new_request.dict())
    db.add(reunion_in_db)
    db.commit()
    db.refresh(reunion_in_db)
    return reunion_in_db