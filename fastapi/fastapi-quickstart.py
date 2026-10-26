from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"name": "david", "age": 40 }

if __name__ == '__main__':
    uvicorn.run("fastapi-quickstart:app", port=8001,reload=True)