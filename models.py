
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    rollno= Column(String(20), nullable=False)
    address= Column(String(20), nullable=False)
    age= Column(Integer, nullable=False)

    