from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from blog import schemas, database
from blog.repository import blog
from sqlalchemy.orm import Session
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_blog(request,db)

@router.get("/{id}", response_model=schemas.Blog)
def read_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.read_blog(id,db)

@router.get("/", response_model=List[schemas.ShowAllBlog])
def read_blogs(db: Session = Depends(database.get_db)):
    return blog.read_blogs(db)

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update_blog(id,request,db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.delete_blog(id,db)