from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from blog.database import Base

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    emailid = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates="creator")
