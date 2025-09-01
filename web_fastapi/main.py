# 임폴트
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from typing_extensions import Annotated
from fastapi import Form

# 디렉토리 초기화
templeates = Jinja2Templates(directory="templates")

# 웹객체 초기화
app = FastAPI()

# 함수들
@app.get("/")
def hello():
    return {"msg": "안녕하세요 fastapi라옹"}
  
@app.get("/test")
def test(request: Request):
    return templeates.TemplateResponse("test.html", context={"request": request, "a": 2, "b": "앒파코"})

@app.post("/toast") # form 데이터를 str 타입으로 어노테이션 하겠다.
def test_post(request: Request, uname: Annotated[str, Form()], upw:Annotated[str, Form()]):
    print(uname, upw)

@app.get("/test_get")
def test_get(request: Request):
    return templeates.TemplateResponse("post_test.html", context={"request":request})

# 서버 실행 구문

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    