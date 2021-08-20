from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class ReunionInDB(Base):
    __tablename__ = "reunion"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_usuario = Column(String)
    contador_reunion = Column(Integer)
      
Base.metadata.create_all(bind=engine)