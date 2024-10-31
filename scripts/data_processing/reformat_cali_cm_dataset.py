import pandas as pd
import numpy as np

#silences warning
pd.set_option('future.no_silent_downcasting', True)

df = pd.read_excel("../../data/raw/Cocci Case Counts by County and Month, 2001-2022.xlsx")
#relabel the columns to be correct
df.columns = df.iloc[0]
df = df.drop(df.index[0])
df = df.reset_index(drop=True)
#remove unnessacary columns
columns = df.columns.tolist()
new_columns = columns[:-2]
df = df[new_columns]
#relabel the counties to match the formatting of all our other datasets
df['County'] = df['County'].str.title()
#relabel the other columns to be more accurate
rename_dict = {
    'Year and\nMonth of\nEstimated\nOnset': "YearMonth",
    'Case\nCount': 'Cases'
}
df = df.rename(columns=rename_dict)
#split the yearmonth columnn into two sepearate columns
df[['Year', 'Month']] = df['YearMonth'].str.split('_', expand=True)
df['Year'] = df['Year'].astype(int)
df['Month'] = df['Month'].astype(int)
#create the datecolumn
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str).str.zfill(2) + '-01')
#remove the yearmont column as it is unnessacary
df = df.drop('YearMonth', axis=1)
#replace sc with nan value
df = df.replace('^SC.*', np.nan, regex=True)
df.to_csv("../../data/processed/Cali_Monthly_Cases.csv", index=False) 