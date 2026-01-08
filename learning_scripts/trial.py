from fastapi import FastAPI
import asyncio

app = FastAPI()

# This is a standard route
@app.get("/")
def read_root():
    return {"Hello": "World"}

# This is the "Async" route you brag about on your resume
@app.get("/heavy-task")
async def heavy_task():
    # Simulate a slow database call (3 seconds)
    # Because we use 'await', the server isn't frozen! It can still answer other users.
    await asyncio.sleep(3)
    return {"status": "Task Complete", "message": "I didn't block the server!"}
