from fastapi import APIRouter, Depends
from app.schemas import User, UserShow

###################call conect database in main ####################
from db.database import Base, engine
from sqlalchemy.orm import Session
from db.database import get_db
from db.models.user import Userdb

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users = []


@router.get('/') # used @router because used APIRouter
def showAll(db:Session = Depends(get_db)):
    return users

@router.post('/')
def create_user(user:User, db:Session = Depends(get_db)):
    user = user.dict()
    
    new_user = Userdb(
        username = user['username'],
        password = user['password'],
        name = user['name'],
        lastname = user['lastname'],
        address = user['address'],
        phone = user['phone'],
        email = user['email'],
        creation = user['creation'],
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"response":new_user}

@router.get('1/{user_id}')#query parameter
def showOne(user_id:int, db:Session = Depends(get_db)):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return{"response": "user no found"}

@router.post('2')# for post parameter
def showOneUserId(userid:UserShow, db:Session = Depends(get_db)):
    for user in users:
        if user["id"] == userid.id:
            return {"user": user}
    return{"response": "user no found"}

@router.put('/{user_id}')
def update(user_id:int, updateUser:User, db:Session = Depends(get_db)):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i]["name"] = updateUser.dict()["name"]
            users[i]["lastName"] = updateUser.dict()["lastName"]
            users[i]["address"] = updateUser.dict()["address"]
            users[i]["phone"] = updateUser.dict()["phone"]
            return {"user": user}
    return{"response": "user no found"}



@router.delete('/{user_id}')#query parameter
def delete(user_id:int, db:Session = Depends(get_db)):
    for i, user in enumerate(users): #i position dict
        if user["id"] == user_id:
            users.pop(i)
            return {"data": user}
    return{"response": "user no found"}