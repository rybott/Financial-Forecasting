# Orders
### Market Order
```python
from alpaca.trading.client import TradingClient 
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

Alpaca = TradingClient("PKW7DQECIZLURTL0KOAA","tkNL2VUeS6lSVtWT6BosI4nfm0sgZw37z6HDllKj")

market_order_data = MarketOrderRequest(
    symbol= "",
    qty= 1, # Can be Fractional Shares
    side= OrderSide.BUY, # OrderSide.SELL
    time_in_force=TimeInForce.DAY
)
market_order = TradingClient.submit_order(market_order_data) # Exicutes Trade
print(market_order)
```

### Limit Orders
```python
from alpaca.trading.client import TradingClient 
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

Alpaca = TradingClient("PKW7DQECIZLURTL0KOAA","tkNL2VUeS6lSVtWT6BosI4nfm0sgZw37z6HDllKj")

limit_order_data = LimitOrderRequest(
    symbol= "",
    qty= 1, # Can be Fractional Shares
    side= OrderSide.BUY, # OrderSide.SELL
    time_in_force= TimeInForce.DAY,
    limit_price= 3 # Price willing to buy at
)
limit_order = TradingClient.submit_order(limit_order_data) # Exicutes Trade
print(market_order)
```
## Getting Orders
### Printing out lists of all your orders in a List of Dictionaries
```python
# Getting your Orders
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

request_params = GetOrdersRequest(
    status= QueryOrderStatus.OPEN,# only Needed if filitering for Open
    side= OrderSide.BUY, # filters for Buy Side, can be Sell side filter too
)
order = Alpaca.get_orders(request_params)
```

## Misc.
```python
# Canceling an Order
Alpaca.cancel_order_by_id("")
# Getting Positions
positions = Alpaca.get_all_positions() # List of Disctionaries
# Nuclear Option - Closing all Positions
Alpaca.close_all_positions(True)
```

# Getting the DataStream
### Gives you up to date data on prices
```python
from alpaca.data.live import StockDataStream
from alpaca.data.live import CryptoDataStream # For Crypto

stream = StockDataStream("PKW7DQECIZLURTL0KOAA","tkNL2VUeS6lSVtWT6BosI4nfm0sgZw37z6HDllKj")

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "Ticker")
```
