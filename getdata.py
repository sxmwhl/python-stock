import akshare as ak 
# stock_daily_df = ak.stock_zh_a_daily(symbol="sh600000", adjust="hfq") 
# stock_daily_df.to_excel('stock.xlsx',sheet_name='sheet1',index=False)

stock_minute_df = ak.stock_zh_a_minute(symbol="sz000888",period=5,adjust="qfq")
stock_minute_df.to_excel('one_minute_5.xlsx',sheet_name='sheet1',index=False)
