from datetime import datetime, timedelta, timezone
import jwt
from backend_app.pydantic_models import AccessCodeModel
from config import Config
from pytz import timezone
from jwt.exceptions import DecodeError
from jwt import (
    ExpiredSignatureError,
    InvalidAudienceError,
    InvalidSignatureError,
    InvalidIssuedAtError,
    InvalidIssuerError,
    InvalidTokenError,
)
from backend_app.api_errors import AuthErrors, DBErrors
from backend_app.pydantic_models import TokenModel


def prepare_token_payload(access_code: AccessCodeModel, token_type: str) -> dict:
    lagos_time = timezone("Africa/Lagos")
    dt = lagos_time.localize(datetime.now())
    if token_type == "access":
        exp = dt + timedelta(minutes=2)
    elif token_type == "refresh":
        exp = dt + timedelta(hours=int(Config.JWT_TTL) + 4320)
    if Config.JWT_AUDIENCE:
        payload = {
            "sub": access_code,
            "iss": Config.JWT_ISSUER,
            "exp": exp,
            "iat": dt,
            "aud": Config.JWT_AUDIENCE,
            "token_type": token_type,
        }
    else:
        payload = {
            "sub": access_code,
            "iss": Config.JWT_ISSUER,
            "exp": exp,
            "iat": dt,
            "token_type": token_type,
        }
    return payload


def sign_token(token_payload: dict) -> str:
    return jwt.encode(token_payload, Config.JWT_PRIVATE_KEY, algorithm="RS256")


def decode_token(token: str) -> bool:
    with open("jwt_credentials/public-key.pem", "r", encoding="utf-8") as fp:
        public_key = fp.read()
    try:
        verify_token = jwt.decode(token, public_key, algorithms=["RS256"])
        return {"data": verify_token, "status": 200}
    except DecodeError:
        return {"data": AuthErrors.jwt_decode_error, "status": 400}
    except ExpiredSignatureError:
        return {"data": AuthErrors.jwt_expired_signature, "status": 400}
    except InvalidAudienceError:
        return {"data": AuthErrors.jwt_invalid_audience, "status": 400}
    except InvalidIssuedAtError:
        return {"data": AuthErrors.jwt_invalid_issued_time, "status": 400}
    except InvalidIssuerError:
        return {"data": AuthErrors.jwt_invalid_issuer, "status": 400}
    except InvalidTokenError:
        return {"data": AuthErrors.jwt_invalid_token, "status": 400}
