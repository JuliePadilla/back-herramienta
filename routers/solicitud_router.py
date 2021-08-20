from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.solicitud_db import SolicitudInDB
from models.solicitud_models import SolicitudInAdd, SolicitudOut

router = APIRouter()

@router.post("/request/solicitud/",response_model=SolicitudOut)
async def register_solicitudes(new_request: SolicitudInAdd, db: Session = Depends(get_db)):
    solicitud_in_db = SolicitudInDB(**new_request.dict())
    db.add(solicitud_in_db)
    db.commit()
    db.refresh(solicitud_in_db)
    return solicitud_in_db