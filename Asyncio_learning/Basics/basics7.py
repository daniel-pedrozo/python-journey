import asyncio

"""
    the Semaphore() allows multiple coroutines to have acces to the same object at the same time
    used to not overload the runing of the code
"""

async def access_resource(semaphore, resource_id):
    async with semaphore:
        #simulate accessing a limited resource
        print(f"Acessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f"Releasing resource {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2) #Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())