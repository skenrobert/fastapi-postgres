from fastapi import FastAPI, Depends
import uvicorn
from app.routers import users

# from db import models

from db.database import Base, engine
from sqlalchemy.orm import Session
from db.database import get_db

################# create table in postgres
def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()
##########################################

app = FastAPI()
app.include_router(users.router)


@app.get('/db')
async def home(db:Session = Depends(get_db)):
    print(db)
    return {"connect"}


# @app.get('/route') # used @app because is in the root app
# def ruta1():
#     return{"msj":"hello work"}



if __name__=="__main__":
    # uvicorn.run("main:app", port=8000,reload=True)
    uvicorn.run("main:app", port=8000)