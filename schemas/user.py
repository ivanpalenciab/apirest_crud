from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional

class UserBase(BaseModel):
    id:Optional[str]
    name:str
    email:EmailStr

class User(UserBase):
    password :str