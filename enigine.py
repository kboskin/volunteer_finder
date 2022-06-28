import databases
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO

DB = databases.Database(SQLALCHEMY_DATABASE_URI)
metadata = sa.MetaData()
engine = sa.create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=SQLALCHEMY_ECHO
)

Session = sessionmaker(bind=engine)
session = Session()