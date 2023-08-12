from sqlalchemy.orm import Session
from app.schemas import users
from app.models.user import User



def getUserByEmail(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        return db_user
    return None

def getUserById(db: Session, post_id: int):
    db_user = db.query(User).filter(User.id == post_id).first()
    if db_user:
        return db_user
    return None

def createUser(db: Session, user: users.UserCreate) -> users.User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
