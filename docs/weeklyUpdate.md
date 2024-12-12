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

October 20-26
- reformated the cali cm dataset so that it is in the same format we need
- wrote the script to reformat the california meteorological dataset
- rewrote the script to reformat the arizona meteorological datastet to be more like the california one, i like the way that pandas does it more
- met with sarah and went over the presentation
- wrote a build dataset script that runs all the python scripts to build out the complete dataset with checkpointing
- dropped the weather description from the datasets
- rewrote all the build scripts to phase out polars in favor of pandas
- worked on the pesticides but then realized that the data was yearly not monthy
- went through the california population estimates dataset and wrote a script converting them all to the correct format

October 27 - November 2
- was missing some california porulation estimate data so i had to go through and had to go through and reformat the new data
- worked on the slides for the persentation with milonas
- met with sarah to go over the presentation and practice
- met with sarah john and milonas and presented on the harbinger project
- combined the population estimates with the rest of the california data
- read through th edescription of the imci grant again
- put together a list of priorities that we want to expand on for my part and wrtie about 1 page on top of that
- got the most recent draft of the paper
- started rewriting the imci grant proposal

November 3 - 9
- continued rewriting the imci grant
- added the rates to the case data
- combined the met data with the rest of the california data
- started preprocessing the air quality data
- went through and made more edits to the imci grant
- came up with a list of names that might be more fitting for our model
- went through the pesticides dataset and there are over 1200 unique pesticides, including the valuues of measurements made it would expand our dataset by almost 4000 columns
- should we only include relevant ones that have been studied, i can make multiple final datasets with one that includes it and one that doesnt too
- wrote the transcript for the research gate video
- wrote up a complimentary document for the research gate video


November 10-23
- updated the data prep script for valley forecast to make it so that the data is split by years
- created 2 new datasets one where there it no training augmentation train2 and one where there is but the years ares split accordingly train3
- retrained the models
- went through the entire paper and changed everything to the naming convention they wanted
- added a section in future research directions to discuss Investigating CM underdiagnosis patterns through integration of demographic and health data, particularly focusing on vulnerable populations (e.g., AIDS and cancer patients) who typically present more severe symptoms. This analysis could help quantify reporting bias and develop correction factors for incidence predictions in underserved communities, ultimately improving model accuracy across diverse populations
- Removed "[cite Beck and another paper that uses blocking for llms]" on page 8 paragraph 4. 
- addressed this concern 
    2. The validation RMSE is notably lower than the test RMSE, raising questions about the proposed model's true performance.
     Additional discussion and analysis on this discrepancy would strengthen the evaluation.
    The concern about the discrepancy between validation and test RMSE has been addressed through two additions to the paper:
    1.	A comprehensive analysis of the validation-test performance gap was added to Section 4.1 (Model Performance Metrics), paragraph 4, page 12:
    "It's worth noting that while the xLSTM performed best on both validation and test sets, there's a significant 
    difference between its validation RMSE (68.33) and test RMSE (273.78). This large gap, common across all models 
    but particularly pronounced in the more complex architectures, can be attributed to several factors. First, the 
    temporal nature of the data means weather patterns and cocci incidence relationships may evolve over time, 
    making generalization challenging. Second, the test set may contain more extreme or unusual cases than the 
    validation set. Third, despite our regularization efforts, the models' capacity to memorize training patterns 
    may be leading to overfitting. The simpler MLP model shows more consistent performance between validation 
    and test sets, which could indicate better generalization despite not achieving the lowest validation RMSE, suggesting that model complexity plays a significant role in the size of this performance gap."
    2.	The future research directions in Section 5 were improved with a more detailed point addressing
     validation frameworks (item 8, page 14):
    "8. Implementing sophisticated validation frameworks, including temporal-aware cross-validation techniques, 
    ensemble methods combining complementary architectures, and enhanced regularization approaches to address 
    the observed validation-test performance gap and improve model generalization."
- note for the timeline of the new dataset 
    Loading ../../data/original/rates.xlsx
    Loaded ../../data/original/rates.xlsx
    Loading weather.csv
    Loaded weather.csv
    Merged DF shape: (385680, 25)
    X tensor shape: torch.Size([1056, 365, 19]), Y tensor shape: torch.Size([1056])
    Split years - Train: ≤2017, Val: 2018-2020, Test: ≥2021
    Train Shapes: (torch.Size([17136, 365, 19]), torch.Size([17136])), 
    Validation Shapes: (torch.Size([144, 365, 19]), torch.Size([144])), 
    Test Shapes: (torch.Size([96, 365, 19]), torch.Size([96]))
    Train Size: 17136, Val Size: 144, Test Size: 96
    Train, val, and test datasets saved
    avg df shape (1056, 20)
- note for the performance of the models being trained
    (harbinger) intellect@intellect:~/Documents/Research/ValleyForecast/src/analysis$ python3 create_cross_model_predictions_v2.py
    training baseline
    RMSE: 422.11840785714605
    Training Time: 0.00025081634521484375
    finished training baseline
    training mlp
    torch.Size([844, 6935])
    finished training mlp
    training lstm
    Epoch: 1/50
    ---------
    Train Loss RMSE: 335.5723623849774, Validation Loss RMSE: 77.30672882916224
    Epoch: 2/50
    ---------
    Train Loss RMSE: 330.2244171787713, Validation Loss RMSE: 74.6672844634156
    Epoch: 3/50
    ---------
    Train Loss RMSE: 323.09477466715174, Validation Loss RMSE: 98.05405725685831
    Epoch: 4/50
    ---------
    Train Loss RMSE: 316.60329904052065, Validation Loss RMSE: 90.40813086748959
    Epoch: 5/50
    ---------
    Train Loss RMSE: 323.46599872123494, Validation Loss RMSE: 90.61068111556474
    Epoch: 6/50
    ---------
    Train Loss RMSE: 323.268162396114, Validation Loss RMSE: 87.12624766525046
    Epoch: 7/50
    ---------
    Train Loss RMSE: 323.2447760542995, Validation Loss RMSE: 99.92497429712579
    Epoch: 8/50
    ---------
    Train Loss RMSE: 316.78972165403826, Validation Loss RMSE: 90.7342774614165
    Epoch: 9/50
    ---------
    Train Loss RMSE: 323.26175685156204, Validation Loss RMSE: 85.11018249341555
    Epoch: 10/50
    ---------
    Train Loss RMSE: 323.3218051566482, Validation Loss RMSE: 97.00581326712945
    Epoch: 11/50
    ---------
    Train Loss RMSE: 322.3301345399031, Validation Loss RMSE: 89.50680635453966
    Epoch: 12/50
    ---------
    Train Loss RMSE: 323.22585562535306, Validation Loss RMSE: 87.36133404170792
    Epoch: 13/50
    ---------
    Train Loss RMSE: 323.07888764507214, Validation Loss RMSE: 90.87569648654178
    Epoch: 14/50
    ---------
    Train Loss RMSE: 323.1213490508479, Validation Loss RMSE: 92.01606676536848
    finished training lstm
    training xlstm
    Epoch 1 Train RMSE Loss: 335.6777, Val RMSE Loss: 83.5544
    Epoch 2 Train RMSE Loss: 335.7345, Val RMSE Loss: 81.3989
    Epoch 3 Train RMSE Loss: 334.7183, Val RMSE Loss: 81.7679
    Epoch 4 Train RMSE Loss: 332.1388, Val RMSE Loss: 79.9122
    Epoch 5 Train RMSE Loss: 328.1723, Val RMSE Loss: 71.1586
    Epoch 6 Train RMSE Loss: 324.8171, Val RMSE Loss: 87.3750
    Epoch 7 Train RMSE Loss: 323.4828, Val RMSE Loss: 90.9164
    Epoch 8 Train RMSE Loss: 322.7312, Val RMSE Loss: 91.9510
    Epoch 9 Train RMSE Loss: 323.3852, Val RMSE Loss: 85.8020
    Epoch 10 Train RMSE Loss: 322.8997, Val RMSE Loss: 93.2280
    finished training xlstm
    running xlstm evaluations
    finished xlstm evaluations

    Outer Fold: 1/5
    Evaluating baseline
    baseline RMSE: 533.9215
    Evaluating mlp
    mlp RMSE: 412.5679
    Evaluating lstm
    lstm RMSE: 401.9865
    Evaluating xlstm
    xlstm RMSE: 401.1520

    Outer Fold: 2/5
    Evaluating baseline
    baseline RMSE: 419.6630
    Evaluating mlp
    mlp RMSE: 143.0950
    Evaluating lstm
    lstm RMSE: 140.6543
    Evaluating xlstm
    xlstm RMSE: 141.9972

    Outer Fold: 3/5
    Evaluating baseline
    baseline RMSE: 459.5896
    Evaluating mlp
    mlp RMSE: 288.2575
    Evaluating lstm
    lstm RMSE: 277.5649
    Evaluating xlstm
    xlstm RMSE: 277.3120

    Outer Fold: 4/5
    Evaluating baseline
    baseline RMSE: 479.3414
    Evaluating mlp
    mlp RMSE: 357.9233
    Evaluating lstm
    lstm RMSE: 341.8964
    Evaluating xlstm
    xlstm RMSE: 341.4152

    Outer Fold: 5/5
    Evaluating baseline
    baseline RMSE: 450.0500
    Evaluating mlp
    mlp RMSE: 264.2976
    Evaluating lstm
    lstm RMSE: 254.3546
    Evaluating xlstm
    xlstm RMSE: 254.2281

    Final Cross-Validation Results:
    ================================
    BASELINE:
    RMSE: 468.5131 (±37.9535)
    MLP:
    RMSE: 293.2283 (±91.4648)
    LSTM:
    RMSE: 283.2913 (±88.0211)
    XLSTM:
    RMSE: 283.2209 (±87.3086)



todo 
- run a correlation matrix onf the pesticide
- did the full training for the irb investigators and student researchers
- did the fulll trining for the export controls  for studnents


