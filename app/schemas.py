from pydantic import BaseModel #create model
from typing import Optional # optinal value in create model
from datetime import datetime # date in model

class User(BaseModel): #Schema
    username:str
    password:str 
    name:str 
    lastname:str 
    address:Optional[str]
    phone:int 
    email:str 
    creation:datetime =datetime.now()

class UserShow(BaseModel): # only used for other form, used for post
    id:int


# class Sale(BaseModel):
#     id = int
#     user_id = int
#     sale = int
#     productos = int