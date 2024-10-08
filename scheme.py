from pydantic import BaseModel

class Usercreateshcema(BaseModel):
    username:str
    password:str
    class Config:
        extra="forbid"

class Userdeletescheme(BaseModel):
    username:str
    class Config:
        extra="forbid"


class userchangescheme(BaseModel):
    password:str
    new_password:str
    class Config:
        extra="forbid"