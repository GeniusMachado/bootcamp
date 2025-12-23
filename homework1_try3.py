import random
import asyncio 
from typing import List, Any, Dict

def create_dirty_data() -> List[Dict[str, Any]]:
	Dirty_Names = ["John", " allahkoH", "   KJDSGHGH", "dshtht  flert", "jdhLHGjosrg "]
	users = []
	for i in range(100):
		dirty_data = { "name": random.choice(Dirty_Names),
				"age":str(random.randint(10,99)),
				"email":"USER@GMAIL.COM"}
		users.append(dirty_data)
	
	return users


def clean_data(dirty_data: Dict[str, Any]) -> Dict[str, Any]:
    try:
        clean_age = int(dirty_data["age"])
    except ValueError:
        clean_age = 0
    return {
        "name": dirty_data["name"].strip().title(),
        "age": clean_age,  # Use the variable here
        "email": dirty_data["email"].lower()
    }

async def save_to_database(users: List[Dict[str, Any]]):
	print(f"starting to save for the length of {len(users)} users...")
	
	for user in users:
		await asyncio.sleep(0.01)
	
	print("saved everything to database successfully")


async def main():
	raw_data = create_dirty_data()
	cleaned_data = [clean_data(user) for user in raw_data]

	adults=[user for user in cleaned_data if user["age"]>=18]
	
	print(f"original count {len(raw_data)}")
	print(f"adult count {len(adults)}")
	
	await save_to_database(adults)

if         __name__ == "__main__":
	asyncio.run(main())
