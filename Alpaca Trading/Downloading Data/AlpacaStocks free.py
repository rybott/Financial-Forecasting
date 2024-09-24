import requests
import os
from dotenv import load_dotenv
import pandas as pd
import duckdb as ddb
import time
from datetime import datetime, timedelta

api_key = os.getenv("Alpaca_API")
secret_key = os.getenv("Alpaca_Secret")
api_key = 'AKFU0CKGM3LJGMNAWKIB'
secret_key = 'V5PK8tpc3gat8fueZDkqH5aPNR9wwObS2nf9SIDR'

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": f'{api_key}',
    "APCA-API-SECRET-KEY": f'{secret_key}'
}

start = datetime(2016,1,1)
end = datetime(2024,9,23)
date_range = []

current_start = start
while current_start + timedelta(days=41) <= end:
    current_end = current_start + timedelta(days=41)
    date_range.append((current_start.strftime('%Y-%m-%d'),current_end.strftime('%Y-%m-%d')))
    current_start = current_start + timedelta(days=41)

con = ddb.connect('AlpacaStockData.duckdb')

# Finshed Stocks AAPL AMZN SPY
listof_stocks = ['AAPL','MSFT','NVDA','AMZN','GOOG','META','BRK.A','LLY','AVGO','TSLA','WMT','JPM','V','UNH','XOM','ORCL','MA','PG','COST','HD','JNJ','ABBV','NFLX','KO','BAC','MRK','CVX','CRM','AMD','TMUS','TMO','PEP','ADBE','LIN','MCD','ACN','CSCO','GE','IBM','DHR','ABT','BX','NOW','AXP','PM','VZ','CAT','TXN','QCOM','WFC','INTU','AMGN','NEE','ISRG','DIS','PFE','MS','UBER','AMAT','SPGI','CMCSA','RTX','GS','T','UNP','LOW','PGR','BKNG','BLK','LMT','SYK','HON','TJX','NKE','ETN','COP','BSX','ELV','ANET','VRTX','SCHW','KKR','C','CB','REGN','MDT','ADI','ADP','DE','PANW','UPS','MMC','SBUX','MELI','GILD','MU','HCA','SHOP','KLAC','BMY','SMX','SPRC','PRFX','SYTA','CLEU','CNEY','LGMK','GNPX','ENTO','UK','TRNR','FRGT','ADTX','STAF','NCPL','PEGY','GRI','WORX','TANH','EAST','VTAK','SNES','EFSH','BSFC','TIVC','DBGI','APVO','MLGO','NAOV','ACON','MYSZ','YCBD','BACK','ATNF','SGBX','TGL','CYCC','GXAI','INM','SEEL','AKAN','EDBL','BKYI','ELAB','PBM','AVGR','BURU','ONCO','SLRX','SXTC','HCTI','DRMA','TNON','SCPX','ZVSA','BPTH','BJDX','ATCH','NUWE','ITP','NITO','CGBS','ASTI','CETX','FAMI','SXTP','SINT','OBLG','CYTO','TAOP','JTAI','FOXO','WNW','PTIX','NUZE','INVO','HSDT','IMTE','NXU','UUU','REVB','SBET','RELI','VMAR','PHIO','SHPH','VS','LQR','JWEL','JFBR','THAR','ALLR','TNFA','SOBR','ATXI','RSLS','PTPI','EZGO','BAOS','VRPX','SEZL','SMMT','WGS','SLNO','LASE','TIL','NEON','DAVE','FTEL','RNA','ASTS','NISN','BYRN','LBPH','ADMA','CADL','KINS','JANX','LUMN','VKTX','MSTR','INSG','AVAH','LSF','AEYE','AKA','EWTX','ADCT','CATX','CVNA','ASPN','CAVA','TREE','WULF','PSNL','PLSE','SERA','OSCR','PI','ROOT','ALTS','ZETA','JVA','BVS','FTAI','NNE','CDNA','RAIL','DYN','FEMY','REAX','CRVO','SPRY','LEXX','APP','BLND','RZLT','USAP','CRVS','VST','TLN','TPC','HROW','ASPI','PNTG','BMR','TPST','VERA','CURV','AMSC','EVER','SG','CDE','NGNE','HRTG','AQST','CCCC','MYO','STOK','MRT','ZJYL','ARQ','VITL','WLFC','SWVL','MOD','RYAM','BNTC','AGBA','KYMR','AXGN','NKTX','TAYD','APLT','IDR','APEI','COHR','HNST','HIMS','BIVI','BNZI','MSS','GHSI','PTN','FAAS','SLXN','VSME','OCTO','NUKK','WVE','VEEA','HSCS','RNAZ','CAPR','NRSN','FCUV','MPLN','XPON','LEDS','RITR','CJET','SLE','DSY','VERO','HAO','CNTM','ATXG','GBNY','MKFG','LUXH','TBIO','VEEE','VBFC','ENG','HCWC','GLXG','PIXY','GIFT','JBDI','POET','CHSN','XFIN','HCWB','OTRK','AENT','HUDI','GLMD','SBC','POLA','TWG','FLYX','ENGN','BMRA','CERO','EJH','MRNS','GNS','EDUC','MDIA','BRLS','EVTL','AMPX','BENF','LNW','XTNT','GSIW','LBRDA','RCAT','AUR','MULN','KXIN','SKYE','LUCY','FGF','CTOR','HWH','LWAY','AEHL','IVDA','HUMA']


con.execute('''
    CREATE TABLE IF NOT EXISTS Alpaca_Stocks (
        Datetime TIMESTAMP,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        Notrades FLOAT,
        volume FLOAT,
        weighted_volume FLOAT,
        Stock VARCHAR(10)
    )''') 

for tick in listof_stocks:
    try:
        for date_toup in date_range:
            start_date = date_toup[0]
            end_date = date_toup[1]
            ticker = tick
            interval = '1Min'
            limit = '1000'

            url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={ticker}&timeframe={interval}&start={start_date}&end={end_date}&limit={limit}&adjustment=raw&feed=sip&sort=asc"
            response = requests.get(url, headers=headers)
            data = response.json()['bars'][ticker]
            print(f"{ticker} - response {response}")
            df = pd.DataFrame(data)
            df.columns = ['close','high','low','Notrades','open','timestamp','volume','weighted_volume']
            df['Stock'] = ticker

            # Replace 'Z' in the timestamp with '+00:00'
            df['timestamp'] = df['timestamp'].str.replace('Z', '+00:00')

            con.register('df', df)
            con.execute(
                '''
                INSERT INTO Alpaca_Stocks
                SELECT 
                    strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z') as Datetime,
                    open,
                    high,
                    low, 
                    close,
                    Notrades,
                    volume,
                    weighted_volume,
                    Stock
                FROM df
                WHERE Datetime NOT IN (SELECT Datetime FROM Alpaca_Stocks)
                ''')
    except:
        print(f"Error with ticker {tick}")
            