# Data Analysis README

## Intro 

This is the source of all the documentation for the data analysis conducted. If you want to know more details about the data that was gathered please read the [Data Processing README](../data_processing/README.md). Our methodology was to start to unveil more information about the data before continuing to process it. all the data up to this point has had minor changes mainly fixing it so that it would al follow a similar naming convention, and formating the data so that it is more releveant to the research we are doing. 

## general_data_analysis_info.py
This script gathers all the general information about the datasets that are being analyzed it writes the info about dtypes, the head and tail of the dataset all to [general_info_dataset_analysis](../../data/analysis_data/general_info_dataset_analysis_20250115_211020.txt)

## calculate_missing_values_percentages.py
This script does as the name suggests and it runs through all of the datasets that we have and looks at each column from each dataset to see the percent of missing data. a new dataset is created that houses all this information called [missing_values_percentages](../../data/analysis_data/missing_values_percentages.csv). this dataset has 4 columns: the dataset the percentages it was taken from, the column, the missing percentage, and the data type.

