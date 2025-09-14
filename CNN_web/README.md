# CNN_web

PyTorch로 학습한 CNN 모델을 FastAPI를 통해 웹에서 이미지 분류 서비스로 배포하는 실습 예제입니다. 사용자는 이미지를 업로드하고, 서버는 업로드된 이미지를 모델로 추론하여 결과를 반환합니다.

## 주요 기능
- 이미지 파일 업로드 (POST)
- PyTorch CNN 모델 로드 및 추론
- 추론 결과를 템플릿에 렌더링하여 반환

## 폴더 구조
```
CNN_web/
├── main.py              # FastAPI 서버 및 추론 코드
├── cnn_model.pt         # 학습된 PyTorch 모델 파일
├── 8.png                # 테스트용 이미지
└── templates/
    ├── index.html       # 파일 업로드 폼
    └── CNN_result.html  # 추론 결과 출력
```

## 주요 엔드포인트
- `/` : 업로드 폼(index.html) 반환 (GET)
- `/uploader` : 이미지 파일 업로드 및 추론 결과 반환 (POST)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2 torch pillow`
2. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
3. 브라우저에서 `http://localhost:8000/` 접속, 이미지 업로드 후 결과 확인

## 동작 설명
- 사용자가 이미지를 업로드하면 서버에 저장 후, CNN 모델로 추론
- 추론 결과를 CNN_result.html에 렌더링하여 사용자에게 반환

## 참고
- `cnn_model.pt` 파일이 필요합니다 (사전 학습된 모델)
- 템플릿 파일은 `templates/` 폴더에 위치
