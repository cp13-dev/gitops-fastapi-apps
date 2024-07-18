from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def hello_world(request: Request):
    data = await request.json()
    user_input = data.get("input", "")
    return {"message": f"Goodbye!! {user_input}"}
