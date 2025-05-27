
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal
from schema import UserCreate

app = FastAPI()
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

@app.post("/users/")
def create_user(user: UserCreate, database: Session = Depends(get_db)):
    db_user = models.User(
        name=user.name,
        rollno=user.rollno,
        address=user.address,
        age=user.age)
    database.add(db_user)
    database.commit()
    database.refresh(db_user)
    return {"message": "User created successfully!", "user_id": db_user.id}
