from datetime import datetime, timedelta, timezone    
import jwt
import calendar

message = {
    "sub": "access_code",
    "iss": "www.backend.dev.radioschoolprg.org",
    "exp": "",
    "iat": "",
    "aud": "www.radioschoolprg.org"
}

# print(utils.get_int_from_datetime(datetime.now(timezone.utc)))

dt = datetime.now()
exp= dt + timedelta(hours=24)
issue_at = calendar.timegm(dt.timetuple())
expiry = calendar.timegm(exp.timetuple())

message["exp"] = expiry
message["iat"] = issue_at

# key = "secret"
# encoded = jwt.encode(message, key, algorithm="HS256")

with open("jwt_credentials/private-key.pem", "r", encoding="utf-8") as fp:
    private_key = fp.read()

with open("jwt_credentials/public-key.pem", "r", encoding="utf-8") as fp:
    public_key = fp.read()

encoded = jwt.encode(message, private_key, algorithm="RS256")

print(encoded.decode())

decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])

print(decoded)