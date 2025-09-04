from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/jquery_test_get")
def jquery_get(request: Request):
    return templates.TemplateResponse("jquery.html", {"request": request})

from fastapi import Form

@app.post("/jquery_test")
def jquery_post(TextID: str = Form(...)):
    print(TextID)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
                    