from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class FortalecimientoInDB(Base):
    __tablename__ = "fortalecimiento"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_usuario = Column(String(100))
    contador_fortalecimiento = Column(Integer)
      
Base.metadata.create_all(bind=engine)