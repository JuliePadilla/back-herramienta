from sqlalchemy import Column, String
from db.db_conection import Base, engine

class OtroRolInDB(Base):
    __tablename__ = "otro_rol"
    id_rol = Column(String(100), primary_key=True, unique=True)
    nombre_rol = Column(String(300))
      
Base.metadata.create_all(bind=engine)