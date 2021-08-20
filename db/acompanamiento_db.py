from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class AcompanamientoInDB(Base):
    __tablename__ = "acompanamiento"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_usuario = Column(String(100))
    contador_acompanamiento = Column(Integer)
      
Base.metadata.create_all(bind=engine)