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

class filterUser(BaseModel):
    username:str
    name:str 
    email:str 
    class Config():
        orm_mode = True 
        
class UpdateUser(BaseModel): #Schema 
    username:str = None 
    password:str = None 
    name:str = None 
    lastname:str = None 
    address:str = None 
    phone:int = None 
    email:str = None 
        
class Sale(BaseModel):
    id = int
    user_id = int
    sale = int
    productos = int