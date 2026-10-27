from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/orm")
def orm():
    return("orm")

if __name__ == "__main__":
    uvicorn.run("orm-quick:app", port=8001, reload=True)