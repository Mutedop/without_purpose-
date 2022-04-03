from datetime import datetime
from enum import Enum

from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL


Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL,
                           connect_args={'check_same_thread': False})
    session = Session(autocommit=False, autoflush=False, bind=engine.connect())
    return session


class PostStatus(Enum):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    nick_name = Column(String)
    created_at = Column(String, default=datetime.utcnow())


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=PostStatus.IN_PROGRESS.value)
    created_at = Column(String, default=datetime.utcnow())


class AuthToken(Base):
    __tablename__ = 'auth_token'
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String, default=datetime.utcnow())
