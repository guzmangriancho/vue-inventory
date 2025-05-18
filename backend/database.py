from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "sqlite:///./products.db"

# engine y sesion
engine = create_engine(database_url, connect_args={"check_same_thread": False})
sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
base = declarative_base()

def init_db():
    # crea tablas si no hay
    import models
    base.metadata.create_all(bind=engine)
