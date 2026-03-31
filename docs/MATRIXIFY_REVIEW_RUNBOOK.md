# Matrixify export review runbook

Use this when a new Matrixify export arrives so documentation stays aligned with live store data.

## Where exports live

Commit **unzipped** CSV folders under **`data/`** (see [data/README.md](../data/README.md)). Zip downloads are gitignored inside `data/` to avoid duplicating the same export; extract before committing.

## Baseline naming

| Region | Example folder name |
|--------|---------------------|
| US | `SFUS-EVERYTHING-Export_YYYY-MM-DD_*` |
| CA | `SFCA_EVERYTHING_Export_YYYY-MM-DD_*` |
| UK | `SFUK_Export_YYYY-MM-DD_*` |

## Comparing two exports

```bash
python3 scripts/diff_matrixify_exports.py \
  data/OLDER_EXPORT_FOLDER \
  data/NEWER_EXPORT_FOLDER \
  > docs/internal_MATRIXIFY_DELTA_US.md
```

Interpret row counts carefully (Matrixify expands discounts, collection membership, etc.). For catalog **facts** (products, collections, blogs), count **unique resource IDs** in the CSVs or use [Export Summary](Export%20Summary.csv) rows where appropriate.

Full end-to-end refresh (theme + docs + HTML): [DOCUMENTATION_REFRESH_RUNBOOK.md](./DOCUMENTATION_REFRESH_RUNBOOK.md).

## After the diff

1. **Row deltas** — Sanity-check large swings in Admin.
2. **New columns** — Update [data-guide.md](./data-guide.md) when metafield namespaces change.
3. **Theme** — Cross-check against the latest theme under `code/`.
4. **Hub metrics** — Update [README.md](../README.md) and [business-user-guide.md](./business-user-guide.md) (and HTML mirrors).

## Deliverable

- `docs/internal_MATRIXIFY_*.md` (optional but useful)
- Edits to `docs/data-guide.md` / `data-guide.html` when schema or import workflows change

*Last updated: March 2026*
