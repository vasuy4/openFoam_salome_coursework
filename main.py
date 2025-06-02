import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from utils import check


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
    }

    return check(*result.values())[1]

if __name__ == '__main__':
    uvicorn.run(app)
