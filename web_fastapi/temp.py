from fastapi import FastAPI

# 앱 객체
app = FastAPI()

@app.get("/")
def hello(): # 함수명 마음대로
    return {"mgs": "하이"}

@app.get("alpaco")
def alpaco():
    return {"mgs": "알파코"}

