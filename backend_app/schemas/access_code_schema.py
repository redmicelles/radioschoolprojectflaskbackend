from ma import ma
from ..models.access_code_models import AccessCode


class AccessCodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccessCode
        load_instance = True