# FastAPI Web 실습 모음

이 저장소는 FastAPI를 활용한 다양한 웹 실습 예제들을 모아둔 프로젝트입니다. 각 폴더는 독립적인 실습 주제와 예제 코드, 템플릿, 모델 등을 포함하고 있습니다. 실습별로 FastAPI의 다양한 기능(REST API, 템플릿, DB 연동, 인증, 머신러닝 모델 배포 등)을 경험할 수 있습니다.

## 폴더 구조 및 실습 주제

- **ajaxtest/** : jQuery와 FastAPI를 연동한 AJAX 실습 (GET/POST)
- **CNN_web/** : PyTorch CNN 모델을 FastAPI로 배포, 이미지 업로드 및 추론 결과 반환
- **content_web/** : 게시판 CRUD, MySQL DB 연동, Jinja2 템플릿 활용
- **login_web/** : JWT 기반 로그인/회원가입, 인증/인가 흐름 구현
- **web_fastapi/** : FastAPI 기본 라우팅, 폼 처리, 템플릿 렌더링 실습
- **web_lab1 ~ web_lab6, web_lab8/** : FastAPI 기초~중급 실습(폼, 템플릿, 파일 업로드, 계산 등)
- **web_time/** : LSTM 기반 주가 예측, 차트 시각화, 머신러닝 모델 웹 배포

## 실행 방법 (예시)

1. Python 3.8+ 환경 준비
2. 필요한 패키지 설치 (예: `pip install fastapi uvicorn jinja2 torch torchvision pymysql passlib python-jose FinanceDataReader scikit-learn matplotlib pillow`)
3. 각 폴더로 이동 후 `main.py` 실행
   ```bash
   uvicorn main:app --reload
   ```
   (포트와 host는 각 실습별 main.py 참고)

## 폴더별 README
각 폴더에 별도의 README가 있어, 실습 목적/주요 코드/실행법/결과 예시 등을 확인할 수 있습니다.

## 참고 사항
- 템플릿 파일은 각 폴더의 `templates/`에 위치
- 일부 실습은 DB(MySQL) 또는 모델 파일(.pt, .pth 등)이 필요
- 실습별로 필요한 추가 패키지/환경이 있을 수 있으니 각 폴더의 README 참고

---

## 폴더별 간단 요약

| 폴더명         | 주요 내용/기능                       |
| -------------- | ------------------------------------ |
| ajaxtest       | jQuery AJAX + FastAPI                |
| CNN_web        | 이미지 분류(CNN) 웹 배포             |
| content_web    | 게시판 CRUD, DB 연동                 |
| login_web      | JWT 로그인/회원가입                  |
| web_fastapi    | FastAPI 기본 라우팅/폼/템플릿        |
| web_lab1~8     | FastAPI 기초~중급 실습               |
| web_time       | LSTM 주가 예측, 차트 시각화          |

---

실습별 상세 내용은 각 폴더의 README를 참고하세요.
