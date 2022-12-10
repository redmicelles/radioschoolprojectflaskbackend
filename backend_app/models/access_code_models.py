from sqlalchemy.dialects.mysql import JSON
from app_config import db

class AccessCode(db.Model):
    __tablename__ = 'access_codes'

    id = db.Column(db.Integer, primary_key=True)
    access_code = db.Column(db.String(255))

    def __init__(self, access_code):
        self.access_code = access_code

    def __repr__(self):
        return '<id {}>'.format(self.id)
