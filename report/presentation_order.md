# Developer compensation presentation order

The whole group has **10 minutes**. This order targets **9 minutes of speaking**
and leaves **1 minute for transitions or questions**. Jamal's slides total
**3 minutes 45 seconds**. The presentation uses the verified EDA results from
Samia's 4,435-row cleaned dataset.

## Speaking order

| Slide | Time | Speaker | Topic and visual |
|---|---|---|---|
| 1 | 0:00-0:45 | Report lead | Question, source, and what compensation means |
| 2 | 0:45-2:00 | Samia | Study sample and the row-count funnel |
| 3 | 2:00-3:00 | Samia | Missing pay, pay cutoffs, and prepared groups |
| 4 | 3:00-4:00 | Jamal | Compensation distribution and median/IQR |
| 5 | 4:00-5:40 | Jamal | Remote versus In-person within experience bands |
| 6 | 5:40-6:45 | Jamal | Role comparisons within experience bands |
| 7 | 6:45-7:45 | Report lead | What these comparisons tell us |
| 8 | 7:45-9:00 | Report lead, with shared closing | Limitations and final takeaway |
| Buffer | 9:00-10:00 | Everyone | Questions and transitions |

The modeling notebook currently has no verified performance results in this local
version. This order presents the completed EDA. If the modeling lead adds verified
results before the presentation, revise the timing together rather than add slides
on top of the 10-minute limit.

## Slide 1 Question and source

**Speaker:** Report lead. **Time:** 45 seconds.

**On the slide:**

- How do experience, role, and work arrangement relate to annual compensation?
- 2025 Stack Overflow Developer Survey.
- Annual total compensation in USD, including bonuses and perks before taxes.

**Say:**

"We investigated how compensation differs across professional experience, role
families, and work arrangements. We used the 2025 Stack Overflow survey and focused
on a prepared sample of employed U.S. respondents. Our analysis describes
associations within that sample."

**Transition:** "Samia will explain how we prepared the sample."

## Slide 2 Study sample

**Speaker:** Samia. **Time:** 75 seconds.

**Show this compact table:**

| Selection step | Respondents |
|---|---:|
| Raw response file | 49,191 |
| United States residents | 7,233 |
| Employment is Employed | 5,413 |
| Reported compensation | 4,532 |
| After compensation cutoffs | 4,435 |

**Say:**

"Each row represents one respondent. We limited the sample to U.S. residents and
the Employed category, then retained respondents who reported compensation. After
our compensation cutoffs, 4,435 respondents remained. The employment question does
not directly distinguish full-time from part-time work, so we describe this as an
employed U.S. sample."

**Be ready to explain:** Notebook 01 does not filter MainBranch to professional
developers. The file's historical fulltime name does not establish full-time status.

## Slide 3 Preparation decisions

**Speaker:** Samia. **Time:** 60 seconds.

**On the slide:**

- 881 employed U.S. respondents did not report compensation.
- Pay retained from $10,000 to about $641,900. The rule removed 97 observations.
- Nine role families and three work arrangements.
- Missing experience remains missing.

**Say:**

"We compared compensation reporters with non-reporters. Non-reporters had higher
median reported experience and were less often Remote, so reporting may affect
which workers appear in the analysis. We checked duplicates and found none among
pay reporters. We applied documented compensation cutoffs and grouped roles and
work arrangements for comparison. We left blank experience values missing because
they could represent either zero years or a skipped answer."

**Qualification:** The cutoffs are analysis choices. An extreme value alone does
not prove an error, and alternative-cutoff sensitivity has not been established.

**Transition:** "Jamal used this same prepared file for the exploratory analysis."

## Slide 4 Compensation distribution

**Speaker:** Jamal. **Time:** 60 seconds.

**Show:** [Raw and natural-log compensation histograms](../figures/pay_distribution.png).

**On the slide:** Median **$150,000**. Middle half **$110,000-$200,000**.
IQR **$90,000**. Mean **about $168,300**.

**Say:**

"I first examined the compensation distribution using all 4,435 prepared
respondents. The median is $150,000, while the mean is about $168,300. The higher
mean reflects the remaining high-pay tail. The middle half of respondents reported
between $110,000 and $200,000, giving an interquartile range of $90,000. The two
histograms show the same respondents on dollar and natural-log scales. The log
view compresses the high values and makes the distribution easier to inspect."

**Point to:** The tail in the dollar plot, then the same distribution on the log
scale. Do not say that taking logs removed observations.

**Transition:** "Next we compared compensation across work arrangements."

## Slide 5 Work arrangement within experience bands

**Speaker:** Jamal. **Time:** 100 seconds.

**Show:** [Work arrangement within experience](../figures/pay_remote_within_experience.png).

**On the slide:**

- Overall Remote median: **$165,000**, n=2,048.
- Overall In-person median: **$115,500**, n=654.
- Overall median gap: **$49,500**.
- Within experience bands: gaps of **$8,500-$34,500**.

**Say:**

"Overall, Remote respondents have a median compensation of $165,000 compared with
$115,500 for In-person respondents, a difference of $49,500. But that pooled
comparison could reflect different experience levels in the groups.

"We therefore compared work arrangements within the same experience bands. The
horizontal axis shows experience, and the vertical axis shows median compensation.
The lines represent Remote, Hybrid, and In-person. The n labels show the number of
people in each cell.

"Remote has a higher median than In-person in all five bands. However, the gaps
range from $8,500 to $34,500, which are smaller than the pooled difference. This
shows why group composition matters when interpreting compensation comparisons.

"The result remains descriptive. People within a band can still differ in exact
experience, employer, location, seniority, specialization, or hours. We cannot
conclude that switching to remote work would produce the observed pay difference."

**Useful examples if asked:**

| Experience | Remote median | In-person median | Gap |
|---|---:|---:|---:|
| 0-2 years | $85,000 | $76,500 | $8,500 |
| 6-10 years | $154,500 | $120,000 | $34,500 |
| 21+ years | $175,000 | $160,000 | $15,000 |

**Transition:** "We made the same kind of within-experience comparison for roles."

## Slide 6 Role family within experience bands

**Speaker:** Jamal. **Time:** 65 seconds.

**Show:** [Role and experience heatmap](../figures/pay_role_within_experience.png).

**On the slide:** Back-end and Full-stack are the two largest named families.
Back-end has the higher median in all four bands meeting the group-size screen.
Those differences are **$30,000-$39,000**.

**Say:**

"This heatmap compares role families within experience bands. Each cell contains
its median compensation and sample size. Color represents the median, and gray
cells have fewer than 30 respondents.

"We also compared the two most common named families, Full-stack and Back-end.
Back-end has the higher median in all four experience bands where each family has
at least 30 respondents. The differences range from $30,000 to $39,000. The youngest
Back-end group has only 22 respondents, so it is excluded from that headline
comparison. Our n-at-least-30 rule flags sparse comparisons. It does not establish
statistical significance or a causal benefit from changing roles."

**Point to:** The Full-stack and Back-end rows, then a gray cell. Avoid reading every
cell in the heatmap.

**Transition:** "These comparisons describe patterns in the sample, which the
report lead will put in context."

## Slide 7 Interpretation of the findings

**Speaker:** Report lead. **Time:** 60 seconds.

**On the slide:**

- Experience-band medians rise from $85,000 in 0-2 years to $170,000 in 11-20 and 21+.
- Role and work-arrangement comparisons differ after looking within experience bands.
- Compensation comparisons need the context of the workers and jobs being compared.

**Say:**

"Experience, role, and work arrangement are associated with compensation in this
sample. Experience-band medians rise and then flatten in the broader senior groups.
Comparisons within bands show that the overall group gaps are not the whole story.
For a student researching compensation, the practical lesson is to compare similar
roles and experience levels and consider the employer and location, rather than
apply a single survey median to every job. These are sample summaries, not a
prediction or guaranteed pay range for an individual."

## Slide 8 Limitations and conclusion

**Speaker:** Report lead, with shared closing. **Time:** 75 seconds.

**On the slide:**

- Self-selected respondents and optional compensation reporting.
- Preparation cutoffs, grouped roles, and missing experience.
- Remaining differences among workers and employers.
- Associations do not establish causal salary effects.

**Say:**

"The survey is self-selected, and compensation reporting is optional. Our missing-
pay check shows that reporters differ from non-reporters on observed characteristics.
The cutoffs change the tails, and broad role families and experience bands combine
different workers. Full-time status is not directly measured. These choices and
limitations affect how widely the results can be applied.

"Our main finding is that compensation varies with experience, role family, and
work arrangement in this prepared sample. The Remote median remains above the
In-person median within each experience band, but those within-band gaps are
smaller than the overall difference. We report these as associations and avoid
claims that changing arrangement or role will cause a particular salary increase."

## Backup figures for questions

Use these only if they help answer a question. They do not need separate main slides.

- [Experience and ln-pay scatterplot](../figures/exp_vs_logpay.png): positive association with substantial variation.
- [Pay by experience box plot](../figures/pay_by_experience.png): medians and spread within experience groups.
- [Pay by role box plot](../figures/pay_by_role.png): Management has the highest pooled median among named families, $200,000.
- [Original work-arrangement counts](../figures/counts_RemoteWork_detail.png): shows the five source choices before grouping.

## Short answers to likely questions

| Question | Answer |
|---|---|
| Why use medians? | High pay pulls the mean upward. The median describes the middle respondent and is more resistant to extremes. |
| What is the IQR? | Q3 minus Q1, here $90,000. It describes the spread of the middle half. |
| Why compare within experience bands? | To reduce broad experience-composition differences between the groups. |
| Does Remote cause higher pay? | These comparisons show associations. Other differences remain, so they do not establish causality. |
| Why require n>=30? | It is a descriptive screen for sparse comparisons, not a significance test. |
| Why keep missing experience missing? | A blank can mean zero years or a skipped response. We cannot distinguish them reliably. |
| What changed from Samia's dataset? | The EDA retains all prepared rows and groups. The original 20+ band displays as 21+ because its members have more than 20 years of experience. |
| Are the notebooks the whole submission? | They are Jamal's Part B. The group also needs its complete report and other required sections. |

## Rehearsal

Jamal should practice slides 4-6 together with a timer and point to the relevant
parts of each chart. Explain what was compared, what was found, and what the
comparison cannot establish. Let the chart support the explanation rather than
read every number aloud.

The findings and figure files come from notebooks 02 and 03. Preparation counts
come from notebook 01 and were checked against the downloaded raw response data.
Source identity and execution records are in this report folder.
