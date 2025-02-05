# Data Processing Documentation

The data processing directory contains all datasets collected for the Harbinger project. A high-level script called "build_dataset.sh" executes Python commands to preprocess and assemble the final datasets used for model training. This document provides an overview of each build script's function.

The dataset is split into input (X) and output (Y) components. The input data is sequential time-series data covering both Arizona and California on a daily basis. It includes meteorological data, smoke particulate matter, general air particulates, pesticide usage, and population estimates. The raw data was collected at varying time resolutions. For data collected at higher-than-daily resolution, we calculated the daily mean. For data collected at lower-than-daily resolution, we duplicated values to create daily entries.

## reformat_arizona_cm_dataset.py
This script reformats the Arizona cocci (Coccidioidomycosis) dataset from the Arizona Department of Health Services. The raw data is located in "data/raw/Event Date by Calendar MonthYear (1994-2023).xlsx". The script first relabels all columns to match our naming conventions. The Excel file contains non-data artifacts in the first two rows and last row, which are removed from the dataset. A year column is added to align with the data collection period. Missing values are replaced with NaN values. Since the original data separates each year into individual sheets, these processing steps run in a loop over each year. After processing, all sheets are combined into a single dataset. All case numbers are converted to integers. The script then converts the year and month columns to datetime format and saves the processed dataset to "data/processed/arizona_cm_combined_data.csv".

## reformat_arizona_met_dataset.py
This script processes raw meteorological data from OpenWeatherAPI for the 15 counties in Arizona, spanning from 1979-2024. The data is located at "data/raw/06d609e5e744bedd55f76ad24b015bae.csv". The script renames all column labels to match our naming conventions. Several columns are dropped as they do not provide additional value: Datetime (redundant code of the actual date), weather main and weather icon (weather descriptors already captured in other columns), timezone (irrelevant), and weather id (another variation of existing weather descriptors).

The date column is converted to datetime format. The script then aggregates hourly samples into daily averages by calculating the mean. The final step removes years outside our output data range (1994-2023). The processed dataset is saved to "data/processed/Arizona_Weather_Data_Daily_Updates_1994_to_2023.csv".

## reformat_arizona_pop_estimates.py
This script processes raw data from the Arizona Office of Economic Opportunity, located at "data/raw/arizona-pop-est-1980to2023.xlsx". The script extracts all samples containing total population estimates for each year. The dataset is then relabeled to match our naming conventions and saved to "data/processed/arizona_pop_est_1980-2023.csv".

## reformat_cali_cm_dataset.py
This script reformats the cocci dataset from the California Department of Public Health. It loads raw data from "data/raw/Cocci Case Counts by County and Month, 2001-2022.xlsx". The script relabels columns to match proper formatting. Since the original data was provided in .xlsx format, artifacts are removed during conversion to CSV. The year-month column is split into two separate columns, then converted into a datetime formatted column. Missing values are replaced with NaN values, and the formatted dataset is saved to "data/processed/Cali_Monthly_Cases.csv".

## reformat_cali_met_dataset.py
This script reformats meteorological data from OpenWeatherAPI for the 48 California counties with the highest cocci case counts. The raw data spans from 1979 to 2024 with hourly updates. The script loads data from "data/raw/open_weather_california.csv" and applies the same processing steps as reformat_arizona_met_dataset.py. The only difference is the timeline - while Arizona's cocci data spans 1994-2023, California's spans 2001-2021. The script adjusts the meteorological data to match this period and saves it to "data/processed/California_Weather_Data_Daily_Updates_2001_to_2022.csv".

## reformat_cali_pop_estimates.py
This script processes population estimates that align with the California cocci dataset timeline. The data comes from the US Census Bureau across three raw files:

- ../../data/raw/co-est2019-annres-06.xlsx
- ../../data/raw/co-est2023-pop-06.xlsx
- ../../data/raw/population_2000_2010(2).xlsx

The script first removes artifacts from the Excel files. It then transforms the data to create a year column, with additional columns containing population estimates for each year. The three datasets are concatenated into a single dataset covering 2000-2023. The final dataset is saved to ../../data/processed/California_Population_2000-2023.csv.

## reformat_cali_pesticides_dataset.py
This script processes California pesticide data from the California Department of Pesticide Regulation, covering 2001-2022 across all California counties. The script reads data from ../../data/raw/davis_pesticides_2001-22.csv and converts the chemname and county columns to string data types. Due to a bug likely related to CSV formatting issues in pandas, the script saves and rereads the CSV using pandas to resolve these issues. The columns are then sorted by year, month, county, and chemname. All column labels are converted to lowercase to match naming conventions. The script resets the index and creates a datetime column from the month and year columns.

## collect_aqs_data.py
This script collects data from the AQS API provided by the US Environmental Protection Agency. It gathers the following pollutants:
- 88101 - PM2.5 (Fine Particulate Matter) - Microscopic particles that enter deep into lungs and bloodstream, from smoke, vehicle emissions, and industrial sources
- 81102 - PM10 (Particulate Matter) - Larger inhalable particles including dust, pollen, and mold. Less harmful than PM2.5 but still affects respiratory health
- 85101 - TSP (Total Suspended Particles) - All airborne particles of any size, measuring general air cleanliness
- 88502 - PM2.5_nonref (Non-reference PM2.5) - Same as PM2.5 but measured using non-reference methods, typically continuous monitors
- 44201 - Ozone (O₃) - Ground-level air pollutant formed by chemical reactions between sunlight and other pollutants, a major part of smog
- 42401 - SO2 (Sulfur Dioxide) - Sharp-smelling gas from burning fossil fuels, particularly coal and oil, contributing to acid rain
- 42101 - CO (Carbon Monoxide) - Odorless, colorless gas from incomplete combustion that blocks oxygen absorption in blood
- 42602 - NO2 (Nitrogen Dioxide) - Reddish-brown gas from vehicles and power plants, causing respiratory problems and contributing to smog

The script collects data from 2000-2022 for California and 1993-2023 for Arizona to match our cocci data timeline. For each pollutant, it creates a separate dataset covering its full time range and saves it to the raw data directory. For example, it creates a dataset for PM2.5 spanning 2000-2022 for California.

## reformat_az_ca_aqs_data.py
This script processes the AQS data collected for both California and Arizona. It removes unnecessary columns that don't contribute to our research: 'state_code', 'county_code', 'site_number', 'parameter_code', 'cbsa_code', 'cbsa', and 'date_of_last_change'. The script then saves three versions of the processed data: one with Arizona pollutants, one with California pollutants, and one combining pollutants from both states.

## reformat_all_dates.py
This script processess all the datasets from above and turns the columns to all lowrer for a better naming convention. It also converts all dfs to have a date col in datetime format

