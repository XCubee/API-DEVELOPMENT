from fastapi import FastAPI
from fastapi.params import Body 

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

@app.post("/post")
def addingpost(payload dict = Body(...)):
    return{
        "Respiration Ekg A of : Person1 "
        "Respiration Ekg A of : Person2 "
    }