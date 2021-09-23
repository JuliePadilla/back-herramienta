from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class EntidadInDB(Base):
    __tablename__ = "entidad"
    id_rol = Column(String(100), primary_key=True, unique=True)
    nombre_entidad = Column(String(300))
    otra_entidad = Column(String(300))
    departamento = Column(String(100))
    municipio = Column(String(100))
      
Base.metadata.create_all(bind=engine)