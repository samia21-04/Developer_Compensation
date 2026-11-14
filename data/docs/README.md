# Survey documentation

Put these files from the 2025 download here:

- `survey_results_schema.csv` — column names and the question each one comes from
- The questionnaire PDF — the exact wording and answer options for every question

Check here before using any column: whether it was multi-select, what the answer options were, and how the question was worded.

`team_source.json` records the verified GitHub version of Samia's preparation
notebook and cleaned dataset. The EDA checks the dataset's content against this
record, allowing Git's LF/CRLF line-ending differences across operating systems.
