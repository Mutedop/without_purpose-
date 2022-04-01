import uuid
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.forms import UserLoginForm, UserCreateForm
from app.models import connect_db, User, AuthToken
from app.utils import get_password_hash


router = APIRouter()


@router.post('/login', name='user_login')
def user_login(user_form: UserLoginForm = Body(..., embed=True),
               database=Depends(connect_db)):
    user = database.query(User).filter(
        User.email == user_form.email).one_or_more()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'email/pass invalid'}
    auth_token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    database.add(auth_token)
    database.commit()
    return {'status': 'ok'}


@router.post('/user', name='user_create')
def create_user(user: UserCreateForm = Body(..., embed=True),
                database=Depends(connect_db)):
    exists_user = (database.query(User.id).
                   filter(User.email == user.email).one_or_none())
    if exists_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='email already')
    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        nick_name=user.nick_name,
    )
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}