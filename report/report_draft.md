# Developer Careers and Compensation

## Project overview

This project examines how professional experience, job roles, and work arrangements
relate to annual compensation in the 2025 Stack Overflow Developer Survey. We
analyze a prepared sample of 4,435 employed U.S. respondents who reported compensation
and met documented pay cutoffs. Median annual total compensation is $150,000, with
the middle half of observations between $110,000 and $200,000.

Remote respondents have higher median compensation than In-person respondents
both overall and within the five experience bands. However, the within-band gaps
are smaller than the overall difference. Role-family comparisons also differ
within experience groups. These findings describe associations in the analyzed
sample and do not establish causal effects of changing roles or work arrangements.

## Research question

Our main question is: How do professional experience, role families, and work
arrangements relate to reported annual compensation among employed U.S. survey
respondents? We examine compensation distributions, compare group medians and
interquartile ranges, and check whether selected differences persist within broad
experience bands.

## Data and study sample

We use the public 2025 Stack Overflow Developer Survey response file, its schema,
and questionnaire. Each row represents one respondent. The downloaded response
file contains 49,191 rows and 172 columns. Stack Overflow collected the survey from
May 29 through June 23, 2025 and converted compensation to USD using exchange rates
from June 25, 2025. Recruitment primarily used Stack Overflow channels, which
favors participation by engaged users. [Stack Overflow methodology](https://survey.stackoverflow.co/2025/methodology)

The outcome is total annual compensation in USD, including salary, bonuses, and
perks before taxes and deductions. The source field ConvertedCompYearly becomes
pay in the processed dataset. It differs from base salary and take-home pay.
Professional experience comes from WorkExp, which measures professional work
experience generally rather than years coding professionally. Role and work
arrangement come from DevType and RemoteWork. Education describes the sample.
[Survey response data and questionnaire](https://github.com/StackExchange/Survey/tree/main/packages/archive/2025)

We restrict the sample as follows:

| Selection step | Respondents remaining |
|---|---:|
| Raw response file | 49,191 |
| United States residents | 7,233 |
| Employment status is Employed | 5,413 |
| Reported compensation | 4,532 |
| After compensation cutoffs | 4,435 |

The 2025 employment question does not directly distinguish full-time from part-time
employment. The preparation also does not restrict MainBranch to professional
developers. We therefore describe the analyzed population as employed U.S. survey
respondents, despite the historical us_fulltime_clean.csv filename.

## Data quality and preparation

### Missing compensation

Among the 5,413 employed U.S. respondents, 881 did not report compensation, or about
16.3%. Non-reporters had median reported professional experience of 17 years,
compared with 14 years among reporters. Approximately 36% of non-reporters were
Remote, compared with 46% of reporters. These observed differences show that the
pay-reporting sample differs from the broader employed respondent group. We cannot
determine the missing compensation amounts or the exact direction of pay bias
from these comparisons alone.

### Duplicates and extreme compensation

No repeated respondent IDs or fully duplicated rows appeared among the 4,532
compensation reporters. The preparation retained annual compensation from $10,000
through the reporters' 99th percentile, approximately $641,900. This removed 51
observations below the lower cutoff and 46 above the upper cutoff, for 97 removed
observations, or approximately 2.1% of pay reporters.

These cutoffs limit unusually low and high reports, but they remain analysis
choices. Some excluded values may be genuine. An extreme value alone does not
establish a reporting error, and sensitivity to alternative cutoffs has not been
evaluated in the completed EDA. No additional observations were removed after
loading the prepared dataset.

### Experience and categorical variables

WorkExp and YearsCode were already numeric, so no text-to-number recoding was
necessary. The preparation copied them into explicitly named numerical columns.
Thirty-five retained respondents had missing professional experience. Because
the questionnaire instructs zero-year respondents to leave this field blank, a
blank can indicate zero years or nonresponse. We retain it as missing rather than
assume either interpretation.

The experience groups are 0-2, 3-5, 6-10, 11-20, and more than 20 years. We display
the final group as 21+ because exactly 20 years belongs in 11-20. This changes
only the display label, not membership. The single-choice role question is grouped
into nine role families. Work arrangements are grouped into Remote, Hybrid, and
In-person. Hybrid includes both original hybrid choices and Your choice. The
original work-arrangement field remains available for descriptive charts.

The prepared dataset has 17 missing work arrangements and 5 missing education
values. Missing categories remain visible in marginal summaries. Numerical
experience analyses and comparisons within experience bands use the 4,400
respondents with reported experience. Natural-log compensation supports plots
while dollar compensation remains available for interpretation.

## Exploratory analysis

### Compensation distribution

Median annual total compensation is $150,000, compared with a mean of approximately
$168,300. The 25th percentile is $110,000 and the 75th percentile is $200,000, giving
an interquartile range of $90,000. The mean exceeds the median because the retained
distribution still has a high-pay tail. We emphasize medians for group comparisons
because they are more resistant to extreme values than means.

The dollar and natural-log histograms show the same retained respondents. The log
scale compresses high values and makes the distribution easier to inspect. Role,
work-arrangement, education, and experience-band bar charts describe sample
composition. For example, an education category's frequency does not establish
its relationship with compensation.

### Compensation and experience

Median reported professional work experience is 14 years. Compensation medians
increase across the early experience groups and reach $170,000 in both the 11-20
and 21+ groups.

| Professional experience | n | Median annual compensation |
|---|---:|---:|
| 0-2 years | 231 | $85,000 |
| 3-5 years | 470 | $102,750 |
| 6-10 years | 980 | $148,000 |
| 11-20 years | 1,440 | $170,000 |
| 21+ years | 1,279 | $170,000 |
| Missing | 35 | $64,000 |

The experience and natural-log compensation scatterplot shows substantial pay
variation at similar experience levels. Pearson correlation between experience
and natural-log compensation is 0.278. The Spearman rank correlation between
experience and compensation is 0.353, using 4,400 complete pairs. These positive
associations do not establish an effect of experience or describe one individual's
future compensation trajectory.

### Compensation by role family

Management has the highest pooled median among named role families at $200,000,
followed by Architect at $185,000 and Back-end developer at $175,000. The Other
category combines different occupations, so its median does not describe one job.

| Role family | n | Median annual compensation |
|---|---:|---:|
| Management | 313 | $200,000 |
| Architect | 280 | $185,000 |
| Back-end developer | 620 | $175,000 |
| Front-end / mobile developer | 265 | $158,000 |
| Infrastructure / ops | 346 | $152,000 |
| Data / AI | 345 | $150,000 |
| Full-stack developer | 1,473 | $140,000 |
| Desktop / embedded developer | 376 | $130,000 |
| Other | 417 | $125,000 |

Box plots complement these medians by displaying quartiles, spread, and unusual
retained values. Points beyond the box-plot whiskers remain part of the analysis;
they are separate from the observations removed by the preparation cutoffs.

### Work arrangement within experience bands

Remote respondents have median compensation of $165,000 (n=2,048), compared with
$115,500 for In-person respondents (n=654). The Hybrid median is $145,849.50
(n=1,716). Seventeen respondents have missing work arrangement. The pooled
Remote-minus-In-person median difference is $49,500, or 42.9% of the In-person
median.

To examine whether broad experience differences could contribute to this pooled
gap, we compare the two arrangements within experience bands.

| Experience | Remote n | In-person n | Remote median | In-person median | Median gap |
|---|---:|---:|---:|---:|---:|
| 0-2 years | 41 | 82 | $85,000 | $76,500 | $8,500 |
| 3-5 years | 152 | 105 | $120,000 | $90,000 | $30,000 |
| 6-10 years | 431 | 150 | $154,500 | $120,000 | $34,500 |
| 11-20 years | 751 | 149 | $177,000 | $147,000 | $30,000 |
| 21+ years | 668 | 147 | $175,000 | $160,000 | $15,000 |

The Remote median remains higher in every band, but each within-band gap is
smaller than the overall $49,500 difference. This pattern shows why the composition
of compared groups matters. These differences are descriptive and are not a
decomposition of how much of the overall gap experience explains.

### Role comparisons within experience bands

A heatmap compares all nine role families within the same experience bands,
displaying medians and sample sizes. We also compare the two most common named
families, Full-stack and Back-end, choosing them by frequency rather than by their
pay difference. Back-end has a higher median in all four bands where both families
have at least 30 respondents, with gaps from $30,000 to $39,000. The 0-2 Back-end
cell has only 22 respondents and is excluded from this headline screened comparison.

An additional Remote/In-person comparison within both role family and experience
has five cells with at least 30 respondents in each arrangement. All five show
positive gaps, but four are Full-stack cells and one is Other. This provides
limited supporting evidence and does not establish that the gap persists in every
occupation after accounting for role. The n>=30 rule is a descriptive screen for
sparse cells, not a significance test or an uncertainty estimate. All observed
cell summaries remain available in the exported tables.

## Findings and limitations

Professional experience, role family, and work arrangement are associated with
compensation in this prepared sample. Looking within experience bands provides
more context than pooled group comparisons. However, broad bands still combine
different experience levels, and role families combine different jobs. Employer,
exact seniority, hours, specialization, and geography within the United States
may differ between groups.

Self-selection into the survey and optional compensation reporting limit
generalization. The missing-pay comparison shows observed differences between
reporters and non-reporters. Compensation cutoffs also change the analyzed sample
and may exclude valid observations. Missing experience cannot be confidently
interpreted as zero, and full-time status is not directly measured.

The publisher reports 49,009 responses used in its website results, while the
downloaded file analyzed here contains 49,191 rows. We report our actual input and
filtering pipeline rather than assume that our sample reproduces the website's
inclusion rules. [Published survey methodology](https://survey.stackoverflow.co/2025/methodology)

The analysis does not establish that changing work arrangement or role causes a
particular compensation increase. Correlations and screened group comparisons
do not replace causal identification or quantify sampling uncertainty.

## Implications and further work

Compensation comparisons are more informative when they consider similar roles
and experience levels, along with employer and location. The sample medians can
provide descriptive context, but they should not serve as guaranteed individual
pay expectations. Further analysis could assess alternative compensation cutoffs,
inspect more detailed roles, and examine additional sources of group differences.

Any predictive modeling should use held-out evaluation and compare performance
with a simple baseline. The completed work reported here establishes the data
preparation and descriptive evidence without making model-performance claims.

## Conclusion

Among 4,435 prepared employed U.S. respondents, median annual total compensation
is $150,000 and the middle half spans $110,000-$200,000. Compensation differs across
experience groups and role families. Remote respondents have a higher median than
In-person respondents overall and in every experience band, with smaller gaps
within bands. These findings support careful comparison of group composition
while retaining the limitations of a self-selected, observational survey sample.

## Contributions to completed work

Samia prepared the dataset, documented the sample filters and quality checks,
examined missing compensation, and created the grouped variables. Jamal completed
the distribution and relationship notebooks, including group summaries, conditional
comparisons, charts, interpretation, and EDA limitations. The EDA retains all rows
of the shared prepared dataset and records its source and input identity.

## References

1. Stack Overflow. (2025). [2025 Developer Survey response data, schema, and questionnaire](https://github.com/StackExchange/Survey/tree/main/packages/archive/2025).
2. Stack Overflow. (2025). [2025 Developer Survey methodology](https://survey.stackoverflow.co/2025/methodology).
3. Stack Overflow. (2025). [2025 Developer Survey work results](https://survey.stackoverflow.co/2025/work).
4. Developer Compensation project team. (2026). [Data preparation notebook](https://github.com/samia21-04/Developer_Compensation/blob/02b883a473bbafc512003792e53b5126ec48e59b/notebooks/01_data_prep.ipynb) and [prepared dataset](https://github.com/samia21-04/Developer_Compensation/blob/02b883a473bbafc512003792e53b5126ec48e59b/data/processed/us_fulltime_clean.csv), source version 02b883a.
5. Project analysis files. (2026). Notebooks 02 and 03 and their exported tables in the current local project working copy.
