class AuthErrors:
    access_code_validation_error = {
        "message": "Access code input validation failed",
        "code": 20,
        "status": "failed",
    }

    invalid_access_code = {
        "message": "Invalid access code",
        "code": 21,
        "status": "failed",
    }

    jwt_decode_error = {
        "message": "Error while decoding JWT",
        "code": 22,
        "status": "failed",
    }

    jwt_expired_signature = {
        "message": "Stale token presented",
        "code": 23,
        "status": "failed",
    }

    jwt_invalid_audience = {
        "message": "Invalid token audience",
        "code": 24,
        "status": "failed",
    }

    jwt_invalid_issuer = {
        "message": "Invalid token issuer",
        "code": 25,
        "status": "failed",
    }

    jwt_invalid_issued_time = {
        "message": "Invalid token time issued",
        "code": 26,
        "status": "failed",
    }

    jwt_invalid_token = {
        "message": "Invalid token presented",
        "code": 27,
        "status": "failed",
    }


class DBErrors:
    db_server_conection_error = {
        "message": "Error while contacting DB Server",
        "code": 40,
        "status": "failed",
    }


class SpecialErrors:
    error_404 = {
        "code": 98,
        "message": "We don't have the resource(s) you've requested",
        "status": "failed",
    }

    error_500 = {
        "code": 99,
        "message": "We can't fulfil your request at this time",
        "status": "failed",
    }
