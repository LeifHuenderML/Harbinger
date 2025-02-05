import pandas as pd
import os

    
# Read the data
df = pd.read_csv("../../data/raw/davis_pesticides_2001-22.csv")
df = df.reset_index(drop=True)
df['CHEMNAME'] = df['CHEMNAME'].astype('string')
df['COUNTY'] = df['COUNTY'].astype('string')

df.to_csv("pesticides.csv", index=False)

df = pd.read_csv("pesticides.csv")

os.remove("pesticides.csv")

df = df.sort_values(by=['YEAR', 'MONTH', 'COUNTY', 'CHEMNAME'], 
                          ascending=[True, True, True, True])

df.columns = df.columns.str.lower()

df = df.reset_index(drop=True)

df['county'] = df['county'].str.title()

df['date'] = pd.to_datetime(dict(year=df['year'], month=df['month'], day=1))

df.to_csv("../../data/processed/california_pesticides_2001-2022.csv", index=False)
