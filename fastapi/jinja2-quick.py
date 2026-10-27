from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")  #模版目录

@app.get("/index")
def index(request: Request):
    name = "root"
    return(templates.TemplateResponse(
        "index.html",   #模版文件
        {   #上下文对象-- 字典
            "request": request,
            "user": name
        }
    ))

if __name__ == "__main__":
    uvicorn.run("jinja2-quick:app", port=8001, reload=True)
