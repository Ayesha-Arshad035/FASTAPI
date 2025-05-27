
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    rollno: str
    address: str
    age: int