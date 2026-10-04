from datetime import datetime

import asyncio, time

def wait_time(delay : int = 30):
    time.sleep(delay)      # Wait for 30 sedonds
    return

print(f"Start Time -> {datetime.now().time()}")
wait_time(2)
print(f"End Time -> {datetime.now().time()}")


async def async_wait_time(delay: int = 30):
    print(f"Waiting for {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Wait complete")
"""
print(f"Start Time -> {datetime.now().time()}")
async_wait_time(5)
print(f"End Time -> {datetime.now().time()}")


print(f"Start Time -> {datetime.now().time()}")
asyncio.run(async_wait_time(5))
print(f"End Time -> {datetime.now().time()}")
"""
async def main():
    print(f"Start Time -> {datetime.now().time()}")
    task = asyncio.create_task(async_wait_time(1))
    print(f"End Time -> {datetime.now().time()}")
    await asyncio.sleep(2)
    print("Where are we now")
    await task      # stops further process till task is complete
    

#asyncio.run(main())

async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.15)
    return "Done"

async def fetch_data() -> dict[str, str]:
    dicti = {"name" : "Anand"}
    print(dicti)
    await asyncio.sleep(0.25)
    dicti.update({"location" : "Chennai"})
    print(dicti)
    await asyncio.sleep(0.25)
    dicti.update({"age" : "Confidential"})
    print(dicti)
    await asyncio.sleep(0.25)
    return dicti

async def main2():
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(fetch_data())

    val1 = await task1
    val2 = await task2
    print(val1)
    print(val2)

asyncio.run(main2())