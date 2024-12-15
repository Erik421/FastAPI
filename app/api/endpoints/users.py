from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.api.models.user import User
from app.db.db import USER_DATA
from app.core.security import get_user_from_db, get_jwt_token_by_name


router = APIRouter()


@router.post("/auth/register")
def register_new_user(user: User):
    USER_DATA.append(user)
    return {"message": f"Пользователь {user.username} успешно зарегистрирован"}


@router.post("/auth/login")
def login(user_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_from_db(user_data.username)
    if user is None or user_data.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    token = get_jwt_token_by_name(user_data.username)
    return token
