import jwt
import bcrypt, hashlib, secrets
import datetime
from src.core.config import Config
from typing import Optional
from fastapi.param_functions import Header
from fastapi import HTTPException
from fastapi import status



ALGORITHM = "HS256"

def create_jwt_token(user_id: int, username: str, is_refresh: bool = False) -> str:
    payload = {
        "iss": Config.APP_NAME_CODE,
        "sub": username,
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "userId": user_id,
    }

    if is_refresh:
        expired_time = Config.REFRESH_TOKEN_EXPIRATION
        secret = Config.REFRESH_SECRET_KEY
    else:
        expired_time = Config.TOKEN_EXPIRATION
        secret = Config.SECRET_KEY

    payload["exp"] = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=int(expired_time))

    token = jwt.encode(payload, secret, algorithm=ALGORITHM)
    return token, expired_time


def verify_jwt_token(jwt_token: str, is_refresh_token: bool = False) -> str:
    try:
        secret = Config.REFRESH_SECRET_KEY if is_refresh_token else Config.SECRET_KEY
        decoded_payload = jwt.decode(
            jwt=jwt_token,
            key=secret,
            algorithms=[ALGORITHM],
            options={"verify_exp": True}
        )
        return decoded_payload
    except Exception as e:
        raise HTTPException(detail="Token has expired or invalid", status_code=status.HTTP_401_UNAUTHORIZED)

def create_refresh_token() -> str:
    refresh_token = secrets.token_urlsafe(64)
    return refresh_token

def exchange_refresh_token(refresh_token: str) -> str:
    decoded_payload = verify_jwt_token(refresh_token, is_refresh_token=True)
    user_id = decoded_payload.get("userId")
    username = decoded_payload.get("sub")

    access_token, expires_in = create_jwt_token(user_id, username, is_refresh=False)
    refresh_token, refresh_expires_in = create_jwt_token(user_id, username, is_refresh=True)

    return access_token, expires_in, refresh_token

def required_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(detail="Token is required", status_code=status.HTTP_401_UNAUTHORIZED)
    if not authorization.startswith("Bearer "):
        raise HTTPException(detail="Invalid token", status_code=status.HTTP_401_UNAUTHORIZED)

    jwt_token = authorization.split(" ")[1]
    payload = verify_jwt_token(jwt_token, is_refresh_token=False)
    return payload.get('userId')