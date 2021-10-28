
import asyncio
import time

def say(what):
    print(what)

async def say_after(delay, what):
    say(what)
    await asyncio.sleep(delay)
    return 'ending'

async def main():
    start=time.time()
    tasks=[]
    for _ in range(100):
        task = asyncio.create_task(
            say_after(2, 'starting'))
        tasks.append(task)

        print(task)
    # for task in tasks:
        # some=await task
        # print(some)
    some=await asyncio.gather(*tasks, return_exceptions=True)
    print(some)
    print('duration->',time.time()-start)
    return 'Done'