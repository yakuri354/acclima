from asyncio import create_task

task_set = set()

async def with_finish(t):
    await t
    task_set.remove(t)

def spawn_task(t):
    task_set.add(t)
    create_task(with_finish(t))