from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field

import uvicorn

app = FastAPI()

class Person(BaseModel):
    name : str = Field(None, title="Name of Person", max_length=20)
    age : int = Field(None, title="Age of Person")
    salary: float = Field(None, title="Monthly Salary in Rupees")


@app.get("/")
async def default_get():
    return "Hello World!"

@app.get("/hello/{name}/{age}")         # ... -> Default
async def parm_check(name : str = Path(..., min_length=2, max_length=20),
            age : int = Path(..., gt=0, lt=100)):
    return {"name": name, "age" : age}

@app.post("/person/")
async def post_method(person : Person):
    return {"name" : person.name, "details" : 
            {"age" : person.age, "salary" : person.salary}}

@app.post("/person2/")
async def post_method2(name : str = Body(..., min_length=2, max_length=20),
            age : int = Body(..., gt=0, lt=100),
            salary : float = Body(..., gt=10000, lt=1000000)):
    return {"name" : name, "details" : {"age" : age, "salary" : salary}}



if __name__ == "__main__":
   uvicorn.run("path_parm:app", host="127.0.0.1", port=8000, reload=True)