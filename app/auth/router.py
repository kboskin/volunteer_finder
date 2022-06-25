from fastapi import APIRouter
from fastapi import Request

from app.auth.auth import AuthService

authRouter = APIRouter()

from pydantic import BaseModel


class SendCodeBody(BaseModel):
    phone_number: str


class VerifyCodeBody(BaseModel):
    phone_number: str
    code: str


@authRouter.post("/code")
async def request_code(model: SendCodeBody):
    return await AuthService.send_code(model.phone_number)


@authRouter.post("/verify")
async def request_code(model: VerifyCodeBody):
    return await AuthService.verify_code(model.phone_number, model.code)
