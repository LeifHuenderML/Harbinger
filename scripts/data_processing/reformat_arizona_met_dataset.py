import pandas as pd
import numpy as np

df = pd.read_csv("../../data/raw/06d609e5e744bedd55f76ad24b015bae.csv")
#rename all the columns to better names
rename_dict = {
    'dt': 'DateTime',
    'dt_iso': 'DateTimeISO',
    'timezone': 'TimeZone',
    'city_name': 'County',
    'lat': 'Latitude',
    'lon': 'Longitude',
    'temp': 'Temperature',
    'visibility': 'Visibility',
    'dew_point': 'DewPoint',
    'feels_like': 'FeelsLike',
    'temp_min': 'TemperatureMinimum',
    'temp_max': 'TemperatureMaximum',
    'pressure': 'Pressure',
    'sea_level': 'SeaLevel',
    'grnd_level': 'GroundLevel',
    'humidity': 'Humidity',
    'wind_speed': 'WindSpeed',
    'wind_deg': 'WindDegree',
    'wind_gust': 'WindGust',
    'rain_1h': 'RainOneHour',
    'rain_3h': 'RainThreeHours',
    'snow_1h': 'SnowOneHour',
    'snow_3h': 'SnowThreeHours',
    'clouds_all': 'CloudsAll',
    'weather_id': 'WeatherID',
    'weather_main': 'WeatherMain',
    'weather_description': 'WeatherDescription',
    'weather_icon': 'WeatherIcon'
}
df = df.rename(columns=rename_dict)
#fix the county column so that it doesnt have county in each of the names
df['County'] = df['County'].str.replace(' County', '')
#drop unnessecary columns
df = df.drop(['DateTime', 'WeatherMain', 'WeatherIcon', 'TimeZone', 'WeatherID'], axis=1)
#make date into the datetime format
df['Date'] = pd.to_datetime(df['DateTimeISO'], format='%Y-%m-%d %H:%M:%S +0000 UTC')
df.drop('DateTimeISO', axis=1)

#aggregate so that it is mean over day not hourly
df['DateOnly'] = df['Date'].dt.date

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

df = df.groupby(['County', 'DateOnly']).agg({
    col: 'mean' for col in numeric_columns
}).reset_index().sort_values(['County', 'DateOnly'])

df = df.rename(columns={'DateOnly': 'Date'})

#narrow down to the years to fit  the cm dataset
df['Date'] = pd.to_datetime(df['Date'])
df = df[(df['Date'] >= pd.to_datetime('1994-01-01')) & 
        (df['Date'] <= pd.to_datetime('2023-12-31'))]
output_path = "../../data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv"
df.to_csv(output_path, index=False)
