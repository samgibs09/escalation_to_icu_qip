import pandas as pd
from scipy.stats import chi2_contingency

# Load the dataset
data = pd.read_excel('Call4Concern(1-59) (anonymised) v3.xlsx')

# Awareness of C4C programme overall and by ward (D)
awareness_overall = data['T'].value_counts(normalize=True) * 100
awareness_by_ward = data.groupby('D')['T'].value_counts(normalize=True).unstack() * 100

# Display awareness
print("Awareness of C4C Programme Overall:")
print(awareness_overall)
print("\nAwareness of C4C Programme by Ward:")
print(awareness_by_ward)

# Perform Chi-square test for independence (categorical data) on awareness by ward
contingency_table_awareness = pd.crosstab(data['D'], data['T'])
chi2_awareness, p_awareness, dof_awareness, expected_awareness = chi2_contingency(contingency_table_awareness)
print(f'\nChi-square statistic for awareness by ward: {chi2_awareness}')
print(f'p-value for awareness by ward: {p_awareness}')

# Filter data for those who are aware of C4C Programme
aware_data = data[data['T'] == 'Yes']

# Mention of C4C programme in escalation
mention_escalation = aware_data['S'].value_counts(normalize=True) * 100
print("\nMention of C4C Programme in Escalation:")
print(mention_escalation)

# Understanding of C4C programme
understanding_how = aware_data['Y'].value_counts(normalize=True) * 100
understanding_why = aware_data['AB'].value_counts(normalize=True) * 100
print("\nUnderstanding of How to Access C4C Programme:")
print(understanding_how)
print("\nUnderstanding of Why to Access C4C Programme:")
print(understanding_why)

# Confidence in using C4C programme
confidence_in_using = aware_data['AC'].value_counts(normalize=True) * 100
print("\nConfidence in Using C4C Programme:")
print(confidence_in_using)

# Perform Chi-square test for understanding how and why to access C4C Programme
table_how = pd.crosstab(aware_data['T'], aware_data['Y'])
chi2_how, p_how, dof_how, expected_how = chi2_contingency(table_how)

table_why = pd.crosstab(aware_data['T'], aware_data['AB'])
chi2_why, p_why, dof_why, expected_why = chi2_contingency(table_why)

table_confidence = pd.crosstab(aware_data['T'], aware_data['AC'])
chi2_confidence, p_confidence, dof_confidence, expected_confidence = chi2_contingency(table_confidence)

# Visibility of poster by ward
poster_visibility_overall = data['AE'].value_counts(normalize=True) * 100
poster_visibility_by_ward = data.groupby('D')['AE'].value_counts(normalize=True).unstack() * 100
print("\nPoster Visibility Overall:")
print(poster_visibility_overall)
print("\nPoster Visibility by Ward:")
print(poster_visibility_by_ward)

# Perform Chi-square test for poster visibility by ward
contingency_table_poster = pd.crosstab(data['D'], data['AE'])
chi2_poster, p_poster, dof_poster, expected_poster = chi2_contingency(contingency_table_poster)

# Effectiveness of poster in understanding
saw_poster_data = data[data['AE'] == 'Yes']
poster_helped_understanding = saw_poster_data['AF'].value_counts(normalize=True) * 100
print("\nEffectiveness of Poster in Understanding C4C Programme:")
print(poster_helped_understanding)

# Perform Chi-square test for understanding from poster
table_understanding = pd.crosstab(saw_poster_data['AE'], saw_poster_data['AF'])
chi2_understanding, p_understanding, dof_understanding, expected_understanding = chi2_contingency(table_understanding)

# Performance of poster viewers in understanding C4C
performance_knowing_what = saw_poster_data['Y'].value_counts(normalize=True) * 100
performance_how_to_access = saw_poster_data['AB'].value_counts(normalize=True) * 100
performance_confidence = saw_poster_data['AC'].value_counts(normalize=True) * 100
print("\nPerformance of Poster Viewers in Understanding C4C Programme:")
print("Knowing What C4C Programme is:")
print(performance_knowing_what)
print("Knowing How to Access C4C Programme:")
print(performance_how_to_access)
print("Confidence in Using C4C Programme:")
print(performance_confidence)

# Asked about concerns on ward round
asked_about_concerns = data['AG'].value_counts(normalize=True) * 100
print("\nAsked About Concerns on Ward Round:")
print(asked_about_concerns)

# Perform Chi-square test for being asked about concerns on ward round
contingency_table_concerns = pd.crosstab(data['D'], data['AG'])
chi2_concerns, p_concerns, dof_concerns, expected_concerns = chi2_contingency(contingency_table_concerns)

# Asked about concerns daily
asked_about_concerns_daily = data['AH'].value_counts(normalize=True) * 100
print("\nAsked About Concerns Daily:")
print(asked_about_concerns_daily)

# Perform Chi-square test for being asked about concerns daily
contingency_table_daily = pd.crosstab(data['D'], data['AH'])
chi2_daily, p_daily, dof_daily, expected_daily = chi2_contingency(contingency_table_daily)
