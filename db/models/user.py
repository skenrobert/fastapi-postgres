from db.database import Base
from sqlalchemy import Column,Integer,String , Boolean,DateTime 
from datetime import datetime 
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class Userdb(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String,unique=True)
    password = Column(String )
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String, unique=True )
    creation = Column(DateTime, default=datetime.now, onupdate=datetime.now )
    status = Column(Boolean,default=False)
    sale = relationship("Sale",backref="user",cascade="delete,merge")

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    sale = Column(Integer)
    productos = Column(Integer)