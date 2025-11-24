from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello krupa am from your Python API with Docker & CI/CD!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
