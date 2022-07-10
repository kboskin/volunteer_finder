from fastapi import APIRouter

from app.auth.auth import AuthService
from pydantic import BaseModel

from app.generic.base import BaseSuccessResponse, object_as_dict
from app.profile.user.user import UserService

authRouter = APIRouter()


class SendCodeBody(BaseModel):
    phone_number: str


class VerifyCodeBody(BaseModel):
    phone_number: str
    code: str


@authRouter.post("/code")
async def request_code(model: SendCodeBody):
    user = await UserService.get_user_by_phone(model.phone_number)
    if not user:
        user = await UserService.create_user_profile(model.phone_number)

    await AuthService.send_code(model.phone_number)
    return BaseSuccessResponse(
        {
            "user": object_as_dict(user),
            "token": AuthService.get_token(model.phone_number)
        }
    )


@authRouter.post("/verify")
async def verify_code(model: VerifyCodeBody):
    phone_number = model.phone_number
    await AuthService.verify_code(phone_number, model.code)
    user = await UserService.get_user_by_phone(phone_number)
    return BaseSuccessResponse({"user": object_as_dict(user), "token": AuthService.get_token(phone_number)})
