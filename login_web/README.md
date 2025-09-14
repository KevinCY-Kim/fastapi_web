# login_web

FastAPI와 JWT(Json Web Token)를 활용한 로그인/회원가입 인증 시스템 실습 예제입니다. JWT를 이용해 안전하게 인증 정보를 관리하고, 대시보드 접근 등 인증 흐름을 구현합니다.

## 주요 기능
- 회원가입 및 비밀번호 해싱
- JWT 기반 로그인/로그아웃
- 인증된 사용자만 접근 가능한 대시보드
- 쿠키를 통한 토큰 저장 및 검증

## 폴더 구조
```
login_web/
├── main.py              # FastAPI 서버 및 인증 로직
└── templates/
    └── login.html       # 로그인 폼 (필요시)
```

## 주요 엔드포인트
- `/` : 로그인 페이지 반환 (GET)
- `/register` : 회원가입 처리 (POST)
- `/login` : 로그인 처리, JWT 발급 (POST)
- `/dashboard` : 인증된 사용자만 접근 가능한 대시보드 (GET)
- `/logout` : 로그아웃, 쿠키 삭제 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2 passlib[bcrypt] python-jose`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 5000
   ```
3. 브라우저에서 `http://localhost:5000/` 접속

## 동작 설명
- 회원가입 시 비밀번호를 해싱하여 저장
- 로그인 시 JWT 토큰을 발급, 쿠키에 저장
- 대시보드 접근 시 토큰 검증 후 렌더링

## 참고
- 실습 목적상 DB 대신 딕셔너리(fake_user_db) 사용
- 실제 서비스 적용 시 DB 연동 필요
