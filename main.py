from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body 
from pydantic import BaseModel

app=FastAPI()
@app.get("/")
def root():
    return{"message":"Hello There"}

@app.get("/saksham")
def getrequest():
    return "Hello World"


@app.post("/createposts")
def createpost(payload:dict= Body(...)):
    print(payload)
    return {
    "new_message": f"title: {payload['saksham']}",
    "message": payload["amity"]
}

@app.get("/addpost")
def addpost(payload:dict = Body(...)):
    return {
        "The text would include a sample case for the  data provided "
    }


#----------------------------------------------------------------
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    rating: Optional[int]=None
    

@app.post("/new")
def addingpost(new_post:Post):
    return{new_post.title}


