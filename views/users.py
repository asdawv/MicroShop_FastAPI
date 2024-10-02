from datetime import datetime
from typing import List
from uuid import uuid4

from fastapi.routing import APIRouter

from models.User import User
from controllers import user
from enums import UserRoles

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/',
            description='Обработчик для получения списка всех пользователей',
            response_model=List[User])
async def get_users():
    return [User(**{
        'id': uuid4(),
        'fullname': f'User #{i}',
        'email': f'user{i}@example.com',
        'password': 'P@ssw0rd',
        'role': UserRoles.USER,
        'created_at': datetime.now(),
    }) for i in range(10)]


@router.post('/',
             description='Обработчик для создания нового пользователя',
             response_model=dict)
async def create_user(new_user: User):
    return user.create_user(user_in=new_user)
