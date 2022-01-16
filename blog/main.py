from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db) ):
    new_post =models.Post(
        title=request.title, 
        body=request.body
        )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/blog")
def get_all(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_one_post(id: int, response: Response, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        # response.status_code=status.HTTP_404_NOT_FOUND 
        # return {"detail":f"post with id {id} does not exist"}
        # or with HTTPException
        raise HTTPException(status_code=404, detail=f"There is no id {id}")
    return post