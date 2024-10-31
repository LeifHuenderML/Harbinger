import pandas as pd
import numpy as np

met_df = pd.read_csv("../../data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv")
cm_df = pd.read_csv('../../data/processed/arizona_cm_combined_data.csv')

#remove trailing whitespace from columns
cm_df = cm_df.rename(columns={
    'Month ': 'Month',
    'Apache ': 'Apache',
    'Cochise ': 'Cochise',
    'Coconino ': 'Coconino',
    'Gila ': 'Gila',
    'Graham ': 'Graham',
    'Greenlee ': 'Greenlee',
    'La Paz ': 'La_Paz',
    'Maricopa ': 'Maricopa',
    'Mohave ': 'Mohave',
    'Navajo ': 'Navajo',
    'Pima ': 'Pima',
    'Pinal ': 'Pinal',
    'Santa Cruz ': 'Santa_Cruz',
    'Yavapai ': 'Yavapai',
    'Yuma ': 'Yuma',
    'Total ': 'Total',
    'Year ': 'Year',
    'DateTimeISO': 'Date'
})

# #remove trailing whitespaces
# for col in ['Apache', 'Greenlee', 'Santa_Cruz']:
#     cm_df[col] = cm_df[col].str.strip()

# #change missing values to nan values for pandas
# for col in ['Apache', 'Greenlee', 'Santa_Cruz']:
#     cm_df[col] = pd.to_numeric(cm_df[col].replace('', np.nan), errors='coerce')

#created for easy parsing
met_df['Year'] = pd.to_datetime(met_df['Date']).dt.year
met_df['Month'] = pd.to_datetime(met_df['Date']).dt.month
#create new column and fill with nan values so that when we populate 
# it iwth the case number for that county we can see if there are any missing values

#iterates through each sample of the met data and finds the corresponding value for the 
#number of ccases
for index, row in met_df.iterrows():
    year = row['Year']
    month = row['Month']
    county = row['County']
    
    matching_row = cm_df[(cm_df['Year'] == year) & (cm_df['Month'] == month)]
    
    if not matching_row.empty and county in matching_row.columns:
        met_df.at[index, 'Cases'] = matching_row[county].iloc[0]

#sanity check that compares all the new values populated into the met  data 
# of case numbers against the case number for that county month year for 
# the cm data
def compare_all_cases(met_df, cm_df, counties, years, months):
    mismatches = []
    for county in counties:
        for year in years:
            for month in months:
                result = compare_cases(met_df, cm_df, county, year, month)
                if result is not None:
                    met_cases, cm_cases = result
                    if met_cases != cm_cases:
                        mismatches.append({
                            'County': county,
                            'Year': year,
                            'Month': month,
                            'met_df_cases': met_cases,
                            'cm_df_cases': cm_cases
                        })
    
    # print(f"\nTotal mismatches found: {len(mismatches)}")
    # if mismatches:
    #     print("\nMismatches:")
    #     for mismatch in mismatches:
    #         print(f"  {mismatch['County']} ({mismatch['Year']}-{mismatch['Month']:02d}): "
    #               f"met_df: {mismatch['met_df_cases']}, cm_df: {mismatch['cm_df_cases']}")
    
    return len(mismatches), mismatches

def compare_cases(met_df, cm_df, county, year, month):
    met_sample = met_df[(met_df['County'] == county) & (met_df['Year'] == year) & (met_df['Month'] == month)]
    cm_sample = cm_df[(cm_df['Year'] == year) & (cm_df['Month'] == month)] 
    
    if met_sample.empty or cm_sample.empty:
        return None
    else:
        try:
            met_cases = met_sample['Cases'].iloc[0]
            cm_cases = cm_sample[county].iloc[0]
            
            if (np.isnan(met_cases) and np.isnan(cm_cases)) or met_cases == cm_cases:
                return None  
            else:
                return met_cases, cm_cases  
        except (KeyError, IndexError):
            return None


counties = ['Apache', 'Cochise', 'Coconino', 'Gila', 'Graham', 'Greenlee',
       'La Paz', 'Maricopa', 'Mohave', 'Navajo', 'Pima', 'Pinal',
       'Santa Cruz', 'Yavapai', 'Yuma']
years = list(range(1994, 2024))  
months = list(range(1, 13))  

mismatch_count, mismatches = compare_all_cases(met_df, cm_df, counties, years, months)

met_df.to_csv("../../data/processed/Arizona_Combined_Weather_Data_And_Case_Number_Daily_Updates_1994_to_2023.csv", index=False)