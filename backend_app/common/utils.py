from datetime import datetime, timedelta, timezone    
import jwt
import calendar
from backend_app.pydantic_models import AccessCodeModel
from config import Config

def prepare_token_payload(access_code: AccessCodeModel, token_type: str) -> dict:
    dt = datetime.now()
    if token_type == "access":
        exp = dt + timedelta(hours=Config.JWT_TTL)
    elif(token_type == "refresh"):
        exp = dt + timedelta(hours=Config.JWT_TTL + 4320)
    issued_at = calendar.timegm(dt.timetuple())
    expiry = calendar.timegm(exp.timetuple())
    payload = {
                "sub": access_code,
                "iss": Config.JWT_ISSUER,
                "exp": expiry,
                "iat": issued_at,
                "aud": Config.JWT_AUDIENCE
            }
    return payload

def sign_token(token_payload: dict):
    return jwt.encode(token_payload, Config.JWT_PRIVATE_KEY, algorithm="RS256")

# message["exp"] = expiry
# message["iat"] = issue_at

# # key = "secret"
# # encoded = jwt.encode(message, key, algorithm="HS256")

# with open("./private-key.pem", "r", encoding="utf-8") as fp:
#     private_key = fp.read()

# with open("./public-key.pem", "r", encoding="utf-8") as fp:
#     public_key = fp.read()

# encoded = jwt.encode(message, private_key, algorithm="RS256")

# print(encoded.decode())

# decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])

# print(decoded)