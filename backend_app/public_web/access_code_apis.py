from backend_app.public_web.utils import CodeGenerator
from backend_app.models.access_code_models import AccessCode
from app_config import db
from flask import(
    abort,
    request,
    make_response
)
from app_config import app
from backend_app.pydantic_models import AccessCodeModel
from pydantic.error_wrappers import ValidationError
from backend_app.common.utils import(
    prepare_token_payload,
    sign_token
)
from backend_app.api_errors import(
    AuthErrors,
    DBErrors
)

def generate_access_code() -> dict:
    """this endpoint generates a 6 character access codes"""
    code_generator = CodeGenerator()
    access_code = code_generator.generate(6)
    try:
        access_code_obj = AccessCode(access_code)
        db.session.add(access_code_obj)
        db.session.commit()
    except Exception as e:
        app.logger.error(f"App failed while saving access code - {access_code} to the database")
        app.logger.error(f"{e}")
        return DBErrors.db_server_conection_error
    return {
        "status": "success",
        "data": {"access_code": access_code}
    }, 201

def generate_tokens() -> dict:
    """this endpoint access and refresh tokens when a valid access code is presented"""
    request_data = request.json
    try:
        endpoint_input = AccessCodeModel(access_code=request_data.get("access_code"))
    except ValidationError as e:
        return AuthErrors.access_code_validation_error, 422

    #verify token existence in DB
    fecth_access_code = AccessCode.query.filter_by(access_code=endpoint_input.access_code).one_or_none()
    if not fecth_access_code:
        return AuthErrors.invalid_access_code, 404

    #Generate JWTs
    access_token = sign_token(prepare_token_payload(endpoint_input.access_code, "access"))
    refresh_token = sign_token(prepare_token_payload(endpoint_input.access_code, "refresh"))
    response = make_response({
        "status": "success",
        "data": {"access_token": access_token, "refresh_token": refresh_token}
        })
    return response, 200
    