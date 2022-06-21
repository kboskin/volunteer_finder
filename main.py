from logging import DEBUG
import databases

import uvicorn
from fastapi import FastAPI
import sqlalchemy as sa

from config import init_sentry, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO

app = FastAPI()

DB = databases.Database(SQLALCHEMY_DATABASE_URI)
metadata = sa.MetaData()
engine = sa.create_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=SQLALCHEMY_ECHO
)

if __name__ == '__main__':
    app.debug = DEBUG
    init_sentry()
    uvicorn.run(app, host='127.0.0.1', port=8000)