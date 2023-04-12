import akshare as ak 
stock_daily_df = ak.stock_zh_a_daily(symbol="sh000888", adjust="qfq") 
#stock_daily_df.to_excel('daily_sh000001.xlsx',sheet_name='sheet1',index=False)
print(stock_daily_df)
#stock_daily_df.to_csv('daily_sh000001.csv',index=False)
#stock_minute_df = ak.stock_zh_a_minute(symbol="sh000001",period=1,adjust="qfq")
#stock_minute_df.to_excel('one_minute_1_000001.xlsx',sheet_name='sheet1',index=False)
