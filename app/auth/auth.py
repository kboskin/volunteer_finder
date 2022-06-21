from fastapi import APIRouter

from app.integrations.twillio.twilio import validate_phone, verify_sms_code

router = APIRouter()

class AuthException(Exception):
    pass


class AuthService:
    @classmethod
    async def login(cls, phone, code):
        if not validate_phone(phone):
            raise AuthException

        status = verify_sms_code(phone, code.strip())
        if status == PhoneVerificationStatus.EXPIRED:
            raise CodeExpiredError("Code has been expired", status=status)

        if status == PhoneVerificationStatus.PENDING:
            raise CodeMismatchError("Invalid verification code", status=status)

