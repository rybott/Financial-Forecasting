# Strat No 2 - The Power of early morning volitility

## I don't think it will work, .02% return in best case scenario is not better than my current plan

## Procedures
1. Figure out if you have the data (Outside training times data)
2. Determine the win rate of the data based on two different variables
    1. How many minutes you look back before 930
    2. How many minutes to look foward 
        (Trailing Stop Loss, 5 min, 10min, 20min, 30min, 60min, etc.)
3. Determine how terrible it does at different confident levels, (e.i. if I only acted on the trade when the output was above a 80% confidence interval, then how well does it do then.)

## Results
1. Getting Data
    - There is premarket data
    - The top 25-percentile makes 3% after 30 minutes and 4% after 45 minutes
2. Train a model to determine if a trade will be in that 25-percentile 
    - Positive trajetory 
    - Maybe a classification system (-4,-3,-2,-1,0,1,2,3,4)
    - Only take trades when the classifier is above a 2 or 3
3. Back test only the ones where the output is >2
4. Develop a better, multilayered loss selling strategey
    - Don't sell right away, have a little confidence in the model.
    1. Stepped Basis
        - Have a stepped basis  
            - First minute the basis is the stock price at time 0
                - If it drops X% below basis 1 sell
            - After 5 minutes the basis is the new stock price at time 5
                - If it drops Y% below basis 2 sell
            - etc. 
    2. Bolinger Bands
        - Have a slightly tighter band, and if the price decreases below the band then sell.
5. Gain selling strategy - as soon as the category is reached, sell.
    - If the classifier says 2, then once the stock gains 2%, then sell.

## Variables
1. Amount of data in the pre market data
2. Selling timing
3. Threshold for the classifier


    