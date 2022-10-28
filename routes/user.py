#fastapi modules
from fastapi import APIRouter
from fastapi.responses import FileResponse

#proyect modules
from cofig.db import con
from Models.user import users
from schemas.user import User, UserBase

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

@user.get("/users")
def getUser():
    return con.execute(users.select()).fetchall()

@user.post("/users/create")
def createUser(user:User ):
    new_user = {"name":user.name,"email":user.email}
    new_password = {"password":f.encrypt(user.password.encode("utf-8"))}
    result = con.execute(users.insert().values(new_user))
    #lastwoid me devuelve el ultimo id
    return con.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users/{id}")
def getUser(id:str):
    return con.execute(users.select().where(users.c.id == id )).first()

@user.delete("/users/{id}/delete")
def deleteUser(id:int):
    return con.execute(users.delete().where(users.c.id== id))

@user.put("/users/{id}/update")
def userUpdate(id:int,user:User):
    con.execute(users.update().values(name=user.name,email =user.email).where(users.c.id == id))
    return "Updated"