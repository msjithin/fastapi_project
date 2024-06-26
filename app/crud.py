from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt 
from passlib.context import CryptContext

from . import models
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

###############################################################################
###########################        CREATE           ###########################
###############################################################################
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password(user.password + "reallyhashed")
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


###############################################################################
###########################         READ            ###########################
###############################################################################
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_password(password):
    return pwd_context.hash(password)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


###############################################################################
###########################        UPDATE           ###########################
###############################################################################
def update_item(db: Session, item_id: int, title: str = None , description: str = None):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        return None
    
    if title:
        db_item.title = title
    if description:
        db_item.description = description
    if title or description:   
        db.commit()
    return db_item


###############################################################################
###########################        DELETE           ###########################
###############################################################################
def delete_user_items(db: Session, user_id: int):
    db.query(models.Item).filter(models.Item.owner_id == user_id).delete()
    db.commit()


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        delete_user_items(db=db, user_id=user_id)  # Delete user's items first
        db.delete(db_user)
        db.commit()
        return True
    return False


def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False



    