from fastapi import APIRouter
from app.schemas import User, UserShow

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users = []


@router.get('/') # used @router because used APIRouter
def showAll():
    return users

@router.post('/')
def create_user(user:User):
    user = user.dict()
    users.append(user)
    return {"response":"201"}

@router.get('1/{user_id}')#query parameter
def showOne(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return{"response": "user no found"}

@router.post('2')# for post parameter
def showOneUserId(userid:UserShow):
    for user in users:
        if user["id"] == userid.id:
            return {"user": user}
    return{"response": "user no found"}

@router.put('/{user_id}')
def update(user_id:int, updateUser:User):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i]["name"] = updateUser.dict()["name"]
            users[i]["lastName"] = updateUser.dict()["lastName"]
            users[i]["address"] = updateUser.dict()["address"]
            users[i]["phone"] = updateUser.dict()["phone"]
            return {"user": user}
    return{"response": "user no found"}



@router.delete('/{user_id}')#query parameter
def delete(user_id:int):
    for i, user in enumerate(users): #i position dict
        if user["id"] == user_id:
            users.pop(i)
            return {"data": user}
    return{"response": "user no found"}