"""
Async snippet demonstrating the usage of async.sleep()
"""

import asyncio
import time
from datetime import datetime


async def custom_sleep():
    """ sleeps for 1 second """
    print(f"SLEEP {datetime.now()}")
    await asyncio.sleep(1)


async def factorial(name, number):
    """ calculates factorial """
    fact = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})")
        await custom_sleep()
        fact *= i
    print(f"Task {name}: Factorial({number}) is {fact}")


start = time.time()
loop = asyncio.get_event_loop()


tasks = [
    asyncio.ensure_future(factorial("A", 2)),
    asyncio.ensure_future(factorial("B", 4))
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f"Total time: {end - start}")
