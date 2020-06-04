import pandas as pd

#my_url= "https://raw.githubusercontent.com/iceman67/DataAnalysis/master/April_sensor_data.csv"

my_url= "April_sensor_data.csv"
#data frame
df = pd.read_csv(my_url)
print(df.head(3))

#print(df.tail())

# 열
#print(df.columns)

# 이상치 (outlier)
#print(df.describe())

#print(df['CO2'].describe())

#print(df[['CO2', 'PM2.5']].describe())

# axis = 0  행을 제거,  axis = 1 열을 제거
df.drop('NO', axis=1, inplace=True)
print(df.columns)
print(df.head(3))

df = df.rename(columns={'Huminity': 'Humidity', 'PM2.5' :'PM25', 'PM10.0':'PM100'})
print(df.columns)
print(df.head(3))


#df['Temperature'].nlargest(5)
#print(df['Temperature'].nlargest(5))

df.nlargest(5, columns='Humidity')
print(df.nlargest(5, columns='Humidity'))

df['Humidity'].nsmallest(3)

df.nsmallest(5, columns='Humidity')
print(df.nsmallest(5, columns='Humidity'))

#df['Temperature'].min()
#df['Temperature'].max()

# EDA




