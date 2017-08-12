from sqlalchemy import Table, Column, Integer, String, ForeignKey, Time, DateTime, Index, or_, Date
from flask_login import UserMixin
from tools.Record import Record
from sqlalchemy.ext.declarative import declarative_base
from tools.dbtools import engine,Session

Base = declarative_base()

class User(Base,Record,UserMixin):
    __tablename__ = 'user'
    Email = Column(String(50))
    Password = Column(String(20))
    Name = Column(String(40))

    @classmethod
    def getUserIdByEmail(cls,email):
        session = Session()
        record = session.query(cls).filter_by(Email=email).first()
        if not record:
            return
        session.close()
        return record

    @classmethod
    def get(cls,id):
        session = Session()
        user_data = session.query(cls).filter_by(id=id).first()
        if not user_data:
            return
        session.close()
        return user_data

    @classmethod
    def addNewUser(cls,email,password,name):
        session = Session()
        new_user = User()
        new_user.Password = password
        new_user.syncVersion = 0
        new_user.Name = name
        new_user.Email = email
        session.add(new_user)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            session.close()
            return str(e)
        user = session.query(User).filter_by(Email=email).first()
        session.close()
        if user:
            return user

    def toJSON(self):
        res = {}
        res['Name'] = self.Name
        res['id'] = str(self.id)
        res['Email'] = self.Email
        return res


Index('Email', User.Email, unique=True)

Base.metadata.create_all(engine)
