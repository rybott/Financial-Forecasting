# Financial-Forecasting
Using Machine Learning Models to create a training Algorithm 

## Introduction
Most of the models for financial forecasting that I have seen where based on time-series and the training of data over time in order to predict the next stock price. Initially I thought that this could work similar to a natural language model, that predicts the next most likely word. Models can do powerful things based on this concept, so theoretically there is not much difference between being able to determine the next word, or the next price based on the previous data. This is the approach that most of the models that I have seen have used for this purposes, but I never had any success with that type of modeling. 

More impressive that natural-language models are the photo generative models. These models can do anything from determine what type of cat is in a photo, to creating any image that a user can think of. From my brief research, this field is far less developed. I have seen some attempts using Convolutional Neural Networks, such as transforming the inputs used, or by taking actual images of the stock charts and using those as inputs.

### Working Hypothesis
My ultimate goal is to follow one of these techniques and transcoding packets of data (such as 100 minutes of candles) into an image like structure that can be read by a CNN as training data, and then used to predict future models. Currently though, as I work to understand more about coding and machine learning, I have decided to take a simplified approach that instead flattens these packets into rows of data and feeding them into different types of ML models such as Regression models and LSTM models. The concept is the same for all of these ideas however. My hypothesis is that all though the market is random and subject to massive changes, more than 50% of the time within a very small window of time (such as a single packet) patterns emerge that will stay consistent and can be exploited. This theory relies on the predictability of human nature, and tries to determine the following:

*"The average trading is looking at there screen and seeing the chart with about 100 minutes of data, and based on what they see, what will they do next?"*

## Phase I - Determining what data to use
### Intervals and Stocks

### Prices

### Trend Analysis
### Derivatives
### Other Considerations...
