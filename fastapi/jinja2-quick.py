from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/index")
def index():
    name = "root"
    return({"name": name})

if __name__ == "__main__":
    uvicorn.run("jinja2-quick:app", port=8001, reload=True)
