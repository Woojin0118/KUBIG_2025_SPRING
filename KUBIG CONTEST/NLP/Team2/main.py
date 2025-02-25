from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from search import search_title
from model import generate_explanation
from db import vectordb

app = FastAPI()
app.mount("/static", StaticFiles(directory="dist", html=True), name="static")

class SearchRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def read_main():
    with open("dist/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/search")
async def search(data: SearchRequest):
    query = data.query
    results = search_title(query, top_k=3)

    if not results:
        return {"result": f"'{query}'에 대한 검색 결과를 찾을 수 없습니다."}

    final_explanation = generate_explanation(query, results)
    return {"result": final_explanation}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
