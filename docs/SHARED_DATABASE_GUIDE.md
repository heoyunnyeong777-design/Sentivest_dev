# 공유 데이터베이스 설정 가이드

## 📋 상황 설명

여러 사람이 같은 프로젝트를 사용할 때, 하나의 데이터베이스를 공유해야 하는 경우입니다.

---

## 🎯 해결 방법

### 방법 1: 클라우드 서버에 PostgreSQL 설치 (권장)

#### 옵션 A: AWS EC2 (Amazon Web Services)

**장점:**
- 무료 티어 제공 (1년간)
- 안정적
- 확장 가능

**단계:**
1. AWS 계정 생성
2. EC2 인스턴스 생성 (Ubuntu 또는 Amazon Linux)
3. SSH로 서버 접속
4. PostgreSQL 설치
5. 원격 접속 허용 설정
6. 보안 그룹 설정 (포트 5432 열기)

**비용:**
- 무료 티어: 1년간 무료 (제한 있음)
- 이후: 월 약 $5-10 (인스턴스 크기에 따라)

---

#### 옵션 B: 클라우드 데이터베이스 서비스 (가장 쉬움) ⭐

**AWS RDS (PostgreSQL)**
- 완전 관리형 서비스
- 자동 백업
- 자동 업데이트
- 설정이 간단

**단계:**
1. AWS 계정 생성
2. RDS 콘솔에서 PostgreSQL 인스턴스 생성
3. 엔드포인트 주소 받기
4. 보안 그룹 설정
5. DATABASE_URL 설정

**비용:**
- 무료 티어: 1년간 무료 (제한 있음)
- 이후: 월 약 $15-30

---

#### 옵션 C: VPS 서버 (CentOS, Ubuntu)

**예시 서비스:**
- DigitalOcean (월 $5부터)
- Linode (월 $5부터)
- Vultr (월 $5부터)
- 네이버 클라우드 플랫폼
- 카카오 i 클라우드

**단계:**
1. VPS 서버 구매
2. CentOS 또는 Ubuntu 선택
3. SSH로 서버 접속
4. PostgreSQL 설치
5. 원격 접속 설정
6. 방화벽 설정

**비용:**
- 월 약 $5-10 (서버 사양에 따라)

---

## 🚀 추천 방법: 클라우드 데이터베이스 서비스

### AWS RDS 사용 (가장 쉬움)

**왜 추천하는가?**
1. 설정이 간단함
2. 자동 백업
3. 자동 업데이트
4. 보안 관리 용이
5. 확장 용이

**단계 요약:**
1. AWS 계정 생성
2. RDS 콘솔 접속
3. PostgreSQL 인스턴스 생성
4. 엔드포인트 주소 복사
5. DATABASE_URL 설정

**DATABASE_URL 예시:**
```
DATABASE_URL=postgresql://admin:비밀번호@sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com:5432/sentivest
```

---

## 📝 실제 설정 예시

### 시나리오: 팀원 3명이 같은 데이터베이스 사용

**서버 설정:**
- 서버: AWS RDS PostgreSQL
- 엔드포인트: `sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com`
- 포트: `5432`
- 데이터베이스: `sentivest`
- 사용자: `sentivest_user`
- 비밀번호: `강력한비밀번호`

**각 팀원의 .env 파일:**
```env
DATABASE_URL=postgresql://sentivest_user:강력한비밀번호@sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com:5432/sentivest
```

**결과:**
- 모든 팀원이 같은 데이터베이스 사용
- 데이터 공유됨
- 실시간으로 동기화됨

---

## 🔒 보안 설정 (중요!)

### 1. 비밀번호 관리
- 강력한 비밀번호 사용
- .env 파일에 저장 (Git에 커밋하지 않음)
- 팀원에게만 공유

### 2. 접근 제한
- 특정 IP만 허용 (가능하면)
- VPN 사용 (권장)
- SSL 연결 사용

### 3. 백업
- 정기적으로 백업
- 클라우드 서비스는 자동 백업 제공

---

## 💰 비용 비교

### 옵션 1: AWS RDS (관리형)
- 무료 티어: 1년간 무료
- 이후: 월 $15-30
- 장점: 관리 편함, 자동 백업

### 옵션 2: EC2 + 직접 설치
- 무료 티어: 1년간 무료
- 이후: 월 $5-10
- 장점: 저렴, 제어 가능
- 단점: 직접 관리 필요

### 옵션 3: VPS (DigitalOcean 등)
- 월 $5-10
- 장점: 저렴, 간단
- 단점: 직접 관리 필요

---

## 🎯 단계별 추천

### 초보자 (권장)
**AWS RDS 사용**
- 설정이 가장 쉬움
- 자동 관리
- 무료 티어 제공

### 중급자
**EC2 + PostgreSQL 직접 설치**
- 더 많은 제어
- 비용 절감
- 직접 관리

### 고급자
**VPS + Docker**
- 완전한 제어
- 유연한 설정
- 비용 절감

---

## 📚 실제 설정 가이드

### AWS RDS 설정 (간단 요약)

1. **AWS 계정 생성**
   - https://aws.amazon.com 접속
   - 계정 생성 (신용카드 필요, 무료 티어 사용)

2. **RDS 콘솔 접속**
   - AWS 콘솔 → RDS → 데이터베이스 생성

3. **PostgreSQL 선택**
   - 엔진: PostgreSQL
   - 버전: 18 (또는 최신)
   - 템플릿: 무료 티어 (또는 프로덕션)

4. **설정 입력**
   - DB 인스턴스 식별자: `sentivest-db`
   - 마스터 사용자 이름: `postgres` (또는 원하는 이름)
   - 마스터 비밀번호: 강력한 비밀번호 설정

5. **네트워크 설정**
   - VPC: 기본값
   - 퍼블릭 액세스: 예 (다른 사람 접속 위해)
   - 보안 그룹: 새로 생성 또는 기존 사용

6. **데이터베이스 이름**
   - `sentivest`

7. **생성 완료**
   - 엔드포인트 주소 복사
   - 예: `sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com`

8. **보안 그룹 설정**
   - 인바운드 규칙 추가
   - 포트: 5432
   - 소스: 팀원 IP 또는 0.0.0.0/0 (모든 IP, 보안상 권장하지 않음)

9. **DATABASE_URL 설정**
   ```
   DATABASE_URL=postgresql://postgres:비밀번호@sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com:5432/sentivest
   ```

---

## 🔄 로컬 → 클라우드 마이그레이션

### 기존 데이터 옮기기

1. **로컬 데이터베이스 백업**
   ```bash
   pg_dump -U postgres -d sentivest > backup.sql
   ```

2. **클라우드 데이터베이스에 복원**
   ```bash
   psql -h sentivest-db.xxxxxx.us-east-1.rds.amazonaws.com \
        -U postgres \
        -d sentivest \
        -f backup.sql
   ```

---

## ✅ 체크리스트

공유 데이터베이스 설정 전:

- [ ] 클라우드 서비스 선택 (AWS RDS 권장)
- [ ] 계정 생성 및 설정
- [ ] PostgreSQL 인스턴스 생성
- [ ] 엔드포인트 주소 확인
- [ ] 보안 그룹 설정 (포트 5432)
- [ ] DATABASE_URL 설정
- [ ] 연결 테스트
- [ ] 팀원에게 DATABASE_URL 공유 (안전하게)
- [ ] .env.example 업데이트 (엔드포인트만, 비밀번호는 제외)

---

## 💡 요약

**질문: 다른 사람도 접속할 수 있게 하려면?**

**답변:**
- 네, 서버에 올려야 합니다
- 클라우드 서버 또는 클라우드 데이터베이스 서비스 사용
- CentOS 같은 서버에 직접 설치 가능
- AWS RDS 같은 관리형 서비스가 가장 쉬움

**추천:**
- 초보자: AWS RDS (가장 쉬움)
- 비용 절감: EC2 + 직접 설치
- 완전한 제어: VPS + Docker

**비용:**
- 무료 티어: 1년간 무료 (제한 있음)
- 이후: 월 $5-30 (선택한 서비스에 따라)

---

## 🎓 다음 단계

1. 클라우드 서비스 선택
2. 계정 생성
3. PostgreSQL 인스턴스 생성
4. DATABASE_URL 설정
5. 팀원과 공유

어떤 방법을 선택하시겠습니까?

