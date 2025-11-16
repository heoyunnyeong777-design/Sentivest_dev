# pgAdmin에서 test_table 확인 방법

## 확인 결과

테이블이 **정상적으로 생성되어 있습니다**:
- 데이터베이스: `mydb`
- 스키마: `public`
- 테이블명: `test_table`
- 데이터: 3행

## pgAdmin에서 확인하는 방법

### 1단계: 올바른 서버에 연결되어 있는지 확인

1. pgAdmin 왼쪽 사이드바에서 **서버 그룹** 확인
2. 서버 이름 클릭 (예: `129.154.55.254`)
3. 연결 정보 확인:
   - Host: `129.154.55.254`
   - Port: `5432`
   - Maintenance Database: `mydb`
   - Username: `admin`

### 2단계: 올바른 데이터베이스 선택

**중요**: `mydb` 데이터베이스를 선택해야 합니다!

1. 서버 아래에서 **Databases** 펼치기
2. **`mydb`** 클릭 (postgres가 아님!)
3. `mydb` 아래에서 **Schemas** 클릭
4. **`public`** 스키마 클릭
5. `public` 아래에서 **Tables** 클릭

### 3단계: 새로고침

pgAdmin에서 테이블 목록이 업데이트되지 않았을 수 있습니다.

1. **Tables** 폴더에 **우클릭**
2. **Refresh** 클릭
   - 또는 **F5** 키 누르기
3. 이제 `test_table`이 보여야 합니다!

### 4단계: 테이블 데이터 확인

1. `test_table` 클릭
2. 상단 탭에서 **Data Output** 탭 클릭
3. 데이터가 보여야 합니다 (3행)

---

## 문제 해결

### test_table이 안 보이는 경우

#### 1. 잘못된 데이터베이스에 연결했을 때

**확인사항:**
- `postgres` 데이터베이스가 아니라 **`mydb`** 데이터베이스를 선택해야 합니다
- 서버 아래: **Databases > mydb > Schemas > public > Tables**

#### 2. 새로고침이 안 된 경우

**해결방법:**
- **Tables** 폴더 우클릭 > **Refresh**
- 또는 전체 서버 새로고침: 서버 이름 우클릭 > **Refresh**

#### 3. 권한 문제

**확인사항:**
- 사용자 `admin`이 `mydb` 데이터베이스에 접근 권한이 있는지 확인
- `public` 스키마에 대한 권한이 있는지 확인

#### 4. 연결 문제

**확인사항:**
- pgAdmin에서 서버 연결이 정상인지 확인
- 서버 이름 옆에 **X** 표시가 있으면 연결이 끊어진 것
- 서버 이름 우클릭 > **Connect Server**

---

## 정확한 경로

pgAdmin에서 다음 경로를 따라가세요:

```
서버 (129.154.55.254:5432)
└── Databases
    └── mydb  ← 여기가 중요!
        └── Schemas
            └── public  ← 여기도 중요!
                └── Tables
                    └── test_table  ← 여기에 있어야 합니다!
```

---

## 빠른 확인 방법

SQL 쿼리로 직접 확인:

1. pgAdmin에서 **Tools > Query Tool** 클릭
2. 다음 쿼리 실행:

```sql
-- 데이터베이스 확인
SELECT current_database();

-- 테이블 목록 확인
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public'
ORDER BY table_name;

-- test_table 데이터 확인
SELECT * FROM test_table;
```

---

## 연결 정보 요약

| 항목 | 값 |
|------|-----|
| Host | 129.154.55.254 |
| Port | 5432 |
| Database | **mydb** ← 이것을 선택해야 함! |
| Schema | **public** |
| Username | admin |
| Table | test_table |

---

## 참고사항

- 테이블은 **`mydb`** 데이터베이스의 **`public`** 스키마에 있습니다
- `postgres` 데이터베이스가 아니라 **`mydb`**를 선택해야 합니다
- 새로고침(F5)을 하면 테이블이 보여야 합니다


