from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/alpaco")
def alpaco(request: Request):
    print(request)
    return templates.TemplateResponse("intro.html", {'request': request, 'name': '김창용', 'gender': '남자'})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
