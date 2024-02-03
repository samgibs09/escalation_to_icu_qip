import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_excel('Call4Concern(1-59) (anonymised) v3.xlsx')

# Awareness of C4C programme overall and by ward
awareness_overall = data['T'].value_counts(normalize=True) * 100
awareness_by_ward = data.groupby('D')['T'].value_counts(normalize=True).unstack() * 100
print(awareness_overall)
print(awareness_by_ward)

# Mention of C4C programme in escalation
mention_escalation = data[data['T'] == 'Yes']['S'].value_counts(normalize=True) * 100

# Understanidng of C4C programme
understanding_how = data[data['T'] == 'Yes']['Y'].value_counts(normalize=True) * 100
understanding_why = data[data['T'] == 'Yes']['AB'].value_counts(normalize=True) * 100

# Confidence in using C4C programme
confidence_in_using = data[data['T'] == 'Yes']['AC'].value_counts(normalize=True) * 100

# Visibility of poster by ward
poster_visibility_overall = data['AE'].value_counts(normalize=True) * 100
poster_visibility_by_ward = data.groupby('D')['AE'].value_counts(normalize=True).unstack() * 100

# Effectiveness of poster in understanding
poster_helped_understanding = data[data['AE'] == 'Yes']['AF'].value_counts(normalize=True) * 100

# Performance of poster viewers in understanding C4C
performance_knowing_what = data[data['AE'] == 'Yes']['Y'].value_counts(normalize=True) * 100
performance_how_to_access = data[data['AE'] == 'Yes']['AB'].value_counts(normalize=True) * 100
performance_confidence = data[data['AE'] == 'Yes']['AC'].value_counts(normalize=True) * 100

# Asked about concerns on ward round
asked_about_concerns = data['AG'].value_counts(normalize=True) * 100

# Asked about concerns daily
asked_about_concerns_daily = data['AH'].value_counts(normalize=True) * 100

# Create a contingency table
contingency_table = pd.crosstab(data['D'], data['T'])

# Perform the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f'Chi-square statistic: {chi2}')
print(f'p-value: {p}')
