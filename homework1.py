import random
import asyncio
def create_list():
	#creates a list of 100 dirty user dictionaries with their name and age and email
	keys=[1,2,3]
	for i in range(99):
    		temp = random.randint(1,107)
    		keys.append(temp)
	lower_limit = 2
	upper_limit = 798
	random_dict = {key: random.randint(lower_limit, upper_limit) for key in keys}
	print(random_dict)

async def clean_list(random_dict: dict) -> dict:
	#make sure this function cleans the list of dictionary using type hinting(trims spaces, lowercase email and converts age into int""
	

async def save_to_database():
	#make it async with await asyncio.sleep(0,1) for each record
	await asyncio.sleep(3)
		print("writing to database")
	#make sure to use a list comprehension YIELD to filter out users under age 1

	

create_list():
	yield random_dict
