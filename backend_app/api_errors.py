class AuthErrors:
    access_code_validation_error = {
        "message": "Access code input validation failed",
        "code": 20,
        "status": "failed"
    }

    invalid_access_code = {
        "message": "Invalid access code presented",
        "code": 21,
        "status": "failed"
    }


class DBErrors:
    db_server_conection_error = {
        "message": "Error while contacting DB Server",
        "code": 40,
        "status": "failed"
    }