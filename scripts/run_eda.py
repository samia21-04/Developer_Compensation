"""Execute notebooks 02 and 03 in fresh namespaces and leave their outputs clear."""
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import traceback


def main():
    root = Path(__file__).resolve().parents[1]
    os.chdir(root / "notebooks")
    os.environ["MPLBACKEND"] = "Agg"
    sys.path.insert(0, str(root / "scripts"))
    import matplotlib.pyplot as plt
    plt.show = lambda: None
    input_path = root / "data/processed/us_fulltime_clean.csv"
    before = hashlib.sha256(input_path.read_bytes()).hexdigest()
    logs = root / "tmp/eda"
    logs.mkdir(parents=True, exist_ok=True)
    results = []
    for filename in ["02_distributions.ipynb", "03_relationships.ipynb"]:
        notebook = json.loads((root / "notebooks" / filename).read_text(encoding="utf-8"))
        namespace = {"__name__": "__main__"}
        capture = io.StringIO()
        count = 0
        try:
            with redirect_stdout(capture), redirect_stderr(capture):
                for i, cell in enumerate(notebook["cells"]):
                    if cell["cell_type"] == "code":
                        exec(compile("".join(cell["source"]), f"{filename}:cell-{i+1}", "exec"), namespace)
                        count += 1
        except Exception:
            capture.write(traceback.format_exc())
            (logs / f"{Path(filename).stem}.log").write_text(capture.getvalue(), encoding="utf-8")
            raise
        (logs / f"{Path(filename).stem}.log").write_text(capture.getvalue(), encoding="utf-8")
        results.append({"notebook": filename, "code_cells_executed": count, "status": "passed"})
        print(f"Passed: {filename} ({count} code cells)", flush=True)
    after = hashlib.sha256(input_path.read_bytes()).hexdigest()
    if before != after:
        raise AssertionError("The prepared input CSV changed while running EDA.")
    report = {"completed_at_utc": datetime.now(timezone.utc).isoformat(), "input_sha256": before,
        "input_unchanged": True, "execution_method": "Every code cell in order, fresh Python namespace per notebook",
        "notebooks": results, "scope": "Part B only; notebooks 01 and 04 not executed"}
    (root / "report/jamal_eda_execution.json").write_text(json.dumps(report, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
