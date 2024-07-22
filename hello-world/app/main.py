from fastapi import FastAPI
from pydantic import Field, BaseModel

class UserRequest(BaseModel):
    user_input: str = Field(
        title="User input",
        description="Here goes the user input"
    )

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello SWISS user!!"}

@app.post("/stars")
async def stars(request: UserRequest):
    data = await request.json()
    user_input = data.get("input", "")
    return {"message": f"*****{user_input}*****"}
