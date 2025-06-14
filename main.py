from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()

class loginData(BaseModel):
    email: str
    password: str


@app.get("/")
def first():
    return {"message: hello its working"}

@app.post("/login")
async def login(data: loginData): 
    return data
