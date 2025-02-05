import pandas as pd
from IPython.display import display

# Set pandas display options to show all columns
pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)        
pd.set_option('display.max_rows', None)     

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

def convert_columns_to_lowercase(dfs, dfs_titles):
    """
    Converts all column names to lowercase for a list of DataFrames in place.
    
    Parameters:
    dfs (list): List of pandas DataFrames to process
    dfs_titles (list): List of titles corresponding to each DataFrame
    """
    # Verify the lengths of dfs and titles match
    if len(dfs) != len(dfs_titles):
        raise ValueError("Number of DataFrames and titles must match!")
    
    # Iterate through the DataFrames and their titles
    for i, (df, title) in enumerate(zip(dfs, dfs_titles)):
        # Get original columns
        original_columns = df.columns.tolist()
        
        # Create dictionary mapping original to lowercase columns
        columns_map = {col: col.lower() for col in original_columns}
        
        # Rename columns using the mapping
        df.rename(columns=columns_map, inplace=True)
        
        # Print information about changes
        print(f"\nProcessing: {title}")
        print("-" * 40)
        for old_col, new_col in columns_map.items():
            if old_col != new_col:
                print(f"Renamed: '{old_col}' -> '{new_col}'")
    
    print("\nAll DataFrames processed successfully!")


convert_columns_to_lowercase(dfs, dfs_titles)

def list_cols(dfs, dfs_titles):
    """
    Lists all columns for each DataFrame along with its corresponding title.
    
    Parameters:
    dfs (list): List of pandas DataFrames to analyze
    dfs_titles (list): List of titles corresponding to each DataFrame
    """
    # Verify the lengths of dfs and titles match
    if len(dfs) != len(dfs_titles):
        raise ValueError("Number of DataFrames and titles must match!")
        
    # Iterate through the DataFrames and their titles
    for i, (df, title) in enumerate(zip(dfs, dfs_titles), 1):
        # Print a separator for better readability
        print('\n' + '='*80)
        print(f"\n{i}. {title}")
        print('-'*40)
        
        # Get and print column information
        columns = df.columns.tolist()
        print(f"Number of columns: {len(columns)}")
        print("\nColumns:")
        for j, col in enumerate(columns, 1):
            print(f"{j}. {col}")
            
        # Print basic DataFrame info
        print(f"\nNumber of rows: {df.shape[0]:,}")
        
    # Print final separator
    print('\n' + '='*80)

list_cols(dfs, dfs_titles)

def check_and_convert_dates(dfs, dfs_titles):
    """
    Checks each DataFrame for date columns and ensures they are in datetime format.
    Attempts to convert any identified date columns to datetime if they aren't already.
    
    Parameters:
    dfs (list): List of pandas DataFrames to check
    dfs_titles (list): List of titles corresponding to each DataFrame
    """
    # Common date column names (lowercase since we converted columns earlier)
    date_column_patterns = ['date', 'datetime', 'time', 'year']
    
    # Verify the lengths of dfs and titles match
    if len(dfs) != len(dfs_titles):
        raise ValueError("Number of DataFrames and titles must match!")
    
    for df, title in zip(dfs, dfs_titles):
        print(f"\nChecking: {title}")
        print("-" * 40)
        
        # Find potential date columns
        date_columns = []
        for col in df.columns:
            if any(pattern in col.lower() for pattern in date_column_patterns):
                date_columns.append(col)
        
        if not date_columns:
            print(f"WARNING: No date columns found in {title}")
            continue
            
        for col in date_columns:
            # Check if already datetime
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                print(f"Column '{col}' is already in datetime format")
                continue
                
            # Try to convert to datetime
            try:
                # First check if it's a year column
                if 'year' in col.lower():
                    if df[col].dtype in ['int64', 'float64']:
                        print(f"Column '{col}' appears to be a year column, keeping as numeric")
                        continue
                
                # Try to convert with pandas automatic parser
                df[col] = pd.to_datetime(df[col], errors='raise')
                print(f"Successfully converted '{col}' to datetime format")
                
            except Exception as e:
                print(f"ERROR converting '{col}' to datetime: {str(e)}")
                print(f"Sample values from '{col}':")
                print(df[col].head().tolist())
                
        # Print summary of datetime columns after conversion
        datetime_cols = df.select_dtypes(include=['datetime64[ns]']).columns
        if len(datetime_cols) > 0:
            print(f"\nDatetime columns in {title}:")
            for col in datetime_cols:
                print(f"- {col}: Range from {df[col].min()} to {df[col].max()}")
        else:
            print(f"\nNo datetime columns in {title} after conversion attempts")


check_and_convert_dates(dfs, dfs_titles)


az_cocci.rename(columns={'datetimeiso': 'date'}, inplace=True)
az_pop.rename(columns={'year': 'date'}, inplace=True)
def rename_date_local_columns(dfs, dfs_titles):
    """
    Renames 'date_local' column to 'date' across all DataFrames in the list.
    
    Args:
        dfs (list): List of pandas DataFrames to process
        dfs_titles (list): List of titles corresponding to each DataFrame
    """
    for df, title in zip(dfs, dfs_titles):
        if 'date_local' in df.columns:
            df.rename(columns={'date_local': 'date'}, inplace=True)
            print(f"Renamed 'date_local' to 'date' in {title}")

rename_date_local_columns(dfs, dfs_titles)

list_cols(dfs, dfs_titles)

import pandas as pd

def rename_and_save_dataframes():
    """
    Reads CSVs, renames date_local to date if present, and saves back to original paths
    """
    file_paths = {
        'az_cocci': "../../data/processed/arizona_cm_combined_data.csv",
        'az_pop': "../../data/processed/arizona_pop_est_1980-2023.csv",
        'az_met': "../../data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv",
        'ca_cocci': "../../data/processed/Cali_Monthly_Cases.csv",
        'ca_pop': "../../data/processed/California_Population_2000-2023.csv",
        'ca_met': "../../data/processed/California_Weather_Data_Daily_Updates_2001_to_2022.csv",
        'az_co': "../../data/processed/arizona_CO_1993_2023.csv",
        'az_no2': "../../data/processed/arizona_NO2_1993_2023.csv",
        'az_oz': "../../data/processed/arizona_Ozone_1993_2023.csv",
        'az_pm2_5': "../../data/processed/arizona_PM2.5_1993_2023.csv",
        'az_pm2_5_nonref': "../../data/processed/arizona_PM2.5_nonref_1993_2023.csv",
        'az_pm10': "../../data/processed/arizona_PM10_1993_2023.csv",
        'az_so2': "../../data/processed/arizona_SO2_1993_2023.csv",
        'az_tsp': "../../data/processed/arizona_TSP_1993_2023.csv",
        'ca_co': "../../data/processed/california_CO_2000_2022.csv",
        'ca_no2': "../../data/processed/california_NO2_2000_2022.csv",
        'ca_oz': "../../data/processed/california_Ozone_2000_2022.csv",
        'ca_pm2_5': "../../data/processed/california_PM2.5_2000_2022.csv",
        'ca_pm2_5_nonref': "../../data/processed/california_PM2.5_nonref_2000_2022.csv",
        'ca_pm10': "../../data/processed/california_PM10_2000_2022.csv",
        'ca_so2': "../../data/processed/california_SO2_2000_2022.csv",
        'ca_tsp': "../../data/processed/california_TSP_2000_2022.csv",
        'ca_az_air_pollutants': "../../data/processed/air_pollutants_ca_and_az.csv",
        'ca_air_pollutants': "../../data/processed/air_pollutants_ca.csv",
        'az_air_pollutants': "../../data/processed/air_pollutants_az.csv"
    }
    
    for name, path in file_paths.items():
        # Read the CSV with low_memory=False for specific files
        low_memory = False if any(x in path.lower() for x in ['co', 'no2', 'ozone', 'pm', 'so2', 'tsp', 'air_pollutants']) else True
        
        try:
            # Read the file
            df = pd.read_csv(path, low_memory=low_memory)
            
            # Save back to the same path
            df.to_csv(path, index=False)
            print(f"Successfully processed and saved: {name}")
            
        except Exception as e:
            print(f"Error processing {name}: {str(e)}")


rename_and_save_dataframes()