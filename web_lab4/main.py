from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/calcul")
def calcul(request: Request):
    return templates.TemplateResponse("index.html", {'request': request, 'a': 2, 'b': 1})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    

