"""
Sentivest 메인 실행 파일
FastAPI 서버 실행
"""
import uvicorn

if __name__ == "__main__":
    # FastAPI 서버 실행
    # host="0.0.0.0"은 모든 네트워크 인터페이스에서 접근 가능
    # host="127.0.0.1"은 로컬에서만 접근 가능 (기본값)
    uvicorn.run(
        "src.sentivest.api.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True  # 코드 변경 시 자동 재시작
    )

