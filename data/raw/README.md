# Raw data

This folder holds the **untouched** survey download. Never edit these files — all cleaning happens in `notebooks/01_data_prep.ipynb`.

## How to get the data

Stack Overflow no longer offers the 2025 survey as a zip on survey.stackoverflow.co. The official copy is in its GitHub archive:

- Folder: https://github.com/StackExchange/Survey/tree/main/packages/archive/2025
- Direct download (141 MB): https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/2025/results.csv

1. Download `results.csv` with the direct link above.
2. Rename it to `survey_results_public.csv` and put it in this folder (`data/raw/`).

Do not use the `raw.githubusercontent.com` address for this file: it returns a 134-byte Git LFS pointer, not the data.

The schema (`schema.csv`) and questionnaire (`survey.pdf`) from the same folder are already in `data/docs/`.

| Check | Value |
|---|---|
| Size | 140,893,245 bytes |
| SHA-256 | `2d1f65308877282edfb4470520eabbc08cb499118432a3dcec6a66c086aa2baa` |
| Shape | 49,191 rows × 172 columns |
| Verified download | November 17, 2026 |

## Why the CSV isn't committed

The file is larger than GitHub's 100 MB file limit, so it is listed in `.gitignore`. Only notebook 01 needs it. Notebooks 02–04 read `data/processed/us_fulltime_clean.csv`, which is committed.

## About the data

- Source: Stack Overflow Annual Developer Survey 2025
- License: Open Database License (ODbL) 1.0; contents under DbCL 1.0
- Fielded May 29 – June 23, 2025; about 49,000 responses from 177 countries
- Salaries converted to USD using the June 25, 2025 exchange rate
- Methodology: https://survey.stackoverflow.co/2025/methodology/
