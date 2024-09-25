# Creates Dataset for testing
import duckdb
import pandas as pd
import pandas_ta as ta
import numpy as np

def trail_stoploss(row, tradingdata, whole_percentage):
    idx = row.name
    td = tradingdata
    pct = whole_percentage/100
    max_holdtime = 30 # Only hold the trade for twenty minutes

    after_td = td.loc[idx:idx+max_holdtime+1]

    basis = td['close'].loc[idx]
    max_price = basis   # Initially the max price is the basis - No Shorting to Start
    min_price = basis - (basis*pct)
    time_stop = idx + max_holdtime
    time_counter = idx

    #print(f"Basis: {basis}")

    for i, row in after_td.iterrows():
        close = row['close']
        #print(f"Close: {close}, Max: {max_price}, Min: {min_price}, Counter: {time_counter-idx}")
        if close > max_price:
            max_price = close
            min_price = max_price - (max_price * pct)
        elif close < min_price:
            profit = (close - basis) / basis
            return [i, profit]

        time_counter += 1
        if time_counter > time_stop:
            break

    # If the loop ends without triggering stop loss, calculate the profit based on the last close
    profit = (close - basis) / basis
    return profit


class Dataset():
    def __init__(self):
        pass

    def get_qry(ticker, start, end):
        con = duckdb.connect(r"C:\Users\rybot\OneDrive\Databases\datadump.duckdb")

        if isinstance(ticker, list):
            text_ticker = str(ticker)
            text_ticker = text_ticker.replace("[","(")
            text_ticker = text_ticker.replace("]",")")
            qry = f'''
                    SELECT * FROM Stocks
                    WHERE Datetime >= '{start}' 
                    AND Datetime < '{end}' 
                    AND Interval = 1
                    AND Stock in {text_ticker}
                    ''' 
        else:
            qry = f'''
                    SELECT * FROM Stocks
                    WHERE Datetime >= '{start}' 
                    AND Datetime < '{end}' 
                    AND Stock = '{ticker}' 
                    AND Interval = 1
                    ''' 
        
        df = con.execute(qry).fetchdf()
        # Sort the Data from oldest to newest
        df = df.sort_values(by='Datetime').reset_index(drop=True)
    
        return df
    
    def process(df,EMA_list,SMA_list):
        df['Time'] = df['Datetime'].dt.time
        start_time = pd.to_datetime('09:00:00').time()
        end_time = pd.to_datetime('16:00:00').time()
        TradingDay_df = df[(df['Time'] > start_time) & (df['Time'] < end_time) & (df.index >= 201)]

        df['Profit'] = TradingDay_df.apply(trail_stoploss, axis=1, tradingdata=df,whole_percentage=5)

        for EMA in EMA_list:
            df[f'EMA{EMA}'] = ta.ema(df['close'], length=EMA)
            df[f'EMA{EMA}_pct'] = df[f'EMA{EMA}'].pct_change()
            df = df.drop([f'EMA{EMA}'],axis=1).copy()

        for SMA in SMA_list:
            df[f'SMA{SMA}'] = ta.sma(df['close'], length=SMA)
            df[f'SMA{SMA}_pct'] = df[f'SMA{SMA}'].pct_change()
            df = df.drop([f'SMA{SMA}'],axis=1).copy()

        df['dydx'] = df['close'].pct_change()

        # 2nd
        df['dydx2'] = df['dydx'].pct_change()

        df = df.drop(['Datetime','open','high','low','close','volume','Stock','interval','Time'], axis=1)
        
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df = df.dropna().copy()


        return [df, TradingDay_df]
    
    def packeting(df, packet_size, EMA_list, SMA_list):
        rows = []
        print(df.info())

        df['Time'] = df['Datetime'].dt.time
        start_time = pd.to_datetime('09:00:00').time()
        end_time = pd.to_datetime('16:00:00').time()
        Trading_df = df[(df['Time'] > start_time) & (df['Time'] < end_time) & (df.index >= 201)]

        df['Profit'] = Trading_df.apply(trail_stoploss, axis=1, tradingdata=df,whole_percentage=5)

        for EMA in EMA_list:
            df[f'EMA{EMA}'] = ta.ema(df['close'], length=EMA)
            df[f'EMA{EMA}_pct'] = df[f'EMA{EMA}'].pct_change()
            df = df.drop([f'EMA{EMA}'],axis=1).copy()

        for SMA in SMA_list:
            df[f'SMA{SMA}'] = ta.sma(df['close'], length=SMA)
            df[f'SMA{SMA}_pct'] = df[f'SMA{SMA}'].pct_change()
            df = df.drop([f'SMA{SMA}'],axis=1).copy()

        df['dydx'] = df['close'].pct_change()

        # 2nd
        df['dydx2'] = df['dydx'].pct_change()

        df = df.drop(['Datetime','open','high','low','close','volume','Stock','interval','Time'], axis=1)
        
        no_profit = df.drop(columns=['Profit'])

        columns = [f'{col}_{i}' for i in range(packet_size + 1) for col in no_profit.columns]
        columns.append('Profit')  # Add a single 'profit' column at the end

        for index, row in Trading_df.iterrows():
            if index > packet_size:
                # Create the packet, excluding 'profit'
                packet = no_profit.loc[index - packet_size:index]
                flatpacket = list(packet.values.flatten())
                current_profit = df.loc[index, 'Profit']
                flatpacket.append(current_profit) 
                rows.append(flatpacket)
        
        return pd.DataFrame(rows, columns=columns)  
        
