import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastName = Column(String(250))
    email = Column(String(250))
    password = Column(String(200), nullable=False)
    user_name = Column(String(250), nullable=False)
    posts = relationship("Post", backref="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=False)
    media = relationship("Media", backref="post")
    comments = relationship("Comment", backref="post")

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    content = Column(String(700))
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String(200))

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    description = Column(String(700))
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), unique= False)
    user_to_id = Column(Integer, ForeignKey('user.id'), unique= False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
