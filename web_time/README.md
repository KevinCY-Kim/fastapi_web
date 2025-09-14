# web_time

LSTM 기반의 주가 예측 모델을 FastAPI로 웹에 배포하는 실습 예제입니다. 최근 60일간의 삼성전자 주가 데이터를 기반으로 14일 후의 주가를 예측하고, 예측 결과와 OHLC 박스플롯을 웹에서 시각화합니다.

## 주요 기능
- LSTM 모델을 이용한 주가 예측
- 예측 결과 및 OHLC 박스플롯 차트 생성 (matplotlib)
- 차트를 base64로 인코딩하여 웹에 렌더링

## 폴더 구조
```
web_time/
├── main.py                    # FastAPI 서버 및 예측/차트 코드
├── lstm_stock_forecast.pt     # 학습된 LSTM 모델 파일
└── templates/
    └── index.html             # 예측 결과 및 차트 출력 템플릿
```

## 주요 엔드포인트
- `/` : 예측 결과 및 차트(index.html) 반환 (GET)

## 실행 방법
1. 패키지 설치: `pip install fastapi uvicorn jinja2 torch FinanceDataReader scikit-learn matplotlib pillow`
2. 모델 파일(`lstm_stock_forecast.pt`) 준비
3. 서버 실행:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
4. 브라우저에서 `http://localhost:8000/` 접속

## 동작 설명
- 최근 90일간의 삼성전자 주가 데이터를 불러와 60일 시퀀스를 LSTM에 입력
- 14일 후의 주가를 예측하고, 실제값과 함께 차트로 시각화
- OHLC(시가, 고가, 저가, 종가) 박스플롯도 함께 출력

## 참고
- 실습 목적상 예측 결과는 예시이며, 실제 투자에 사용하지 마세요
- 템플릿 파일은 `templates/` 폴더에 위치
