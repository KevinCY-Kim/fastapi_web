# web_lab5

FastAPI에서 GET 파라미터를 받아 템플릿에 전달하는 실습 예제입니다. 두 개의 엔드포인트(one, two)에서 각각 덧셈, 곱셈 결과를 출력합니다.

## 주요 기능
- GET 파라미터 수신 및 템플릿 렌더링

## 폴더 구조
```
web_lab5/
├── main.py                # FastAPI 서버 코드
└── templates/
    ├── one.html           # 덧셈 결과 템플릿
    └── two.html           # 곱셈 결과 템플릿
```

## 주요 엔드포인트
- `/one` : a, b 파라미터 덧셈 결과 템플릿 렌더링 (GET)
- `/two` : a, b 파라미터 곱셈 결과 템플릿 렌더링 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 9000
   ```
3. 브라우저에서 `http://localhost:9000/one?a=2&b=3` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
