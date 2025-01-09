# Data Processing Documentation

The data processing directory handles the incorporation of all the datasets gathered for harbinger. The high level script labelled "build_dataset.sh" is a script that runs the python commands to go through and preprocess and assemble the final datasets that we are training our models on. Below I will go over the entire overview of what each build script does. 

The dataset consists of the input dataset and the output dataset ie x y dataset. The data that goes into constituding x is sequential time based data that covers both arizona and california on a daily basis it includes meteorological data, Smoke particaulate matter, generall air particulate. pesticide usage, and population estimates. the data that was gathered covered a different resolution of timeline, so for any data that was gathered in which the resolution was higher than daily we collected the mean for the day. for any data where the resoluation was lower than daily we would duplicate out to create it into daily.

## reformat_arizona_cm_dataset.py
reformat_arizona_cm_dataset.py as in the name reformats the arizona cocci (cm) dataset. It loads the raw data gathered provided to us from "". The raw data is from the "data/raw/Event Date by Calendar MonthYear (1994-2023).xlsx" directory. It starts by relabelling all the colunmns to the proper names. Since it was loaded as a .xlsx file there was artifacts in the first 2 and last row that is not data. This is removed from the dataset. We then add a year column that aligns whith when the data was gathered. We handle any missing values by replacing them with NaN values. The original data had each year on a seperate sheet so all the actions above happen in a loop going over each year. After this we go through and combine all the sheets to form one dataset. All the case numbers get cast to integers. Finally we convert the year and month col to datetime and then save the newly created dataset to "data/processed/arizona_cm_combined_data.csv".

## reformat_arizona_met_dataset.py
This script takes the raw meteorological data gathered from OpenWeatherAPI, this data is from the 15 counties in arizona and covers all the time between 1979-2024 in the location "data/raw/06d609e5e744bedd55f76ad24b015bae.csv". We go through and rename all the columns labels and the columns to match our naming conventions. We drop the columns that do not serve a purpose for us. Namely Datetime which is just a code we allready have the actual date, weather main and weather icon which are just more descriptors for the weather which is allready captured in other columns. Timezone this is irrelevant. and weather id which is another variation off of the weather descriptors that we have. 
We then convert the date column to the datetime format and save a newly created. We then need to aggregate the samples so that is is not captured hourly but the daily average by capturing the mean. Finally we remove the years that our output data does not match to ie the output data only ranges from 1994-2023. we save this newly created dataset to "data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv"

## reformat_arizona_pop_estimates.py
This script takes the raw data provided by "" located in the  "data/raw/arizona-pop-est-1980to2023.xlsx" directory. It grabs all the samples that contian the total population estimates for that year. Relabells the dataset to mathc our naming conventions then saves it to the file path "data/processed/arizona_pop_est_1980-2023.csv"

## combine_arizona_cm_and_met.py
This script is going to be depreciated because the way that we plan on using the data has changed

## combine_arizona_cmmet_and_rates.py
This script is going to be depreciated because the way that we plan on using the data has changed

## reformat_cali_cm_dataset.py
This script reformats the cocci dataset provided to us from the california department of public health. it loads the raw data in from "data/raw/Cocci Case Counts by County and Month, 2001-2022.xlsx". it then relabells the columns to pe in the proper formatting. The original data was provided to us in .xlsx formatting so we needed to remove artifacts from it to make it into a  csv. We spli the year month column into 2 seperaate ones, and then converde it int oa datetime formatted column. Finallly we replce any missing values with NaA values and save the newly formatted dataset to "data/processed/Cali_Monthly_Cases.csv" 

## reformat_cali_met_dataset.py
This script reformats the meterological data provided to us from OpenWeatherAPI. the raw data covers the 48 counties in california with the highest number of case counts.  the timeline of the raw data spans from 1979 to 2024 and is on an hourly updated basis. we start by loading the raw data from "data/raw/open_weather_california.csv", all the same changes are made to this as the reformat_arizona_pop_estimates.py from above. The only difference is that the cocci case data is from a different timeline than the arizona coccis data so we slim the met datas timeline down to being from 2001-2021, and save it to "data/processed/California_Weather_Data_Daily_Updates_2001_to_2022.csv"

## reformat_cali_pop_estimates.py
This script processes the population esimates from the same years that match up with the california cocci dataset. This data was gathered from "". The raw data is from 3 seperate files under the raw folder :
../../data/raw/co-est2019-annres-06.xlsx
../../data/raw/co-est2023-pop-06.xlsx
../../data/raw/population_2000_2010(2).xlsx
It first removes all the artifacts from the xlsx file that it was loaded in from. I then does a transformation so that  there is a year column and then each column is the values of the population estimates for that given year. The three datasets are concatenated into one large dataset containiong the years 2000 - 2023. This final dataset is saved to ../../data/processed/California_Population_2000-2023.csv

## python3 combine_cali_cm_and_met.py
This script is going to be depreciated because the way that we plan on using the data has changed

## python3 combine_cali_cmmet_and_cases.py
This script is going to be depreciated because the way that we plan on using the data has changed

