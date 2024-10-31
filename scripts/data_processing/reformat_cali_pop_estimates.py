import pandas as pd
import numpy as np

df = pd.read_excel("../../data/raw/co-est2019-annres-06.xlsx")
#remove bad rows
df.columns = df.iloc[2]
df = df.drop(list(range(0,4)))
df = df.reset_index(drop=True)
df = df.drop(list(range(58,63)))
df = df.reset_index(drop=True)
#relabel county column
df = df.rename(columns={df.columns[0]: 'Year'})

df = df.drop(['Census', 'Estimates Base'], axis=1)
df.columns = [str(col).replace('.0', '') for col in df.columns]

df['Year'] = df['Year'].str.replace(' County, California', '')
df['Year'] = df['Year'].str.replace('.', '')

df = df.T.reset_index()

df.columns = df.iloc[0]
df = df.drop(0)
df = df.reset_index(drop=True)

df_2010_2019 = df.copy()

df = pd.read_excel("../../data/raw/co-est2023-pop-06.xlsx")
#remove bad rows
df.columns = df.iloc[2]
df = df.drop(list(range(0,4)))
df = df.reset_index(drop=True)

df = df.drop(list(range(58,64)))
df = df.reset_index(drop=True)

df.columns = ['Year', 'unk', '2020', '2021', '2022', '2023']
df = df.drop('unk', axis=1)

df['Year'] = df['Year'].str.replace(' County, California', '')
df['Year'] = df['Year'].str.replace('.', '')

df = df.T.reset_index()

df.columns = df.iloc[0]
df = df.drop(0)
df = df.reset_index(drop=True)

df = pd.concat([df_2010_2019, df], ignore_index=True)

df_2010_2023 = df.copy()

df = pd.read_excel("../../data/raw/population_2000_2010(2).xlsx")
df.columns = df.iloc[2]
df = df.drop(list(range(0,4)))
df = df.reset_index(drop=True)
df = df.drop(list(range(58,66)))
df = df.reset_index(drop=True)
new_columns = ['Year', 'unk1']
# Add the year columns from 2000-2009
new_columns.extend([str(year) for year in range(2000, 2010)])
# Add the last two columns
new_columns.extend(['unk2', '2010'])

# Assign the new column names
df.columns = new_columns
df = df.drop(['unk1', 'unk2'], axis=1)


df['Year'] = df['Year'].str.replace(' County, California', '')
df['Year'] = df['Year'].str.replace(' County', '')
df['Year'] = df['Year'].str.replace('.', '')

df = df.T.reset_index()

df.columns = df.iloc[0]
df = df.drop(0)
df = df.reset_index(drop=True)

df = pd.concat([df, df_2010_2023], ignore_index=True)
df = df.drop(10)
df = df.reset_index(drop=True)


df = df.loc[df.index.repeat(12)].copy()

# Create month column (1-12 for each year)
df['Month'] = [(i % 12) + 1 for i in range(len(df))]

# Reset the index if needed
df = df.reset_index(drop=True)

df['date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')

df.to_csv("../../data/processed/California_Population_2000-2023", index=False)
