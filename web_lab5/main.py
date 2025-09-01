from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/one")
def one(request: Request, a: int, b: int):
    return templates.TemplateResponse("one.html", {'request': request, 'a': a, 'b': b})
                                                   
@app.get("/two")
def two(request: Request, a: int, b: int):
    return templates.TemplateResponse("two.html", {'request': request, 'a': a, 'b': b})
    
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9000)
    