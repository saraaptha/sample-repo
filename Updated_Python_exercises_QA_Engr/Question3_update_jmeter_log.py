import pandas as pd
import os
import pytz
from pytz import timezone
from datetime import datetime
import datetime as dt

def to_pst(timestamp):
    date = datetime.fromtimestamp(int(timestamp)/1000)
    date_time_str = date.strftime("%d/%m/%Y %H:%M:%S")
    date_time_format = datetime.strptime(date_time_str,"%d/%m/%Y %H:%M:%S")
    date_time_utc = date_time_format.replace(tzinfo=timezone('UTC'))
    date_time_pst =  date_time_utc.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S %Z')
    return date_time_pst

os.getcwd()
dir = "C:/Users/saraa/Updated_Python_exercises_QA_Engr/"
os.chdir(dir)
os.listdir()
data = pd.read_csv(dir+"Jmeter_log1.jtl", sep=',')
#data.head()

df = data[data['responseCode'] == 504]
filtered_col = [i for i in df.columns if i in['timeStamp','label','responseCode','responseMessage','failureMessage']]

df['timeStamp'] = df['timeStamp'].apply(to_pst)
pd.set_option('display.max_columns', None)
final_df = df[filtered_col]
print(final_df)

#sample output
#                   timeStamp                              label  responseCode  \
# 4   2021-02-09 11:31:23 PST  Direct_test_Services_QuoteRequest           504
# 5   2021-02-09 11:31:23 PST              Internal_Quote_Travel           504
# 6   2021-02-09 11:31:30 PST   Proxy_test_Services_QuoteRequest           504
# 24  2021-02-09 11:32:55 PST   Proxy_test_Services_QuoteRequest           504
# 25  2021-02-09 11:33:04 PST              Internal_Quote_Travel           504
#
#      responseMessage  failureMessage
# 4   Gateway Time-out             NaN
# 5    Gateway Timeout             NaN
# 6    Gateway Timeout             NaN
# 24   Gateway Timeout             NaN
# 25   Gateway Timeout             NaN