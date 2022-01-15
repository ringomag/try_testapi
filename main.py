from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def index():
    return {"data":{"name":"optimus prime", "race":"autobots"}}

@app.get("/about")
def about():
    return {"data":"about optimus prime"}