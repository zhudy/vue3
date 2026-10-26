from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/test", tags=["路径装饰器带参数的接口"],
          summary="总结",
          description="描述",
          response_description="返回的描述")
def t():
    return {"method": "post" }

@app.get("/get")
def g():
    return {"method": "get" }

@app.post("/post")
def p():
    return {"method": "post" }

@app.put("/put")
def pu():
    return {"method": "put" }

@app.delete("/delete")
def d():
    return {"method": "delete" }

if __name__ == '__main__':
    uvicorn.run("fastapi-quickstart:app", port=8001,reload=True)