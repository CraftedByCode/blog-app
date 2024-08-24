from fastapi import HTTPException
from starlette import status

from blog import models
        
def create_blog(request, db):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
def read_blog(id, db):
    blog = db.get(models.Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with id {id} is not availabe",
        )
    return blog

def read_blogs(db):
    blogs = db.query(models.Blog).all()
    return blogs

def update_blog(id, request, db):
    blog = db.get(models.Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"operation failed": f"blog with id {id} is not found"},
        )
    try:
        db.query(models.Blog).filter(models.Blog.id == id).update(
            {"title": request.title, "body": request.body}
        )
        
        db.commit()
        return {
            "message": f"blog with id {id} of title and body are updated sucessfully"
        }
    except Exception as e:
        db.rollback()
        return {"Issue": str(e)}
    
def delete_blog(id, db):
    blog = db.get(models.Blog, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"operation failed": f"blog with id {id} is not found"},
        )
    try:
        db.query(models.Blog).filter(models.Blog.id == id).delete(
            synchronize_session=False
        )
        db.commit()
        return {"operation": f"a blog with a id {id} is removed from db"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"issue": f"except as {str(e)}"},
        )