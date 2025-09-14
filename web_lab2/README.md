# web_lab2

FastAPI 라우팅과 Jinja2 템플릿을 활용하여 사용자 정보를 웹에 출력하는 실습 예제입니다.

## 주요 기능
- FastAPI 라우팅
- Jinja2 템플릿 렌더링 (userinfo.html)

## 폴더 구조
```
web_lab2/
├── main.py                # FastAPI 서버 코드
└── templates/
    └── userinfo.html      # 사용자 정보 출력 템플릿
```

## 주요 엔드포인트
- `/` : 기본 메시지 반환 (GET)
- `/user` : 사용자 정보 템플릿 렌더링 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 9000
   ```
3. 브라우저에서 `http://localhost:9000/user` 등 접속

## 참고
- 템플릿 파일은 `templates/` 폴더에 위치
