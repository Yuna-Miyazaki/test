from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>My First Deploy</title>
        </head>
        <body>
            <h1>Hello, Hackathon!</h1>
            <p>PythonアプリをRenderで公開できました。</p>
        </body>
    </html>
    """

@app.get("/api")
def api():
    return {"message": "これはPythonで作ったAPIです"}