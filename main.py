import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# HTMLテンプレートが置かれているフォルダを指定
templates = Jinja2Templates(directory="templates")


# 1. 画面を表示するルーティング（ブラウザでアクセス）
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # index.htmlに渡したいデータを辞書型で指定
    context = {
        "request": request,
        "title": "FastAPI ✕ Tailwind サンプル",
        "message": "Renderへようこそ！",
    }
    return templates.TemplateResponse("index.html", context)


# 2. APIエンドポイント（データをJSON形式で返す）
@app.get("/api/info")
async def get_info():
    return {
        "status": "success",
        "framework": "FastAPI",
        "css": "Tailwind CSS",
        "note": "APIも同じ main.py で動いています",
    }


# ローカル環境でのテスト用（python main.py で起動可能にする）
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
