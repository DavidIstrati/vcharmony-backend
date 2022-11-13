from ast import Str
from unicodedata import category
from sqlalchemy import Boolean, Column, Computed, Index, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from .database_config import Base


class Users(Base):
    __tablename__ = "users"

    userId = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    date = Column(String)
    entityType = Column(String)
    institution = Column(String)