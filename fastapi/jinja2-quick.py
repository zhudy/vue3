from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")  #模版目录

@app.get("/index")
def index(request: Request):
    name = "root"
    books = ["西游记","红楼梦","三国演义","水浒传"]
    info = {"name": "张三", "age": 32, "gender": "female"}
    pi = 3.1415926
    #以上是业务逻辑层，以下是页面展示层
    return(templates.TemplateResponse(
        "index.html",   #模版文件
        {   #上下文对象-- 字典
            "request": request,
            "user": name,
            "books": books,
            "info": info,
            "pi": pi
        }
    ))

if __name__ == "__main__":
    uvicorn.run("jinja2-quick:app", port=8001, reload=True)
