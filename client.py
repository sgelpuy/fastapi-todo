import requests

# API 서버 주소 (로컬에서 실행 중인 FastAPI)
BASE = "http://127.0.0.1:8000"

# 1) 전체 목록 조회 (GET) - 응답 JSON을 파이썬 딕셔너리로 변환
res = requests.get(f"{BASE}/todos")
print("상태코드:", res.status_code)
data = res.json()                 # JSON 문자열 -> 파이썬 딕셔너리
print("할 일 개수:", data["count"])
for todo in data["todos"]:
    mark = "완료" if todo["done"] else "진행중"
    print(f"  - [{todo['id']}] {todo['title']} ({mark})")

# 2) 새 할 일 추가 (POST) - 파이썬 딕셔너리를 JSON으로 전송
new_item = {"title": "requests로 API 호출하기", "done": False}
res = requests.post(f"{BASE}/todos", json=new_item)
print("\n추가 결과(JSON):", res.json())

# 3) 방금 추가한 항목 단건 조회 (GET + 경로 파라미터)
new_id = res.json()["id"]
res = requests.get(f"{BASE}/todos/{new_id}")
print("단건 조회:", res.json())

# 4) 검색 (GET + 쿼리 파라미터)
res = requests.get(f"{BASE}/search", params={"keyword": "API"})
print("검색 결과 개수:", len(res.json()["result"]))
