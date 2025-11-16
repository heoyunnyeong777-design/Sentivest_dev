"""
환경 변수 및 애플리케이션 설정을 한 곳에서 관리합니다.

이 모듈은 .env와 시스템 환경변수에서 값을 읽어
애플리케이션 전역에서 import 하여 사용할 수 있도록 제공합니다.

가볍게 시작하고, 필요해질 때 항목을 추가하는 방식을 권장합니다.

사용 예시)
    from src.sentivest.config import settings
    print(settings.APP_NAME)
    print(settings.DATABASE_URL)

주의사항)
- .env 파일은 비밀정보가 포함되므로 Git에 커밋하지 않습니다.
- 운영/개발 환경이 다르면 .env 파일만 바꿔도 설정이 전환됩니다.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv

# 1) .env 파일 로드
# - 현재 실행 디렉토리에 존재하는 .env를 읽어 환경변수에 주입합니다.
# - 동일 키가 이미 환경에 있어도 .env 값으로 덮어쓰도록 override=True 사용.
load_dotenv(override=True)


@dataclass(frozen=True)
class Settings:
    """애플리케이션 전역 설정 값 집합.

    필드 추가 가이드
    - 지금 필요한 값만 최소한으로 추가합니다.
    - 새 환경변수가 필요해지면: (.env에 키 추가) → (여기 필드 추가) → (코드에서 사용)
    - 문자열/불리언/정수 등 간단한 타입부터 사용합니다.
    """

    # [앱 기본정보]
    APP_NAME: str = os.getenv("APP_NAME", "Sentivest")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

    # [실행 모드]
    # - 개발 단계에서는 True(자세한 로그, 자동 리로드 등)
    # - 배포 단계에서는 False로 전환 권장
    DEBUG: bool = os.getenv("DEBUG", "True").strip().lower() == "true"

    # [서버 바인딩]
    # - FastAPI/uvicorn 실행 시 사용할 호스트/포트
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))

    # [보안]
    # - 세션/토큰/서명 등에 사용될 수 있는 키(예시)
    # - 배포 환경에서는 반드시 강력한 랜덤 문자열 사용
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")

    # [데이터베이스]
    # - SQLAlchemy/psycopg 등에서 사용하는 표준 연결 문자열
    # - 현재 값은 클라우드 PostgreSQL을 가리키도록 .env에서 관리
    #   예) postgresql://admin:pass1234@129.154.55.254:5432/mydb
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    # [CORS]
    # - 프론트엔드(대시보드) 도메인을 쉼표(,)로 구분해 나열
    #   예) http://localhost:3000,http://localhost:5173
    ALLOWED_ORIGINS: List[str] = tuple(
        origin.strip()
        for origin in os.getenv(
            "ALLOWED_ORIGINS",
            "http://localhost:3000,http://localhost:5173",
        ).split(",")
        if origin.strip()
    )  # tuple로 고정하여 불변 특성 부여


# settings 인스턴스는 애플리케이션 전역에서 재사용됩니다.
settings = Settings()
