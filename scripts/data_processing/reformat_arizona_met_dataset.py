import polars as pl
from category_encoders import BinaryEncoder

df = pl.read_csv("../../data/raw/06d609e5e744bedd55f76ad24b015bae.csv")
# rename all the columns 
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
df = df.rename(rename_dict)
#rename all the counties to mach the arizona cm data
rename_dict = {
    'Coconino County': 'Coconino',
    'Maricopa County': 'Maricopa',
    'Pinal County': 'Pinal',
    'Pima County': 'Pima',
    'Yuma County': 'Yuma',
    'Cochise County': 'Cochise',
    'La Paz County': 'La Paz',
    'Navajo County': 'Navajo',
    'Gila County': 'Gila',
    'Graham County': 'Graham',
    'Santa Cruz County': 'Santa Cruz',
    'Apache County': 'Apache',
    'Greenlee County': 'Greenlee',
    'Mohave County': 'Mohave',
    'Yavapai County': 'Yavapai'
}

df = df.with_columns(
    pl.col("County").replace(rename_dict)
)
#remove irrelavent columns
df = df.drop(['DateTime', 'WeatherMain', 'WeatherIcon', 'TimeZone', 'WeatherID'])

#convert date column to datetime format
df = df.with_columns([
    pl.col("DateTimeISO").str.to_datetime("%Y-%m-%d %H:%M:%S +0000 UTC").alias("Date")
])

df = df.drop('DateTimeISO')
#fix formatting issue for null value columns
cols_with_null = ['Visibility', 'SeaLevel', 'GroundLevel', 'WindGust', 'RainOneHour', 'RainThreeHours', 'SnowOneHour', 'SnowThreeHours']
df = df.with_columns(pl.col(cols_with_null).cast(pl.Float64))
df.head()
#save 
output_path = "../../data/processed/Arizona_Weather_Data_Hourly_Updates_1979_to_2024.csv"
df.write_csv(output_path)

#convert the weather description column to be onehot encoded for better effect with lstm
unique_values = df["WeatherDescription"].unique()
for value in unique_values:
    df = df.with_columns(
        pl.when(pl.col("WeatherDescription") == value).then(1).otherwise(0).alias(f"WeatherDescription_{value}")
    )
#save
output_path = "../../data/processed/Arizona_Weather_Data_Hourly_Updates_With_One_Hot_Encoding_1979_to_2024.csv"
df.write_csv(output_path)
#revove this colunmn as it is now unnesacary because it has been one hot encoded
df = df.drop('WeatherDescription')
#convet the df so that it is daily update instead of hourly updates
df = (
    df.group_by(['County', pl.col('Date').dt.date()])
    .mean()
    .sort(['County', 'Date']) 
)
#save
output_path = "../../data/processed/Arizona_Weather_Data_Daily_Updates_With_One_Hot_Encoding_1979_to_2024.csv"
df.write_csv(output_path)
#grab ontly the values for the time period that we have cm data for
df = df.filter(
    (pl.col('Date') >= pl.date(1994, 1, 1)) & 
    (pl.col('Date') <= pl.date(2023, 12, 31))
)
#save
output_path = "../../data/processed/Arizona_Weather_Data_Daily_Updates_With_One_Hot_Encoding_1994_to_2023.csv"
df.write_csv(output_path)


