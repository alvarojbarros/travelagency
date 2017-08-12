from sqlalchemy import Table, Column, Integer, String, ForeignKey, Time, DateTime, Index, or_, Date
from flask_login import UserMixin
from tools.Record import Record
from sqlalchemy.ext.declarative import declarative_base
from tools.dbtools import engine

Base = declarative_base()

class User(Base,Record,UserMixin):
    __tablename__ = 'user'
    Email = Column(String(50))
    Password = Column(String(20))
    Name = Column(String(40))

Index('Email', User.Email, unique=True)

Base.metadata.create_all(engine)
