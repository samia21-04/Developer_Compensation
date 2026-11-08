# Raw data

This folder holds the **untouched** survey download. Never edit these files — all cleaning happens in `notebooks/01_data_prep.ipynb`.

## How to get the data

1. Go to https://survey.stackoverflow.co/ and download the **2025** data (CSV zip).
2. Unzip it.
3. Move `survey_results_public.csv` into this folder (`data/raw/`).
4. Move the schema CSV and the questionnaire PDF into `data/docs/`.

Download date: [fill in]

## Why the CSV isn't committed

The raw file is likely larger than GitHub's 100 MB file limit, so it is listed in `.gitignore`. Each group member downloads it using the steps above. Check the license file included in the zip and note its terms in the final report.

## About the data

- Source: Stack Overflow Annual Developer Survey 2025
- Fielded May 29 – June 23, 2025; about 49,000 responses from 177 countries
- Salaries converted to USD using the June 25, 2025 exchange rate
- Methodology: https://survey.stackoverflow.co/2025/methodology/
