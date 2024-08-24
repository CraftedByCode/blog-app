from fastapi import HTTPException
from starlette import status

import blog.hashing,blog.models


def create_user(request, db):
    hashed_password = blog.hashing.Hash.bcrypt(request.password)
    new_user = blog.models.User(name=request.name, emailid=request.emailid, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id, db):
    user = db.get(blog.models.User,id)
    if not user:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={f"issue":f"user with id {id} is not found!"}
        )
    return user