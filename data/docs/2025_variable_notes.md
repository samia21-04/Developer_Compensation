# Variables in the current team analysis

The EDA uses Samia's verified GitHub dataset with 4,435 respondents. See
`team_source.json` for the exact repository version. Notebook 01 defines the
prepared sample and groups; notebooks 02 and 03 retain every prepared row.

| Prepared field | Meaning and use |
|---|---|
| `ResponseId` | Respondent identifier, used to check one row per respondent |
| `pay` | `ConvertedCompYearly` renamed by notebook 01, annual total compensation in USD |
| `log_pay` | Natural logarithm of pay, used for distribution and scatter plots |
| `WorkExp_num` | General professional work experience in years, already numeric in the source |
| `YearsCode_num` | Total years coding, including education and hobby coding; not substituted for work experience |
| `exp_band` | Prepared experience intervals: 0-2, 3-5, 6-10, 11-20, and more than 20 years |
| `role` | Nine role families prepared from the single-choice DevType question |
| `RemoteWork` | Prepared Remote, Hybrid, or In-person group |
| `RemoteWork_detail` | Original five work-arrangement options, retained for descriptive counts |
| `EdLevel` | Highest completed education category |
| `OrgSize` | Prepared employer size category |
| `Age` | Prepared age category |

The EDA displays the source band called 20+ as 21+ because notebook 01 places
exactly 20 years in 11-20. Band membership stays the same. Hybrid includes both
hybrid source options and Your choice, following notebook 01.

Missing work experience remains unknown because a blank can represent zero years
or nonresponse. The EDA shows missing categories explicitly and excludes unknown
experience from numerical and within-experience comparisons. The prepared file
has 35 missing experience values, 17 missing work arrangements, and 5 missing
education values.

The actual population is U.S. employed survey respondents who report compensation
and meet notebook 01's cutoffs. Employment does not directly identify full-time
status, and notebook 01 does not apply a professional-developer identity filter.
The source filename does not establish a narrower population.
