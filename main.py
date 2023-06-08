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

@app.get('/users')
def showAll():
    return users

@app.post('/users')
def create_user(user:User):
    user = user.dict()
    users.append(user)
    return {"response":"201"}

@app.get('/users1/{user_id}')#query parameter
def showOne(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return{"response": "user no found"}

@app.post('/users2')# for post parameter
def showOneUserId(userid:UserShow):
    for user in users:
        if user["id"] == userid.id:
            return {"user": user}
    return{"response": "user no found"}

@app.put('/users/{user_id}')
def update(user_id:int, updateUser:User):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i]["name"] = updateUser.dict()["name"]
            users[i]["lastName"] = updateUser.dict()["lastName"]
            users[i]["address"] = updateUser.dict()["address"]
            users[i]["phone"] = updateUser.dict()["phone"]
            return {"user": user}
    return{"response": "user no found"}



@app.delete('/users/{user_id}')#query parameter
def delete(user_id:int):
    for i, user in enumerate(users): #i position dict
        if user["id"] == user_id:
            users.pop(i)
            return {"data": user}
    return{"response": "user no found"}

if __name__=="__main__":
    uvicorn.run("main:app", port=8000,reload=True)