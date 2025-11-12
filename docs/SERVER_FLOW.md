# 서버 실행 흐름 (시각적 설명)

## 🔄 전체 흐름도

```
1. 사용자가 터미널에서 실행
   python main.py
   ↓
2. Python이 main.py를 읽음
   ↓
3. uvicorn.run()이 실행됨
   ↓
4. uvicorn이 "src.sentivest.api.app:app"을 찾음
   ↓
5. app.py 파일을 열고 app 변수를 찾음
   ↓
6. FastAPI 애플리케이션이 로드됨
   ↓
7. 서버가 시작됨 (포트 8000에서 대기)
   ↓
8. "INFO: Uvicorn running on http://127.0.0.1:8000" 출력
   ↓
9. 서버가 요청을 기다림 (대기 상태)
```

## 🌐 요청 처리 흐름

```
브라우저: http://127.0.0.1:8000 접속
   ↓
브라우저가 서버에 "GET /" 요청을 보냄
   ↓
uvicorn이 요청을 받음
   ↓
uvicorn이 FastAPI 앱에 요청을 전달함
   ↓
FastAPI가 @app.get("/") 데코레이터를 찾음
   ↓
root() 함수를 실행함
   ↓
{"message": "Hello World!", ...}를 반환함
   ↓
uvicorn이 응답을 브라우저에 보냄
   ↓
브라우저가 JSON을 화면에 표시함
```

## 📊 단계별 상세 설명

### 단계 1: 서버 시작
```
python main.py
→ Python 인터프리터가 main.py를 실행
→ import uvicorn (uvicorn 라이브러리를 가져옴)
→ if __name__ == "__main__": 조건이 True이므로 실행
→ uvicorn.run() 함수 호출
```

### 단계 2: FastAPI 앱 로드
```
uvicorn.run("src.sentivest.api.app:app", ...)
→ uvicorn이 "src.sentivest.api.app:app"를 파싱
→ "src.sentivest.api.app" = 파일 경로
→ ":app" = 그 파일 안에 있는 app 변수
→ Python이 src/sentivest/api/app.py 파일을 열음
→ app 변수를 찾음 (FastAPI 인스턴스)
```

### 단계 3: 서버 시작
```
uvicorn이 서버를 시작함
→ host="127.0.0.1", port=8000으로 서버 시작
→ 소켓을 열고 요청을 기다림
→ "INFO: Uvicorn running on http://127.0.0.1:8000" 출력
```

### 단계 4: 요청 처리 (예: 브라우저에서 접속)
```
브라우저: http://127.0.0.1:8000 접속
→ 브라우저가 HTTP 요청을 보냄
  GET / HTTP/1.1
  Host: 127.0.0.1:8000
→ uvicorn이 요청을 받음
→ FastAPI 앱에 요청을 전달함
→ FastAPI가 라우터에서 @app.get("/")를 찾음
→ root() 함수를 실행함
→ {"message": "Hello World!", ...} 반환
→ uvicorn이 HTTP 응답을 만듦
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"message": "Hello World!", ...}
→ 브라우저가 응답을 받음
→ 브라우저가 JSON을 화면에 표시함
```

## 🔍 코드 실행 순서

### 1. main.py 실행
```python
import uvicorn  # 1. uvicorn 라이브러리 가져오기
if __name__ == "__main__":  # 2. 이 파일이 직접 실행될 때만
    uvicorn.run(...)  # 3. 서버 시작
```

### 2. app.py 로드
```python
from fastapi import FastAPI  # 1. FastAPI 가져오기
app = FastAPI(...)  # 2. FastAPI 앱 생성
@app.get("/")  # 3. "/" 경로에 GET 요청 처리
async def root():  # 4. 요청 처리 함수
    return {...}  # 5. 응답 반환
```

### 3. 요청 처리
```python
# 브라우저가 "GET /" 요청을 보냄
# ↓
# FastAPI가 @app.get("/")를 찾음
# ↓
# root() 함수 실행
# ↓
# {"message": "Hello World!", ...} 반환
```

## 🎯 핵심 포인트

1. **uvicorn**: 웹 서버 (요청을 받고 응답을 보냄)
2. **FastAPI**: 웹 프레임워크 (API를 정의함)
3. **데코레이터 (@app.get)**: 어떤 경로에 어떤 함수를 실행할지 정의
4. **비동기 (async)**: 여러 요청을 동시에 처리할 수 있게 함

## 💡 비유로 이해하기

- **uvicorn** = 식당의 주방 (요리를 만드는 곳)
- **FastAPI** = 메뉴판 (어떤 요리를 만들지 정의)
- **데코레이터 (@app.get)** = 주문표 (어떤 요리를 주문하면 어떤 요리를 만들지)
- **함수 (root)** = 요리사 (실제로 요리를 만드는 사람)
- **브라우저** = 손님 (주문을 하고 요리를 받음)

손님이 주문 → 주방이 주문을 받음 → 메뉴판을 확인 → 요리사가 요리 → 주방이 손님에게 서빙

## 🧪 직접 실험해보기

### 실험 1: 다른 경로 추가
```python
@app.get("/test")
async def test():
    return {"message": "테스트입니다!"}
```
→ http://127.0.0.1:8000/test 접속하면 "테스트입니다!"가 표시됨

### 실험 2: 메시지 변경
```python
@app.get("/")
async def root():
    return {
        "message": "안녕하세요!",  # 변경
        "version": __version__,
        "status": "running"
    }
```
→ 저장하면 서버가 자동으로 재시작됨 (reload=True)
→ 브라우저를 새로고침하면 변경된 메시지가 보임

### 실험 3: POST 요청 추가
```python
@app.post("/data")
async def create_data():
    return {"message": "데이터를 생성했습니다!"}
```
→ POST 요청으로 데이터를 보낼 수 있음

