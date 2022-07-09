from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, HTTPBearer

from fastapi import Depends, Header
from jose import jwt, JWTError

from app.auth.exceptions import CredentialsException, AuthException
from app.profile.user.user import UserService
from config import AUTH

oauth2_scheme = HTTPBearer()


async def get_user_by_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = CredentialsException("Could not validate credentials")
    try:
        payload = jwt.decode(token.credentials, AUTH.secret_key, algorithms=[AUTH.algorithm])
        phone: str = payload.get("idx")
        if phone is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await UserService.get_user_by_phone(phone)

    if user is None:
        raise credentials_exception
    elif not user.is_active:
        raise AuthException("Inactive user")
    else:
        return user


IS_AUTHENTICATED = Depends(get_user_by_token)
