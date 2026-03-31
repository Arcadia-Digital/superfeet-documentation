#!/usr/bin/env python3
"""
Compare two Matrixify (or similar) CSV export folders.

For each `*.csv` in `new_dir`, compares to same filename in `old_dir`:
- row count (excluding header)
- header columns (set difference if headers differ)

Usage:
  python3 scripts/diff_matrixify_exports.py \\
    data/SFUS-EVERYTHING-Export_2025-10-16_184845 \\
    data/SFUS-EVERYTHING-Export_NEW \\
    > docs/internal_MATRIXIFY_DELTA.md

If a file exists only in one tree, it is listed under added/removed.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def read_header_and_rows(csv_path: Path) -> tuple[list[str], int]:
    with csv_path.open(newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return [], 0
        n = sum(1 for _ in reader)
        return header, n


def main() -> int:
    ap = argparse.ArgumentParser(description="Diff Matrixify CSV export directories")
    ap.add_argument("old_dir", type=Path, help="Baseline export folder")
    ap.add_argument("new_dir", type=Path, help="New export folder")
    args = ap.parse_args()
    old_root = args.old_dir.resolve()
    new_root = args.new_dir.resolve()
    if not old_root.is_dir() or not new_root.is_dir():
        print("Both arguments must be directories.", file=sys.stderr)
        return 1

    new_files = {p.name: p for p in new_root.glob("*.csv")}
    old_files = {p.name: p for p in old_root.glob("*.csv")}

    added = sorted(set(new_files) - set(old_files))
    removed = sorted(set(old_files) - set(new_files))
    common = sorted(set(new_files) & set(old_files))

    lines = [
        f"# Matrixify export diff",
        "",
        f"- **Baseline:** `{old_root}`",
        f"- **New:** `{new_root}`",
        "",
        "## File inventory",
        "",
        "| File | Old rows | New rows | Delta | Header match |",
        "|------|----------|----------|-------|--------------|",
    ]

    mismatches = []
    for name in common:
        oh, orows = read_header_and_rows(old_files[name])
        nh, nrows = read_header_and_rows(new_files[name])
        delta = nrows - orows
        hdr_ok = oh == nh
        extra = ""
        if not hdr_ok:
            extra = "columns differ"
            mismatches.append((name, set(oh) - set(nh), set(nh) - set(oh)))
        lines.append(
            f"| {name} | {orows} | {nrows} | {delta:+d} | "
            f"{'yes' if hdr_ok else 'NO — ' + extra} |"
        )

    lines.extend(["", f"## Added CSV files ({len(added)})", ""])
    if added:
        lines.extend(f"- `{n}`" for n in added)
    else:
        lines.append("_None._")
    lines.extend(["", f"## Removed CSV files ({len(removed)})", ""])
    if removed:
        lines.extend(f"- `{n}`" for n in removed)
    else:
        lines.append("_None._")

    if mismatches:
        lines.extend(["", "## Column set differences", ""])
        for name, only_old, only_new in mismatches:
            if only_old or only_new:
                lines.append(f"### `{name}`")
                if only_old:
                    lines.append(f"- Only in **old**: {sorted(only_old)[:50]}{'…' if len(only_old) > 50 else ''}")
                if only_new:
                    lines.append(f"- Only in **new**: {sorted(only_new)[:50]}{'…' if len(only_new) > 50 else ''}")
                lines.append("")

    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
