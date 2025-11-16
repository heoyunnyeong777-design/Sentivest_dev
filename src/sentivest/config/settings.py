"""
환경 변수 및 애플리케이션 설정을 한 곳에서 관리합니다.

이 모듈은 .env와 시스템 환경변수에서 값을 읽어
애플리케이션 전역에서 import 하여 사용할 수 있도록 제공합니다.

가볍게 시작하고, 필요해질 때 항목을 추가하는 방식을 권장합니다.

사용 예시)
    from src.sentivest.config import settings  # settings 객체 불러오기
    print(settings.APP_NAME)                   # 앱 이름 출력
    print(settings.DATABASE_URL)               # DB 연결 문자열 출력

주의사항)
- .env 파일은 비밀정보(비밀번호, 토큰 등)가 포함되므로 Git에 커밋하지 않습니다.
- 운영/개발 환경이 다르면 .env 파일만 바꿔도 설정이 전환됩니다.
"""

from __future__ import annotations  # 미래 버전 호환을 위한 선언 (타이핑 관련)

import os  # 운영체제 환경변수(os.environ)를 읽기 위해 사용
from dataclasses import dataclass  # 간단한 설정 묶음을 깔끔하게 표현하기 위해 사용
from typing import List  # 타입 힌트: 리스트 타입 표기를 위해 사용

from dotenv import load_dotenv  # .env 파일을 읽어 환경변수로 로드하기 위해 사용

# 1) .env 파일 로드
# - 현재 실행 디렉토리에 있는 .env 파일을 읽어서
#   그 안의 "KEY=VALUE" 들을 운영체제 환경변수(os.environ)에 주입합니다.
# - override=True: 이미 같은 KEY가 환경에 있어도 .env 값을 덮어쓰도록 함.
load_dotenv(override=True)


@dataclass(frozen=True)  # dataclass: 설정 값을 담는 간단한 클래스 생성, frozen=True로 불변(읽기전용)화
class Settings:
    """애플리케이션 전역 설정 값 집합.

    필드 추가 가이드
    - 지금 필요한 값만 최소한으로 추가합니다.
    - 새 환경변수가 필요해지면: (.env에 KEY 추가) → (여기 필드 추가) → (코드에서 사용)
    - 문자열/불리언/정수 등 간단한 타입부터 사용합니다.
    """

    # [앱 기본정보]
    APP_NAME: str = os.getenv("APP_NAME", "Sentivest")  # 앱 이름(기본값: Sentivest)
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")  # 앱 버전(기본값: 0.1.0)

    # [실행 모드]
    # - DEBUG 가 True면 개발 모드(자세한 로그, 자동 리로드 등)로 동작할 수 있습니다.
    # - .env 에서 DEBUG=False 로 바꾸면 배포 모드에 가깝게 동작시키는 데 도움이 됩니다.
    DEBUG: bool = os.getenv("DEBUG", "True").strip().lower() == "true"  # 문자열을 소문자로 바꿔 비교하여 bool로 변환

    # [서버 바인딩]
    # - uvicorn 같은 서버를 띄울 때 사용할 호스트/포트입니다.
    # - HOST는 기본 127.0.0.1(내 컴퓨터), PORT는 기본 8000입니다.
    HOST: str = os.getenv("HOST", "127.0.0.1")  # 서버가 바인딩할 주소
    PORT: int = int(os.getenv("PORT", "8000"))  # 서버가 바인딩할 포트(문자열을 int로 변환)

    # [보안]
    # - SECRET_KEY는 서명/세션/토큰 등에 사용할 수 있는 비밀 키입니다.
    # - 실제 배포에서는 강력한 랜덤 문자열을 사용하세요.
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")  # 기본값은 반드시 교체 권장

    # [데이터베이스]
    # - DATABASE_URL은 데이터베이스 연결 문자열입니다.
    # - 예시: postgresql://admin:pass1234@129.154.55.254:5432/mydb
    #   * 앞 부분(postgresql://)은 DB 종류
    #   * admin 은 사용자명, pass1234 는 비밀번호
    #   * 129.154.55.254 는 DB 서버 주소, 5432 는 포트
    #   * mydb 는 데이터베이스 이름
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")  # 비어 있으면 연결 코드는 실패할 수 있으니 .env에서 꼭 채우세요

    # [CORS]
    # - 프론트엔드(웹 앱)에서 백엔드 API에 접속할 수 있도록 허용할 주소 목록입니다.
    # - 쉼표(,)로 구분하여 여러 개를 넣을 수 있습니다.
    #   예: "http://localhost:3000,http://localhost:5173"
    ALLOWED_ORIGINS: List[str] = tuple(  # tuple로 감싸서 불변(읽기전용) 시맨틱을 가짐
        origin.strip()  # 각 항목의 앞뒤 공백 제거
        for origin in os.getenv(
            "ALLOWED_ORIGINS",
            "http://localhost:3000,http://localhost:5173",  # 기본 허용 주소(개발용)
        ).split(",")  # 문자열을 쉼표 기준으로 나눠 리스트로 만듦
        if origin.strip()  # 공백만 있는 값은 제외
    )


# 아래 settings 인스턴스 하나만 만들어 두고
# 애플리케이션 전체에서 같은 설정 값을 재사용합니다.
# 사용 예: from src.sentivest.config import settings
settings = Settings()
