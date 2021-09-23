from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class Cita_ProyectoInDB(Base):
    __tablename__ = "cita_proyecto"
    id_rol = Column(String(100), primary_key=True, unique=True)
    texto_proyecto = Column(String(3000))
    tema_proyecto= Column(String(20))
    otro_tema_proyecto = Column(String(100))
    correo_proyecto = Column(String(100))

Base.metadata.create_all(bind=engine)