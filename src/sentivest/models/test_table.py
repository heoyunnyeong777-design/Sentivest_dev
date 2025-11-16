"""
라이트 버전 예시 모델: test_table
- 이미 클라우드 DB에 만든 테이블과 호환되는 간단한 구조
"""

from __future__ import annotations

from sqlalchemy import Column, Integer, String, Text, DateTime, func

from src.sentivest.database.connection import Base


class TestTable(Base):
    """간단한 테스트 테이블 모델.
    __tablename__은 실제 DB 테이블 이름과 일치해야 합니다.
    """

    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), nullable=True)
