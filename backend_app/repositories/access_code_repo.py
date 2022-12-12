from app_config import db
# from ..models.
from ..models.access_code_models import AccessCode
from typing import List


class AccessCodeRepo:


    def create(access_code):
        db.session.add(access_code)
        db.session.commit()
        
    def fetchById(_id:int)-> 'AccessCode':
        return db.session.query(AccessCode).filter_by(id=_id).first()
    
    def fetchAll(self) -> List['AccessCode']:
        return db.session.query(AccessCode).all()
    
    def delete(self,_id) -> None:
        access_code= db.session.query(AccessCode).filter_by(id=_id).first()
        db.session.delete(access_code)
        db.session.commit()
        
    def update(self,access_code_data):
        db.session.merge(access_code_data)
        db.session.commit() 