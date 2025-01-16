import asyncio

""" 
    The asyncio.gather is a quick way to concurrently run multiple coroutines
    You dont need to create separete task like on 'basics2.py'               
    The gather() is not good with error randiling!                           
"""

async def fetch_data(id,sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Run coroutines concurrently and gather their return value
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    #Process the result
    for result in results:
        print(f"Received result: {result}")


asyncio.run(main()) 