"""
FastAPI 애플리케이션
"""
from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from src.sentivest import __version__
from src.sentivest.database.connection import get_db
from src.sentivest.models.test_table import TestTable

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


@app.get("/test-table", summary="test_table 조회", tags=["examples"])
async def list_test_table(
    limit: int = Query(20, ge=1, le=100, description="가져올 최대 행 수 (1~100)"),
    db: Session = Depends(get_db),
):
    """클라우드 DB의 test_table을 조회하는 예시 엔드포인트.
    - 서버가 떠 있으면 http://127.0.0.1:8000/test-table 로 확인할 수 있습니다.
    - limit 파라미터로 최대 행 수를 조절할 수 있습니다.
    """
    rows = (
        db.query(TestTable)
        .order_by(TestTable.id.asc())
        .limit(limit)
        .all()
    )
    # 간단 직렬화
    return [
        {
            "id": r.id,
            "name": r.name,
            "description": r.description,
            "created_at": r.created_at,
            "updated_at": r.updated_at,
        }
        for r in rows
    ]

