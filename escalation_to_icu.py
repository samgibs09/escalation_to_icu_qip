import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

# Load the dataset
data = pd.read_excel('Call4Concern(1-59) (anonymised) v3.xlsx')
print("dataset loaded")

# Awareness of C4C programme overall and by ward (D)
awareness_overall_raw = data['Are you aware of the Call4Concern Program?'].value_counts(normalize=False)
awareness_by_ward_raw = data.groupby('What Ward')['Are you aware of the Call4Concern Program?'].value_counts(normalize=False).unstack()

awareness_overall = data['Are you aware of the Call4Concern Program?'].value_counts(normalize=True) * 100
awareness_by_ward = data.groupby('What Ward')['Are you aware of the Call4Concern Program?'].value_counts(normalize=True).unstack() * 100

# Display awareness
print("\nAwareness of C4C Programme Overall (raw):")
print(awareness_overall_raw)
print("\nAwareness of C4C Programme by Ward (raw):")
print(awareness_by_ward_raw)

print("\nAwareness of C4C Programme Overall:")
print(awareness_overall)
print("\nAwareness of C4C Programme by Ward:")
print(awareness_by_ward)

# Perform Chi-square test for independence (categorical data) on awareness by ward
contingency_table_awareness = pd.crosstab(data['What Ward'], data['Are you aware of the Call4Concern Program?'])
chi2_awareness, p_awareness, dof_awareness, expected_awareness = chi2_contingency(contingency_table_awareness)
print(f'\nChi-square statistic for awareness by ward: {chi2_awareness}')
print(f'p-value for awareness by ward: {p_awareness}')

# Filter data for those who are aware of C4C Programme
aware_data = data[data['Are you aware of the Call4Concern Program?'] == 'Yes']

# Mention of C4C programme in escalation
mention_escalation_raw = aware_data['Do they mention c4c??'].value_counts(normalize=False)
mention_escalation = aware_data['Do they mention c4c??'].value_counts(normalize=True) * 100
print("\nThose Mentioning of C4C Programme when asked about Escalation (raw):")
print(mention_escalation_raw)
print("\nThose Mentioning of C4C Programme when asked about Escalation:")
print(mention_escalation)

# Understanding of C4C programme
understanding_why_raw = aware_data['Do they accurately describe why you would use C4C?'].value_counts(normalize=False)
understanding_how_raw = aware_data['Accurately described how to contact'].value_counts(normalize=False)
understanding_why = aware_data['Do they accurately describe why you would use C4C?'].value_counts(normalize=True) * 100
understanding_how = aware_data['Accurately described how to contact'].value_counts(normalize=True) * 100
print("\nOf those who are awere of C4C: Understand How to Access C4C Programme (raw):")
print(understanding_how_raw)
print("\nOf those who are aware of C4C: Understanding of Why to Access C4C Programme (raw):")
print(understanding_why_raw)
print("\nOf those who are awere of C4C: Understand How to Access C4C Programme:")
print(understanding_how)
print("\nOf those who are aware of C4C: Understanding of Why to Access C4C Programme:")
print(understanding_why)

# Confidence in using C4C programme
confidence_in_using_raw = aware_data['How confident would you feel using the Call4Concern program if necessary?'].value_counts(normalize=False)
confidence_in_using = aware_data['How confident would you feel using the Call4Concern program if necessary?'].value_counts(normalize=True) * 100
print("\nOf those that are aware of C4C programme: Confidence in Using C4C Programme (raw):")
print(confidence_in_using_raw)
print("\nOf those that are aware of C4C programme: Confidence in Using C4C Programme:")
print(confidence_in_using)

# Visibility of poster by ward
poster_visibility_overall_raw = data['Have you seen the informational poster about the C4C program'].value_counts(normalize=False)
poster_visibility_by_ward_raw = data.groupby('What Ward')['Have you seen the informational poster about the C4C program'].value_counts(normalize=False).unstack()
poster_visibility_overall = data['Have you seen the informational poster about the C4C program'].value_counts(normalize=True) * 100
poster_visibility_by_ward = data.groupby('What Ward')['Have you seen the informational poster about the C4C program'].value_counts(normalize=True).unstack() * 100
print("\nPoster Visibility Overall (raw):")
print(poster_visibility_overall_raw)
print("\nPoster Visibility by Ward (raw):")
print(poster_visibility_by_ward_raw)
print("\nPoster Visibility Overall:")
print(poster_visibility_overall)
print("\nPoster Visibility by Ward:")
print(poster_visibility_by_ward)

# Perform Chi-square test for poster visibility by ward
contingency_table_poster = pd.crosstab(data['What Ward'], data['Have you seen the informational poster about the C4C program'])
chi2_poster, p_poster, dof_poster, expected_poster = chi2_contingency(contingency_table_poster)

# Display the results of the Chi-square test
print(f'\nChi-square statistic for poster visibility by ward: {chi2_poster}')
print(f'p-value for poster visibility by ward: {p_poster}')

# Effectiveness of poster in understanding
saw_poster_data = data[data['Have you seen the informational poster about the C4C program'] == 'Yes']
poster_helped_understanding_raw = saw_poster_data['Does the poster help you understand what C4C is?'].value_counts(normalize=False)
poster_helped_understanding = saw_poster_data['Does the poster help you understand what C4C is?'].value_counts(normalize=True) * 100
print("\nEffectiveness of Poster in self-reported improvement of understanding C4C Programme (raw):")
print(poster_helped_understanding_raw)
print("\nEffectiveness of Poster in self-reported improvement of understanding C4C Programme:")
print(poster_helped_understanding)

# Performance of poster viewers in understanding C4C
poster_awareness_of_c4c_raw = saw_poster_data['Are you aware of the Call4Concern Program?'].value_counts(normalize=False)
poster_understanding_why_raw = saw_poster_data['Do they accurately describe why you would use C4C?'].value_counts(normalize=False)
poster_how_to_access_raw = saw_poster_data['Accurately described how to contact'].value_counts(normalize=False)
poster_confidence_raw = saw_poster_data['How confident would you feel using the Call4Concern program if necessary?'].value_counts(normalize=False)
poster_recall_raw = saw_poster_data['Do they mention c4c??'].value_counts(normalize=False)
poster_awareness_of_c4c = saw_poster_data['Are you aware of the Call4Concern Program?'].value_counts(normalize=True) * 100
poster_understanding_why = saw_poster_data['Do they accurately describe why you would use C4C?'].value_counts(normalize=True) * 100
poster_how_to_access = saw_poster_data['Accurately described how to contact'].value_counts(normalize=True) * 100
poster_confidence = saw_poster_data['How confident would you feel using the Call4Concern program if necessary?'].value_counts(normalize=True) * 100
poster_recall = saw_poster_data['Do they mention c4c??'].value_counts(normalize=True) * 100
print("\nPerformance of Poster Viewers in Understanding C4C Programme (raw):")
print("\nAwareness of C4C Programme (raw):")
print(poster_awareness_of_c4c_raw)
print("\nKnowing Why to access C4C Programme (raw):")
print(poster_understanding_why_raw)
print("\nKnowing How to Access C4C Programme (raw):")
print(poster_how_to_access_raw)
print("\nConfidence in Using C4C Programme (raw):")
print(poster_confidence_raw)
print("\nRecall of C4C Programme when asked about Escalation (raw):")
print(poster_recall_raw)

print("\nPerformance of Poster Viewers in Understanding C4C Programme:")
print("\nAwareness of C4C Programme:")
print(poster_awareness_of_c4c)
print("\nKnowing Why to access C4C Programme:")
print(poster_understanding_why)
print("\nKnowing How to Access C4C Programme:")
print(poster_how_to_access)
print("\nConfidence in Using C4C Programme:")
print(poster_confidence)
print("\nRecall of C4C Programme when asked about Escalation:")
print(poster_recall)

# Performance of non-poster viewers in understanding C4C
non_poster_data = data[data['Have you seen the informational poster about the C4C program'] == 'No']
non_poster_recall_raw = non_poster_data['Do they mention c4c??'].value_counts(normalize=False)
non_poster_awareness_of_c4c_raw = non_poster_data['Are you aware of the Call4Concern Program?'].value_counts(normalize=False)
non_poster_recall = non_poster_data['Do they mention c4c??'].value_counts(normalize=True) * 100
non_poster_awareness_of_c4c = non_poster_data['Are you aware of the Call4Concern Program?'].value_counts(normalize=True) * 100
print("\nPerformance of Non-Poster Viewers in Understanding C4C Programme (raw):")
print("\nAwareness of C4C Programme (raw):")
print(non_poster_awareness_of_c4c_raw)
print("\nRecall of C4C Programme when asked about Escalation (raw):")
print(non_poster_recall_raw)

print("\nPerformance of Non-Poster Viewers in Understanding C4C Programme:")
print("\nAwareness of C4C Programme:")
print(non_poster_awareness_of_c4c)
print("\nRecall of C4C Programme when asked about Escalation:")
print(non_poster_recall)


# Filter data for those who are aware of C4C Programme and create a copy to avoid SettingWithCopyWarning
aware_data = data[data['Are you aware of the Call4Concern Program?'] == 'Yes'].copy()

# For poster visibility subsets
saw_poster_data = data[data['Have you seen the informational poster about the C4C program'] == 'Yes'].copy()
non_poster_data = data[data['Have you seen the informational poster about the C4C program'] == 'No'].copy()

# Convert categorical 'Yes'/'No' responses to numeric values for analysis
saw_poster_data['Do they mention c4c??_numeric'] = saw_poster_data['Do they mention c4c??'].map({'Yes': 1, 'No': 0})
non_poster_data['Do they mention c4c??_numeric'] = non_poster_data['Do they mention c4c??'].map({'Yes': 1, 'No': 0})

# Now perform the T-test on the numeric columns

# Ensure the NaN values are handled or filtered out before this step
t_test_awareness_of_c4c = ttest_ind(
    saw_poster_data.dropna(subset=['Are you aware of the Call4Concern Program?'])['Are you aware of the Call4Concern Program?'].map({'Yes': 1, 'No': 0}),
    non_poster_data.dropna(subset=['Are you aware of the Call4Concern Program?'])['Are you aware of the Call4Concern Program?'].map({'Yes': 1, 'No': 0})
)
t_test_recall = ttest_ind(
    saw_poster_data.dropna(subset=['Do they mention c4c??_numeric'])['Do they mention c4c??_numeric'],
    non_poster_data.dropna(subset=['Do they mention c4c??_numeric'])['Do they mention c4c??_numeric']
)

print(f'T-test for difference in awareness of C4C programme between poster and non-poster viewers: {t_test_awareness_of_c4c.statistic}, p-value: {t_test_awareness_of_c4c.pvalue}')
print(f'T-test for difference in recall of C4C programme between poster and non-poster viewers: {t_test_recall.statistic}, p-value: {t_test_recall.pvalue}')

# Asked about concerns on ward round
asked_about_concerns_raw = data['Have you been asked about any concerns that you may have during the ward round?'].value_counts(normalize=False)
asked_about_concerns = data['Have you been asked about any concerns that you may have during the ward round?'].value_counts(normalize=True) * 100
print("\nAsked About Concerns on Ward Round (raw):")
print(asked_about_concerns_raw)
print("\nAsked About Concerns on Ward Round:")
print(asked_about_concerns)

# Perform Chi-square test for being asked about concerns on ward round
contingency_table_concerns = pd.crosstab(data['What Ward'], data['Have you been asked about any concerns that you may have during the ward round?'])
chi2_concerns, p_concerns, dof_concerns, expected_concerns = chi2_contingency(contingency_table_concerns)

# Display the results of the Chi-square test
print(f'\nChi-square statistic for being asked about concerns on ward round: {chi2_concerns}')
print(f'p-value for being asked about concerns on ward round: {p_concerns}')

# Asked about concerns on ward round by ward
asked_about_concerns_by_ward_raw = data.groupby('What Ward')['Have you been asked about any concerns that you may have during the ward round?'].value_counts(normalize=False).unstack()
asked_about_concerns_by_ward = data.groupby('What Ward')['Have you been asked about any concerns that you may have during the ward round?'].value_counts(normalize=True).unstack() * 100
print("\nAsked About Concerns on Ward Round by Ward (raw):")
print(asked_about_concerns_by_ward_raw)
print("\nAsked About Concerns on Ward Round by Ward:")
print(asked_about_concerns_by_ward)

# Perform Chi-square test for being asked about concerns on ward round by ward
contingency_table_concerns = pd.crosstab(data['What Ward'], data['Have you been asked about any concerns that you may have during the ward round?'])
chi2_concerns, p_concerns, dof_concerns, expected_concerns = chi2_contingency(contingency_table_concerns)

# Display the results of the Chi-square test
print(f'\nChi-square statistic for being asked about concerns on ward round: {chi2_concerns}')
print(f'p-value for being asked about concerns on ward round: {p_concerns}')

# Asked about concerns daily
asked_about_concerns_daily_raw = data['Are you asked about your concerns daily?'].value_counts(normalize=False)
asked_about_concerns_daily = data['Are you asked about your concerns daily?'].value_counts(normalize=True) * 100
print("\nAsked About Concerns Daily (raw):")
print(asked_about_concerns_daily_raw)
print("\nAsked About Concerns Daily:")
print(asked_about_concerns_daily)

# Perform Chi-square test for being asked about concerns daily
contingency_table_daily = pd.crosstab(data['What Ward'], data['Are you asked about your concerns daily?'])
chi2_daily, p_daily, dof_daily, expected_daily = chi2_contingency(contingency_table_daily)

# Display the results of the Chi-square test
print(f'\nChi-square statistic for being asked about concerns daily: {chi2_daily}')
print(f'p-value for being asked about concerns daily: {p_daily}')

# Asked about concerns daily by ward
asked_about_concerns_daily_by_ward_raw = data.groupby('What Ward')['Are you asked about your concerns daily?'].value_counts(normalize=False).unstack()
asked_about_concerns_daily_by_ward = data.groupby('What Ward')['Are you asked about your concerns daily?'].value_counts(normalize=True).unstack() * 100
print("\nAsked About Concerns Daily by Ward (raw):")
print(asked_about_concerns_daily_by_ward_raw)
print("\nAsked About Concerns Daily by Ward:")
print(asked_about_concerns_daily_by_ward)

# Perform Chi-square test for being asked about concerns daily by ward
contingency_table_daily = pd.crosstab(data['What Ward'], data['Are you asked about your concerns daily?'])
chi2_daily, p_daily, dof_daily, expected_daily = chi2_contingency(contingency_table_daily)

# Display the results of the Chi-square test
print(f'\nChi-square statistic for being asked about concerns daily: {chi2_daily}')
print(f'p-value for being asked about concerns daily: {p_daily}')

# Create a contingency table for poster visibility vs awareness
contingency_table_poster_awareness = pd.crosstab(
    data['Have you seen the informational poster about the C4C program'], 
    data['Are you aware of the Call4Concern Program?']
)

# Perform Chi-square test for independence
chi2_poster_awareness, p_poster_awareness, _, _ = chi2_contingency(contingency_table_poster_awareness)

# Display the results
print(f'Chi-square statistic for poster visibility vs awareness: {chi2_poster_awareness}')
print(f'p-value for poster visibility vs awareness: {p_poster_awareness}')

# Create a contingency table for awareness of the poster vs awareness of the C4C program
contingency_table_awareness_poster = pd.crosstab(
    data['Are you aware of the Call4Concern Program?'],
    data['Have you seen the informational poster about the C4C program']
)

# Display the contingency table
print("\nContingency Table: Awareness of Program vs Awareness of Poster")
print(contingency_table_awareness_poster)

# Count of people who are aware of the program but not aware of the poster
count_aware_program_not_poster = contingency_table_awareness_poster.loc['Yes', 'No']
print(f"\nNumber of people aware of the C4C program but not aware of the poster: {count_aware_program_not_poster}")

# Analysis for poster viewers on describing how to use the program
how_to_use = saw_poster_data['Accurately described how to contact'].value_counts(normalize=True) * 100
print("\nHow well poster viewers describe how to use the program:")
print(how_to_use)

# Analysis for poster viewers on recalling how to escalate
how_to_escalate = saw_poster_data['Do they accurately describe why you would use C4C?'].value_counts(normalize=True) * 100
print("\nHow well poster viewers recall how to escalate:")
print(how_to_escalate)

# Analysis for poster viewers on confidence in using the program
confidence = saw_poster_data['How confident would you feel using the Call4Concern program if necessary?'].value_counts(normalize=True) * 100
print("\nConfidence in using the program by poster viewers:")
print(confidence)

# Asked about concerns 'every day' vs not asked about concerns 'every day' for 'Do you feel able to participate in decisions relating to your/the patient's care with the healthcare team?'
# Map textual responses to numerical values for analysis
response_mapping = {
    'Always': 5,
    'Often': 4,
    'Sometimes': 3,
    'Rarely': 2,
    'Never': 1
}

# Apply mapping to create a new column with numerical values for participation
data['participation_score'] = data['Do you feel able to participate in decisions relating to your/the patient\'s care with the healthcare team?'].map(response_mapping)

# Regroup 'Are you asked about your concerns daily?' into 'Every day' and 'Not Every day'
data['daily_concern_inquiry_group'] = data['Are you asked about your concerns daily?'].apply(lambda x: 'Every day' if x == 'Every day' else 'Not Every day')

# Calculate mean participation scores for the new grouping
mean_participation_scores_regrouped = data.groupby('daily_concern_inquiry_group')['participation_score'].mean()
print("\nMean Participation Scores for Regrouped Data:")
print(mean_participation_scores_regrouped)

# Separate the groups for 'Every day' and 'Not Every day'
every_day_scores = data[data['daily_concern_inquiry_group'] == 'Every day']['participation_score']
not_every_day_scores = data[data['daily_concern_inquiry_group'] == 'Not Every day']['participation_score']

# Perform Mann-Whitney U Test as the data is ordinal
u_stat, p_val_mw = mannwhitneyu(every_day_scores.dropna(), not_every_day_scores.dropna(), alternative='two-sided')

print(f'\nMann-Whitney U test results: U statistic={u_stat}, p-value={p_val_mw}')

# Interpret results
if p_val_mw < 0.05:
    print("There is a significant difference in feeling able to participate in decisions between those asked about their concerns 'Every day' and 'Not Every day'.")
else:
    print("There is no significant difference in feeling able to participate in decisions between those asked about their concerns 'Every day' and 'Not Every day'.")

# Aware of C4C programme vs not aware of C4C programme for 'Do you feel able to participate in decisions relating to your/the patient's care with the healthcare team?'

# Separate the groups for 'Yes' and 'No'
aware_scores = data[data['Are you aware of the Call4Concern Program?'] == 'Yes']['participation_score']
not_aware_scores = data[data['Are you aware of the Call4Concern Program?'] == 'No']['participation_score']

# Create a contingency table for awareness vs. categorical representation of participation
participation_categories = data['Do you feel able to participate in decisions relating to your/the patient\'s care with the healthcare team?']
awareness = data['Are you aware of the Call4Concern Program?']

contingency_table = pd.crosstab(awareness, participation_categories)

print("\nContingency Table: Awareness of C4C vs. Participation in Decisions")
print(contingency_table)

# Summarize participation scores by awareness
summary_by_awareness = data.groupby('Are you aware of the Call4Concern Program?')['participation_score'].agg(['mean', 'median', 'count'])

print("\nSummary of Participation Scores by Awareness of C4C")
print(summary_by_awareness)

# Perform Mann-Whitney U Test as the data is ordinal
u_stat, p_val_mw = mannwhitneyu(aware_scores.dropna(), not_aware_scores.dropna(), alternative='two-sided')

print(f'\nMann-Whitney U test results: U statistic={u_stat}, p-value={p_val_mw}')

# Interpret results

if p_val_mw < 0.05:
    print("There is a significant difference in feeling able to participate in decisions between those aware of the C4C programme and those not aware.")
else:
    print("There is no significant difference in feeling able to participate in decisions between those aware of the C4C programme and those not aware.")

