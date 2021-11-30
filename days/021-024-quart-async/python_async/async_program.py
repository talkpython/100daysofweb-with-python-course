import datetime
import colorama
import random
import asyncio


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)

    # Changed from asyncio.get_event_loop() => asyncio.new_event_loop()
    # There has been a deprecation:
    # DeprecationWarning: There is no current event loop.
    loop = asyncio.new_event_loop()
    data = asyncio.Queue()

    task1 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(generate_data(20, data))
    # task4 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(process_data(40, data))

    final_task = asyncio.gather(task1, task2, task3)
    loop.run_until_complete(final_task)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx*idx
        await data.put((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get()

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()
