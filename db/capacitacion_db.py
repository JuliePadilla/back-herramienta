from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class CapacitacionInDB(Base):
    __tablename__ = "capacitacion"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_usuario = Column(String(100))
    contador_capacitacion = Column(Integer)
      
Base.metadata.create_all(bind=engine)