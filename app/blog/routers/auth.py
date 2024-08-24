from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import text
from sqlalchemy.orm import Session
from starlette import status

from blog import hashing, models, schemas
import blog.JWTtokens as token
from blog.database import get_db

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.emailid == request.username).first()
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"Invalid Credentials": f"Username/Password is invalid!"},
        )
        
    verify_status = hashing.Hash.verify_user(request.password, user.password)
    if not verify_status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"Invalid Credentials": f"Username/Password is invalid!"},
        )
    
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        {"sub": user.emailid},
        expires_delta=access_token_expires
    )
    
    return schemas.Token(access_token=access_token, token_type="bearer")
