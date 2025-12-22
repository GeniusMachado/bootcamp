import random
def create_list():
	#creates a list of 100 dirty user dictionaries with their name and age and email
	keys=[1,2,3]
	for i in range(0,99):
    		temp = random.randint(1,107)
    		keys.append(temp)
	lower_limit = 2
	upper_limit = 798
	random_dict = {key: random.randint(lower_limit, upper_limit) for key in keys}
	print(random_dict)

def clean_list():
	#make sure this function cleans the list of dictionary using type hinting(trims spaces, lowercase email and converts age into int""
 pass

def save_to_database():
	#make it async with await asyncio.sleep(0,1) for each record

	#make sure to use a list comprehension YIELD to filter out users under age 1

 pass

create_list()
