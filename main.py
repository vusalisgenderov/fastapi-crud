from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from scheme import Usercreateshcema,Userdeletescheme,userchangescheme
from service import *
app = FastAPI()


@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}

@app.post("/user")
def create_user(item: Usercreateshcema,db:Session=Depends(get_db)):
    message=create_user_in_db(data=item,db=db)
    return message

@app.delete("/user")
def delete_user(item:Userdeletescheme,db:Session=Depends(get_db)):
    message=delete_user_in_db(data=item,db=db)
    return message

@app.get("/user")
def get_user(username: str, db: Session = Depends(get_db)):
    user = get_current_user(username=username, db=db)
    return user

@app.put("/user")
def update_user(username:str,item:userchangescheme,db: Session = Depends(get_db)):
    message = change_user_password(user_name=username,data=item,db=db)
    return message

@app.delete("/all_user")
def reset_my_base():
    msg=reset_base()
    return {"msg":"base reseted"}

