from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
class user(BaseModel):
    username:str
    email:str
    password:str


class user_delete(BaseModel):
    username:str
    password:str


class note(BaseModel):
    created_on: datetime
    description: str


class full_user(BaseModel):
    username: str
    email: str
    notes: List[Optional[note]]
