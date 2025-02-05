import pandas as pd 

# load all datasets
az_cocci = pd.read_csv("../../data/processed/arizona_cm_combined_data.csv")
az_pop = pd.read_csv("../../data/processed/arizona_pop_est_1980-2023.csv")
az_met = pd.read_csv("../../data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv")
ca_cocci = pd.read_csv("../../data/processed/Cali_Monthly_Cases.csv")
ca_pop = pd.read_csv("../../data/processed/California_Population_2000-2023.csv")
ca_met = pd.read_csv("../../data/processed/California_Weather_Data_Daily_Updates_2001_to_2022.csv")
az_co = pd.read_csv("../../data/processed/arizona_CO_1993_2023.csv", low_memory=False)
az_no2 = pd.read_csv("../../data/processed/arizona_NO2_1993_2023.csv", low_memory=False)
az_oz = pd.read_csv("../../data/processed/arizona_Ozone_1993_2023.csv", low_memory=False)
az_pm2_5 = pd.read_csv("../../data/processed/arizona_PM2.5_1993_2023.csv", low_memory=False)
az_pm2_5_nonref = pd.read_csv("../../data/processed/arizona_PM2.5_nonref_1993_2023.csv", low_memory=False)
az_pm10 = pd.read_csv("../../data/processed/arizona_PM10_1993_2023.csv", low_memory=False)
az_so2 = pd.read_csv("../../data/processed/arizona_SO2_1993_2023.csv", low_memory=False)
az_tsp = pd.read_csv("../../data/processed/arizona_TSP_1993_2023.csv", low_memory=False)
ca_co = pd.read_csv("../../data/processed/california_CO_2000_2022.csv", low_memory=False)
ca_no2 = pd.read_csv("../../data/processed/california_NO2_2000_2022.csv", low_memory=False)
ca_oz = pd.read_csv("../../data/processed/california_Ozone_2000_2022.csv", low_memory=False)
ca_pm2_5 = pd.read_csv("../../data/processed/california_PM2.5_2000_2022.csv", low_memory=False)
ca_pm2_5_nonref = pd.read_csv("../../data/processed/california_PM2.5_nonref_2000_2022.csv", low_memory=False)
ca_pm10 = pd.read_csv("../../data/processed/california_PM10_2000_2022.csv", low_memory=False)
ca_so2 = pd.read_csv("../../data/processed/california_SO2_2000_2022.csv", low_memory=False)
ca_tsp = pd.read_csv("../../data/processed/california_TSP_2000_2022.csv", low_memory=False)
ca_az_air_pollutants = pd.read_csv("../../data/processed/air_pollutants_ca_and_az.csv", low_memory=False)
ca_air_pollutants = pd.read_csv("../../data/processed/air_pollutants_ca.csv", low_memory=False)
az_air_pollutants = pd.read_csv("../../data/processed/air_pollutants_az.csv", low_memory=False)

# list of dataframes and their titles
dfs = [az_cocci, az_pop, az_met, ca_cocci, ca_pop, ca_met, 
       az_co, az_no2, az_oz, az_pm2_5, az_pm2_5_nonref, az_pm10, az_so2, az_tsp,
       ca_co, ca_no2, ca_oz, ca_pm2_5, ca_pm2_5_nonref, ca_pm10, ca_so2, ca_tsp, 
       ca_az_air_pollutants, ca_air_pollutants, az_air_pollutants]

dfs_titles = ['Arizona Cocci Case Count', 
              'Arizona Population Estimates',
              'Arizona Weather Data',
              'California Cocci Case Count',
              'California Population Estimates',
              'California Weather Data',
              'Arizona CO Data 1993-2023',
              'Arizona NO2 Data 1993-2023',
              'Arizona Ozone Data 1993-2023',
              'Arizona PM2.5 Data 1993-2023',
              'Arizona PM2.5 Non-Reference Data 1993-2023',
              'Arizona PM10 Data 1993-2023',
              'Arizona SO2 Data 1993-2023',
              'Arizona TSP Data 1993-2023',
              'California CO Data 2000-2022',
              'California NO2 Data 2000-2022',
              'California Ozone Data 2000-2022',
              'California PM2.5 Data 2000-2022',
              'California PM2.5 Non-Reference Data 2000-2022',
              'California PM10 Data 2000-2022',
              'California SO2 Data 2000-2022',
              'California TSP Data 2000-2022',
              'California and Arizona Air Pollutants',
              'California Air Pollutants',
              'Arizona Air Pollutants']

def missing_value_percentages(df, title):
    # Calculate percentage of missing values for each column
    missing_percentages = (df.isnull().sum() / len(df)) * 100
    
    # Get data types for each column
    dtypes = df.dtypes
    
    # Convert to a DataFrame and add the dataset title and dtypes
    missing_df = pd.DataFrame({
        'Dataset': title,
        'Column': missing_percentages.index,
        'Missing_Percentage': missing_percentages.values,
        'Data_Type': dtypes.values
    })
    
    return missing_df

# Combine all results
all_missing_stats = pd.concat([
    missing_value_percentages(df, title) 
    for df, title in zip(dfs, dfs_titles)
], ignore_index=True)

# Sort by percentage if desired
all_missing_stats = all_missing_stats.sort_values('Missing_Percentage', ascending=False).reset_index(drop=True)

all_missing_stats.to_csv("../../data/analysis_data/missing_values_percentages.csv", index=False)
