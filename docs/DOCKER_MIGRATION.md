# PostgreSQL Docker 전환 가이드

## 📋 전환 전 준비사항

### 1. Docker 설치 확인
- Docker Desktop이 설치되어 있어야 함
- Docker가 실행 중이어야 함

### 2. 기존 데이터 백업 (중요!)
- 현재 데이터베이스의 데이터를 백업
- 필요하면 나중에 복원 가능

---

## 🚀 Docker로 전환하는 방법

### 방법 1: Docker Desktop 설치 후 전환 (권장)

#### 1단계: Docker Desktop 설치

**Windows:**
1. Docker Desktop 다운로드
   - https://www.docker.com/products/docker-desktop/
   - Windows용 다운로드
2. 설치 파일 실행
3. 설치 완료 후 재시작
4. Docker Desktop 실행
5. 설치 확인:
   ```bash
   docker --version
   ```

#### 2단계: 기존 PostgreSQL 서비스 중지 (선택사항)

**방법 A: 서비스만 중지 (데이터 유지)**
```bash
# PowerShell에서 (관리자 권한)
Stop-Service postgresql-x64-18
```

**방법 B: 서비스 완전 중지 및 자동 시작 해제**
```bash
# PowerShell에서 (관리자 권한)
Stop-Service postgresql-x64-18
Set-Service postgresql-x64-18 -StartupType Disabled
```

#### 3단계: Docker로 PostgreSQL 실행

**명령어 실행:**
```bash
docker run --name postgres-sentivest \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=wjsghk123! \
  -e POSTGRES_DB=sentivest \
  -p 5432:5432 \
  -d \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:18
```

**명령어 설명:**
- `--name postgres-sentivest`: 컨테이너 이름
- `-e POSTGRES_USER=postgres`: 사용자 이름
- `-e POSTGRES_PASSWORD=wjsghk123!`: 비밀번호
- `-e POSTGRES_DB=sentivest`: 데이터베이스 이름
- `-p 5432:5432`: 포트 매핑 (호스트:컨테이너)
- `-d`: 백그라운드 실행
- `-v postgres_data:/var/lib/postgresql/data`: 데이터 영구 저장 (볼륨)
- `postgres:18`: PostgreSQL 18 이미지

#### 4단계: 연결 확인

**방법 1: Python 스크립트로 확인**
```python
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="wjsghk123!",
    dbname="sentivest"
)
print("Connection successful!")
```

**방법 2: psql 명령어로 확인**
```bash
docker exec -it postgres-sentivest psql -U postgres -d sentivest
```

---

## 📝 docker-compose 사용 (권장)

### docker-compose.yml 파일 생성

더 편리하게 관리하기 위해 `docker-compose.yml` 파일을 만듭니다:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:18
    container_name: postgres-sentivest
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: wjsghk123!
      POSTGRES_DB: sentivest
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

**사용 방법:**
```bash
# 컨테이너 시작
docker-compose up -d

# 컨테이너 중지
docker-compose down

# 컨테이너 중지 및 볼륨 삭제 (데이터 삭제)
docker-compose down -v

# 로그 확인
docker-compose logs -f postgres
```

---

## 🔄 기존 데이터 마이그레이션 (선택사항)

### 기존 데이터베이스 데이터를 Docker로 옮기기

#### 1단계: 기존 데이터베이스 백업

```bash
# PowerShell에서
$env:Path += ";C:\Program Files\PostgreSQL\18\bin"
pg_dump -U postgres -d sentivest > backup.sql
```

#### 2단계: Docker PostgreSQL 실행

```bash
docker run --name postgres-sentivest \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=wjsghk123! \
  -e POSTGRES_DB=sentivest \
  -p 5432:5432 \
  -d \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:18
```

#### 3단계: 백업 데이터 복원

```bash
# PowerShell에서
$env:Path += ";C:\Program Files\PostgreSQL\18\bin"
psql -U postgres -d sentivest -f backup.sql
```

또는 Docker 컨테이너를 통해:

```bash
# 백업 파일을 컨테이너에 복사
docker cp backup.sql postgres-sentivest:/backup.sql

# 복원
docker exec -i postgres-sentivest psql -U postgres -d sentivest < backup.sql
```

---

## 🔧 Docker 명령어 모음

### 컨테이너 관리

```bash
# 컨테이너 시작
docker start postgres-sentivest

# 컨테이너 중지
docker stop postgres-sentivest

# 컨테이너 재시작
docker restart postgres-sentivest

# 컨테이너 삭제 (데이터는 볼륨에 있음)
docker rm postgres-sentivest

# 컨테이너 로그 확인
docker logs postgres-sentivest

# 컨테이너 상태 확인
docker ps -a
```

### 데이터베이스 접속

```bash
# Docker 컨테이너 내에서 psql 실행
docker exec -it postgres-sentivest psql -U postgres -d sentivest

# SQL 명령어 실행
docker exec postgres-sentivest psql -U postgres -d sentivest -c "SELECT 1;"
```

### 볼륨 관리

```bash
# 볼륨 목록 확인
docker volume ls

# 볼륨 상세 정보
docker volume inspect postgres_data

# 볼륨 삭제 (주의: 데이터 삭제됨)
docker volume rm postgres_data
```

---

## ⚠️ 주의사항

### 1. 포트 충돌
- 기존 PostgreSQL 서비스가 실행 중이면 포트 5432 충돌
- 기존 서비스를 중지하거나 다른 포트 사용

**다른 포트 사용:**
```bash
docker run --name postgres-sentivest \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=wjsghk123! \
  -e POSTGRES_DB=sentivest \
  -p 5433:5432 \  # 호스트 5433 포트 사용
  -d \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:18
```

**DATABASE_URL 변경:**
```
DATABASE_URL=postgresql://postgres:wjsghk123!@localhost:5433/sentivest
```

### 2. 데이터 백업
- 볼륨을 사용하면 데이터가 유지됨
- 볼륨을 삭제하면 데이터도 삭제됨
- 정기적으로 백업 권장

### 3. 보안
- 비밀번호는 `.env` 파일에 저장
- Git에 커밋하지 않기
- 프로덕션에서는 강력한 비밀번호 사용

---

## 🔄 전환 비교

### 직접 설치 (현재)
```
✅ 설치 완료
✅ 실행 중
✅ 데이터 있음
❌ 복잡한 관리
```

### Docker 사용
```
✅ 간단한 관리
✅ 쉬운 삭제/재생성
✅ 환경 통일
⚠️ Docker 설치 필요
⚠️ 전환 작업 필요
```

---

## 💡 추천 사항

### 현재 상황
- PostgreSQL이 이미 설치되어 있음
- 데이터베이스가 생성되어 있음
- 정상 작동 중

### 권장
**현재는 직접 설치된 PostgreSQL 사용을 권장합니다:**
- 이미 설정 완료
- 추가 작업 불필요
- 정상 작동 중

### Docker로 전환하는 경우
- 새로운 프로젝트 시작
- 여러 환경에서 통일된 환경 필요
- 컨테이너 관리 경험을 쌓고 싶을 때

---

## 📚 Docker Compose 파일 예시

프로젝트 루트에 `docker-compose.yml` 파일 생성 (권장):

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:18
    container_name: postgres-sentivest
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: wjsghk123!
      POSTGRES_DB: sentivest
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

**사용:**
```bash
docker-compose up -d      # 시작
docker-compose down       # 중지
docker-compose logs -f    # 로그 확인
```

---

## ✅ 체크리스트

Docker로 전환하기 전:

- [ ] Docker Desktop 설치 확인
- [ ] 기존 PostgreSQL 데이터 백업 (필요 시)
- [ ] 기존 PostgreSQL 서비스 중지 (포트 충돌 방지)
- [ ] docker-compose.yml 파일 생성 (선택사항)
- [ ] Docker 컨테이너 실행
- [ ] 연결 테스트
- [ ] .env 파일 확인 (DATABASE_URL)

---

## 🎯 요약

**Docker로 전환하는 방법:**
1. Docker Desktop 설치
2. 기존 PostgreSQL 서비스 중지 (선택)
3. Docker로 PostgreSQL 실행
4. 연결 테스트
5. .env 파일 확인

**docker-compose 사용 (권장):**
1. `docker-compose.yml` 파일 생성
2. `docker-compose up -d` 실행
3. 연결 테스트

**현재 상황:**
- 이미 설치된 PostgreSQL 사용 중
- 정상 작동 중
- Docker로 전환 가능하지만 필수 아님

Docker로 전환하시겠습니까? 필요하면 더 자세히 안내하겠습니다.

