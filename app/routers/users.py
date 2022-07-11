from fastapi import APIRouter
from database import Data
from fastapi import Depends
router = APIRouter()

@router.get('/users/',tags=['users'])
async def read_users(username:str,Data = Depends(Data)):
    return Data.get_all _by_username(username)