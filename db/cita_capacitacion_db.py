from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class Cita_CapacitacionInDB(Base):
    __tablename__ = "cita_capacitacion"
    id_rol = Column(String(100), primary_key=True, unique=True)
    texto_capacitacion = Column(String(3000))
    personas_capacitacion = Column(Integer)
    modalidad_capacitacion = Column(String(20))
    tema_capacitacion = Column(String(100))
    otro_tema_capacitacion = Column(String(100))
    fecha_capacitacion = Column(String(100))
    correo_capacitacion = Column(String(100))

Base.metadata.create_all(bind=engine)