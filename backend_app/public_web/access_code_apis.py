from backend_app.public_web.utils import CodeGenerator
from backend_app.models.access_code_models import AccessCode

from flask import abort

from ..repositories.access_code_repo import AccessCodeRepo  
from ..schemas.access_code_schema import AccessCodeSchema

accessCodeRepo = AccessCodeRepo()
accessCodeSchema = AccessCodeSchema()
acessCodeListSchema = AccessCodeSchema(many=True)
ITEM_NOT_FOUND = "Item not found for id: {}"


def get_all_access_token():
    return acessCodeListSchema.dump(accessCodeRepo.fetchAll()), 200
    
def generate_access_code():
    code_generator = CodeGenerator()
    access_code = code_generator.generate(6)
    try:
        accessCodeRepo.create(AccessCode(access_code))
    except Exception as e:
        print(e)
        abort(
            424,
            "failed"
        )
    return {
        "access_code": access_code
    }, 200

   