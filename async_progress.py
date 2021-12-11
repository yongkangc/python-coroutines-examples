import requests
import os
import time
import asyncio  # asynchronous functions
import aiohttp  # asynchronous way to make http requests

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
SYMBOLS = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'GOOGL']
results = []

# syncrhonounsly loop

start = time.time()


def get_symbols_sync():
    for symbol in SYMBOLS:
        print('Working on symbol {}'.format(symbol))

        url = URL.format(symbol, api_key)
        response = requests.get(url)
        results.append(response.json())
    end = time.time()
    total_time = end - start
    print("It took {} seconds to make {} API calls".format(
        total_time, len(SYMBOLS)))
    print('You did it!')


# asynchrnous loop

async def get_symbols_async_1():  # the keyword async makes it a async function
    # however the request function here is still synchronous
    start = time.time()
    for symbol in SYMBOLS:
        print('Working on symbol {}'.format(symbol))

        url = URL.format(symbol, api_key)
        response = requests.get(url)
        results.append(response.json())
    end = time.time()
    total_time = end - start

    print("It took {} seconds to make {} API calls".format(
        total_time, len(SYMBOLS)))
    print('You did it!')
# asynchrnous loop


async def get_symbols_async_2():  # with asyncrhnous request function
    start = time.time()
    # session = aiohttp.ClientSession()  # session we can do a get request with
    async with aiohttp.ClientSession() as session:  # async session
        for symbol in SYMBOLS:
            print('Working on symbol {}'.format(symbol))

            url = URL.format(symbol, api_key)
            # instead of request.get, we are doing session.get()
            # example of coroutine. wait for the session to return with await
            response = await session.get(url)
            results.append(await response.json())


def get_task_1(session):
    # get all the task for the session to send the api calls all at once
    tasks = []  # list of all the functions we want to call
    for symbol in SYMBOLS:
        tasks.append(session.get(URL.format(symbol, api_key)))

    return tasks


def get_task(session):
    # get all the task for the session to send the api calls all at once
    tasks = []
    for symbol in SYMBOLS:
        tasks.append(asyncio.create_task(
            session.get(URL.format(symbol, api_key))))  # automatically add the task to the event loop

    return tasks


async def get_symbols_async():  # send all the api calls at the asame time

    async with aiohttp.ClientSession() as session:
        tasks = get_task(session)

        # star references the list of tasks
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


# creationg an event loop to check when aasync is done
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols_async())
# loop.close()

# same approach as above but abstracted
asyncio.run(get_symbols_async())
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(
    total_time, len(SYMBOLS)))
print('You did it!')
