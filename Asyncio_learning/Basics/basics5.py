import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    #set the result of the future
    future.set_result(value)
    print(f"Set the future result to: {value}")


async def main():
    #Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    #schedule setting the future result
    asyncio.create_task(set_future_result(future, "future result is redy"))

    #wait for the future result 
    result = await future
    print(f"Received the future result: {result}")


asyncio.run(main())