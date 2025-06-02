import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import subprocess

from utils import check


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "information": "Добро пожаловать!", "is_correct": False}
    )

@app.post("/run")
async def run(request: Request):
    subprocess.run(['sh', 'Run.sh'])
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "information": "Запуск...", "is_correct": True}
    )

@app.post("/clear", response_class=HTMLResponse)
async def clear(request: Request):
    subprocess.run(['sh', 'Clean.sh'])
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "information": "Старые данные удалены", "is_correct": False}
    )

@app.post("/calculate")
async def calculate(
    request: Request,
    U: float = Form(...),
    widthInput: float = Form(...),
    widthOutput: float = Form(...),
    sideTriangle: float = Form(...),
    lenCone: float = Form(...),
    widthBase: float = Form(...),
    ten: float = Form(...),
    coneT: float = Form(...),
    minSize: float = Form(...),
    maxSize: float = Form(...),
):
    result = {
        "U": U,
        "widthInput": widthInput,
        "widthOutput": widthOutput,
        "sideTriangle": sideTriangle,
        "lenCone": lenCone,
        "widthBase": widthBase,
        "ten": ten,
        "coneT": coneT,
        "minSize": minSize,
        "maxSize": maxSize,
    }

    check_answer = check(*result.values())
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "information": check_answer[1], "is_correct": check_answer[0]}
    )

if __name__ == '__main__':
    uvicorn.run(app)
