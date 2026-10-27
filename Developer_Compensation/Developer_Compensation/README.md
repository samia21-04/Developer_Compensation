# Developer Careers and Compensation

**CSC 3780 Fundamentals of Data Science — Fall 2026 — Final Project**
Instructor: Kiril Kuzmin
Section: [Section] · Group: [Group number]
Members: [Name 1], [Name 2], [Name 3], [Name 4]

## Question

How do experience, job roles, and work arrangements (remote, hybrid, in-person) relate to reported developer compensation?

## Data

Stack Overflow Annual Developer Survey 2025 — https://survey.stackoverflow.co/
One row = one survey respondent. Our population: full-time employed respondents in the United States who reported compensation. Compensation measure: `ConvertedCompYearly` (annual pay in USD).

See `data/raw/README.md` for download instructions and `data/docs/` for the schema and questionnaire.

## How to run

```bash
pip install -r requirements.txt
```

1. Download the 2025 survey zip and place `survey_results_public.csv` in `data/raw/` (see `data/raw/README.md`).
2. Run the notebooks in order, top to bottom:

| Notebook | Covers (rubric) | Reads | Writes |
|---|---|---|---|
| `01_data_prep.ipynb` | Describe data, data quality, preparation | `data/raw/survey_results_public.csv` | `data/processed/us_fulltime_clean.csv` |
| `02_distributions.ipynb` | Distributions | processed CSV | `figures/` |
| `03_relationships.ipynb` | Relationships, interpretation | processed CSV | `figures/` |
| `04_modeling.ipynb` | Optional modeling | processed CSV | `figures/` |

## Repository layout

```
data/raw/         untouched download (never edited)
data/processed/   cleaned dataset written by notebook 01
data/docs/        survey schema + questionnaire
notebooks/        analysis, run in numbered order
figures/          saved plots used in the report
report/           final PDF report + member contributions
```

## Team workflow

- Work on your own branch and open a pull request into `main`.
- Clear notebook outputs before committing (Kernel → Restart & Clear Output).
- Notebooks 02–04 load the processed CSV — never re-clean the raw data in them.
- Before submission, run every notebook top to bottom on a fresh clone.

## Limitations (summary)

Respondents are self-selected, and many do not report compensation. Results describe this sample only, and associations are not causal effects.
