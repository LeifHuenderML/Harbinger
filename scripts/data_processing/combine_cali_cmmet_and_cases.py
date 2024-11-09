import pandas as pd

df = pd.read_csv("../../data/processed/cali_combined_weather_and_case.csv")
pop_df = pd.read_csv("../../data/processed/California_Population_2000-2023.csv")

#remove uneeded columns
pop_df = pop_df.drop(['Year','Month'], axis=1)
#reshape the df so that is will merge nicely
pop_df = pop_df.melt(
    id_vars=['date'],           
    var_name='County',          
    value_name='Population'     
)
#fix naming convention
pop_df = pop_df.rename(columns={'date':'Date'})

#convert pop df to be daily values
pop_df['Date'] = pd.to_datetime(pop_df['Date'])

pop_df_indexed = pop_df.set_index(['Date', 'County'])

date_range = pd.date_range(
    start=pop_df['Date'].min(),
    end=pop_df['Date'].max(),
    freq='D'  
)

counties = pop_df['County'].unique()

new_index = pd.MultiIndex.from_product(
    [date_range, counties],
    names=['Date', 'County']
)

daily_pop_df = pop_df_indexed.reindex(new_index).groupby('County').ffill()

daily_pop_df = daily_pop_df.reset_index()


#merge pop df with df 
df['Date'] = pd.to_datetime(df['Date'])
daily_pop_df['Date'] = pd.to_datetime(daily_pop_df['Date'])

df = df.merge(
    daily_pop_df[['County', 'Date', 'Population']],  
    on=['County', 'Date'],                     
    how='left'                                 
)

df['Rates'] = (df['Cases'] / df['Population']) * 100000

df.to_csv("../../data/processed/cali_combined_weather_population_and_rate.csv", index=False)