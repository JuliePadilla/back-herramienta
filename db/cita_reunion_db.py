from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class Cita_ReunionInDB(Base):
    __tablename__ = "cita_reunion"
    id_rol = Column(String(100), primary_key=True, unique=True)
    texto_reunion = Column(String(100))
    tema_reunion = Column(String(3000))
    fecha_reunion = Column(String(100))
    hora_reunion = Column(String(100))
    correo_reunion = Column(String(100))

Base.metadata.create_all(bind=engine)