from fastapi import FastAPI, HTTPException, Depends, Form,Response, Request, Cookie
from passlib.context import CryptContext # 암호 생성기
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates  
import jwt # 토큰 발급기
from datetime import datetime, timedelta
import secrets # 시크릿키 생성
import uvicorn
from typing import Optional

app = FastAPI()

# html 폴더
templates = Jinja2Templates(directory="templates")

# css 파일, 미디어 파일 관리 폴더 static을 장착(mount)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 토큰에서 사용할 보안키 (놀이공권 입장권에도 고유번호가 있음)
SECRET_KEY = secrets.token_hex(32) # 32바이트 길이의 시크릿키 생성

# 토큰 발급 알고리즘
ALGORITHM = "HS256"

# 토큰 유효시간
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 비밀번호 암호화 생성기 정의
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 우리는 DB를 쓰지 않고 딕셔너리에 사용자, 비밀번호를 저장 할 예정
fake_user_db = {} # 회원가입하면 여기다가 저장, 웹서버 끊이면 값이 사라짐

# 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 로그인 페이지
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# 회원가입 
@app.post("/register") # 회원가입 정보 받아와야지,   # ...은 필수 값이라는 의미
async def register(username: str = Form(...), password: str = Form(...)):
    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자입니다.")
    
    hashed_password = hash_password(password)
    fake_users_db[username] = {"username": username, "password": hashed_password}
    return RedirectResponse(url="/", status_code=303)  # 회원가입 후 로그인 페이지로 이동

# 비밀번호 검증 함수
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT 토큰 생성 함수
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire}) # 딕셔너리로 expire(날짜와 함께) 정보를 추가해 줌
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 회원가입 했으면 로그인을 가능하게 해야 하니까
# 로그인 후 검증하는 함수가 필요함
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = fake_users_db.get(username) # db에서 딕셔너리로 로그인 정보 가져옴
    
    if not user or not verify_password(password, user["password"]): # 비교
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 잘못되었습니다.")
    
    access_token = create_access_token(
        data={"sub": username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
               # /dashboard에 303상태(GET) 코드로 이동하는 리다이렉트 변동함수
    response = RedirectResponse(url="/dashboard", status_code=303)

    # HTTP-only 쿠키에 토큰 저장
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,  # JavaScript에서 접근 불가, XSS 해킹 방법 방지.
        secure=False,  # HTTPS 연결에서만 쿠키 전송, 우리는 http를 쓸 것이기 때문에 false로 해야함.
        samesite="lax", # CSRF 보호
        max_age=1800    # 30분
    )
    print("access_token:",access_token)  
    return response

# 48번째 줄 함수에서 login 후처리(검증)한 후 대쉬보드 페이지를 get 
# 그러면 대쉬보드 get 함수를 만들자


# 대시보드 페이지 (JWT 인증 필요)
@app.get("/dashboard", response_class=HTMLResponse) # 리다이렉트리스폰이 dashboard로 이동
                                                    # access_token도 던짐
async def dashboard(
    request: Request,
    access_token: Optional[str] = Cookie(None)
):
    # 엑세스 토큰이 존재하지 않는 GET방식이다, 합법적으로 로그인해서 들어온 접속이 아니라는 뜻
    if not access_token:
                # GET방식으로 메인페이지에 보내버림
        return RedirectResponse(url="/", status_code=303)
    
    try: # access token이 들어오면, 유저 정보가 decoding되어 들어옴
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username: str = payload.get("sub")
        
        # 유저가 없거나, 존재하지 않거나 또는 fake_users_db에 없으면 401에러 발생
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=401, detail="인증 실패")

        return templates.TemplateResponse("dashboard.html", {"request": request, "username": username})
    
    except jwt.ExpiredSignatureError:  # 토큰이 만료되었을 때 발생하는 예외
        response = RedirectResponse(url="/", status_code=303)
        response.delete_cookie("access_token")
        return response
    
    except jwt.PyJWTError: # 토큰이 유효하지 않거나 변조되었을 때 발생하는 예외
        response = RedirectResponse(url="/", status_code=303)
        response.delete_cookie("access_token")
        return response

# 로그아웃도 가능하게
@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("access_token")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)