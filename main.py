from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Hello world"}}


@app.get("/about")
def about():
    return {"data": "about page"}
