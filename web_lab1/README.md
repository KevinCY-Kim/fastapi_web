# web_lab1

FastAPI의 기본 라우팅과 Jinja2 템플릿 렌더링을 실습하는 예제입니다. 간단한 인사 메시지와 템플릿을 통한 데이터 전달을 경험할 수 있습니다.

## 주요 기능
- FastAPI 기본 라우팅
- Jinja2 템플릿 렌더링 (intro.html)

## 폴더 구조
```
web_lab1/
├── main.py            # FastAPI 서버 코드
└── templates/
    └── intro.html     # 템플릿 예제
```

## 주요 엔드포인트
- `/` : 인사 메시지 반환 (GET)
- `/alpaco` : 템플릿 렌더링 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 5000
   ```
3. 브라우저에서 `http://localhost:5000/alpaco` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
