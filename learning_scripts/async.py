import asyncio

async def fetch():
 print("start fetching data:")
 await asyncio.sleep(3)
 print("data fetched")
 return {"name":"Genesis"}

async def main():
 print("this is the main function")
 result = await fetch()
 print(result)

asyncio.run(main())
