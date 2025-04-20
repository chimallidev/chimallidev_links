from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app= FastAPI()

#Monta los archivos estáticos (CSS, imágenes, fuentes)
app.mount("/static", StaticFiles(directory="static"), name="static")

#Configura Jinja2
templates= Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    return "Hola Mundo"