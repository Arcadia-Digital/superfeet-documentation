# Matrixify / store data exports

Place **Matrixify** (or equivalent) CSV export **folders** here after unzipping.

## Suggested layout

| Region | Example folder |
|--------|----------------|
| US | `SFUS-EVERYTHING-Export_YYYY-MM-DD_*` |
| Canada | `SFCA_EVERYTHING_Export_YYYY-MM-DD_*` |
| UK | `SFUK_Export_YYYY-MM-DD_*` |

Use a stable prefix and date so diffs and docs stay traceable.

## Archives

`*.zip` is ignored in this directory (see `data/.gitignore`); extract before committing or keep zips outside the repo.

## Large files

Matrixify **`Discounts.csv`** can exceed GitHub’s ~50 MB guidance (millions of discount-code rows). For documentation-only refreshes you can omit discounts from the export, delete that CSV after diffing, or use [Git LFS](https://git-lfs.github.com) if you must keep it in Git.

## Review workflow

See [MATRIXIFY_REVIEW_RUNBOOK.md](../docs/MATRIXIFY_REVIEW_RUNBOOK.md) and [DOCUMENTATION_REFRESH_RUNBOOK.md](../docs/DOCUMENTATION_REFRESH_RUNBOOK.md).
