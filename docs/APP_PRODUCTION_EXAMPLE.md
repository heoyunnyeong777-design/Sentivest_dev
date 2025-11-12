# app.py 프로덕션 구조 예시

## 현재 app.py (테스트용)

```python
from fastapi import FastAPI
from src.sentivest import __version__

app = FastAPI(
    title="Sentivest API",
    description="AI 기반 주식 예측 및 뉴스 감정 분석 대시보드",
    version=__version__
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

## 향후 app.py (프로덕션)

```python
"""
FastAPI 애플리케이션
프로덕션 버전
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from src.sentivest import __version__
from src.sentivest.api.routes import prediction, sentiment, news
from src.sentivest.config import settings
from src.sentivest.database import engine, Base

# FastAPI 앱 생성
app = FastAPI(
    title="Sentivest API",
    description="AI 기반 주식 예측 및 뉴스 감정 분석 대시보드",
    version=__version__,
    docs_url="/docs" if settings.DEBUG else None,  # 프로덕션에서는 문서 비활성화 가능
    redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS 설정 (프론트엔드와 통신하기 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip 압축 (응답 크기 최적화)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# 라우터 등록
app.include_router(prediction.router, prefix="/api/prediction", tags=["prediction"])
app.include_router(sentiment.router, prefix="/api/sentiment", tags=["sentiment"])
app.include_router(news.router, prefix="/api/news", tags=["news"])

# 루트 엔드포인트
@app.get("/")
async def root():
    """API 루트 엔드포인트"""
    return {
        "message": "Sentivest API",
        "version": __version__,
        "status": "running",
        "docs": "/docs" if settings.DEBUG else "disabled"
    }

# 헬스체크 엔드포인트
@app.get("/health")
async def health_check():
    """서버 상태 확인"""
    return {
        "status": "healthy",
        "version": __version__,
        "database": "connected"  # 데이터베이스 연결 상태 확인
    }

# 예외 처리 핸들러
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """전역 예외 처리"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc) if settings.DEBUG else "An error occurred"
        }
    )

# 시작 이벤트
@app.on_event("startup")
async def startup_event():
    """서버 시작 시 실행"""
    # 데이터베이스 테이블 생성
    Base.metadata.create_all(bind=engine)
    print("🚀 Sentivest API 서버가 시작되었습니다!")

# 종료 이벤트
@app.on_event("shutdown")
async def shutdown_event():
    """서버 종료 시 실행"""
    print("👋 Sentivest API 서버가 종료되었습니다.")
```

## app.py의 역할 정리

### 1. FastAPI 애플리케이션 생성
```python
app = FastAPI(...)
```
- **역할**: FastAPI 앱의 인스턴스를 생성합니다
- **필수**: 서버가 작동하려면 반드시 필요합니다

### 2. 라우터 등록
```python
app.include_router(prediction.router, prefix="/api/prediction")
app.include_router(sentiment.router, prefix="/api/sentiment")
app.include_router(news.router, prefix="/api/news")
```
- **역할**: 각 기능의 라우터를 등록합니다
- **필수**: 새로운 API를 추가할 때마다 여기에 등록해야 합니다

### 3. 미들웨어 설정
```python
app.add_middleware(CORSMiddleware, ...)
app.add_middleware(GZipMiddleware, ...)
```
- **역할**: 요청/응답을 가로채서 처리합니다
- **예시**: CORS 설정, 압축, 로깅, 인증 등

### 4. 예외 처리
```python
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    ...
```
- **역할**: 전역 예외를 처리합니다
- **필수**: 에러 발생 시 일관된 응답을 제공합니다

### 5. 이벤트 핸들러
```python
@app.on_event("startup")
async def startup_event():
    ...

@app.on_event("shutdown")
async def shutdown_event():
    ...
```
- **역할**: 서버 시작/종료 시 실행할 코드
- **예시**: 데이터베이스 연결, 캐시 초기화 등

## main.py와의 관계

```python
# main.py
uvicorn.run("src.sentivest.api.app:app", ...)
```

- `main.py`: 서버를 **실행**하는 파일
- `app.py`: FastAPI 애플리케이션을 **정의**하는 파일
- `main.py`가 `app.py`의 `app` 변수를 import해서 서버를 시작합니다

## 파일 구조

```
src/sentivest/api/
├── __init__.py
├── app.py          # ⭐ 핵심 파일: FastAPI 앱 정의 + 라우터 등록
└── routes/
    ├── __init__.py
    ├── prediction.py   # 주식 예측 라우터
    ├── sentiment.py    # 감정 분석 라우터
    └── news.py         # 뉴스 라우터
```

## 요약

1. **app.py는 필수 파일입니다** ✅
2. **나중에 더 중요한 역할을 합니다** ✅
3. **라우터를 등록하는 중심 역할** ✅
4. **미들웨어, 예외 처리 등을 설정하는 곳** ✅
5. **서버 시작/종료 이벤트를 처리하는 곳** ✅
6. **main.py가 이 파일을 import해서 사용합니다** ✅

## 결론

**app.py는 프로젝트의 핵심 파일입니다!**
- 현재는 테스트용이지만 구조는 프로덕션 기반
- 나중에 실제 기능을 추가할 때 이 파일에 라우터를 등록합니다
- 절대 삭제하거나 버려지는 파일이 아닙니다
- 오히려 프로젝트가 커질수록 더 중요한 역할을 합니다

