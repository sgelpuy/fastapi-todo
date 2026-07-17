# FastAPI To-Do API

FastAPI로 만든 할 일(To-Do) 관리 REST API. Docker로 AWS Lightsail에 배포.

## 기술 스택
- FastAPI / Uvicorn / Pydantic
- Docker (python:3.11-slim)
- AWS Lightsail (Ubuntu 22.04)

## 로컬 실행
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
브라우저: http://127.0.0.1:8000/docs

## Docker 실행
```
docker build -t todo-api:1.0 .
docker run -d --name todo-api -p 8000:8000 todo-api:1.0
```

## 작성자
jsyang9455
