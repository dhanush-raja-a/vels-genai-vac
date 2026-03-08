from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE USER
@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = models.User(name=user.name, age=user.age)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# READ USERS
@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(models.User).all()

    return users


# READ SINGLE USER
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    return user


# UPDATE USER
@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    db_user.name = user.name
    db_user.age = user.age

    db.commit()

    return db_user


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == user_id).first()

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}