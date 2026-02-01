import sqlmodel 
from sqlmodel import SQLModel
from .config import DATABASE_URL

if not DATABASE_URL:
    raise NotImplementedError("DATABASE_URL is not set")

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL needs to be set")



engine = sqlmodel.create_engine(str(DATABASE_URL))


def init_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)