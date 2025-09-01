from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/user")
def user(request: Request):
    return templates.TemplateResponse("userinfo.html", {"request": request, "uid": "Kevin", "upw": "1234", "uname": "Kevin Kim", "ugender": "male"})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)