import asyncio
import random
from typing import List, Dict, Any # Standard "Senior" imports for Type Hinting

# 1. DATA GENERATION (Simulating "Dirty" Data)
# Returns a List of Dictionaries. 
# "Any" means the values can be strings, ints, etc.
def create_dirty_data() -> List[Dict[str, Any]]:
    dirty_users = []
    names = ["  john ", "ALICE", "  boB", "Eve  "]
    
    for _ in range(100):
        # We create 100 random users with "messy" data
        user = {
            "name": random.choice(names),     # Needs trimming
            "age": str(random.randint(10, 80)), # Wrong type (String instead of Int)
            "email": "USER@GMAIL.COM"         # Wrong casing (Uppercase)
        }
        dirty_users.append(user)
    
    return dirty_users

# 2. THE CLEANING FUNCTION (Type Hinting & Logic)
# Takes a single dirty dict, returns a clean dict
def clean_user_record(user: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": user["name"].strip().title(), # "  john " -> "John"
        "age": int(user["age"]),              # "25" -> 25 (Integer)
        "email": user["email"].lower()        # "USER@..." -> "user@..."
    }

# 3. ASYNC DATABASE SAVE (The "FastAPI" Skill)
# This mimics saving to a database which takes time
async def save_batch_to_db(users: List[Dict[str, Any]]):
    print(f"Starting save for {len(users)} users...")
    
    for user in users:
        # This is the MAGIC line. 
        # await allows the CPU to do other things while "waiting" for the DB.
        await asyncio.sleep(0.01) 
    
    print("Database save complete!")

# 4. ORCHESTRATION (Putting it together)
async def main():
    # Step 1: Get data
    raw_data = create_dirty_data()
    
    # Step 2: Clean data using List Comprehension (Very Pythonic)
    # logic: [ function(item) for item in list ]
    cleaned_data = [clean_user_record(user) for user in raw_data]
    
    # Step 3: Filter logic (List Comprehension with IF)
    # We only want adults (age >= 18)
    valid_users = [u for u in cleaned_data if u["age"] >= 18]
    
    print(f"Original count: {len(raw_data)}")
    print(f"Valid Adult count: {len(valid_users)}")
    
    # Step 4: Async Save
    await save_batch_to_db(valid_users)

# Run the async program
if __name__ == "__main__":
    asyncio.run(main())
