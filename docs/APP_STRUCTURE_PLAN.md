# app.py 구조 계획

## 현재 상태 (테스트용)

```python
# src/sentivest/api/app.py
from fastapi import FastAPI
from src.sentivest import __version__

app = FastAPI(...)

@app.get("/")  # 테스트용
async def root():
    return {"message": "Hello World!"}

@app.get("/health")  # 헬스체크 (실제로도 유용)
async def health_check():
    return {"status": "healthy"}
```

## 향후 계획 (실제 기능 추가)

### 1단계: 라우터 분리
```python
# src/sentivest/api/app.py
from fastapi import FastAPI
from src.sentivest.api.routes import prediction, sentiment, news

app = FastAPI(...)

# 라우터 등록
app.include_router(prediction.router, prefix="/api/prediction", tags=["prediction"])
app.include_router(sentiment.router, prefix="/api/sentiment", tags=["sentiment"])
app.include_router(news.router, prefix="/api/news", tags=["news"])

@app.get("/")  # 루트는 유지하거나 제거 가능
async def root():
    return {"message": "Sentivest API", "version": __version__}

@app.get("/health")  # 헬스체크는 유지
async def health_check():
    return {"status": "healthy"}
```

### 2단계: 라우터 파일 생성
```python
# src/sentivest/api/routes/prediction.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_prediction():
    # 주식 예측 로직
    return {"prediction": "..."}
```

### 3단계: 서비스 레이어 사용
```python
# src/sentivest/api/routes/prediction.py
from fastapi import APIRouter
from src.sentivest.services.prediction import PredictionService

router = APIRouter()
prediction_service = PredictionService()

@router.get("/{stock_code}")
async def get_prediction(stock_code: str):
    result = prediction_service.predict(stock_code)
    return result
```

## 파일 구조 변화

### 현재
```
src/sentivest/api/
├── __init__.py
├── app.py          # 모든 엔드포인트가 여기에 있음 (테스트용)
└── routes/
    └── __init__.py
```

### 향후
```
src/sentivest/api/
├── __init__.py
├── app.py          # FastAPI 앱 생성 + 라우터 등록만
└── routes/
    ├── __init__.py
    ├── prediction.py   # 주식 예측 API
    ├── sentiment.py    # 감정 분석 API
    └── news.py         # 뉴스 API
```

## 요약

1. **현재 app.py**: 테스트용이지만 구조는 프로덕션 기반
2. **향후 계획**: 라우터를 분리해서 실제 기능 추가
3. **app.py의 역할**: FastAPI 앱 생성 + 라우터 등록만 담당
4. **실제 로직**: routes 폴더에 분리된 파일들에 작성

