from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"Goodbye SWISS user!!"}

@app.post("/stars")
async def stars(request: Request):
    data = await request.json()
    user_input = data.get("input", "")
    return {"message": f"*****{user_input}*****"}
