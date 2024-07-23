import os
import json
import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from pydantic import Field, BaseModel


app = FastAPI()
security = HTTPBasic()

class UserRequest(BaseModel):
    user_input: str = Field(
        title="User input",
        description="Here goes the user input"
    )

def authenticate(credentias: HTTPBasicCredentials=Depends(security)):
    correct_username = secrets.compare_digest(credentias.username, os.getenv("BASIC_AUTH_USERNAME"))
    correct_password = secrets.compare_digest(credentias.password, os.getenv("BASIC_AUTH_PASSWORD"))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )

@app.get("/")
def root():
    return {"Hello SWISS user!!"}

@app.post("/stars", dependencies=[Depends(authenticate)])
def stars(request: UserRequest):
    data = json.loads(request.json())
    user_input = data.get("user_input", "")
    return {"message": "HELLO WORLD:" f"*****{user_input}*****"}
