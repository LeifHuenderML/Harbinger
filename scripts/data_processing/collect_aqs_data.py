import requests
import time
import pandas as pd
from datetime import datetime

def get_aqs_data(year, parameter, state):
    # API credentials
    email = "leifhuenderai@gmail.com"
    api_key = "bayfrog74"
    
    # Format dates for the year
    bdate = f"{year}0101"
    edate = f"{year}1231"
    
    base_url = "https://aqs.epa.gov/data/api/dailyData/byState"
    print(f"Fetching {year} data for parameter {parameter} in state {state}")
    
    url = f"{base_url}?email={email}&key={api_key}&param={parameter}&bdate={bdate}&edate={edate}&state={state}"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["Header"][0]["status"] == "Success":
            df = pd.DataFrame(data["Data"])
            print(f"Successfully retrieved {len(df)} rows")
            return df
        else:
            print(f"Error: {data['Header'][0]['status']}")
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def process_state_data(state_code, state_name, start_year, end_year):
    # Dictionary to map parameter codes to names
    parameter_names = {
        "88101": "PM2.5",
        "81102": "PM10",
        "85101": "TSP",
        "88502": "PM2.5_nonref",
        "44201": "Ozone",
        "42401": "SO2",
        "42101": "CO",
        "42602": "NO2"
    }

    # Process each parameter separately
    for param_code, param_name in parameter_names.items():
        param_data = []
        
        # Get data for each year in the specified range
        for year in range(start_year, end_year + 1):
            print(f"\nProcessing {state_name} data for year {year} for {param_name}")
            df = get_aqs_data(year, param_code, state_code)
            
            if df is not None:
                param_data.append(df)
                # # Save each year's data for this parameter
                # df.to_csv(f"../../data/raw/air_quality/{state_name.lower()}_{param_name}_{year}.csv", index=False)
                # print(f"Saved {param_name} data for {year}")
            
            # Wait between requests to respect API rate limits
            time.sleep(5)
        
        # Combine all years for this parameter
        if param_data:
            param_final_df = pd.concat(param_data, ignore_index=True)
            param_final_df.to_csv(
                f"../../data/raw/air_quality/{state_name.lower()}_{param_name}_{start_year}_{end_year}.csv", 
                index=False
            )
            print(f"\nAll {state_name} {param_name} data from {start_year} to {end_year} has been saved!")
        
        # Wait between parameters to be extra safe with rate limits
        time.sleep(10)

def main():
    # Process California data (2000-2022)
    print("\nStarting California data collection...")
    process_state_data("06", "California", 2000, 2022)
    
    # Process Arizona data (1993-2023)
    print("\nStarting Arizona data collection...")
    process_state_data("04", "Arizona", 1993, 2023)
    
    print("\nAll data collection completed!")

if __name__ == "__main__":
    main()