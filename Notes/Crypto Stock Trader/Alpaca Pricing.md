## Features
| **Feature**                    | **Basic Plan (Free)**                                                       | **Algo Trader Plus Plan ($99/month)**                          |
| ------------------------------ | --------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Pricing**                    | Free                                                                        | $99 / month                                                    |
| **Securities Coverage**        | US Stocks & ETFs                                                            | US Stocks & ETFs                                               |
| **Real-Time Market Coverage**  | IEX only (limited real-time data)                                           | All US Stock Exchanges                                         |
| **WebSocket Subscriptions**    | 30 symbols                                                                  | Unlimited                                                      |
| **Historical Data**            | Available since 2016                                                        | Available since 2016                                           |
| **Historical Data Limitation** | 15-minute delay                                                             | No restriction                                                 |
| **Historical API Calls**       | 200 calls per minute                                                        | 10,000 calls per minute                                        |
| **Crypto Trading**             | Historical crypto data without authentication; other data requires API keys | Comprehensive real-time and historical data                    |
| **Data Sources**               | IEX (Investors Exchange LLC)                                                | Direct feeds from CTA (NYSE) and UTP (Nasdaq) SIPs             |
| **SDKs and Integration**       | Python, Go, NodeJS, C#                                                      | Python, Go, NodeJS, C#                                         |
| **Market Data API**            | HTTP and WebSocket protocols for real-time and historical data              | HTTP and WebSocket protocols for real-time and historical data |
| **Support for Indicators**     | Use third-party libraries to calculate indicators                           | Use third-party libraries to calculate indicators              |
| **Authentication**             | Required for most data endpoints                                            | Required for most data endpoints                               |
### Notes:
- **Historical Crypto Data**: Available without authentication in the Basic plan.
- **Advanced Market Coverage**: Available in the Algo Trader Plus plan, offering real-time data from all US stock exchanges.
- **Integration and SDKs**: Both plans offer user-friendly SDKs in multiple programming languages, facilitating integration into trading applications.

For more details, refer to Alpaca’s [official documentation](https://docs.alpaca.markets) and their [pricing page](https://alpaca.markets/pricing).

## Affects on Crypto Scalp Trading
| Feature                    | Basic Plan (Free)                                                                                 | Impact on Crypto Scalp Trading                                                  |
|----------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Pricing                    | Free                                                                                              | No direct cost, but limited features may require upgrades                       |
| Real-Time Market Coverage  | IEX only for equities; indicative pricing feed for options                                        | Limited real-time data for accurate and timely decision-making                  |
| WebSocket Subscriptions    | 30 symbols                                                                                        | May not be sufficient for monitoring multiple crypto pairs simultaneously       |
| Historical Data            | Available since 2016                                                                              | Sufficient for backtesting strategies but with limitations                      |
| Historical Data Limitation | 15-minute delay                                                                                   | Significant lag can impact the relevance of backtesting and historical analysis |
| Historical API Calls       | 200 calls per minute                                                                              | May be sufficient for basic needs but could hinder high-frequency data access   |
| Crypto Trading             | Limited access to historical crypto data without authentication; real-time data requires API keys | Limited real-time insights can affect the ability to execute timely trades      |
| Data Sources               | IEX (Investors Exchange LLC) for equities                                                         | Does not impact crypto directly, but indicates limited overall data sources     |
| Support for Indicators     | Use third-party libraries to calculate indicators                                                 | Requires additional setup and may not be as seamless as built-in solutions      |
#### Impact Analysis:

1. **Real-Time Data Limitations**:
    - **Crypto scalp trading relies heavily on real-time data** for making quick and accurate trading decisions. The Basic Plan’s reliance on limited real-time data sources means that the data you receive might not be as timely or comprehensive as needed for effective scalp trading.
    - **WebSocket limitations** with only 30 symbols may not suffice if you plan to monitor multiple cryptocurrency pairs, as this restricts the number of real-time data streams you can subscribe to simultaneously.

1. **Historical Data and Back testing**:
    - **15-minute delay in historical data** means that any back testing or historical analysis you perform might not reflect the most recent market conditions, potentially leading to less effective trading strategies.
    - **API call limitations** (200 calls per minute) may be adequate for low-frequency trading but could be restrictive for high-frequency scalp trading, where more frequent data updates are required.

1. **Technical Indicators**:
    - While you can use third-party libraries to calculate technical indicators, the **lack of built-in support** means you’ll need additional setup and integration, which could complicate the process and increase the time required to get your trading system up and running.

1. **General Constraints**:
    - **Limited market coverage** and reliance on IEX for real-time equity data indicate that the overall infrastructure provided by the Basic Plan might not be robust enough for high-frequency trading environments where comprehensive and instantaneous data is crucial.
### Conclusion:
For effective crypto scalp trading, the limitations of Alpaca’s free tier primarily center around restricted access to real-time data and historical data delays, which can significantly impact the efficacy of your trading strategies. Upgrading to a plan that offers more comprehensive real-time market coverage and higher API call limits would likely be necessary to mitigate these issues and enhance your trading performance.

# Crypto Fees

While Alpaca stock trading remains commission-free, crypto trading includes a small fee per trade dependent on your executed volume and order type. Any market or exchange consists of two parties, buyers and sellers. When you place an order to buy crypto on the Alpaca Exchange, there is someone else on the other side of the trade selling what you want to buy. The seller's posted order on the order book is providing liquidity to the exchange and allows for the trade to take place. Note, that both buyers and sellers can be makers or takers depending on the order entered and current quote of the coin. **A maker is someone who adds liquidity, and the order gets placed on the order book. A Taker on the other hand removes the liquidity by placing a market or marketable limit order which executes against posted orders.**

| Tier | 30D Crypto Volume (USD)  | Maker | Take  |
|------|--------------------------|-------|-------|
| 1    | 0 - 100,000              | 0.15% | 0.25% |
| 2    | 100,000 - 500,000        | 0.12% | 0.22% |
| 3    | 500,000 - 1,000,000      | 0.10% | 0.20% |
| 4    | 1,000,000 - 10,000,000   | 0.08% | 0.18% |
| 5    | 10,000,000- 25,000,000   | 0.05% | 0.15% |
| 6    | 25,000,000 - 50,000,000  | 0.02% | 0.13% |
| 7    | 50,000,000 - 100,000,000 | 0.02% | 0.12% |
| 8    | 100,000,000+             | 0.00% | 0.10% |
