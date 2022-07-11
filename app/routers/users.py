from fastapi import APIRouter
from database import Data
from fastapi import Depends
from models.models import user,user_delete, full_user
router = APIRouter()

@router.get('/user/',tags=['users'],response_model=full_user)
async def read_users(username:str,Data = Depends(Data)):
    return Data.get_all_by_username(username)


@router.post('/user/',tags=['users'])
async def upload_users(user:user,Data = Depends(Data)):
    Data.create_account(user.username,user.email,user.password)
    return 'Complete'


@router.delete('/user/',tags=['users'])
async def delete_users(user:user_delete,Data =Depends(Data)):
    Data.delete_account(user.username,user.password)
    return 'Complete'