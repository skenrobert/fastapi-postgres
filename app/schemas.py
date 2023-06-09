from pydantic import BaseModel #create model
from typing import Optional # optinal value in create model
from datetime import datetime # date in model

class User(BaseModel): #Schema
    id:int
    name:str
    lastName:str
    address:Optional[str]
    phone:str
    date_create:datetime =datetime.now()

class UserShow(BaseModel): # only used for other form, used for post
    id:int
