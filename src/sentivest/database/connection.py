"""
SQLAlchemy 연결 모듈 (라이트 버전)
- settings.DATABASE_URL을 사용해 엔진/세션을 만듭니다
- FastAPI 의존성에서 사용할 get_db() 제공
- init_db()로 등록된 모델 테이블을 생성할 수 있습니다
"""

from __future__ import annotations  # 미래 버전 호환(타이핑 등) 목적의 선언

from typing import Generator  # 제너레이터 타입 힌트를 위해 사용

from sqlalchemy import create_engine, text  # DB 엔진 생성, 간단 쿼리 실행(text)
from sqlalchemy.orm import sessionmaker, declarative_base  # 세션 팩토리, Base 클래스 생성

from src.sentivest.config import settings  # .env 값을 읽어 둔 settings 객체

# 1) psycopg3 드라이버 사용을 위한 URL 보정
#    - SQLAlchemy에서 PostgreSQL + psycopg3를 쓰려면 접두사가 postgresql+psycopg 이어야 합니다.
#    - 사용자가 .env 에 postgresql://... 형태로 넣었다면 아래에서 안전하게 바꿔 줍니다.
_database_url = settings.DATABASE_URL or ""
if _database_url.startswith("postgresql://"):
    _database_url = _database_url.replace("postgresql://", "postgresql+psycopg://", 1)

# 2) SQLAlchemy 엔진 생성
#    - DB와 실제 통신을 담당하는 핵심 객체입니다.
#    - pool_pre_ping=True: 연결이 유효한지 체크해 죽은 커넥션을 자동으로 교체합니다.
#    - echo=settings.DEBUG: 개발 모드(DEBUG=True)일 때 실행되는 SQL을 콘솔에 출력해 디버깅에 도움을 줍니다.
engine = create_engine(
    _database_url,
    pool_pre_ping=True,
    echo=settings.DEBUG,
)

# 3) 세션 팩토리
#    - 세션(Session)은 DB 작업(쿼리, 트랜잭션 등)을 수행하는 창구입니다.
#    - SessionLocal() 로 호출할 때마다 독립적인 세션 인스턴스를 얻습니다.
SessionLocal = sessionmaker(
    autocommit=False,   # 자동 커밋 금지(명시적 트랜잭션 제어 권장)
    autoflush=False,    # flush 타이밍을 명시적으로 제어(성능/예측성 개선)
    bind=engine,        # 위에서 만든 엔진에 묶습니다
)

# 4) Base 클래스 (모든 모델은 이 클래스를 상속)
#    - 각 모델 클래스는 Base를 상속하여 SQLAlchemy에 "메타데이터"로 등록됩니다.
#    - 나중에 Base.metadata.create_all(...) 로 테이블 일괄 생성이 가능합니다.
Base = declarative_base()


def get_db() -> Generator:
    """요청마다 DB 세션을 열고, 완료 후 닫아주는 제너레이터.
    FastAPI에서 Depends(get_db)로 사용합니다.

    사용 예)
        @app.get("/items")
        def list_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()  # 새 세션 열기
    try:
        yield db          # 뷰/핸들러에 세션을 넘겨 사용하게 함
    finally:
        db.close()        # 요청 처리 후 반드시 세션 정리


def init_db() -> None:
    """등록된 모델 기반으로 테이블을 생성합니다.
    - 모델 파일이 Base에 등록되어 있어야 합니다 (import 필요)
    - 라이트 버전에서는 필요한 모델만 import 하고 create_all 호출

    주의)
    - 이미 테이블이 존재하면 create_all은 건너뜁니다(안전).
    - 스키마 변경 추적이 필요해지면 Alembic 같은 마이그레이션 도구를 고려하세요.
    """
    # 예시 모델 import (필요한 만큼만 추가)
    from src.sentivest.models.test_table import TestTable  # noqa: F401  # pylint: disable=unused-import

    # Base에 등록된 모든 모델의 테이블 생성
    Base.metadata.create_all(bind=engine)


def check_connection() -> bool:
    """간단한 연결 체크.
    SELECT 1이 성공하면 True, 실패하면 False를 반환합니다.

    사용 예)
        if not check_connection():
            raise RuntimeError("DB 연결 실패")
    """
    try:
        with engine.connect() as conn:      # 엔진에서 커넥션을 하나 얻고
            conn.execute(text("SELECT 1"))  # 매우 가벼운 건강검진 쿼리 실행
        return True
    except Exception:
        return False
