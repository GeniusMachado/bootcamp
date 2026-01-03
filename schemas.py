from typing import Optional
from sqlmodel import SQLModel, Field


class Candidate(SQLModel, table=True):
    id: Optional[int]= Field(default=None, primary_key=True)
    name: str
    years_experience: int
    tech_stack: str
    visa_sponsorship_needed: bool
