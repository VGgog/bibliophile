from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    from src.config import Config
except ModuleNotFoundError:
    from config import Config

engine = create_engine(Config.db_url)
session = sessionmaker(engine)
base = declarative_base()


def get_db():
    """Create dependency"""
    db = session()
    try:
        yield db
    finally:
        db.close()
