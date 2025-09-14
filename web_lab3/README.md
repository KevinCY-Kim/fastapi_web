# web_lab3

FastAPI에서 GET 파라미터를 받아 템플릿에 전달하는 실습 예제입니다.

## 주요 기능
- GET 파라미터 수신 및 템플릿 렌더링

## 폴더 구조
```
web_lab3/
├── main.py                # FastAPI 서버 코드
└── templates/
    └── gettest.html       # 파라미터 출력 템플릿
```

## 주요 엔드포인트
- `/add` : GET 파라미터(name, gender) 수신 및 템플릿 렌더링 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 5100
   ```
3. 브라우저에서 `http://localhost:5100/add?name=홍길동&gender=남자` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
