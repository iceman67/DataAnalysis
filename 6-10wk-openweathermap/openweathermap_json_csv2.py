import requests
import json
"""#### openweathermap 결과 CSV 저장"""

def search_city_extract(city):

    API_KEY = 'a070fcd8fc2db8d5d1f140466a2012b4'  # initialize your key here
    # call API and convert response into Python dictionary
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    #print (url)
    response = requests.get(url)
    # error like unknown city name, inavalid api key
    if response.status_code != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    data = response.json()
   
    # get current temperature and convert it into Celsius
    now = datetime.now()
  
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    current_pressure = data['main']['pressure']
      
    current_temperature = data['main']['temp']  
    current_humidity = data['main']['humidity']    
    #print("{},{},{},{}".format(date_time,current_temperature, current_humidity, current_pressure))
    
    result = list()
    result.append(date_time)
    result.append(current_temperature)
    result.append(current_humidity)
    result.append(current_pressure)
    return result



import csv
import requests
from datetime import datetime
import time


try:
    count = int(input("# of service rqeusts:"))
except ValueError as e:
    print(e)

city='cheonan'
try:
    city = input("city:")
except ValueError as e:
    print(e)


delay = 600
with open("{}.csv".format(city), "w", newline='') as csv_file:
    fieldnames = ['date', 'temperature','humidity','pressure']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(count):
        result = search_city_extract(city)
        print (result)
        writer.writerow({'date': result[0], 'temperature':  result[1], 'humidity':result[2],  'pressure':result[3] })
        time.sleep(delay)

