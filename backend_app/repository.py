from backend_app.models.access_code_models import AccessCode
from app_config import db


class PublicWebRepo:
    @staticmethod
    def create_access_code(access_code):
        access_code_obj = AccessCode(access_code)
        db.session.add(access_code_obj)
        db.session.commit()

    @staticmethod
    def fetch_access_code(access_code):
        return AccessCode.query.filter_by(access_code=access_code).one_or_none()
