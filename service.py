from models import User
from scheme import Usercreateshcema,Userdeletescheme,userchangescheme
from sqlalchemy.orm import Session
from exceptions import UserNottFoundException
def create_user_in_db(data:Usercreateshcema,db:Session):
    new_user=User(username=data.username,password=data.password)
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
    user = db.query(User).filter_by(username=user_name,password=data.password).first()
    if not user:
        raise UserNottFoundException()
    db.query(User).update({"password":data.new_password})
    db.commit()

    return {"msg": "user is updated"}
    