from fastapi.security import HTTPBearer
from fastapi.params import Depends
from fastapi import HTTPException
from typing import Any

import jwt


from core.config import settings

check_auth_header_exists = HTTPBearer()

ACCESS_DENIED = HTTPException(status_code=403, detail="Invalid auth header")


async def decode_token(encoded_token: str, is_refresh=False) -> dict:
    try:
        if not is_refresh:
            decoded_token = jwt.decode(
                encoded_token,
                settings.JWT_ACCESS_SECRET,
                algorithms=[settings.SECURITY_ALGORITHM],
            )
        else:
            decoded_token = jwt.decode(
                encoded_token,
                settings.JWT_REFRESH_SECRET,
                algorithms=[settings.SECURITY_ALGORITHM],
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Auth token expired")
    except jwt.InvalidTokenError:
        raise ACCESS_DENIED
    except jwt.PyJWTError as _:
        raise HTTPException(status_code=400, detail="Bad authorization header passed")
    decoded_token["original_token"] = encoded_token
    return decoded_token


async def validate_token(auth: Any = Depends(check_auth_header_exists)):
    return await decode_token(auth.credentials)


async def validate_refresh_token(auth: Any = Depends(check_auth_header_exists)):
    return await decode_token(auth.credentials, True)


# * meant for Microservice & Debug validation


async def check_debug_auth_token(auth: Any = Depends(check_auth_header_exists)) -> bool:
    """validates that the debug request is made with the secret, and not anyone else"""
    token = auth.credentials
    if token.strip() != settings.DEBUG_SECRET.strip():
        raise ACCESS_DENIED
    return True


async def validate_internal_api_key(
    auth: Any = Depends(check_auth_header_exists),
) -> bool:
    api_key = auth.credentials
    if api_key != settings.INTERNAL_API_KEY:
        raise ACCESS_DENIED
    return True
