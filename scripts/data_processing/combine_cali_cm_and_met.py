import pandas as pd
import numpy as np

met_df = pd.read_csv("../../data/processed/California_Weather_Data_Daily_Updates_2001_to_2022.csv")
cm_df = pd.read_csv('../../data/processed/Cali_Monthly_Cases.csv')



def spread_monthly_cases(df):
    df['Date'] = pd.to_datetime(df['Date'])  
    expanded_data = []
    for _, row in df.iterrows():
        start_date = row['Date'].replace(day=1)
        end_date = start_date + pd.offsets.MonthEnd(1)
    
        month_dates = pd.date_range(
            start=start_date,
            end=end_date,
            freq='D'
        )
        for date in month_dates:
            expanded_data.append({
                'County': row['County'],
                'Cases': row['Cases'],
                'Year': row['Year'],
                'Month': row['Month'],
                'Date': date
            })    
    expanded_df = pd.DataFrame(expanded_data)
    expanded_df = expanded_df.sort_values(['County', 'Date']).reset_index(drop=True)

    return expanded_df

cm_df = spread_monthly_cases(cm_df)
cm_df = cm_df.drop(['Month', 'Year'], axis=1)

cm_df['Date'] = pd.to_datetime(cm_df['Date'])
met_df['Date'] = pd.to_datetime(met_df['Date'])
df = pd.merge(
        met_df,
        cm_df,  
        on=['County', 'Date'],
        how='left'  
    )

df.to_csv("../../data/processed/cali_combined_weather_and_case.csv", index=False)