```python
import asyncio

from polygon import WebSocketClient

from polygon.websocket.models import WebSocketMessage, CryptoTrade

from typing import List

from polygon import RESTClient

import aioconsole

import pandas as pd

import ast

  

from TrendAnalysis import process_trade

  

API_KEY = "s2zC3SQEf3MgBQzTygqvYc9QfLNI_ABq"

  

ws = WebSocketClient(api_key=API_KEY,market="crypto",subscriptions=["XAS.BTC-USD"])

stop_event = asyncio.Event()

  

#client = RESTClient(api_key=API_KEY)

#client.get_snapshot_crypto_book(ticker="BTC-USD")

  

print("Trading will Comense Now")

  

# Function to handle incoming messages

async def handle_msg(msg: List[WebSocketMessage]):

    for m in msg:

        m_dict = m.__dict__

        await process_trade(m_dict)

  

async def wait_for_enter():

    # Wait for the user to press Enter

    await aioconsole.ainput("Press Enter to stop the WebSocket: ")

    stop_event.set()

  

async def Reporting():

    with open('data.txt', 'r') as file:

        content = file.read()

    Dict_list = ast.literal_eval(content)

    df = pd.DataFrame(Dict_list)

  

    print(df.info())

    print(df.head())

  

# Function to run the WebSocket client

async def run_ws():

    while not stop_event.is_set():

        await ws.connect(processor=handle_msg)

    try:

        while not stop_event.is_set():

            await asyncio.sleep(.00000001)  # Yield control back to the event loop

    finally:

        await ws.close()

        print("WebSocket stopped.")

  

# Main function to run the event loop

async def main():

    ws_task = asyncio.create_task(run_ws())

    enter_task = asyncio.create_task(wait_for_enter())

  

    await enter_task

    stop_event.set()

    await ws_task

  

    # Run the reporting coroutine

    await Reporting()

  

    '''

    Previous Attempt

    await asyncio.gather(

        run_ws()

    )

    '''

  
  

# Standard boilerplate to run the main function

if __name__ == "__main__":

    asyncio.run(main())
```