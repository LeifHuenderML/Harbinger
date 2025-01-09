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
- finished the paper and resubmit for publication

December 8 - January 8
- updated readme to be more accurate with the projects current status
- created a readme file in dataprocessing so that there is more information on what all the build scripts are doing
- updated the reformat_arizona_met_dataset.py to no longer save multiple output files. it didnt make any sense because we only really need the years that match the output data and i was saving  versions with years beyond the output data. 
- added a lot of documentation to the data processing page
- recieved the changes that needed to be made to the paper
- went through and made all the subsequent edits
- updated the manuscript upload
- updated the marked manuscript upload
- updated the response to reviews
- added more documentation to the data preprocessing
- ended up removing 4 scripts that were being used to preprocess data that ended up not being very helpful
- had an idea to try and find the top correlative chemical usages spent some time working on it got these results


    Top 10 Counties with Highest Total Coccidioidomycosis Cases:
County
Kern               39238.0
Los Angeles        11560.0
Fresno              9331.0
Tulare              4393.0
San Diego           3853.0
San Luis Obispo     3156.0
Orange              2540.0
Riverside           2495.0
Ventura             2310.0
Kings               2151.0
Name: Cases, dtype: float64

Top pesticides with highest relative usage in KERN County:
Relative usage ratio:
Chemname
SULFURIC ACID                                                               75385.589509
DAZOMET, SODIUM SALT                                                         4075.368770
RONNEL                                                                       1378.840411
ALKYL* DIMETHYL BENZYL AMMONIUM CHLORIDE *(67%C12, 25%C14, 7%C16, 1%C18)      816.715449
METALAXYL                                                                     208.390306
NAA, ETHYL ESTER                                                               83.800904
CHLORDANE                                                                      77.191524
ALKYL PYRIDINES, MIXED                                                         76.923077
HARPIN PROTEIN                                                                 75.268937
TOXAPHENE                                                                      63.677564
dtype: float64

Actual pounds used:
Chemname
SULFURIC ACID                                                                  7977.62
DAZOMET, SODIUM SALT                                                            516.83
RONNEL                                                                           17.20
ALKYL* DIMETHYL BENZYL AMMONIUM CHLORIDE *(67%C12, 25%C14, 7%C16, 1%C18)    1319468.08
METALAXYL                                                                    112256.09
NAA, ETHYL ESTER                                                              41529.16
CHLORDANE                                                                       232.43
ALKYL PYRIDINES, MIXED                                                            7.50
HARPIN PROTEIN                                                                 4245.45
TOXAPHENE                                                                      1136.19
Name: KERN, dtype: float64

Top pesticides with highest relative usage in LOS ANGELES County:
Relative usage ratio:
Chemname
ALKYL (95%C14, 3%C12, 2%C16) DIMETHYL BENZYL AMMONIUM CHLORIDE    5405.063342
DEET, OTHER RELATED                                                241.783734
DEET                                                               209.378533
OIL OF CEDARWOOD                                                   180.301746
LACTIC ACID                                                        117.087176
HEXAFLUMURON                                                       101.037423
DICHLOBENIL                                                        100.248313
BROMACIL, LITHIUM SALT                                              60.235178
N-OCTYL BICYCLOHEPTENE DICARBOXIMIDE                                47.911601
NICARBAZIN                                                          40.823989
dtype: float64

Actual pounds used:
Chemname
ALKYL (95%C14, 3%C12, 2%C16) DIMETHYL BENZYL AMMONIUM CHLORIDE      1026.96
DEET, OTHER RELATED                                                  106.75
DEET                                                                2028.34
OIL OF CEDARWOOD                                                       0.34
LACTIC ACID                                                           21.73
HEXAFLUMURON                                                          96.98
DICHLOBENIL                                                       828288.91
BROMACIL, LITHIUM SALT                                             35455.65
N-OCTYL BICYCLOHEPTENE DICARBOXIMIDE                               67291.79
NICARBAZIN                                                           126.53
Name: LOS ANGELES, dtype: float64

Top pesticides with highest relative usage in FRESNO County:
Relative usage ratio:
Chemname
SODIUM ARSENITE                                                       11543.817644
DISODIUM CYANODITHIOIMIDO CARBONATE                                    5910.454529
SODIUM DODECYLBENZENESULFONATE                                          567.968256
ALKYL* DIMETHYL BENZYL AMMONIUM CHLORIDE *(58%C14, 28%C16, 14%C12)      206.797658
TRICHLORFON                                                             106.199495
ORTHO-PHENYLPHENOL                                                       68.129406
PARA-TERT-AMYLPHENOL                                                     66.733927
DICHLORPROP BUTOXYETHANOL ESTER                                          53.712328
ENDOSULFAN                                                               45.988046
ORTHO-BENZYL-PARA-CHLOROPHENOL                                           38.887288
dtype: float64

Actual pounds used:
Chemname
SODIUM ARSENITE                                                          220.50
DISODIUM CYANODITHIOIMIDO CARBONATE                                      460.74
SODIUM DODECYLBENZENESULFONATE                                            11.76
ALKYL* DIMETHYL BENZYL AMMONIUM CHLORIDE *(58%C14, 28%C16, 14%C12)      2094.65
TRICHLORFON                                                             7730.98
ORTHO-PHENYLPHENOL                                                     56165.74
PARA-TERT-AMYLPHENOL                                                   19600.19
DICHLORPROP BUTOXYETHANOL ESTER                                          197.38
ENDOSULFAN                                                            502641.95
ORTHO-BENZYL-PARA-CHLOROPHENOL                                         32588.37
Name: FRESNO, dtype: float64

Top pesticides with highest relative usage in TULARE County:
Relative usage ratio:
Chemname
DIFENACOUM                                    94.571110
AMMONIUM SULFAMATE                            34.632289
COPPER SULFATE (BASIC)                        32.456148
SORBITOL OCTANOATE                            29.579296
DICAMBA, DIMETHYLAMINE SALT, OTHER RELATED    20.590742
COPPER OXYCHLORIDE                            19.749800
2,4-D, PROPYL ESTER                           19.642242
PYRIPROXYFEN                                  19.617645
E-8-DODECENYL ACETATE                         19.266872
PETROLEUM DISTILLATES                         19.120227
dtype: float64

Actual pounds used:
Chemname
DIFENACOUM                                          14.77
AMMONIUM SULFAMATE                                 171.00
COPPER SULFATE (BASIC)                        10594827.29
SORBITOL OCTANOATE                                1799.15
DICAMBA, DIMETHYLAMINE SALT, OTHER RELATED        2844.65
COPPER OXYCHLORIDE                             2073106.53
2,4-D, PROPYL ESTER                               2522.91
PYRIPROXYFEN                                     93506.73
E-8-DODECENYL ACETATE                             3881.39
PETROLEUM DISTILLATES                          1340023.15
Name: TULARE, dtype: float64

Top pesticides with highest relative usage in SAN DIEGO County:
Relative usage ratio:
Chemname
ZINC OXIDE                               7.472385e+06
ARSENIC ACID                             1.793914e+03
2,4-DINITROPHENOL                        5.054050e+02
STREPTOMYCES GRISEOVIRIDIS STRAIN K61    1.524231e+02
ZINC 2-PYRIDINETHIOL-1-OXIDE             1.264946e+02
NOSEMA LOCUSTAE SPORES                   4.507765e+01
ETHYLENE                                 3.896607e+01
COPPER CARBONATE, BASIC                  2.921542e+01
IBA                                      2.678010e+01
SODIUM ARSENATE                          2.043262e+01
dtype: float64

Actual pounds used:
Chemname
ZINC OXIDE                               14167.64
ARSENIC ACID                             17607.11
2,4-DINITROPHENOL                           45.88
STREPTOMYCES GRISEOVIRIDIS STRAIN K61       52.81
ZINC 2-PYRIDINETHIOL-1-OXIDE                19.77
NOSEMA LOCUSTAE SPORES                       2.40
ETHYLENE                                 12934.66
COPPER CARBONATE, BASIC                   5187.97
IBA                                        203.10
SODIUM ARSENATE                              1.92
Name: SAN DIEGO, dtype: float64

Top pesticides with highest relative usage in SAN LUIS OBISPO County:
Relative usage ratio:
Chemname
ANCYMIDOL                                     53.021606
POLYOXYETHYLENE LANOLIN                       49.243757
DIETHANOLAMIDE OF LAURIC AND MYRISTIC ACID    49.243757
SODIUM BROMIDE                                47.158852
TRICHODERMA HARZIANUM RIFAI STRAIN KRL-AG2    32.365087
DIOCTYL DIMETHYL AMMONIUM CHLORIDE            22.399504
MUSCALURE                                     10.833561
HYPOCREA ATROVIRIDIS                           9.019906
HYPOCREA (TELEOMORPH)                          9.019906
PHENOTHRIN, OTHER RELATED                      8.732968
dtype: float64

Actual pounds used:
Chemname
ANCYMIDOL                                          38.15
POLYOXYETHYLENE LANOLIN                             0.21
DIETHANOLAMIDE OF LAURIC AND MYRISTIC ACID          0.59
SODIUM BROMIDE                                3297749.67
TRICHODERMA HARZIANUM RIFAI STRAIN KRL-AG2        935.00
DIOCTYL DIMETHYL AMMONIUM CHLORIDE             112413.16
MUSCALURE                                          65.96
HYPOCREA ATROVIRIDIS                               69.93
HYPOCREA (TELEOMORPH)                              69.93
PHENOTHRIN, OTHER RELATED                           0.23
Name: SAN LUIS OBISPO, dtype: float64

Top pesticides with highest relative usage in ORANGE County:
Relative usage ratio:
Chemname
SODIUM HYDROXIDE             54.470378
MCPA, 2-ETHYL HEXYL ESTER    33.658603
DIKEGULAC SODIUM             32.939446
4-AMINOPYRIDINE              32.300972
LINALOOL                     31.434600
HYDRAMETHYLNON               26.764201
BENZYL BENZOATE              20.350138
FENOXYCARB                   19.274909
TRIFORINE                    14.970005
ABAMECTIN, OTHER RELATED     14.304605
dtype: float64

Actual pounds used:
Chemname
SODIUM HYDROXIDE                58.80
MCPA, 2-ETHYL HEXYL ESTER     4822.89
DIKEGULAC SODIUM             23158.19
4-AMINOPYRIDINE                396.54
LINALOOL                      1250.39
HYDRAMETHYLNON                7874.82
BENZYL BENZOATE                  8.65
FENOXYCARB                     116.15
TRIFORINE                      339.75
ABAMECTIN, OTHER RELATED         0.69
Name: ORANGE, dtype: float64

Top pesticides with highest relative usage in RIVERSIDE County:
Relative usage ratio:
Chemname
SODIUM CYANIDE                  5110.779678
TRIFLOXYSULFURON-SODIUM          317.958705
PCP, OTHER RELATED               149.590518
CYCLOHEXANE                      133.041185
PENTACHLOROPHENOL                130.158095
ACETIC ACID                       58.626753
NONANOIC ACID, OTHER RELATED      41.059225
NONANOIC ACID                     41.023497
SIDURON                           34.583354
BARBAN                            30.833260
dtype: float64

Actual pounds used:
Chemname
SODIUM CYANIDE                   58628.50
TRIFLOXYSULFURON-SODIUM           4714.54
PCP, OTHER RELATED                  72.99
CYCLOHEXANE                          0.50
PENTACHLOROPHENOL                  506.29
ACETIC ACID                      29064.32
NONANOIC ACID, OTHER RELATED      7149.88
NONANOIC ACID                   135848.00
SIDURON                          46624.21
BARBAN                              11.94
Name: RIVERSIDE, dtype: float64

Top pesticides with highest relative usage in VENTURA County:
Relative usage ratio:
Chemname
PSEUDOMONAS SYRINGAE STRAIN: ESC 11                                544.272949
3,4',5-TRIBROMOSALICYLANILIDE                                      358.213542
DIPROPYL ISOCINCHOMERONATE                                         159.189710
KINOPRENE                                                           62.313981
ANILAZINE                                                           59.813111
FERRIC SODIUM EDTA                                                  40.892525
THIRAM                                                              29.453869
DICLORAN                                                            27.649960
DIMETHYLAMINE 2-(2,4-DICHLOROPHENOXY)PROPIONATE                     24.388999
BACILLUS THURINGIENSIS (BERLINER), SUBSP. AIZAWAI, SEROTYPE H-7     22.942271
dtype: float64

Actual pounds used:
Chemname
PSEUDOMONAS SYRINGAE STRAIN: ESC 11                                    20.10
3,4',5-TRIBROMOSALICYLANILIDE                                           0.02
DIPROPYL ISOCINCHOMERONATE                                             52.86
KINOPRENE                                                              11.72
ANILAZINE                                                            1972.59
FERRIC SODIUM EDTA                                                  42418.60
THIRAM                                                             619939.53
DICLORAN                                                           515728.28
DIMETHYLAMINE 2-(2,4-DICHLOROPHENOXY)PROPIONATE                       651.05
BACILLUS THURINGIENSIS (BERLINER), SUBSP. AIZAWAI, SEROTYPE H-7     16109.15
Name: VENTURA, dtype: float64

Top pesticides with highest relative usage in KINGS County:
Relative usage ratio:
Chemname
SEDAXANE                     41.009681
NOVALURON                    30.601044
MCPP, DIETHANOLAMINE SALT    27.541674
TCMTB                        23.308073
FLONICAMID                   21.869825
SODIUM CHLORATE              18.547820
NALED                        17.116515
PROFENOFOS                   16.834804
OXAMYL                       16.650020
ETHEPHON                     13.869580
dtype: float64

Actual pounds used:
Chemname
SEDAXANE                         266.25
NOVALURON                      81497.77
MCPP, DIETHANOLAMINE SALT          6.69
TCMTB                          47459.62
FLONICAMID                    201905.95
SODIUM CHLORATE              4676630.40
NALED                        1393918.74
PROFENOFOS                     75738.40
OXAMYL                        504670.58
ETHEPHON                     2033476.78
Name: KINGS, dtype: float64


todo 
- change the build scripts so that there is a x dataset and y dataset
- run a correlation matrix onf the pesticide
- did the full training for the irb investigators and student researchers
- did the fulll trining for the export controls  for studnents


