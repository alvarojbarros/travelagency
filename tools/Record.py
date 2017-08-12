from sqlalchemy import Column, Integer

class Record(object):
    id = Column(Integer, primary_key=True,autoincrement=True)
    syncVersion = Column(Integer)
