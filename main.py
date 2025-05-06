from fastapi import FastAPI, Request, HTTPException, status 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import utils
import constants

app= FastAPI()

#Monta los archivos estáticos (CSS, imágenes, fuentes)
app.mount("/static", StaticFiles(directory="static"), name="static")

#Configura Jinja2
templates= Jinja2Templates(directory="templates")

@app.get("/", response_class = HTMLResponse, status_code = status.HTTP_200_OK)
async def home(request: Request):
    context = {
        "request": request,
        "pagina_titulo": utils.index_title,
        "meta_descripcion": utils.index_meta_description,
        "GITHUB": constants.GITHUB,
        "X": constants.X,
        "YOUTUBE": constants.YOUTUBE,
        "TIK_TOK": constants.TIK_TOK,
        "INSTAGRAM": constants.INSTAGRAM,
        "CORREO": constants.CORREO,
        "SOLUCIONINT": constants.SOLUCIONINT,
        "APP_SOLUCIONINT": constants.APP_SOLUCIONINT
    }

    try:
        return templates.TemplateResponse("index.html", context)
    
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "La página no ha sido encontrada")

@app.get("/cursos", response_class = HTMLResponse, status_code= status.HTTP_200_OK)
async def cursos(request: Request):
    context= {
        "request": request,
        "pagina_titulo": utils.cursos_title,
        "meta_descripcion": utils.cursos_meta_description,
        "GITHUB": constants.GITHUB,
        "X": constants.X,
        "CURSO_PYTHON": constants.CURSO_PYTHON,
        "YOUTUBE": constants.YOUTUBE
    }

    try: 
        return templates.TemplateResponse("cursos.html", context)
    
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "La página no ha sido encontrada")