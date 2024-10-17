import pandas as pd
import numpy as np

#load dataframes
df = pd.read_csv("../../data/processed/Arizona_Combined_Weather_Data_And_Case_Number_Daily_Updates_With_One_Hot_Encoding_1994_to_2023.csv")
df2 = pd.read_csv("../../data/processed/arizona_pop_est_1980-2023.csv")
#make an empty row for the rates and population
new_row = pd.DataFrame({col: [np.nan] for col in df.columns}, index=[0])
new_row['Rates'] = np.nan
new_row2 = pd.DataFrame({col: [np.nan] for col in df.columns}, index=[0])
new_row2['Population'] = np.nan
#concatenate the new row to the existing DataFrame
df = pd.concat([df, new_row, new_row2], ignore_index=True)
#the last 2 rows are somehow missing values
df = df.iloc[:-2]
#remove trailing whitespace from the counties col
df2['County'] = df2['County'].str.strip()
#add the population data to the dataset
for index, row in df.iterrows():
    year = str(int(row['Year'])) 
    county = row['County']
    matching_row = df2[df2['County'] == county]

    if not matching_row.empty and year in matching_row.columns:
        df.at[index, 'Population'] = matching_row[year].iloc[0]
    else:
        print(f"No population data found for {county} in {year}")
df['Rates'] = df['Cases'] / df['Population']
df.to_csv("../../data/processed/Arizona_Combined_Dataset_1994_to_2023.csv", index=False)
