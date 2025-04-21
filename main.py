from fastapi import FastAPI, Request, HTTPException, status 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import utils

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
        "meta_descripcion": utils.index_meta_description
    }

    try:
        return templates.TemplateResponse("index.html", context)
    
    except:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "La página no ha sido encontrada")