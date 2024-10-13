import polars as pl

years = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
dfs = []
column_labels = ['Month','APACHE','COCHISE','COCONINO','GILA','GRAHAM','GREENLEE','LA PAZ','MARICOPA','MOHAVE','NAVAJO','PIMA','PINAL','SANTA CRUZ','YAVAPAI','YUMA','Total', 'Year']

for year in years:
    try:
        df = pl.read_excel("../../data/raw/Event Date by Calendar MonthYear (1994-2023).xlsx", sheet_name=str(year))
        #relabel the columns 
        labels = {df.columns[i]: str(df.row(1)[i]) for i in range(len(df.columns))}
        df = df.rename(labels)
        #remove the junk from the first couple row that is not data
        df = df.slice(2, len(df))
        #remove the junk from the last row which is not data
        df = df.slice(0, len(df) - 1)
        #relabel the month column
        df = df.rename({'None': 'Month'})
        # add a year column and populate it with the year of the dfs data
        df = df.with_columns(pl.lit(str(year)).alias('Year'))
        #if there is a missing column populate it with NaN values
        for column in column_labels:
            if column not in df.columns:
                df = df.with_columns(pl.lit("None").alias(column))
        #gets only the columns specified in the column labels
        df = df.select(column_labels)
        #add it to the array of dataframes
        dfs.append(df)
    except Exception as e:
        print(f"Error processing year {year}: {str(e)}")
#combine all the dataframes 
df = pl.concat(dfs, how="vertical")
#cast all the colums to integers
expressions = [
    pl.when(pl.col(col) == "None")
    .then(None)
    .otherwise(pl.col(col).cast(pl.Int64, strict=False))
    .alias(col)
    for col in df.columns
]
df = df.with_columns(expressions)

rename_dict = {
    'Month': 'Month',
    'APACHE': 'Apache',
    'COCHISE': 'Cochise',
    'COCONINO': 'Coconino',
    'GILA': 'Gila',
    'GRAHAM': 'Graham',
    'GREENLEE': 'Greenlee',
    'LA PAZ': 'La Paz',
    'MARICOPA': 'Maricopa',
    'MOHAVE': 'Mohave',
    'NAVAJO': 'Navajo',
    'PIMA': 'Pima',
    'PINAL': 'Pinal',
    'SANTA CRUZ': 'Santa Cruz',
    'YAVAPAI': 'Yavapai',
    'YUMA': 'Yuma',
    'Total': 'Total',
    'Year': 'Year'
}
df = df.rename(rename_dict)

#convert the year and month col to datetime
df = df.with_columns([
    pl.datetime(
        year=pl.col("Year"),
        month=pl.col("Month"),
        day=1
    ).alias("DateTimeISO")
])
#save to file
output_path = "../../data/processed/arizona_cm_combined_data.csv"
df.write_csv(output_path)

df.head()