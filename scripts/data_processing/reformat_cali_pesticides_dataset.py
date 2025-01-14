import pandas as pd

#read ca_pesticides
ca_pesticides = pd.read_csv("../../data/raw/davis_pesticides_2001-22.csv")
# sort by county month value 
ca_pesticides = ca_pesticides.sort_values(by=['YEAR', 'MONTH', 'COUNTY', 'CHEMNAME']).reset_index(drop=True)
# fix naming convention
ca_pesticides = ca_pesticides.rename(columns=lambda x: x.title().strip())

# Pivot the DataFrame
pivoted_ca_pesticides = ca_pesticides.pivot_table(
    index=['Year', 'Month', 'County'],  # These will identify unique rows
    columns='Chemname',                 # Each chemical becomes a column
    values=['Lbs_Chm_Used', 'Area_Planted', 'Applications'],  # Values to spread across new chemical columns
    fill_value=0  # Fill NaN values with 0
).reset_index()

# Flatten the multi-level column names
pivoted_ca_pesticides.columns = [f'{col[0]}_{col[1]}' if col[1] else col[0] for col in pivoted_ca_pesticides.columns]

ca_pesticides = pivoted_ca_pesticides.copy()

ca_pesticides.to_csv("../../data/processed/cali_pesticides_2001-2022.csv", index=False)
ca_pesticides.head()
