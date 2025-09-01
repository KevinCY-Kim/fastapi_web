from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from typing_extensions import Annotated
from fastapi import Form

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/page")
def logins(request: Request):
    return templates.TemplateResponse("login.html", context = {"request": request})

@app.post("/login")
def login(request: Request, name: Annotated[str, Form()], 
                            pwd: Annotated[str, Form()], 
                            gender: Annotated[str, Form()], 
                            email: Annotated[str, Form()]):
    print(name, pwd, gender, email)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
