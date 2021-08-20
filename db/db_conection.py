from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creando Motor y Conexion con la Base de Datos
DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/elp"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

#Creacion de la Sesion 
SessionLocal = sessionmaker(autocommit=False, 
                            autoflush=False, 
                            bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Creando Base para la creacion de los modelos
Base = declarative_base()