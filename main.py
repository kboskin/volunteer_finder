import asyncio

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import authRouter
from config import init_sentry, DEBUG, CORS
from enigine import DB

app = FastAPI(debug=DEBUG)
app.include_router(authRouter, prefix="/auth")

if DEBUG:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def connect_to_db():
    return await DB.connect()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(connect_to_db())


if __name__ == '__main__':
    app.debug = DEBUG
    init_sentry()
    uvicorn.run(app, host='127.0.0.1', port=8000)
