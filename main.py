from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


class Post(BaseModel):
    title: str
    body: str
    published: Optional[bool]=False


app=FastAPI()


@app.get("/blog")
def index(limit=10, published=True, sort: Optional[str]=None):
    #get only 10 published blogs
    if published:
        return {"data": f"{limit} blogs from list"}
    else:
        return {"data":f"No published posts"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def about(id: int):
    return {"data":id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data":["1","2","3"]}

@app.post("/blog")
def create_post(post_data: Post):
    return {"data":post_data}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=8000)
