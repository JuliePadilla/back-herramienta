from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.otro_rol_db import OtroRolInDB
from models.otro_rol_models import OtroRolInAdd, OtroRolOut

router = APIRouter()

@router.post("/otro_rol/crear/",response_model=OtroRolOut)
async def register_roles(new_rol: OtroRolInAdd, db: Session = Depends(get_db)):
    rol_in_db = OtroRolInDB(**new_rol.dict())
    db.add(rol_in_db)
    db.commit()
    db.refresh(rol_in_db)
    return rol_in_db

