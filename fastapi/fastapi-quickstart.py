from fastapi import FastAPI
import uvicorn
from typing import Union
from pydantic import BaseModel
from datetime import date
from typing import List

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    birth: date
    friends: List[int]

@app.post("/data", tags=["演示request body"])
def data(data:User):
    print(data, type(data))
    return {}

@app.post("/jobs/{id}", tags=["职位id"],
          summary="{id} 职位的详细信息",
          description="描述",
          response_description="返回的描述")
def j(id, kd, xl, gj:Union[str, None]=None, xb=None):
    #基于关键词、学历、工作经验三个关键词去查询数据库...
    return {"jobs": id,
            "关键词": kd,   #keyword
            "学历": xl,
            "工作经验": gj,
            "性别": xb }

@app.post("/user/{id}", tags=["用户id"],
          summary="{id} 用户的详细信息",
          description="描述",
          response_description="返回的描述")
def u(id):
    return {"user": id }

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