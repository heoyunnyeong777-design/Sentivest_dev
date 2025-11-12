# Sentivest - AI 기반 주식 예측 및 뉴스 감정 분석 대시보드

AI를 활용한 주식 시장 예측 및 뉴스 감정 분석 플랫폼입니다.

## 📋 프로젝트 소개

Sentivest는 머신러닝과 자연어 처리 기술을 활용하여:
- 주식 가격 예측
- 금융 뉴스 감정 분석
- 종합 대시보드를 제공하는 백엔드 시스템입니다.

## 🚀 주요 기능

- **주식 예측**: AI 모델을 활용한 주식 가격 예측
- **감정 분석**: 뉴스 기사 및 소셜 미디어의 감정 분석
- **뉴스 수집**: 금융 뉴스 자동 수집 및 처리
- **REST API**: 대시보드와 통신하기 위한 RESTful API

## 📁 프로젝트 구조

```
Sentivest_dev/
├── src/
│   └── sentivest/           # 메인 패키지
│       ├── api/             # API 엔드포인트 관련
│       │   └── routes/      # API 라우트 정의
│       ├── config/          # 설정 파일 관리
│       ├── database/        # 데이터베이스 연결 및 설정
│       ├── models/          # 데이터 모델 정의
│       ├── services/        # 비즈니스 로직
│       │   ├── news/        # 뉴스 수집 및 처리
│       │   ├── prediction/  # 주식 예측 서비스
│       │   └── sentiment/   # 감정 분석 서비스
│       └── utils/           # 유틸리티 함수
└── tests/                   # 테스트 코드
```

## 🛠️ 기술 스택

- **언어**: Python
- **프레임워크**: (추가 예정)
- **데이터베이스**: (추가 예정)
- **AI/ML**: (추가 예정)

## 📦 설치 방법

```bash
# 저장소 클론
git clone https://github.com/yourusername/Sentivest_dev.git
cd Sentivest_dev

# 가상환경 생성 (추가 예정)
# python -m venv venv
# source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate     # Windows

# 의존성 설치 (추가 예정)
# pip install -r requirements.txt
```

## 🚧 개발 상태

현재 프로젝트는 초기 설정 단계입니다. 아래는 단계별 개발 계획입니다.

### 1단계: 프로젝트 기본 설정 ✅
- [x] 프로젝트 폴더 구조 생성
- [ ] `.gitignore` 파일 생성
- [ ] `requirements.txt` 파일 생성 (의존성 패키지 목록)
- [ ] `.env.example` 파일 생성 (환경 변수 템플릿)
- [ ] `pyproject.toml` 또는 `setup.py` 생성 (패키지 설정)

### 2단계: 환경 설정 및 의존성 설치
- [ ] 가상환경(venv) 생성 및 활성화
- [ ] 기본 패키지 설치 (FastAPI, SQLAlchemy 등)
- [ ] 환경 변수 설정 파일 작성
- [ ] 데이터베이스 연결 설정

### 3단계: 기본 패키지 구조 및 설정 파일
- [x] `src/sentivest/__init__.py` 파일 생성
- [x] 각 서브 패키지에 `__init__.py` 파일 생성
- [ ] `src/sentivest/config/` 설정 모듈 작성
  - [ ] 환경 변수 로드
  - [ ] 데이터베이스 설정
  - [ ] API 설정
- [ ] `src/sentivest/utils/` 유틸리티 함수 작성

### 4단계: 데이터베이스 설정
- [ ] 데이터베이스 연결 클래스 작성
- [ ] 데이터베이스 모델 기본 구조 설정
- [ ] 마이그레이션 설정 (Alembic)

### 5단계: 데이터 모델 정의
- [ ] `src/sentivest/models/` 데이터 모델 작성
  - [ ] 주식 정보 모델
  - [ ] 뉴스 데이터 모델
  - [ ] 감정 분석 결과 모델
  - [ ] 예측 결과 모델
- [ ] Pydantic 스키마 모델 작성 (API 요청/응답)

### 6단계: 서비스 레이어 구현
- [ ] `src/sentivest/services/news/` 뉴스 서비스
  - [ ] 뉴스 수집 함수
  - [ ] 뉴스 데이터 처리 함수
- [ ] `src/sentivest/services/sentiment/` 감정 분석 서비스
  - [ ] 감정 분석 함수 (기본 버전)
  - [ ] 감정 점수 계산
- [ ] `src/sentivest/services/prediction/` 예측 서비스
  - [ ] 주식 데이터 수집 함수
  - [ ] 예측 모델 기본 구조

### 7단계: API 엔드포인트 구현
- [ ] FastAPI 애플리케이션 초기화
- [ ] `src/sentivest/api/routes/` 라우트 작성
  - [ ] 헬스체크 엔드포인트
  - [ ] 주식 예측 API
  - [ ] 감정 분석 API
  - [ ] 뉴스 조회 API
- [ ] API 문서 자동 생성 설정 (Swagger)
- [ ] 에러 핸들링 미들웨어

### 8단계: AI 모델 통합
- [ ] 감정 분석 모델 선택 및 통합
  - [ ] 모델 로드 함수
  - [ ] 텍스트 전처리
  - [ ] 예측 함수
- [ ] 주식 예측 모델 선택 및 통합
  - [ ] 시계열 데이터 전처리
  - [ ] 모델 학습 함수 (또는 사전 학습 모델 사용)
  - [ ] 예측 함수

### 9단계: 테스트 코드 작성
- [ ] `tests/` 테스트 구조 설정
- [ ] 유닛 테스트 작성
  - [ ] 서비스 함수 테스트
  - [ ] 모델 테스트
- [ ] API 통합 테스트 작성
- [ ] 테스트 실행 및 커버리지 확인

### 10단계: 문서화 및 배포 준비
- [ ] API 문서 보완
- [ ] README 업데이트
- [ ] 배포 설정 파일 작성
- [ ] Docker 설정 (선택사항)

## 📝 라이센스

(라이센스 정보 추가 예정)

## 👥 기여자

(기여자 정보 추가 예정)

## 📞 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 등록해주세요.
