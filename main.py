








from fastapi import FastAPI
from pydantic import BaseModel
from schemas import Candidate
from typing import List
import asyncio

app = FastAPI()

saved = []

junior= []


@app.get("/")
def read_root():
    return "Welcome to the root page"

@app.get("/item/{item_id}")
def read_root(item_id):
    return {"item_id": "Lawrence so banana", "status": "Maro padle Hahhah"}

@app.post("/inventory")
def inventory(masala: int)->dict:

    saved.append(masala)
    print(saved)
    return {"saved":"masala"}

@app.post("/screen-candidate/")
async def resume_review(candidate: Candidate)-> dict:
    stack_lower= [skill.lower() for skill in candidate.tech_stack]
    if candidate.visa_sponsorship_needed == True:
        return {"Rejected":"We cannot offer sponsorship at this time"}

    elif candidate.years_experience < 3:
        junior.append(candidate.name)
        return {"Junior":"Added to junior talent pool"}

    elif "python" not in stack_lower:
        return {"Rejected":"Python is required for this role"}

    else:
        return {"Accepted":"Welcome to the interview round!"}
