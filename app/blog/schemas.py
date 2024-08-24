from typing import List

from pydantic import BaseModel


class User(BaseModel):
    name: str
    emailid: str
    password: str

class BlogBase(BaseModel):
    title: str
    body: str
    

    model_config={
        "from_attributes":True
    }
    
class Blog(BlogBase):
    model_config={
        "from_attributes":True
    }
    
class ShowUser(BaseModel):
    name: str
    emailid: str
    blogs: List[Blog]
    
    model_config = {
        "from_attributes": True
    }
    
class ShowAllBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
    model_config = {
        "from_attributes": True
    }

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    email: str | None = None