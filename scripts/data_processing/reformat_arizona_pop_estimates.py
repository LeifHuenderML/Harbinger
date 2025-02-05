import pandas as pd

def reshape_population_data(df):
    """
    Transforms population data from wide format (years as columns) to long format
    (year and population as separate columns).
    
    Parameters:
    df (DataFrame): Input DataFrame with 'County' and year columns
    
    Returns:
    DataFrame: Reshaped DataFrame with columns: 'county', 'year', 'population'
    """
    # Create a copy to avoid modifying the original
    df_long = df.melt(
        id_vars=['County'],
        var_name='year',
        value_name='population'
    )
    
    # Clean up county names (strip whitespace)
    df_long['County'] = df_long['County'].str.strip()
    
    # Convert year to datetime
    df_long['year'] = pd.to_datetime(df_long['year'], format='%Y')
    
    # Sort values
    df_long = df_long.sort_values(['County', 'year'])
    
    # Reset index
    df_long = df_long.reset_index(drop=True)
    
    return df_long


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
# Example usage:
df_transformed = reshape_population_data(df)
df_transformed.to_csv("../../data/processed/arizona_pop_est_1980-2023.csv", index=False)

# df_transformed.head(50)