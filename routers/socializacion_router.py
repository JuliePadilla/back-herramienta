from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.socializacion_db import SocializacionInDB
from models.socializacion_models import SocializacionInAdd, SocializacionOut

router = APIRouter()

@router.post("/request/socializacion/",response_model=SocializacionOut)
async def register_socializacion(new_request: SocializacionInAdd, db: Session = Depends(get_db)):
    socializacion_in_db = SocializacionInDB(**new_request.dict())
    db.add(socializacion_in_db)
    db.commit()
    db.refresh(socializacion_in_db)
    return socializacion_in_db