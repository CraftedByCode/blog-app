from fastapi import FastAPI

from blog.routers.auth  import router as auth_router
from blog.routers.home  import router as home_router
from blog.routers.blogs import router as blogs_router
from blog.routers.users import router as users_router

from blog import database,models

app = FastAPI()

models.Base.metadata.create_all(database.engine) 

app.include_router(auth_router)
app.include_router(home_router)
app.include_router(blogs_router)
app.include_router(users_router)

