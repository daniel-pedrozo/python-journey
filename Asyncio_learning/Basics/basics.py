import asyncio

"""Event loop = a loop that manage the tasks to make a code run fluid"""

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # simulating an I/O operation with a sleep
    print("Data fetched")
    return {"data": "some data"} # returning some data 


# Define another coroutine that calls the firts coroutine
async def main():
    print("Start, of main coroutine")
    task = fetch_data(2)
    #Await the fech_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f"Received result : {result}")
    print("End of main coroutine")

#I cant call only the function
#main()
#Function that have asyn upfront cant be called normaly 

# Run the async function
asyncio.run(main())
