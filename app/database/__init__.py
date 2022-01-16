from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql+psycopg2://postgres:monoliza@localhost/bibliophile")
session = sessionmaker(engine)
base = declarative_base()
