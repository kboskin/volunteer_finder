import databases
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO

DB = databases.Database(SQLALCHEMY_DATABASE_URI)
engine = sa.create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=SQLALCHEMY_ECHO
)

Base = declarative_base(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()