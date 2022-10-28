
#pydantic Modules

#fastapi Modules
from msilib.schema import File
from fastapi import FastAPI
from fastapi.responses import FileResponse

#Proyect Modules
from routes.user import user



app = FastAPI()

app.include_router(user)

@app.get("/")
def hola_mundo():
    return "<h1> Hola mundo</h1>"