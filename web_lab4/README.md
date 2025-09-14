# web_lab4

FastAPI와 Jinja2 템플릿을 활용한 간단한 계산기 예제입니다.

## 주요 기능
- GET 요청으로 계산 결과를 템플릿에 렌더링

## 폴더 구조
```
web_lab4/
├── main.py                # FastAPI 서버 코드
└── templates/
    └── index.html         # 계산 결과 출력 템플릿
```

## 주요 엔드포인트
- `/calcul` : 계산 결과 템플릿 렌더링 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
3. 브라우저에서 `http://localhost:8000/calcul` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
