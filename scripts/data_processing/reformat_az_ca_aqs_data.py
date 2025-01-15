import pandas as pd

pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)        
pd.set_option('display.max_rows', None)   

file_paths = [
    "../../data/processed/arizona_CO_1993_2023.csv",
    "../../data/processed/arizona_NO2_1993_2023.csv",
    "../../data/processed/arizona_Ozone_1993_2023.csv",
    "../../data/processed/arizona_PM2.5_1993_2023.csv",
    "../../data/processed/arizona_PM2.5_nonref_1993_2023.csv",
    "../../data/processed/arizona_PM10_1993_2023.csv",
    "../../data/processed/arizona_SO2_1993_2023.csv",
    "../../data/processed/arizona_TSP_1993_2023.csv",
    "../../data/processed/california_CO_2000_2022.csv",
    "../../data/processed/california_NO2_2000_2022.csv",
    "../../data/processed/california_Ozone_2000_2022.csv",
    "../../data/processed/california_PM2.5_2000_2022.csv",
    "../../data/processed/california_PM2.5_nonref_2000_2022.csv",
    "../../data/processed/california_PM10_2000_2022.csv",
    "../../data/processed/california_SO2_2000_2022.csv",
    "../../data/processed/california_TSP_2000_2022.csv"
]

az_co = pd.read_csv("../../data/raw/air_quality/arizona_CO_1993_2023.csv", low_memory=False)
az_no2 = pd.read_csv("../../data/raw/air_quality/arizona_NO2_1993_2023.csv", low_memory=False)
az_oz = pd.read_csv("../../data/raw/air_quality/arizona_Ozone_1993_2023.csv", low_memory=False)
az_pm2_5 = pd.read_csv("../../data/raw/air_quality/arizona_PM2.5_1993_2023.csv", low_memory=False)
az_pm2_5_nonref = pd.read_csv("../../data/raw/air_quality/arizona_PM2.5_nonref_1993_2023.csv", low_memory=False)
az_pm10 = pd.read_csv("../../data/raw/air_quality/arizona_PM10_1993_2023.csv", low_memory=False)
az_so2 = pd.read_csv("../../data/raw/air_quality/arizona_SO2_1993_2023.csv", low_memory=False)
az_tsp = pd.read_csv("../../data/raw/air_quality/arizona_TSP_1993_2023.csv", low_memory=False)
ca_co = pd.read_csv("../../data/raw/air_quality/california_CO_2000_2022.csv", low_memory=False)
ca_no2 = pd.read_csv("../../data/raw/air_quality/california_NO2_2000_2022.csv", low_memory=False)
ca_oz = pd.read_csv("../../data/raw/air_quality/california_Ozone_2000_2022.csv", low_memory=False)
ca_pm2_5 = pd.read_csv("../../data/raw/air_quality/california_PM2.5_2000_2022.csv", low_memory=False)
ca_pm2_5_nonref = pd.read_csv("../../data/raw/air_quality/california_PM2.5_nonref_2000_2022.csv", low_memory=False)
ca_pm10 = pd.read_csv("../../data/raw/air_quality/california_PM10_2000_2022.csv", low_memory=False)
ca_so2 = pd.read_csv("../../data/raw/air_quality/california_SO2_2000_2022.csv", low_memory=False)
ca_tsp = pd.read_csv("../../data/raw/air_quality/california_TSP_2000_2022.csv", low_memory=False)

# list of dataframes and their titles
dfs = [az_co, az_no2, az_oz, az_pm2_5, az_pm2_5_nonref, az_pm10, az_so2, az_tsp,
       ca_co, ca_no2, ca_oz, ca_pm2_5, ca_pm2_5_nonref, ca_pm10, ca_so2, ca_tsp]
az_dfs = [az_co, az_no2, az_oz, az_pm2_5, az_pm2_5_nonref, az_pm10, az_so2, az_tsp]
ca_dfs = [ca_co, ca_no2, ca_oz, ca_pm2_5, ca_pm2_5_nonref, ca_pm10, ca_so2, ca_tsp]


cols_to_drop = ['state_code', 'county_code', 'site_number', 'parameter_code', 'cbsa_code', 'cbsa', 'date_of_last_change']

df = pd.concat([df.drop(cols_to_drop, axis=1) for df in dfs], ignore_index=True)
az_df = pd.concat([df.drop(cols_to_drop, axis=1) for df in az_dfs], ignore_index=True)
ca_df = pd.concat([df.drop(cols_to_drop, axis=1) for df in ca_dfs], ignore_index=True)

for path, df in zip(file_paths, dfs):
    df.to_csv(path, index=False)

df.to_csv("../../data/processed/air_pollutants_ca_and_az.csv", index=False)
az_df.to_csv("../../data/processed/air_pollutants_az.csv", index=False)
ca_df.to_csv("../../data/processed/air_pollutants_ca.csv", index=False)
