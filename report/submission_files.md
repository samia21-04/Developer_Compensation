# Jamal Part B handoff files

The current analysis uses Samia's cleaned GitHub CSV with **4,435 respondents**.
The current notebook titles and opening notes identify the team dataset. They do
not use the earlier raw-data preview.

## Jamal analysis files

| File or folder | Purpose |
|---|---|
| `notebooks/02_distributions.ipynb` | Pay and experience distributions and categorical charts |
| `notebooks/03_relationships.ipynb` | Pay comparisons, within-experience checks, interpretation, and limitations |
| `scripts/eda_common.py` | Shared loading checks, summaries, labels, and figure saving |
| `scripts/run_eda.py` | Runs both notebooks and checks that the prepared input stays unchanged |
| `figures/` | Thirteen EDA charts |
| `tables/` | Eighteen CSV summaries and conditional cell counts |
| `report/jamal_eda_findings.md` | EDA and Findings text for the team report |
| `report/jamal_distributions.md` | Additional distribution interpretation |
| `report/report_draft.md` | Paste-ready draft covering completed preparation and EDA |
| `report/presentation_order.md` | Timed group presentation order and speaking notes |
| `report/contributions.md` | Jamal contribution entry alongside the team entries |

## Source and reproducibility files

- `notebooks/01_data_prep.ipynb` is Samia's preparation notebook from GitHub.
- `data/processed/us_fulltime_clean.csv` is her prepared dataset from GitHub.
- `data/docs/team_source.json` records the repository version and file hashes.
- `requirements.txt` lists the analysis packages.
- `.vscode/settings.json` helps VS Code resolve the local `scripts/eda_common.py` helper.
- `report/jamal_eda_execution.json` records the successful run of notebooks 02 and 03.
- `report/jamal_eda_run_metadata.json` records the exact input and sample description.

Keep the folder structure when sharing the notebooks. Sending only the two `.ipynb`
files leaves out the helper and data needed to rerun them. Samia's notebook also
needs the raw survey file in `data/raw/survey_results_public.csv` to rerun preparation;
the large raw file is not included in the Part B review bundle.

## Team submission still needs assembly

The team repository's report outline calls for a final `report/final_report.pdf`
covering the question, data, preparation, EDA, findings, limitations, recommendations,
sources, and member contributions. Modeling belongs to its designated lead if the
team includes it. The local modeling notebook is still a scaffold, so the presentation
order does not invent model-performance results.

The two completed EDA notebooks are Jamal's notebook deliverables. They are not the
entire group submission. Check the course assignment for its required upload format
and whether saved notebook outputs are required. The repository workflow requests
clear notebook outputs before committing, so run all cells to view their results.

The course-site upload remains a separate team step. The Part B work is prepared
on `codex/jamal-part-b` for review and integration into the team project.
