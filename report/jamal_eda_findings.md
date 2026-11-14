# Jamal Part B EDA and findings

## Sample and scope

This analysis uses all 4,435 rows of the team's prepared CSV. The preparation notebook selects U.S. employed respondents who report compensation and keeps pay between $10,000 and the reporters' 99th percentile ($641,900), excluding 97 of 4,532 pay reporters. No further respondents are removed in this EDA. The 2025 survey does not directly identify full-time status, and notebook 01 does not apply a professional-developer identity filter. Findings describe this prepared sample.

## Distributions

Median annual total compensation is $150,000; Q1 is $110,000, Q3 is $200,000, and IQR is $90,000. Mean pay is $168,300, consistent with the remaining right tail. Raw and natural-log histograms show the same respondents. Reported professional work experience has a median of 14 years, with 35 missing values. The nine role families, prepared work arrangements, original work options, education, and experience bands are shown in the categorical bar charts.

## Experience and role relationships

The experience/ln-pay Pearson correlation is 0.278; the rank correlation between experience and pay is 0.353 (complete pairs n=4,400). These summarize different aspects of the association and are not a causal estimate. Among named role families, Management has the highest pooled median ($200,000, n=313), while Desktop / embedded developer has the lowest ($130,000, n=376). These families combine different jobs. The two most common named families are Full-stack developer and Back-end developer. Of 4 experience bands with both families n>=30, 4 have a higher median for Back-end developer; the comparison-minus-reference gap ranges from $30,000 to $39,000. The role-by-experience heatmap compares all nine families and masks cells below n=30.

## Work arrangement within experience groups

Remote respondents have median annual compensation $165,000 (n=2,048), compared with $115,500 for In-person respondents (n=654). The pooled remote-minus-in-person median gap is $49,500 (42.9% of the in-person median). Among 5 experience bands with both categories n>=30, 5 have a positive remote-minus-in-person gap. The within-band gaps range from $8,500 to $34,500. The size and direction should be read from the within-band table rather than assumed to equal the pooled difference. In the additional role-by-experience check, 5 cells have at least 30 Remote and 30 In-person respondents; 5 of those have a positive remote-minus-in-person median gap. Cells excluded by the screen are still listed with counts in the CSV. This check does not establish a causal effect.

## Interpretation and limitations

The pooled pay gaps combine differences in the experience and role composition of the groups. Within-experience and within-role-and-experience comparisons provide more comparable descriptive groups, but broad bands leave residual experience differences. Hours, employer, seniority, specialization, and geography within the United States are not controlled. The results do not show that remote work or changing roles causes higher pay.

Recruitment favors engaged Stack Overflow users and compensation reporting is optional. Notebook 01 found 881 non-reporters among 5,413 employed U.S. respondents; non-reporters had higher median reported experience and were less often Remote than reporters. The reporting sample can therefore differ from the broader respondent population. These findings should not be generalized to all U.S. workers.

The pay cutoffs alter the tails and may exclude some genuine observations; sensitivity to alternative preparation cutoffs was not assessed by these notebooks. Professional work experience is broader than professional coding experience. Blank experience can mean zero years or nonresponse, so missing experience is kept visible and excluded from within-experience comparisons rather than imputed. Work arrangement is missing for 17 respondents and education for 5.

Role families combine occupations, especially Other. The prepared Hybrid category includes Your choice; the detailed-work bar chart shows the original options. The original 20+ experience label is displayed as 21+ because notebook 01's boundaries place exactly 20 years in 11-20. Sparse conditional cells are flagged. The n>=30 display screen does not measure uncertainty or establish statistical significance.

## Figures and tables

- Distributions: pay_distribution.png, experience_distribution.png, and counts_*.png in figures/.
- Group comparisons: pay_by_experience.png, pay_by_role.png, and pay_by_remote.png.
- Conditional comparisons: pay_remote_within_experience.png and pay_role_within_experience.png.
- Scatterplot: exp_vs_logpay.png. All dollar summaries and counts are exported to tables/.

## Sources and reproducibility

- [Team preparation notebook](../notebooks/01_data_prep.ipynb) and processed CSV.
- [2025 survey archive](https://github.com/StackExchange/Survey/tree/main/packages/archive/2025).
- [2025 work results](https://survey.stackoverflow.co/2025/work).
- [2025 methodology](https://survey.stackoverflow.co/2025/methodology).
- Input SHA-256: `f086e0b9370dca3aede85d9fb9c6a236634f35ee54c096f589670b00a5ba4679`. Full run information is in jamal_eda_run_metadata.json.
