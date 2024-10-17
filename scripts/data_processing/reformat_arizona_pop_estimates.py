import pandas as pd

#read the xlsx file
df = pd.read_excel("../../data/raw/arizona-pop-est-1980to2023.xlsx")
#grab all the samples that contain the county total for that year which is most pertinent to us
df = df[df['County'].str.contains('Total', case=False, na=False)]
#reset index
df = df.reset_index(drop=True)
#remove place column as it is irrelavent
df = df.drop('Place', axis=1)
#relabel the county values so that they no longer contain the word Total
df['County'] = df['County'].str.replace('Total', '', case=False)
#save
df.to_csv("../../data/processed/arizona_pop_est_1980-2023.csv", index=False)
