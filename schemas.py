from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    years_experience: int
    tech_stack: list[str]
    visa_sponsorship_needed: bool
