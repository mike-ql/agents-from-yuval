
import asyncio

async def say(what, when):
    loop = asyncio.get_event_loop()
    print("Inside async func, event loop: ", loop)
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()
print(loop)
loop.run_until_complete(say('hello world', 1))
loop.close()