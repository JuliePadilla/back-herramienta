from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class SolicitudInDB(Base):
    __tablename__ = "solicitud"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_rol = Column(String(100))
    lineamientos = Column(Integer)
    socializacion = Column(Integer)
    acompanamiento = Column(Integer)
    fortalecimiento = Column(Integer)
    medicion = Column(Integer)
    proyecto = Column(Integer)
    charla = Column(Integer)
    capacitacion = Column(Integer)
    reunion = Column(Integer)
 
Base.metadata.create_all(bind=engine)