from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db, engine
from app.schemas import users as usersSchema
from app.lib import users as usersLib
from app.lib import auth as authLib


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: usersSchema.UserCreate, db: Session = Depends(get_db),):
    _user = usersLib.getUserByEmail(db, user.email)
    if _user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credentials already taken"
        )
        
    new_user = usersLib.createUser(db, user)
    access_token_expires = timedelta(minutes=authLib.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authLib.create_access_token(
        data={"sub": new_user.email}, expires_delta=access_token_expires
    )
    return {
        "data": {
            "user": new_user,
            "access_token": access_token, 
            "token_type": "bearer"
        }
    }

@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
):
    user = authLib.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=authLib.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authLib.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {
        "data": {
            "user": user,
            "access_token": access_token, 
            "token_type": "bearer"
        }
    }



