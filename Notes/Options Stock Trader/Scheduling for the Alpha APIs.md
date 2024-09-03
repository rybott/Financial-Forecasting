```python
import asyncio
import aiohttp
import datetime

async def call_first_api(session):
    while True:
        # Call the first API
        async with session.get('https://first-api-url.com') as response:
            data = await response.json()
            print("Called first API:", data)
            await analyze_data_from_first_api(data)
        # Sleep for 1 second before the next call, yielding control to the event loop
        await asyncio.sleep(1)

async def call_second_api(session):
    while True:
        now = datetime.datetime.now()
        wait_time = 60 - now.second  # Calculate time to wait until the start of the next minute
        await asyncio.sleep(wait_time)
        # Call the second API
        async with session.get('https://second-api-url.com') as response:
            data = await response.json()
            print("Called second API:", data)
            await analyze_data_from_second_api(data)
        # Sleep until the start of the next minute, yielding control to the event loop
        await asyncio.sleep(60 - datetime.datetime.now().second)

async def analyze_data_from_first_api(data):
    # Add your data analysis code here
    print("Analyzed data from first API:", data)

async def analyze_data_from_second_api(data):
    # Add your data analysis code here
    print("Analyzed data from second API:", data)

async def main():
    async with aiohttp.ClientSession() as session:
        first_api_task = asyncio.create_task(call_first_api(session))
        second_api_task = asyncio.create_task(call_second_api(session))
        # Run both tasks concurrently
        await asyncio.gather(first_api_task, second_api_task)

# Run the main function
asyncio.run(main())

```