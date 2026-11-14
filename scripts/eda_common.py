"""Shared input checks, labels, and chart helpers for notebooks 02 and 03."""
import hashlib
import json
from pathlib import Path
import platform
import textwrap

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd

MISSING = "Missing / not reported"
EXPERIENCE_ORDER = ["0-2", "3-5", "6-10", "11-20", "21+"]
MIN_GROUP_N = 30  # Descriptive display screen, not a significance test.
REMOTE_LABELS = {
    "Hybrid (some remote, leans heavy to in-person)": "Hybrid: mainly in-person",
    "Hybrid (some in-person, leans heavy to flexibility)": "Hybrid: mainly flexible",
    "Your choice (very flexible, you can come in when you want or just as needed)": "Your choice",
}


def labels(series):
    return (series.astype("string").str.strip().str.replace("\u2019", "'", regex=False)
            .str.replace("\ufffd", "'", regex=False).replace("", pd.NA))


def education_labels(series):
    result = labels(series)
    for prefix, short in {
        "Bachelor": "Bachelor's degree", "Master": "Master's degree",
        "Professional degree": "Professional degree", "Associate": "Associate degree",
        "Some college": "Some college, no degree", "Secondary school": "Secondary school",
        "Primary/elementary": "Primary / elementary school", "Other": "Other",
    }.items():
        result = result.mask(result.str.startswith(prefix, na=False), short)
    return result.fillna(MISSING)


def load_data(root):
    """Read the team CSV without filtering, imputing, or writing any input data."""
    path = root / "data/processed/us_fulltime_clean.csv"
    manifest_path = root / "data/docs/team_source.json"
    if not manifest_path.exists():
        raise FileNotFoundError("Missing data/docs/team_source.json, which records Samia's GitHub source.")
    provenance = json.loads(manifest_path.read_text(encoding="utf-8"))
    input_bytes = path.read_bytes()
    input_hash = hashlib.sha256(input_bytes).hexdigest()
    # Git can check out text with LF or CRLF. Compare normalized content so a
    # legitimate cross-platform checkout still matches the recorded GitHub data.
    content_hash = hashlib.sha256(input_bytes.replace(b"\r\n", b"\n")).hexdigest()
    if content_hash != provenance["files"]["data/processed/us_fulltime_clean.csv"]["content_sha256"]:
        raise ValueError("The prepared CSV differs from the verified GitHub copy. Refresh the data-source record before analysis.")
    source = pd.read_csv(path)
    required = {"ResponseId", "pay", "log_pay", "WorkExp_num", "exp_band", "role",
                "RemoteWork", "RemoteWork_detail", "EdLevel"}
    if absent := required - set(source.columns):
        raise ValueError(f"Missing prepared columns: {sorted(absent)}. Check notebook 01's output.")
    if source.empty or source.ResponseId.isna().any() or source.ResponseId.duplicated().any():
        raise ValueError("The prepared file must have one nonmissing, unique ResponseId per row.")
    for column in ["pay", "log_pay", "WorkExp_num"]:
        values = pd.to_numeric(source[column], errors="coerce")
        if (source[column].notna() & (values.isna() | ~np.isfinite(values))).any():
            raise ValueError(f"Non-numeric or non-finite {column} values require preparation review.")
    if source.pay.isna().any() or not source.pay.gt(0).all():
        raise ValueError("The prepared sample must have positive annual USD pay on every row.")
    if source.log_pay.isna().any() or not np.allclose(source.log_pay, np.log(source.pay)):
        raise ValueError("Prepared log_pay is expected to be the natural logarithm of pay.")
    if source.WorkExp_num.dropna().lt(0).any():
        raise ValueError("Negative professional experience requires preparation review.")
    expected_bands = pd.cut(source.WorkExp_num, [0, 2, 5, 10, 20, np.inf],
        labels=["0-2", "3-5", "6-10", "11-20", "20+"], include_lowest=True).astype("string")
    if not expected_bands.fillna(MISSING).eq(source.exp_band.fillna(MISSING)).all():
        raise ValueError("Experience bands differ from notebook 01's boundaries. Review the preparation rules.")
    expected_remote = source.RemoteWork_detail.map({
        "Remote": "Remote", "In-person": "In-person",
        "Hybrid (some remote, leans heavy to in-person)": "Hybrid",
        "Hybrid (some in-person, leans heavy to flexibility)": "Hybrid",
        "Your choice (very flexible, you can come in when you want or just as needed)": "Hybrid",
    })
    if not expected_remote.fillna(MISSING).eq(source.RemoteWork.fillna(MISSING)).all():
        raise ValueError("Prepared work-arrangement groups do not match notebook 01's mapping.")
    data = source.copy()
    data["PayUSD"] = source.pay
    data["LogPay"] = source.log_pay  # Natural log, matching preparation and modeling.
    data["ExperienceYears"] = source.WorkExp_num
    # Presentation label only: notebook 01's right-closed 20+ band begins above 20.
    data["ExperienceBand"] = source.exp_band.astype("string").replace({"20+": "21+"}).fillna(MISSING)
    data["RoleGroup"] = source.role.fillna(MISSING)
    data["WorkArrangement"] = source.RemoteWork.fillna(MISSING)
    data["WorkArrangementDetail"] = labels(source.RemoteWork_detail).replace(REMOTE_LABELS).fillna(MISSING)
    data["Education"] = education_labels(source.EdLevel)
    output = {"figures": root / "figures", "tables": root / "tables", "report": root / "report"}
    for directory in output.values():
        directory.mkdir(parents=True, exist_ok=True)
    info = {
        "input_file": "data/processed/us_fulltime_clean.csv",
        "input_sha256": input_hash,
        "input_content_sha256": content_hash,
        "input_rows": len(source), "analysis_rows": len(data),
        "source_repository": provenance["repository"],
        "source_commit": provenance["commit"],
        "source_preparation_notebook": "notebooks/01_data_prep.ipynb",
        "population": "U.S. employed respondents with reported compensation, after notebook 01's pay cutoffs",
        "population_limit": "2025 does not directly distinguish full-time work; no professional-developer identity filter in notebook 01",
        "preparation": "Notebook 01 retains pay from $10,000 through the reporters' 99th percentile ($641,900)",
        "experience_label": "Original 20+ displayed as 21+; original band membership preserved",
        "missing_experience": int(data.ExperienceYears.isna().sum()),
        "missing_work_arrangement": int(source.RemoteWork.isna().sum()),
        "missing_education": int(source.EdLevel.isna().sum()),
        "log_base": "natural logarithm (ln), supplied by notebook 01",
        "additional_eda_row_removals": 0,
        "versions": {"python": platform.python_version(), "pandas": pd.__version__,
                     "numpy": np.__version__, "matplotlib": matplotlib.__version__},
    }
    (output["report"] / "jamal_eda_run_metadata.json").write_text(json.dumps(info, indent=2), encoding="utf-8")
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.dpi": 110})
    return data, info, output


def band_order(data):
    observed = set(data.ExperienceBand.dropna())
    return [value for value in EXPERIENCE_ORDER + [MISSING] if value in observed]


def pay_summary(data, by=None):
    groups = [("All respondents", data)] if by is None else data.groupby(by, observed=True, dropna=False, sort=False)
    records = []
    for key, group in groups:
        pay = group.PayUSD
        record = {"n": len(pay), "median_usd": pay.median(),
            "q1_usd": pay.quantile(.25), "q3_usd": pay.quantile(.75),
            "iqr_usd": pay.quantile(.75)-pay.quantile(.25)}
        if by is None:
            record["group"] = key
        elif isinstance(by, list):
            record.update(zip(by, key if isinstance(key, tuple) else (key,)))
        else:
            record[by] = key
        records.append(record)
    columns = (["group"] if by is None else by if isinstance(by, list) else [by]) + ["n", "median_usd", "q1_usd", "q3_usd", "iqr_usd"]
    return pd.DataFrame(records, columns=columns)


def dollars(value, position=None):
    return f"${value:,.0f}"


def wrapped(values, width=34):
    return [textwrap.fill(str(value), width) for value in values]


def save_figure(fig, filename, info, output):
    fig.text(.01, .015, f"U.S. employed respondents | prepared sample n={info['analysis_rows']:,} | descriptive comparisons", fontsize=8, color="#555555")
    fig.tight_layout(rect=(0, .06, 1, 1))
    fig.savefig(output["figures"] / f"{filename}.png", dpi=160, bbox_inches="tight")
    plt.show()
    plt.close(fig)


def count_plot(data, column, title, filename, info, output):
    counts = data[column].value_counts().sort_values()
    fig, ax = plt.subplots(figsize=(11, max(4, .5 * len(counts) + 1.7)))
    ax.barh(range(len(counts)), counts, color="#31688e")
    ax.set_yticks(range(len(counts)), wrapped(counts.index))
    for i, value in enumerate(counts):
        ax.text(value+counts.max()*.015, i, f"{value:,}", va="center", fontsize=9)
    ax.set_xlim(0, counts.max()*1.18)
    ax.set(xlabel="Respondents", title=f"{title} (n={len(data):,})")
    counts.rename_axis(column).reset_index(name="n").to_csv(output["tables"] / f"{filename}.csv", index=False)
    save_figure(fig, filename, info, output)


def box_plot(data, column, order, title, filename, info, output):
    groups = [data.loc[data[column].eq(label), "PayUSD"].to_numpy() for label in order]
    fig, ax = plt.subplots(figsize=(11, max(4.8, .54*len(order)+1.7)))
    ax.boxplot(groups, vert=False, patch_artist=True,
        boxprops={"facecolor": "#90c3d4"}, medianprops={"color": "#173f5f"},
        flierprops={"marker": ".", "markersize": 3, "alpha": .35})
    tick_labels = [f"{label} (n={len(group):,})" for label, group in zip(order, groups)]
    ax.set_yticks(range(1, len(order)+1), wrapped(tick_labels, 36))
    ax.xaxis.set_major_formatter(FuncFormatter(dollars))
    ax.set(xlabel="Annual total compensation in USD", title=title)
    ax.grid(axis="x", alpha=.2)
    save_figure(fig, filename, info, output)
