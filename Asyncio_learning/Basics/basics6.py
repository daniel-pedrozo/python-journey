import asyncio

#A shared variable
shared_resource = 0

#An asyncio look
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        #cretical section starts
        print(f"Resource before modification {shared_resource}")
        shared_resource += 1 #modifying
        await asyncio.sleep(1)
        print(f"REspurce after modification: {shared_resource}")

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())