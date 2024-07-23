from sqlalchemy import Column, Integer, String, Boolean, Table, Date 
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=True)
    confirmed = Column(Boolean, default=False)
    role = Column(String(50), default="user")  # Додано поле ролі


class Photos(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    photo_urls = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True) # Додано поле опису
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_by = relationship("User")
    tags = relationship("Tags", secondary="photo_tags") # Додано зв'язок з тегами


class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag = Column(String(255), nullable=False, unique=True)  # Теги є унікальними

photo_tags = Table(
    'photo_tags',
    Base.metadata,
    Column('photo_id', ForeignKey('photos.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)