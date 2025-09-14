# web_lab6

FastAPI에서 폼 데이터를 받아 처리하고, Jinja2 템플릿을 활용하는 실습 예제입니다.

## 주요 기능
- 폼 데이터 수신 및 출력
- Jinja2 템플릿 렌더링 (login.html)

## 폴더 구조
```
web_lab6/
├── main.py                # FastAPI 서버 코드
└── templates/
    └── login.html         # 로그인 폼 템플릿
```

## 주요 엔드포인트
- `/page` : 로그인 폼 템플릿 렌더링 (GET)
- `/login` : 폼 데이터 처리 (POST)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
3. 브라우저에서 `http://localhost:8000/page` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
