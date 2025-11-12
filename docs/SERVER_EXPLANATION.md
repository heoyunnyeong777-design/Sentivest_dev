# 서버 실행 원리 설명

## 📚 기본 개념

### 1. 웹 서버란?
- 웹 서버는 클라이언트(브라우저)의 요청을 받아서 처리하고 응답을 보내는 프로그램입니다
- 예를 들어, 브라우저에서 `http://127.0.0.1:8000`을 입력하면
  - 브라우저가 서버에 "GET /" 요청을 보냅니다
  - 서버가 요청을 처리하고 "Hello World!"를 응답으로 보냅니다
  - 브라우저가 화면에 표시합니다

### 2. FastAPI란?
- FastAPI는 Python으로 웹 API를 만들 수 있는 프레임워크입니다
- API 엔드포인트(URL 경로)를 쉽게 만들 수 있습니다
- 자동으로 API 문서를 생성해줍니다

### 3. Uvicorn이란?
- Uvicorn은 ASGI 서버입니다 (웹 서버 프로그램)
- FastAPI 애플리케이션을 실행하는 역할을 합니다
- 클라이언트의 요청을 받아서 FastAPI 애플리케이션에 전달합니다

---

## 🔄 실행 흐름 (단계별)

### 단계 1: `python main.py` 실행
```
사용자가 터미널에서: python main.py
↓
Python이 main.py 파일을 읽습니다
```

### 단계 2: `main.py` 파일 분석
```python
# main.py의 내용
import uvicorn  # 1. uvicorn 라이브러리를 가져옵니다

if __name__ == "__main__":  # 2. 이 파일이 직접 실행될 때만 실행
    uvicorn.run(  # 3. uvicorn 서버를 시작합니다
        "src.sentivest.api.app:app",  # 4. FastAPI 앱의 위치를 지정
        host="127.0.0.1",  # 5. 서버 주소 (로컬호스트)
        port=8000,  # 6. 포트 번호
        reload=True  # 7. 코드 변경 시 자동 재시작
    )
```

**설명:**
- `import uvicorn`: uvicorn 서버를 사용하기 위해 가져옵니다
- `if __name__ == "__main__"`: 이 파일이 직접 실행될 때만 실행됩니다
- `uvicorn.run()`: 웹 서버를 시작하는 함수입니다
- `"src.sentivest.api.app:app"`: FastAPI 앱이 있는 위치입니다
  - `src.sentivest.api.app` = 파일 경로
  - `:app` = 그 파일 안에 있는 `app` 변수
- `host="127.0.0.1"`: 로컬 컴퓨터에서만 접근 가능합니다
- `port=8000`: 8000번 포트를 사용합니다
- `reload=True`: 코드를 수정하면 자동으로 서버를 재시작합니다

### 단계 3: FastAPI 앱 찾기
```
uvicorn이 "src.sentivest.api.app:app"를 찾습니다
↓
src/sentivest/api/app.py 파일을 열고
그 안에 있는 app 변수를 찾습니다
```

### 단계 4: `app.py` 파일 분석
```python
# src/sentivest/api/app.py의 내용
from fastapi import FastAPI  # 1. FastAPI 클래스를 가져옵니다
from src.sentivest import __version__  # 2. 버전 정보를 가져옵니다

# 3. FastAPI 애플리케이션을 생성합니다
app = FastAPI(
    title="Sentivest API",
    description="AI 기반 주식 예측 및 뉴스 감정 분석 대시보드",
    version=__version__
)

# 4. "/" 경로에 GET 요청이 오면 실행될 함수
@app.get("/")
async def root():
    return {
        "message": "Hello World!",
        "version": __version__,
        "status": "running"
    }

# 5. "/health" 경로에 GET 요청이 오면 실행될 함수
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": __version__
    }
```

**설명:**
- `from fastapi import FastAPI`: FastAPI 클래스를 가져옵니다
- `app = FastAPI(...)`: FastAPI 애플리케이션을 생성합니다
- `@app.get("/")`: 데코레이터 - "/" 경로에 GET 요청이 오면 아래 함수를 실행합니다
- `async def root():`: 비동기 함수 - 요청을 처리하는 함수입니다
- `return {...}`: JSON 형식으로 응답을 보냅니다

### 단계 5: 서버 시작
```
uvicorn이 서버를 시작합니다
↓
"INFO: Uvicorn running on http://127.0.0.1:8000" 메시지가 출력됩니다
↓
서버가 요청을 기다립니다 (대기 상태)
```

### 단계 6: 요청 처리
```
1. 브라우저에서 http://127.0.0.1:8000 접속
   ↓
2. 브라우저가 서버에 "GET /" 요청을 보냅니다
   ↓
3. uvicorn이 요청을 받습니다
   ↓
4. uvicorn이 FastAPI 앱에 요청을 전달합니다
   ↓
5. FastAPI가 @app.get("/") 데코레이터를 찾습니다
   ↓
6. root() 함수를 실행합니다
   ↓
7. {"message": "Hello World!", ...}를 반환합니다
   ↓
8. uvicorn이 응답을 브라우저에 보냅니다
   ↓
9. 브라우저가 JSON을 화면에 표시합니다
```

---

## 📁 파일 구조와 역할

```
Sentivest_dev/
├── main.py                    # 서버를 시작하는 파일
├── requirements.txt            # 필요한 패키지 목록
└── src/
    └── sentivest/
        ├── __init__.py        # 버전 정보 등
        └── api/
            └── app.py         # FastAPI 애플리케이션 (API 엔드포인트 정의)
```

### 각 파일의 역할:

1. **main.py**
   - 서버를 시작하는 진입점
   - uvicorn을 실행해서 FastAPI 앱을 서버로 만듦

2. **requirements.txt**
   - 프로젝트에 필요한 패키지 목록
   - `pip install -r requirements.txt`로 설치

3. **app.py**
   - FastAPI 애플리케이션 정의
   - API 엔드포인트(URL 경로) 정의
   - 각 엔드포인트가 어떤 데이터를 반환하는지 정의

---

## 🎯 핵심 개념 정리

### 1. 데코레이터 (@app.get)
```python
@app.get("/")
async def root():
    return {"message": "Hello World!"}
```
- `@app.get("/")`: "/" 경로에 GET 요청이 오면 아래 함수를 실행
- 데코레이터는 함수를 꾸며주는 역할을 합니다

### 2. 엔드포인트 (Endpoint)
- API의 특정 경로를 의미합니다
- 예: `http://127.0.0.1:8000/` = "/" 엔드포인트
- 예: `http://127.0.0.1:8000/health` = "/health" 엔드포인트

### 3. HTTP 메서드
- GET: 데이터를 가져올 때 사용
- POST: 데이터를 보낼 때 사용
- PUT: 데이터를 수정할 때 사용
- DELETE: 데이터를 삭제할 때 사용

### 4. 비동기 (async/await)
```python
async def root():  # 비동기 함수
    return {...}
```
- 여러 요청을 동시에 처리할 수 있게 해줍니다
- 서버가 더 효율적으로 작동합니다

---

## 🧪 실습: 직접 테스트해보기

### 1. 서버 실행
```bash
python main.py
```

### 2. 브라우저에서 접속
- http://127.0.0.1:8000
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs (API 문서)

### 3. 코드 수정해보기
```python
# app.py에서 메시지 변경
@app.get("/")
async def root():
    return {
        "message": "안녕하세요!",  # "Hello World!"를 변경
        "version": __version__,
        "status": "running"
    }
```
- 저장하면 서버가 자동으로 재시작됩니다 (reload=True)
- 브라우저를 새로고침하면 변경된 메시지가 보입니다

---

## 💡 추가 학습 자료

### 다음 단계로 배울 것들:
1. POST 요청 처리하기
2. 요청 데이터 받기 (Query Parameters, Request Body)
3. 데이터베이스 연결하기
4. 에러 처리하기
5. 인증/인가 구현하기

### 유용한 리소스:
- FastAPI 공식 문서: https://fastapi.tiangolo.com/
- Uvicorn 공식 문서: https://www.uvicorn.org/

---

## ❓ 자주 묻는 질문

### Q1: 왜 uvicorn이 필요한가요?
- FastAPI는 웹 프레임워크이고, uvicorn은 웹 서버입니다
- FastAPI는 API를 정의하고, uvicorn은 실제로 서버를 실행합니다

### Q2: host="127.0.0.1"과 "0.0.0.0"의 차이는?
- `127.0.0.1`: 로컬 컴퓨터에서만 접근 가능 (보안)
- `0.0.0.0`: 다른 컴퓨터에서도 접근 가능 (배포 시 사용)

### Q3: 포트 번호는 무엇인가요?
- 포트는 컴퓨터에서 프로그램을 구분하는 번호입니다
- 웹 서버는 보통 8000번 포트를 사용합니다
- 다른 프로그램이 8000번 포트를 사용 중이면 에러가 발생합니다

### Q4: async/await는 필수인가요?
- FastAPI에서는 선택사항이지만, 성능 향상을 위해 사용하는 것을 권장합니다
- 일반 함수도 사용할 수 있습니다: `def root():`

---

## 🎓 정리

1. **main.py**가 서버를 시작합니다 (uvicorn.run)
2. **app.py**에 API 엔드포인트를 정의합니다 (@app.get)
3. 브라우저가 요청을 보내면 서버가 처리해서 응답을 보냅니다
4. uvicorn이 요청을 받아서 FastAPI에 전달하고, FastAPI가 처리합니다

이제 서버가 어떻게 작동하는지 이해하셨나요? 🚀

