# content_web

FastAPI와 MySQL을 연동하여 간단한 게시판 CRUD(생성, 조회, 삭제) 기능을 구현한 실습 예제입니다. Jinja2 템플릿을 활용해 게시글 목록, 상세, 작성 폼을 제공합니다.

## 주요 기능
- 게시글 목록 조회, 상세 조회, 작성, 삭제 (CRUD)
- MySQL 데이터베이스 연동 (SQLAlchemy 사용)
- Jinja2 템플릿 렌더링

## 폴더 구조
```
content_web/
├── main.py                # FastAPI 서버 및 게시판 로직
└── templates/
    ├── list.html          # 게시글 목록
    ├── detail.html        # 게시글 상세
    └── write.html         # 게시글 작성 폼
```

## 주요 엔드포인트
- `/` : 게시글 목록(list.html) 반환 (GET)
- `/write` : 게시글 작성 폼(write.html) 반환 (GET), 게시글 작성 처리 (POST)
- `/content/{content_id}` : 게시글 상세(detail.html) 반환 (GET)
- `/content/{content_id}` : 게시글 삭제 (DELETE)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2 sqlalchemy pymysql`
2. MySQL DB 준비 및 테이블 생성 (content 테이블 필요)
3. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
4. 브라우저에서 `http://localhost:8000/` 접속

## 동작 설명
- 게시글 목록, 상세, 작성, 삭제를 각각의 엔드포인트에서 처리
- 템플릿을 통해 결과를 웹으로 렌더링

## 참고
- DB 연결 정보는 main.py에서 수정 가능
- 실습 목적상 간단한 예제 구조
