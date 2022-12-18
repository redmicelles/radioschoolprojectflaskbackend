from backend_app.public_web.utils import CodeGenerator
from backend_app.models.access_code_models import AccessCode
from app_config import db
from flask import abort, request, make_response
from app_config import app
from backend_app.pydantic_models import (
    AccessCodeModel,
    TokenModel,
    TokenVerificationModel,
    TokenRefreshModel,
)
from pydantic.error_wrappers import ValidationError
from backend_app.common.utils import prepare_token_payload, sign_token, decode_token
from backend_app.api_errors import AuthErrors, DBErrors
from backend_app.repository import PublicWebRepo


def generate_access_code() -> dict:
    """this endpoint generates a 6 character access codes"""
    code_generator = CodeGenerator()
    access_code = code_generator.generate(6)
    try:
        PublicWebRepo.create_access_code(access_code)
    except Exception as e:
        return DBErrors.db_server_conection_error, 424
    return {"status": "success", "data": {"access_code": access_code}}, 201


def generate_tokens() -> dict:
    """this endpoint access and refresh tokens when a valid access code is presented"""
    request_data = request.json
    try:
        endpoint_input = AccessCodeModel(access_code=request_data.get("access_code"))
    except ValidationError as e:
        return AuthErrors.access_code_validation_error, 422

    # verify token existence in DB
    fecth_access_code = PublicWebRepo.fetch_access_code(
        access_code=endpoint_input.access_code
    )
    if not fecth_access_code:
        return AuthErrors.invalid_access_code, 404

    # Generate JWTs
    access_token = sign_token(
        prepare_token_payload(endpoint_input.access_code, token_type="access")
    )
    refresh_token = sign_token(
        prepare_token_payload(endpoint_input.access_code, token_type="refresh")
    )
    # access_token["token_type"] = "refresh token"
    response = make_response(
        {
            "status": "success",
            "data": {"access_token": access_token, "refresh_token": refresh_token},
        }
    )
    return response, 200


def verify_token() -> dict:
    request_data = request.json
    endpoint_input = TokenVerificationModel(token=request_data.get("token"))
    token_validity = decode_token(bytes(endpoint_input.token, encoding="utf8"))
    if token_validity.get("status") == 400:
        return token_validity.get("data"), token_validity.get("status")
    try:
        verify_sub = PublicWebRepo.fetch_access_code(
            token_validity.get("data").get("sub")
        )
        if not verify_sub:
            return AuthErrors.invalid_access_code, 400
        return {"data": "Token is valid!", "status": "success"}
    except:
        return {
            "data": token_validity.get("data"),
            "status": "success",
        }, token_validity.get("status")


def refresh_token() -> dict:
    request_data = request.json
    endpoint_input = TokenRefreshModel(
        access_token=request_data.get("access_token"),
        refresh_token=request_data.get("refresh_token")
    )
    #check if refresh token is valid
    refresh_token_validity = decode_token(bytes(endpoint_input.refresh_token, encoding="utf8"))
    if refresh_token_validity.get("status") == 400:
        return refresh_token_validity["data"], refresh_token_validity["status"]
    access_token_validity = decode_token(bytes(endpoint_input.access_token, encoding="utf8"))
    if access_token_validity.get("status") == 400 and access_token_validity.get("data").get("code") != 23:
        return access_token_validity["data"], refresh_token_validity["status"]
    elif access_token_validity.get("status") == 400 and access_token_validity.get("data").get("code") == 23:
        #refresh the tokens
        subscriber = refresh_token_validity.get("data").get("sub")
        access_token = sign_token(
        prepare_token_payload(subscriber, token_type="access")
            )
        refresh_token = sign_token(
            prepare_token_payload(subscriber, token_type="refresh")
            )
        response = make_response(
                {
                    "status": "success",
                    "data": {"access_token": access_token, "refresh_token": refresh_token},
                }
            )
        return response, 200
    else:
        return 

    # return refresh_token_validity["data"], refresh_token_validity["status"]
    #check is access token has expired

    #check if access token has a valid sub

    #refresh access and refresh tokens
