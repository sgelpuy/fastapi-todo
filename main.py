from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI 앱 생성 (title/version은 자동 문서에 표시됨)
app = FastAPI(title="할 일 관리 API", version="1.0")

# 메모리에 저장하는 할 일 목록 (실제 서비스는 데이터베이스 사용)
todos = [
    {"id": 1, "title": "FastAPI 배우기", "done": False},
    {"id": 2, "title": "API 서버 만들기", "done": False},
]


# 요청 본문(JSON) 구조 정의 - 클라이언트가 보내는 데이터의 형태
class TodoIn(BaseModel):
    title: str
    done: bool = False


# [GET] 기본 경로 - 서버가 살아있는지 확인
@app.get("/")
def read_root():
    return {"message": "할 일 관리 API에 오신 것을 환영합니다"}


# [GET] 전체 목록 조회
@app.get("/todos")
def get_todos():
    return {"count": len(todos), "todos": todos}


# [GET] 검색 - 쿼리 파라미터 (예: /search?keyword=API)
@app.get("/search")
def search_todos(keyword: str = ""):
    result = [t for t in todos if keyword in t["title"]]
    return {"keyword": keyword, "result": result}


# [GET] 단건 조회 - 경로 파라미터 (예: /todos/1)
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다")


# [POST] 새 할 일 추가 - 요청 본문(JSON) 사용
@app.post("/todos")
def create_todo(todo: TodoIn):
    new_id = (max(t["id"] for t in todos) + 1) if todos else 1
    new_todo = {"id": new_id, "title": todo.title, "done": todo.done}
    todos.append(new_todo)
    return new_todo


# [PUT] 할 일 수정
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoIn):
    for t in todos:
        if t["id"] == todo_id:
            t["title"] = todo.title
            t["done"] = todo.done
            return t
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다")


# [DELETE] 할 일 삭제
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            deleted = todos.pop(i)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다")
