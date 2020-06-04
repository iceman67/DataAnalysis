import pandas as pd
 
#my_url= "https://raw.githubusercontent.com/iceman67/DataAnalysis/master/April_sensor_data.csv"

my_url= "friday.csv"

# 문자열을 날짜값으로 변환 
df = pd.read_csv(my_url, parse_dates=['REG_DATE'])

# index 컬럼 지정 
df = df.set_index("NO", drop = True)

df['weekday'] = df['REG_DATE'].dt.day_name()
print(df.columns)

 
