import pandas as pd
 
#my_url= "https://raw.githubusercontent.com/iceman67/DataAnalysis/master/April_sensor_data.csv"

my_url= "April_sensor_data.csv"

# 문자열을 날짜값으로 변환 
df = pd.read_csv(my_url, parse_dates=['REG_DATE'])

# index 컬럼 지정 
df = df.set_index("NO", drop = True)

df['weekday'] = df['REG_DATE'].dt.day_name()
print(df.columns)

print(df.head())
print(df['CO2'][df['weekday']=='Friday'].head())
print(df['CO2'][df['weekday']=='Sunday'].head())


df_friday = df[df['weekday']=='Friday']
print(df_friday.head())


df_sunday = df[df['weekday']=='Sunday']
print(df_sunday.head())


df_friday.to_csv('friday.csv')
df_sunday.to_csv('sunday.csv')
