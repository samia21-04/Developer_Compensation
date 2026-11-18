# Developer Careers and Compensation

**CSC 3780 Fundamentals of Data Science — Fall 2026 — Final Project**
Instructor: Kiril Kuzmin
Section: [Section] · Group: [Group number]
Members: [Samia Haynes], Jamal Ford, [Name 3], [Name 4]

## Question

How do experience, job roles, and work arrangements (remote, hybrid, in-person) relate to reported developer compensation?

## Data

Stack Overflow Annual Developer Survey 2025.

- Original dataset (141 MB CSV): https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/2025/results.csv ([archive folder](https://github.com/StackExchange/Survey/tree/main/packages/archive/2025), [methodology](https://survey.stackoverflow.co/2025/methodology/))
- Processed dataset (4,435 rows × 12 columns): https://github.com/samia21-04/Developer_Compensation/blob/main/data/processed/us_fulltime_clean.csv

One row = one survey respondent. The prepared sample contains employed respondents in the United States who reported compensation and meet notebook 01's pay cutoffs. The 2025 employment question does not directly distinguish full-time from part-time work. Compensation measure: `ConvertedCompYearly` (annual total pay in USD), renamed `pay` in the processed file.

See `data/raw/README.md` for download instructions and `data/docs/` for the schema and questionnaire.

## How to run

```bash
pip install -r requirements.txt
```

1. Only for notebook 01: download the 2025 `results.csv` and save it as `data/raw/survey_results_public.csv` (see `data/raw/README.md`). Notebooks 02–04 need only the committed processed CSV.
2. Run the notebooks in order, top to bottom:

| Notebook | Covers (rubric) | Reads | Writes |
|---|---|---|---|
| `01_data_prep.ipynb` | Describe data, data quality, preparation | `data/raw/survey_results_public.csv` | `data/processed/us_fulltime_clean.csv` |
| `02_distributions.ipynb` | Distributions | processed CSV | `figures/` |
| `03_relationships.ipynb` | Relationships, interpretation | processed CSV | `figures/` |
| `04_modeling.ipynb` | Optional modeling | processed CSV | `figures/` |

### Jamal's Part B

Notebooks 02 and 03 use the committed processed CSV directly. To regenerate their
figures, CSV summary tables, and findings draft from the repository root:

```bash
python scripts/run_eda.py
```

This executes every code cell in each notebook, starting each notebook with a fresh
namespace, and keeps the notebook output cells clear. It checks that the input CSV
is unchanged. The results are saved to `figures/`, `tables/`, and
`report/jamal_eda_findings.md`; the execution record and input hash are in `report/`.
Interactive notebook runs are also supported from the repository root or `notebooks/`.

`eda_common` is the local helper file `scripts/eda_common.py`, shared by notebooks
02 and 03. Keep that file and the data with the notebooks. Open the whole repository
folder in VS Code so its included `.vscode/settings.json` can resolve the helper
for editor navigation. Restart the notebook kernel and run all cells after updates.

The EDA preserves notebook 01's role families, work-arrangement grouping, experience
band membership, and pay cutoffs. The band stored as `20+` is displayed as `21+`
because its lower boundary is strictly greater than 20 years. Missing categories
remain visible; conditional plots flag cells below n=30. This is a descriptive
display rule, not a significance test. The full project still needs the shared
fresh-clone run of all four notebooks before submission.

## Repository layout

```
data/raw/         untouched download (never edited)
data/processed/   cleaned dataset written by notebook 01
data/docs/        survey schema + questionnaire
notebooks/        analysis, run in numbered order
figures/          saved plots used in the report
tables/           EDA summaries and conditional cell counts in CSV format
scripts/          shared EDA helpers and the Part B execution command
report/           final PDF report + member contributions
```

## Team workflow

- Work on your own branch and open a pull request into `main`.
- Clear notebook outputs before committing (Kernel → Restart & Clear Output).
- Notebooks 02–04 load the processed CSV — never re-clean the raw data in them.
- Before submission, run every notebook top to bottom on a fresh clone.

## Limitations (summary)

Respondents are self-selected, and many do not report compensation. Results describe this sample only, and associations are not causal effects.
