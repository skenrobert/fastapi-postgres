from fastapi import FastAPI
import uvicorn
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


app = FastAPI()




users = []

@app.get('/route')
def ruta1():
    return{"msj":"hello work"}

@app.get('/user')
def showAll():
    return users

@app.post('/users')
def create_user(user:User):
    user = user.dict()
    users.append(user)
    return {"response":"201"}

@app.get('/user1/{user_id}')#query parameter
def showOne(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return{"response": "user no found"}

@app.post('/user2')
def showOneUserId(userid:UserShow):
    for user in users:
        if user["id"] == userid.id:
            return {"user": user}
    return{"response": "user no found"}

if __name__=="__main__":
    uvicorn.run("main:app", port=8000,reload=True)