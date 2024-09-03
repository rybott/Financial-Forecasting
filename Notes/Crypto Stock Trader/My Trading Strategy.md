## Step 1 - Actual Trade [DEPRECATED]
- Keep a very tight Stop loss Order, so that as soon as the price decreases even a little we sell right away
- **Reason:**
	- Because we have such high volumes, small losses or gains add up, we don't need lots of return per trade if we can make 10,000 trades a day
	- We don't want to have to worry about past trades, that will add more complexity, we can make 10,000 trades a day because we aren't look at 10,000 trades at once, just the long/short signals, nothing else.

## Step 1 - Trading Logic
### Current Entry Strategy
- If the Price and VWAP increase for X conecutive candles, you Buy, Very Simple

### Current Exit Strategy
1. Making an Order
	- **Call the API for the Last Order**
     		- Call the API For the Last Order
   		- Can you Call for just the last Order
       		- Does the API slow down alot if you call all Orders and there are a thousand or a million trades that come up
     	- **Record the Order**
        	- Once you have the order object, you can just parse through it for the needed information
2. Sell the Order
	- **Calculate the P/L**
		- Using a rolling Basis, which changes every websocket call, and compare it to the current price to get the P/L
	- **SELL ORDER**
		- If the P/L I calculated < 0 then SELL

## Step 2 - EMA
- 9 20 200

## Step 3 - Volume Bars
- Figure out how they know the volume bar is buying or selling. The Hight of the buying bars tells you your sentiment

| Volume | Buy                                        | Sell                                       |
| ------ | ------------------------------------------ | ------------------------------------------ |
| High   | The Price will start/continue to go higher | The Price will start/continue to go down   |
| Low    | The Price will start/Continue to go down   | The Price will start/continue to go higher |




## Step __ - Final  Studies
- Make sure to record as much data as possible every day, especially the data around trades, maybe like 50 bars before and 25 after, depending on that there might be a lot of data, and unnecessary data so adjust accordingly
- Eventually you will teach a AI to learn from this data how the original bot did with its trades based on the incoming data, then:
- The AI will be able to bring in a confidence interval (+/-) as to whether the trade is a good trade or not and I can feed that into the trading bot as a positive feedback loop. 
