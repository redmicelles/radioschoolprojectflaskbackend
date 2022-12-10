from backend_app.public_web.utils import CodeGenerator
from backend_app.models.access_code_models import AccessCode
from app_config import db
from flask import abort

def generate_access_code():
    """this endpoint generates a 6 character access codes"""
    code_generator = CodeGenerator()
    access_code = code_generator.generate(6)
    try:
        access_code_obj = AccessCode(access_code)
        db.session.add(access_code_obj)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(
            424,
            "failed"
        )
    return {
        "access_code": access_code
    }, 200