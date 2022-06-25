from datetime import timedelta, datetime

import jwt

from app.auth.exceptions import AuthException, CodeExpiredError, NumberIssueError
from app.integrations.twillio.twilio import validate_phone, verify_sms_code, PhoneVerificationStatus, send_sms_code
from config import AUTH


class AuthService:
    @classmethod
    async def send_code(cls, phone):
        if not validate_phone(phone):
            raise AuthException("invalid phone")

        if not send_sms_code(phone):
            raise AuthException("invalid phone")
        else:
            return {"message": "success"}

    @classmethod
    async def verify_code(cls, phone, code):
        if not validate_phone(phone):
            raise AuthException("invalid phone")

        status = verify_sms_code(phone, code.strip())
        if status == PhoneVerificationStatus.EXPIRED:
            raise CodeExpiredError("Code has been expired", status=status)

        if status == PhoneVerificationStatus.PENDING:
            raise NumberIssueError("Invalid verification code", status=status)

    @classmethod
    def get_token(cls, phone: str) -> str:
        access_token_expires = timedelta(minutes=AUTH.access_token_expire_minutes)
        to_encode = {"idx": phone}
        if access_token_expires:
            expire = datetime.utcnow() + access_token_expires
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, AUTH.secret_key, algorithm=AUTH.algorithm)
        return encoded_jwt
