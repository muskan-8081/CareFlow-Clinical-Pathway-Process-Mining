\# Patient Pathway Prefix Analysis



\## 1. Objective

To identify common starting sequences in patient pathways by analyzing the first 3, 5, and 8 recorded activities for each patient case.



\## 2. Methodology

\- Loaded the hospital event dataset using Python and Pandas.

\- Converted timestamps into datetime format.

\- Removed records with missing case IDs, activity names, or timestamps.

\- Sorted activities chronologically within each patient case.

\- Reconstructed individual patient activity sequences.

\- Extracted up to the first 3, 5, and 8 activities from each sequence.

\- Counted the number of cases sharing each activity prefix.



\## 3. Analysis Results



A total of 1,049 patient cases were analyzed.



\### Common 3-Activity Prefix



The most common starting sequence was:



ER Registration → ER Triage → ER Sepsis Triage



This sequence appeared in 807 cases, representing approximately 76.9% of the analyzed cases.



Other observed starting sequences included:

\- ER Registration → ER Triage → CRP: 43 cases.

\- ER Registration → ER Triage → Leucocytes: 40 cases.

\- ER Registration → ER Triage → LacticAcid: 25 cases.



\### Common 5-Activity Prefix



The most common sequence was:



ER Registration → ER Triage → ER Sepsis Triage → Leucocytes → CRP



This sequence appeared in 187 cases.



The second most common sequence placed CRP before Leucocytes and appeared in 105 cases.



\### Common 8-Activity Prefix



The most common sequence was:



ER Registration → ER Triage → ER Sepsis Triage → Leucocytes → CRP → LacticAcid → IV Liquid → IV Antibiotics



This sequence appeared in 76 cases.



Other frequent sequences showed variations in the order of laboratory activities before IV treatment activities.



\## 4. Key Observations



\- A large proportion of cases shared the same first three recorded activities.

\- The order of Leucocytes, CRP, and LacticAcid varied across patient pathways.

\- IV Liquid and IV Antibiotics appeared in several common longer activity sequences.

\- Patient pathways shared common starting patterns but showed variations as more activities were included.



\## 5. Generated Output



The analysis generated:



`data/patient\_pathway\_prefix\_analysis.csv`



The file contains the requested prefix length, activity sequence, and number of cases sharing each sequence.



\## 6. Conclusion



Patient pathway prefix analysis identified common starting activity sequences across 1,049 patient cases. The most frequent first-three-activity sequence was ER Registration → ER Triage → ER Sepsis Triage, observed in 807 cases.



The analysis provides a clearer understanding of shared patient journey patterns and variations in subsequent activities.



\## 7. Limitations



\- Prefixes contain up to the requested number of activities; shorter patient sequences are included without padding.

\- The analysis reflects recorded activity order and does not establish clinical appropriateness.

\- Activities with identical timestamps may have an uncertain relative order.

\- Common sequences do not necessarily indicate identical clinical conditions or treatment requirements.

