September 1 - 7

- made final edits to the paper
- did a deep dive looking for more data
- found county annual reports for arizona from 2006-2024 https://www.azdhs.gov/preparedness/epidemiology-disease-control/valley-fever/index.php#data-reports-publications
- submitted several data request forms for more granular cm data
- created this new repository for the next stint of my research
- wrote the readme for harbinger
- started defining the structure for a long view of what is to come from my research
- found smoke particulate matter data for california  https://github.com/echolab-stanford/daily-10km-smokePM
- updated the data base to include air quality, smoke pm, and met data 
- waiting to look for weather data for arizona until i get response about cm data from arizona
- weather data to purchase would only be 150 for all of arizona
- made a data request to arizona department of environmental quality for air quality data
- wrote a whitepaper draft for the grant application john suggested
- started exploring all the data collected trying to get it cleaned and aligned all into one dataset
- added toxicity data 
- added the rest of the data sent to me from the AQMIS

September 8-14

- got the link for maricopa county data request https://urldefense.com/v3/__https://phdra.maricopa.gov/__;!!JYXjzlvb!ni8lfOLNdqI4EjEK6G0dxK6UucqskeLLaJE-Hdg9Kbte2Y5LKKhWhukQ85yE9ATvFA0q5kv7Piosw_5YmY9BOBBpF2-Wc3zDU8STAUR3$
- got the link for adhs data request https://urldefense.com/v3/__https://app.smartsheet.com/b/form/9bbeb6d02c53462598b267705825aabe__;!!JYXjzlvb!ni8lfOLNdqI4EjEK6G0dxK6UucqskeLLaJE-Hdg9Kbte2Y5LKKhWhukQ85yE9ATvFA0q5kv7Piosw_5YmY9BOBBpF2-Wc3zDU0nuR9Gx$
- emailed Dr alves fosss a request for endorsement
- made more improvements to the whitepaper
- made the final edits to the ValleyForecast paper
- made endorsement requests to 6 people 
- sent john the final draft of the paper
- sent sarah the cm incidence figure
- imported all the new data sarah gathered
- created a CV for the whitepaper and sent it to sarah
- registered an account with Journal of Biomedical Informatics
- registered an orcid id
- created a cover letter for paper submission
- created a statement of significance

September 15-21
- created a graphical abstract
https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract
- corresponded with the arizona department of health service to get cm coundy monthly updates from 1994 to present
- long meeting over grant discussion
- reviewed the Ro3 grant to assess deeper on its applicability for our research
- revised the visual abstract
- submitted the paper for review in the journal of biomedical informatics
- reviewed the atd grant to assess deeper on its applicability for our research
- emailed the people on the october 10 event
- reviewed the eeid grant to assess deeper on its applicability for our research
- read throug the grant proposal whitepaper that sarah created
- Dr. Asghari Ilani agreed to endorse me on arXiv so i corresponded with him more and will hopefully be able to post the preprint soon
- updated the research gate preprint to include the new edits made to the paper
- found the coccihub team meeting link https://teams.microsoft.com/l/meetup-join/19%3ameeting_OWU5OWU3ZDctMWIxOS00OTFkLTk0YWQtNzgxOGExNjVmNzlj%40thread.v2/0?context=%7b%22Tid%22%3a%229ce70869-60db-44fd-abe8-d2767077fc8f%22%2c%22Oid%22%3a%228df7eca6-7a72-4ecf-a2d3-b1c3b272fd3d%22%7d 
    - Meeting ID: 275 197 179 725
    - Passcode: GzuQPM
    - Thu Oct 10, 2024 5pm – 6pm (UTC)

September 22-28
- recieved the montly update for counties of cm incidence in california
- finalized the grants that we should apply to 
- created a conda environment and a setup script
- assembled all the counties in arizona that need to be purchased
- ordered all the arizona data
- started writing a script to process all the arizona monthly data
- read through the email that mary sent me that had more info on the ro3
- created and sent the email that asks questions to dr soule to mary.
- continued working on extracting the arizona valley fever data, turned out to be more challenging than first imagined
- compiled the information and send mary and teryy the eamil with the compiled information "we are trying to understand the grant"
    - we are tyring to figure out the differenct between ro3 and ro3 attached to a funding opoptuinty
    - if terry doesnt know to joel knisley

September 29- October 5
- continued trying to parse the valley fever data from arizona
- retrieved the arizona meteorological data
- uplodaed the meteorological data to the cloud
- met with sarah and mary to discuss the grants further
- did the presentation over the grants with sarah for john
- finished verifying that the reworking of the cm data was successful for arizona
- uploaded the new df to the dropbox
- sat  in for the meeting with john and leda
- preprocessed the meteorological data 
- met with john and sarah to discuss the grants 
- emailed lacey and kevin the grant that fits their stuff    
# notes from leda meeting
    - r21 early career one good for mary and fits with our research two years enough to support a postdoc researcher, due in january
    - washu has giant medical program and is getting a new updated med database extending to 2024, they are open to collaboration for free just want the accreditaton for collaboration
    - neihs or naiaid woulld be the two ones that are fittingg for the r21
    - looking at the smoke pm matter and pm matter and relation to infectous disease, very new field that is why there is not much development yet on it
    - leda has a good network of people that are willing to look over our porposal - jr thompsan is a very good person to reach out to - with the r21 we would have to identify a mentor collaborator and he might be helpful
    - sensors for stubble burning to monitor plant disease transmission with the deq
    - infrastructure type grants, epa,  sbir grants, mackel engineering , for development of sensors funding
    - dusttracker doesnt saturate at high pm levels, thats what the epa uses
    - look up for john if there is a big grant for smoke pm and infectous disease and one for remotes sensing with nasa

October 6 - 13:
- read over all the meeting notes about coccihub
- relabelled the columns for the arizonda data
- renamed all the counties for the arizona data
- removed 'DateTime', 'WeatherMain', 'WeatherIcon', 'TimeZone', 'WeatherID' from the arizona data
- converted arizona date to datetime
- created the cleaned dataset data/processed/Arizona_Weather_Data_Hourly_Updates.csv
- onehot encoded the weather description column
- created the data/processed/Arizona_Weather_Data_Hourly_Updates_With_One_Hot_Encoding.csv"
- created data/processed/Arizona_Weather_Data_Daily_Updates_With_One_Hot_Encoding_1979_to_2024.csv"
- created data/processed/Arizona_Weather_Data_Daily_Updates_With_One_Hot_Encoding_1994_to_2023.csv"
- merged the weather data and the cm data so that each sample in the weather data would have that counties monthly case number
- did a thourough sanity check to ensure that there are no mismaches betwen the merging of the datasets
- created this new dataset "../../data/processed/Arizona_Combined_Weather_Data_And_Case_Number_Daily_Updates_With_One_Hot_Encoding_1994_to_2023.csv"
- shared "../../data/processed/Arizona_Combined_Weather_Data_And_Case_Number_Daily_Updates_With_One_Hot_Encoding_1994_to_2023.csv" to the dropbox
- reviewed sarahs codebase to see what she did for converting the cases to rates for california

October 14-19
- reached out to NIH staff for clarification on the RO3 Grant
- found the dataset for population estimates of arizona for 1980-2023 https://oeo.az.gov/population/estimates
- wrote a script to grab all the usefull information from the population estimates and convert it into a usable df
- went back and added better commenting to the scrips i have worked on
- emailed sarah that we need to add billing to dropbox teams
- updated past scripts to not save with index
- it took a lot of work but i was able to get the rates and population added to the dataset, wrote the code for it in combine_arizona_cmet_and_rates.py
- created a new dataset called "../../data/processed/Arizona_Combined_Dataset_1994_to_2023.csv"
- meeting notes
    -we will be presenting the whole idea of comorbitidies, we will prestend to the nih and will like their funding too, put an aspect on how this will hepl with functional medicine,
    - dr malones is a concierge physiscian, he had an idea to take all his ptients biometric readings, he is very interested in data driven medicine
    - we are doing data driven scientific discovery
    - time limit 2 - 3 slides 
    - she is goint into correlations and explainability and i will go into the predictive model
    - meeting at 12:30 on monday 
- got enrolled in the citi program for irb investogators and student researchers
- sent kristopher waynant the posters from last summers research
- sent kristopher waynant the papers from last summers research
- sent kristopher waynant the links from last summers research
- sent kristopher waynant a write up about the experiience from last summers research 
- took the b2b survey
- updated my cv as kristhopher waynant asked

