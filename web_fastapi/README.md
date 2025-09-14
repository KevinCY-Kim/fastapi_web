# web_fastapi

FastAPI의 기본적인 라우팅, 폼 데이터 처리, Jinja2 템플릿 렌더링을 실습하는 예제입니다. 다양한 HTTP 메서드와 폼 전송, 템플릿 활용법을 익힐 수 있습니다.

## 주요 기능
- GET/POST 라우팅 실습
- 폼 데이터 수신 및 처리
- Jinja2 템플릿 렌더링

## 폴더 구조
```
web_fastapi/
├── main.py                  # FastAPI 서버 코드
├── temp.py                  # 추가 실습 코드(옵션)
└── templates/
    ├── post_test.html       # POST 폼 예제
    ├── signup.html          # 회원가입 폼 예제
    └── test.html            # 템플릿 렌더링 예제
```

## 주요 엔드포인트
- `/` : 기본 인사 메시지 반환 (GET)
- `/test` : 템플릿 렌더링 (GET)
- `/toast` : 폼 데이터 처리 (POST)
- `/test_get` : GET 방식 폼 처리 (GET)
- `/signup` : 회원가입 폼 및 처리 (GET/POST)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
3. 브라우저에서 `http://localhost:8000/` 등 접속

## 동작 설명
- 다양한 라우팅 및 폼 전송/처리를 실습
- 템플릿 파일을 통해 결과를 웹으로 렌더링

## 참고
- 실습 목적상 간단한 예제 위주
- 템플릿 파일은 `templates/` 폴더에 위치
