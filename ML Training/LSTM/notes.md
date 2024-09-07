# Notes on Financial Forecasting  

## Common Mistakes with using LSTM
### 1. Using Min Max Pricing
- Source https://www.youtube.com/watch?v=aIklUbW0UWI (Lazy Programmer)
- 

### 2. Prices as Inputs
- Source https://www.youtube.com/watch?v=aIklUbW0UWI (Lazy Programmer)
#### Concepts
- *Stationarity*: 
  - Stationary Time-Series have distributions that do not change over time
  - Weak Stationarity: mean and variance don't change over time [**Low Stationarity**]
  - *Put into my own words*: Stationarity describes data that, over time, does not vary from its original distribution
  - **Importance**
    1. If the data we train the model with have one distribution that changes when you use a different time period for actual predictions, the predictions will be based on the wrong distribution
- *Extrapolation*
  - Not an issue with my current program. Lecture discusses the issue with training within a parameter (Price of stock in training between $5 - $100, and in testing the actual price between $200 - $300)
  - Does not state a solution
#### Proposed Solutions in Lecture

#### My proposed Solutions and Critic's of Lecture
1. Stationarity: 
    - My hope with my current model is that my data is stationarity, and that in every 100 minutes the distribution and complex relationships that change the price of a stock will not be a confounding issue on my training if I can show it enough of these 100 minute packets. 
    - In other words, a model can tell you the kind of cat in the photo, only if the model has seen that photo, my hope is to feed the model so many "photos" (packets of data) that the model will be able to differentiate between profitable packets and non profitable packets.
2. Extrapolation: 
   - This issue is different but the same at the core for my models as what he discussed. Using absolute pricing is a bad idea because of the issues discussed in the video, but I will get around this by only using Derivative and EMA's in my data

### 3. Prices as Targets
- Source https://www.youtube.com/watch?v=xOcyV5Q2G5I&list=TLPQMDcwOTIwMjQVhov7Riy40Q&index=2 (Lazy Programmer)
#### Concepts
- ***Mentioned in Passing - Not Discussed***
  - Naive Forecast - Mentioned as a good comparison to RMSE 
  - Log prices and Log Returns and issues with them due to *volatility clustering*
  - Arima vs LSTM
  - GARCH to model variance time series
  - Naive Forecast, Optimal Forecast, and Random Walk 

### 4. Train-Test Splits
- Source https://www.youtube.com/watch?v=6t9hKclQNH4&list=TLPQMDcwOTIwMjQVhov7Riy40Q&index=3 (Lazy Programmer)
#### Concepts