from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, this is Todo App. I update automatically! Try 2."}
