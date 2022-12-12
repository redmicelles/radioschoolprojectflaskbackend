from backend_app.public_web.utils import CodeGenerator
from backend_app.models.access_code_models import AccessCode
from app_config import db

import jwt
from datetime import datetime, timedelta
from config import Config

from flask import abort, request, jsonify, make_response

from ..repositories.access_code_repo import AccessCodeRepo  
from ..schemas.access_code_schema import AccessCodeSchema

accessCodeRepo = AccessCodeRepo()
accessCodeSchema = AccessCodeSchema()
acessCodeListSchema = AccessCodeSchema(many=True)
ITEM_NOT_FOUND = "Item not found for id: {}"


from deco import token_required

@token_required
def get_all_access_token(current_user):
    print(current_user)
    return acessCodeListSchema.dump(accessCodeRepo.fetchAll()), 200
    
def generate_access_code():
    """
    This endpooint generates unique access code for enabling the Radioschool website visitors to access
    pages open to Non-Admin Users
    - Access code is six characters long
    - Access code contains only letter and numbers
    - Access code is not case sensitive (from the frontend basically)
    """

    code_generator = CodeGenerator()
    access_code = code_generator.generate(6)
    try:
        access_code_obj = AccessCode(access_code)
        AccessCodeRepo.create(access_code_obj)
    except Exception as e:
        print(e)
        abort(
            424,
            "failed"
        )
    return {
        "access_code": access_code
    }, 200

   

def grant_access_token():

    """
    This endpoint generate a Access and Refresh Tokens for users who provides a valid access code. \n
    The tokens will include the following claims:
    - sub
    - aud
    - exp
    - iat
    - iss
    """
    
    access_code_req_json = request.get_json()
    data = access_code_req_json

    if not data or not data.get("access_code"):
        make_response("Could not verify", 
        401,
        {'WWW-Authenticate': 'Basic realm = "Supply access_code!!" '})

    user = db.session.query(AccessCode).filter_by(access_code = data["access_code"]).first()
    print(user)

    if isinstance(user, type(None)):
            return {"message": "Could not verify", 
        "status":401,
        'WWW-Authenticate': 'Basic realm: Supply access_code!!'}

    access_code = AccessCodeRepo.fetchById(user.id)
    if access_code:
        access_token_data = {
                "sub": "guest",
                "aud": "portal.radioschoolng.org",
                "exp": datetime.utcnow() + timedelta(days=1),
                "iat": datetime.utcnow(),
                "iss": "backend.radioschoolng.org",
                "access_code": access_code.access_code
            }
        

        refresh_token_data = access_token_data.copy()
        refresh_token_data.update({"exp":refresh_token_data["exp"] + timedelta(seconds=86400)})
        refresh_token_data.pop("access_code")
        
        encoded_access_token_data = jwt.encode(access_token_data, 
        Config.SECRET_KEY, algorithm="HS256")

        encoded_refresh_token_data = jwt.encode(refresh_token_data, 
        Config.SECRET_KEY, algorithm="HS256")

        return {"status_code": 200, 
            "content" : {"status": "success", "data": {
                "access_token": encoded_access_token_data,
                "refresh_token": encoded_refresh_token_data
                }}}

    return {"status_code": 404, "content":{"status": "failed", "message": "Invalid Access Code", "code": 10}}
    