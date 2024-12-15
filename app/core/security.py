from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.core.config import settings
from app.db.db import USER_DATA


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
EXP_TIME = timedelta(minutes=10)


def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_jwt_token_by_name(username):
    return {"access_token": create_jwt_token({"sub": username, "exp": datetime.utcnow() + EXP_TIME})}


def get_user_from_db(username: str):
    for user in USER_DATA:
        if username == user.username:
            return user
    return None


def get_user_from_token(token=Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")
