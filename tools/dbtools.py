from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/travelagency1?charset=utf8', pool_recycle=3600)
Session = sessionmaker(bind=engine)
