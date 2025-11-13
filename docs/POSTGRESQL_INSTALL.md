# PostgreSQL 설치 가이드 (Windows)

## 📋 설치 전 준비사항

1. **관리자 권한** 필요 (선택사항, 권장)
2. **인터넷 연결** 필요
3. **디스크 공간**: 약 500MB 이상

---

## 🚀 설치 방법

### 방법 1: 공식 설치 프로그램 사용 (권장)

#### 1단계: 다운로드

1. **공식 웹사이트 접속**
   - https://www.postgresql.org/download/windows/
   - 또는 직접 다운로드: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

2. **버전 선택**
   - 최신 버전 선택 (예: PostgreSQL 16)
   - Windows x86-64 선택

3. **설치 파일 다운로드**
   - `postgresql-16.x-x-windows-x64.exe` 파일 다운로드

#### 2단계: 설치 실행

1. **다운로드한 파일 실행**
   - `postgresql-16.x-x-windows-x64.exe` 더블클릭

2. **설치 마법사 시작**
   - "Next" 클릭

3. **설치 경로 선택**
   - 기본 경로: `C:\Program Files\PostgreSQL\16` (권장)
   - 또는 원하는 경로 선택
   - "Next" 클릭

4. **구성 요소 선택**
   - 모든 항목 선택 (기본값 유지)
   - **필수 항목:**
     - PostgreSQL Server
     - pgAdmin 4 (관리 도구)
     - Stack Builder
     - Command Line Tools
   - "Next" 클릭

5. **데이터 디렉토리 선택**
   - 기본 경로: `C:\Program Files\PostgreSQL\16\data` (권장)
   - "Next" 클릭

6. **비밀번호 설정** ⚠️ **중요!**
   - **PostgreSQL superuser (postgres) 비밀번호 입력**
   - 이 비밀번호는 반드시 기억해야 함!
   - 복잡한 비밀번호 권장 (영문, 숫자, 특수문자)
   - "Next" 클릭

7. **포트 설정**
   - 기본 포트: `5432` (권장, 변경하지 않음)
   - "Next" 클릭

8. **로케일 설정**
   - 기본값: `[Default locale]` (권장)
   - "Next" 클릭

9. **설치 시작**
   - "Next" 클릭
   - 설치 진행 대기 (약 5-10분)

10. **설치 완료**
    - "Finish" 클릭
    - **Stack Builder 실행 안 함** (선택사항)

#### 3단계: 설치 확인

**방법 1: 명령 프롬프트에서 확인**
```bash
# PowerShell 또는 CMD에서
psql --version
```

**방법 2: 서비스 확인**
```bash
# PowerShell에서
Get-Service -Name postgresql*
```

**방법 3: pgAdmin 4 실행**
- 시작 메뉴에서 "pgAdmin 4" 실행
- 설정한 비밀번호 입력

---

## ✅ 설치 확인

### 1. psql 명령어 확인

```bash
# PowerShell에서
psql --version
```

**예상 결과:**
```
psql (PostgreSQL) 16.x
```

### 2. PostgreSQL 서비스 확인

```bash
# PowerShell에서
Get-Service -Name postgresql*
```

**예상 결과:**
```
Status   Name               DisplayName
------   ----               -----------
Running  postgresql-x64-16  postgresql-x64-16 - PostgreSQL Server 16
```

### 3. 연결 테스트

```bash
# PowerShell에서
psql -U postgres
```

**실행 후:**
- 비밀번호 입력 요청
- 설정한 비밀번호 입력
- `postgres=#` 프롬프트가 나타나면 성공!

**연결 종료:**
```sql
\q
```

---

## 🔧 기본 설정

### 1. 환경 변수 설정 (선택사항)

PostgreSQL이 자동으로 PATH에 추가됩니다. 
만약 `psql` 명령어가 작동하지 않으면:

1. 환경 변수 확인
   - `C:\Program Files\PostgreSQL\16\bin`이 PATH에 있는지 확인

2. 수동 추가 (필요 시)
   - 시스템 속성 → 고급 → 환경 변수
   - PATH에 `C:\Program Files\PostgreSQL\16\bin` 추가

### 2. PostgreSQL 서비스 관리

**서비스 시작:**
```bash
# PowerShell에서 (관리자 권한 필요)
Start-Service postgresql-x64-16
```

**서비스 중지:**
```bash
Stop-Service postgresql-x64-16
```

**서비스 재시작:**
```bash
Restart-Service postgresql-x64-16
```

### 3. 기본 사용자 및 데이터베이스

- **기본 사용자**: `postgres` (superuser)
- **기본 데이터베이스**: `postgres`
- **포트**: `5432`

---

## 🛠️ pgAdmin 4 사용 방법

### 1. pgAdmin 4 실행

- 시작 메뉴에서 "pgAdmin 4" 실행
- 처음 실행 시 마스터 비밀번호 설정 (pgAdmin용)

### 2. 서버 연결

1. 왼쪽 패널에서 "Servers" 우클릭
2. "Register" → "Server" 선택
3. "General" 탭:
   - Name: `Local PostgreSQL` (원하는 이름)
4. "Connection" 탭:
   - Host: `localhost`
   - Port: `5432`
   - Username: `postgres`
   - Password: 설치 시 설정한 비밀번호
5. "Save" 클릭

### 3. 데이터베이스 생성

1. 왼쪽 패널에서 "Databases" 우클릭
2. "Create" → "Database" 선택
3. Name: `sentivest` (프로젝트 이름)
4. "Save" 클릭

---

## 🔐 보안 설정 (중요!)

### 1. 비밀번호 보안

- **절대 Git에 커밋하지 않기!**
- `.env` 파일에 저장 (`.gitignore`에 포함됨)

### 2. 방화벽 설정

- PostgreSQL 포트(5432)는 로컬에서만 접근하도록 설정 권장
- 개발 단계에서는 localhost만 사용

---

## 🐛 문제 해결

### 문제 1: `psql` 명령어를 찾을 수 없음

**해결 방법:**
1. 환경 변수 확인
2. PostgreSQL 설치 경로 확인
3. PATH에 `C:\Program Files\PostgreSQL\16\bin` 추가

### 문제 2: 비밀번호를 잊어버림

**해결 방법:**
1. PostgreSQL 서비스 중지
2. `pg_hba.conf` 파일 수정
3. 인증 방식 변경 후 서비스 재시작
4. 비밀번호 재설정

### 문제 3: 포트가 이미 사용 중

**해결 방법:**
1. 다른 포트 사용 (예: 5433)
2. 또는 기존 서비스 중지

### 문제 4: 서비스가 시작되지 않음

**해결 방법:**
1. 로그 파일 확인: `C:\Program Files\PostgreSQL\16\data\log\`
2. 데이터 디렉토리 권한 확인
3. 방화벽 설정 확인

---

## 📝 다음 단계

PostgreSQL 설치가 완료되면:

1. **데이터베이스 생성**
   ```bash
   psql -U postgres
   CREATE DATABASE sentivest;
   \q
   ```

2. **`.env` 파일 설정**
   ```env
   DATABASE_URL=postgresql://postgres:your-password@localhost:5432/sentivest
   ```

3. **SQLAlchemy 연결 테스트**

---

## 📚 추가 자료

- **공식 문서**: https://www.postgresql.org/docs/
- **pgAdmin 문서**: https://www.pgadmin.org/docs/
- **SQL 튜토리얼**: https://www.postgresqltutorial.com/

---

## ✅ 체크리스트

설치 완료 후 확인:

- [ ] `psql --version` 명령어 작동
- [ ] PostgreSQL 서비스 실행 중
- [ ] `psql -U postgres` 연결 성공
- [ ] pgAdmin 4 실행 및 연결 성공
- [ ] 데이터베이스 생성 완료
- [ ] `.env` 파일에 연결 정보 저장

---

## 💡 팁

1. **비밀번호 관리**
   - 비밀번호를 안전한 곳에 기록
   - `.env` 파일에 저장 (Git에는 커밋하지 않음)

2. **데이터베이스 백업**
   - 정기적으로 백업하는 습관 기르기

3. **개발 환경**
   - 로컬에서는 `localhost`만 사용
   - 프로덕션에서는 보안 강화

4. **성능 최적화**
   - 개발 단계에서는 기본 설정으로 충분
   - 프로덕션에서는 튜닝 필요

