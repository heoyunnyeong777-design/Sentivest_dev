# PostgreSQL 데이터베이스 확인 방법

## 방법 1: pgAdmin 4 사용 (가장 쉬운 방법) ⭐

### 1단계: pgAdmin 4 실행
1. **시작 메뉴**에서 "pgAdmin 4" 검색
2. "pgAdmin 4" 실행
3. 처음 실행 시 마스터 비밀번호 설정 (pgAdmin용, 기억해두세요)

### 2단계: 서버 연결
1. 왼쪽 패널에서 "Servers" 우클릭
2. "Register" → "Server" 선택
3. "General" 탭:
   - Name: `Local PostgreSQL` (원하는 이름)
4. "Connection" 탭:
   - Host name/address: `localhost`
   - Port: `5432`
   - Username: `postgres`
   - Password: `wjsghk123!` (설치 시 설정한 비밀번호)
5. "Save" 클릭

### 3단계: 데이터베이스 확인
1. 왼쪽 패널에서 "Servers" → "Local PostgreSQL" 확장
2. "Databases" 확장
3. **"sentivest"** 데이터베이스 확인!

---

## 방법 2: psql 명령어 사용 (터미널)

### 1단계: PostgreSQL 연결
```bash
# PowerShell에서
$env:Path += ";C:\Program Files\PostgreSQL\18\bin"
psql -U postgres
```

### 2단계: 비밀번호 입력
- 비밀번호 입력: `wjsghk123!`
- `postgres=#` 프롬프트가 나타나면 성공!

### 3단계: 데이터베이스 목록 확인
```sql
\l
```
또는
```sql
SELECT datname FROM pg_database;
```

### 4단계: sentivest 데이터베이스로 이동
```sql
\c sentivest
```

### 5단계: 연결 종료
```sql
\q
```

---

## 방법 3: Python 스크립트로 확인

### 데이터베이스 목록 보기
```python
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="wjsghk123!",
    dbname="postgres"
)

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database ORDER BY datname")
databases = cur.fetchall()

print("Databases:")
for db in databases:
    print(f"  - {db[0]}")

cur.close()
conn.close()
```

---

## 간단한 확인 스크립트

아래 스크립트를 실행하면 모든 데이터베이스를 확인할 수 있습니다:

```bash
python view_databases.py
```

