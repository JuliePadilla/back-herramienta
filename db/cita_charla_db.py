from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class Cita_CharlaInDB(Base):
    __tablename__ = "cita_charla"
    id_rol = Column(String(100), primary_key=True, unique=True)
    texto_charla = Column(String(3000))
    personas_charla = Column(Integer)
    modalidad_charla = Column(String(20))
    tema_charla = Column(String(100))
    otro_tema_charla = Column(String(100))
    fecha_charla = Column(String(100))
    correo_charla = Column(String(100))

Base.metadata.create_all(bind=engine)