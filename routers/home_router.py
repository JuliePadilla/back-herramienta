from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.home_db import RolInDB
from models.home_models import RolInAdd, RolOut
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/rol/crear/",response_model=RolOut)
async def register_roles(new_rol: RolInAdd, db: Session = Depends(get_db)):
    rol_in_db = RolInDB(**new_rol.dict(),id_rol=str(uuid.uuid4()),fecha=datetime.now())
    db.add(rol_in_db)
    db.commit()
    db.refresh(rol_in_db)
    return rol_in_db

