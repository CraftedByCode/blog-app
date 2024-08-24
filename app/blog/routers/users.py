from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import blog.database, blog.schemas
from blog.repository import users

router  = APIRouter(
    tags=['users'],
    prefix='/user'
)

@router.post('/', response_model=blog.schemas.ShowUser)
def create_user(request: blog.schemas.User, db: Session = Depends(blog.database.get_db)):
    return users.create_user(request,db)

@router.get('/{id}', response_model=blog.schemas.ShowUser)
def get_user(id: int, db: Session = Depends(blog.database.get_db)):
    return users.get_user(id,db)