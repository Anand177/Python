from datetime import datetime
from fastapi import FastAPI

import uvicorn

fast = FastAPI()

#C:\Learning\AI\agents>uv run fastapi dev ..\..\Python\Python\FastAPI\simple.py

@fast.get("/")
async def index():
    return "Hello World"

@fast.get("/v1/get")
async def get_time():
    return {"time" : f"{datetime.now().time()}"}

@fast.get("/v1/name/{name}")
async def print_name(name : str):
    return f"Hello {name}"

#http://127.0.0.1:8000/v1/hello/?name=Anand&age=38

@fast.get("/v1/hello/")
async def print_name(name : str, age: int):
    return {"name" : name, "age" : age}


if __name__ == "__main__":
   uvicorn.run("simple:fast", host="127.0.0.1", port=8000, reload=True)