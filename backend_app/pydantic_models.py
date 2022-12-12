from pydantic import BaseModel, Field
from backend_app.app_enums import TokenTypeEnum

class AccessCodeModel(BaseModel):
    access_code: str = Field(min_length=6, max_length=6)

class TokenModel(BaseModel):
    access_token: TokenTypeEnum = TokenTypeEnum.access
    refresh_token: TokenTypeEnum = TokenTypeEnum.refresh