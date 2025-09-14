# web_lab8

PyTorch로 학습한 CNN 모델을 FastAPI로 웹에 배포하는 실습 예제입니다. 이미지를 업로드하면 모델이 분류 결과를 반환합니다.

## 주요 기능
- 이미지 파일 업로드 및 추론
- PyTorch CNN 모델 로드 및 예측
- 결과를 템플릿에 렌더링

## 폴더 구조
```
web_lab8/
├── main.py                  # FastAPI 서버 및 추론 코드
├── cnn_model.pth            # 학습된 PyTorch 모델 파일
├── 8.png, dogs.png          # 테스트 이미지
├── images/                  # 이미지 폴더
└── templates/
    ├── index.html           # 파일 업로드 폼
    └── CNN_result.html      # 추론 결과 출력
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

## 참고
- `cnn_model.pth` 파일이 필요합니다 (사전 학습된 모델)
- 템플릿 파일은 `templates/` 폴더에 위치
