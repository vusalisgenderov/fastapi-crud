from models import User
from scheme import Usercreateshcema,Userdeletescheme,userchangescheme
from sqlalchemy.orm import Session
from exceptions import UserNottFoundException
import psycopg2
from setting import DATABASE_URL
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user_in_db(data:Usercreateshcema,db:Session):
    hashed_password=hash_password(data.password)
    new_user=User(username=data.username,password=hashed_password)
    user=db.query(User).filter_by(username=new_user.username).first()
    if user:
        raise UserNottFoundException()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}

def delete_user_in_db(data:Userdeletescheme,db:Session):
    user_in_db= db.query(User).filter_by(username=data.username).first()
    if not user_in_db:
        raise UserNottFoundException()
    db.delete(user_in_db)
    db.commit()
    return {"msg":"user is deleted"}

def get_current_user(*, username: str, db):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise UserNottFoundException()
    
    return {"msg":user.username}

def change_user_password(user_name:str,data:userchangescheme,db:Session):
    hashed_password=hash_password(data.password)
    hashed_password1=hash_password(data.new_password)

    user = db.query(User).filter_by(username=user_name,password=hashed_password).first()
    if not user:
        raise UserNottFoundException()
    db.query(User).filter_by(username=user_name,password=hashed_password).update({"password":hashed_password1})
    db.commit()
    
    return {"msg": "user is updated"}


def reset_base():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("DELETE FROM users;")

    cur.execute("ALTER SEQUENCE users_id_seq RESTART WITH 1;")
    conn.commit()
    cur.close()
    conn.close()
    return {"msg":"all user is deleted"}