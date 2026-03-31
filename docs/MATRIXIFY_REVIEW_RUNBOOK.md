# Matrixify export review runbook

Use this when a new Matrixify export arrives so documentation stays aligned with live store data.

**Storage:** Keep Matrixify CSV folders outside this documentation repository (internal drive, secure share, or vendor workspace). This repo intentionally does not track large data exports.

## Suggested baseline naming

Use clear folder names per store and date, for example:

| Region | Example folder name |
|--------|---------------------|
| US | `SFUS-EVERYTHING-Export_YYYY-MM-DD` |
| CA | `SFCA_EVERYTHING_Export_YYYY-MM-DD` |
| UK | `SFUK_Export_YYYY-MM-DD` |

## Comparing two exports (optional)

If you copy `scripts/diff_matrixify_exports.py` into a workspace that contains two export folders:

```bash
python3 scripts/diff_matrixify_exports.py \
  path/to/OLDER_EXPORT_FOLDER \
  path/to/NEWER_EXPORT_FOLDER \
  > matrixify-delta-notes.md
```

The script summarizes row counts and header differences per CSV. Interpret row counts carefully (Matrixify often expands discounts, collection membership, etc. into many rows).

## What to do with the diff

1. **Row deltas** — Large swings in `Products.csv`, `Metaobjects.csv`, `Pages.csv`, or `Menus.csv` usually deserve a quick sanity check in Admin, not necessarily doc edits.
2. **New columns** — Update [data-guide.md](./data-guide.md) when new metafield namespaces or important columns appear in product or metaobject exports.
3. **Cross-check theme** — Spot-check metafields and metaobject types against the current theme (export from **Online Store → Themes** or your development pipeline).
4. **Hub metrics** — If [README.md](../README.md) or [business-user-guide.md](./business-user-guide.md) cite product/collection counts as facts, refresh them from the new export or label them “as of &lt;date&gt;”.

## Deliverable

- A short delta note (markdown or ticket) describing material catalog or schema changes
- Edits to `docs/data-guide.md` and matching `data-guide.html` when workflows or namespaces change

*Last Updated: March 2026*
