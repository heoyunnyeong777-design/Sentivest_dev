"""
FastAPI 애플리케이션
"""
from fastapi import FastAPI
from src.sentivest import __version__

# FastAPI 앱 생성
app = FastAPI(
    title="Sentivest API",
    description="AI 기반 주식 예측 및 뉴스 감정 분석 대시보드",
    version=__version__
)


@app.get("/")
async def root():
    """루트 엔드포인트 - Hello World"""
    return {
        "message": "Hello World!",
        "version": __version__,
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """헬스체크 엔드포인트"""
    return {
        "status": "healthy",
        "version": __version__
    }

