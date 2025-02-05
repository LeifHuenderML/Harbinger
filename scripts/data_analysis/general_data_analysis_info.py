import pandas as pd
import sys
from io import StringIO
from datetime import datetime

# Set pandas display options to show all columns
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)        
pd.set_option('display.max_rows', None)     

# Create a timestamp for the output file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"../../data/analysis_data/general_info_dataset_analysis_{timestamp}.txt"

# Function to capture DataFrame info as string
def get_df_info(df):
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

# Modified display_info function to return formatted string
def format_info(df, title):
    output = []
    output.append(f"\n{title} Info")
    output.append("="*50 + "\n" + "="*50)
    output.append(get_df_info(df))
    output.append(f"\n{title} Head")
    output.append("="*50 + "\n" + "="*50)
    output.append(df.head().to_string())
    output.append(f"\n{title} Tail")
    output.append("="*50 + "\n" + "="*50)
    output.append(df.tail().to_string())
    return "\n".join(output)

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

# Write all information to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Dataset Analysis Report\n")
    f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*50 + "\n\n")
    
    for df, title in zip(dfs, dfs_titles):
        f.write(format_info(df, title))
        f.write("\n\n" + "="*100 + "\n\n")  # Section separator

print(f"Analysis has been written to {output_file}")