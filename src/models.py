import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200))
    

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    user_mail = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('follower.id'))
    user = relationship(Follower)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(String)
    comment_id = Column(String(700))
    likes_id = Column(Integer)
    photos_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Photos(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    users_id = Column(String)
    description_id = Column(String(250))
    likes_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    users_id = Column(String)
    comment = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
