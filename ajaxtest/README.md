# ajaxtest

jQuery와 FastAPI를 연동하여 AJAX 통신을 실습하는 예제입니다. 클라이언트에서 jQuery로 비동기 요청을 보내고, FastAPI에서 이를 처리하는 기본 구조를 익힐 수 있습니다.

## 주요 기능
- jQuery를 이용한 AJAX GET/POST 요청
- FastAPI에서 폼 데이터 수신 및 응답
- Jinja2 템플릿 렌더링

## 폴더 구조
```
ajaxtest/
├── main.py           # FastAPI 서버 코드
└── templates/
    └── jquery.html   # jQuery AJAX 테스트용 HTML
```

## 주요 코드 및 엔드포인트
- `/jquery_test_get` : GET 요청, 템플릿(jquery.html) 반환
- `/jquery_test` : POST 요청, 폼 데이터(TextID) 수신 및 처리

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 5000
   ```
3. 브라우저에서 `http://localhost:5000/jquery_test_get` 접속

## 동작 설명
- `jquery.html`에서 입력값을 받아 jQuery로 AJAX POST 요청을 보냅니다.
- FastAPI가 해당 요청을 받아 처리 후 응답을 반환합니다.

## 참고
- jQuery CDN이 HTML에 포함되어 있어 별도 설치 불필요
- 실습 목적상 간단한 폼 처리 및 콘솔 출력 위주
