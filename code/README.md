# Theme exports (Shopify)

Drop **Download theme** exports from **Shopify Admin → Online Store → Themes** (or your pipeline) into this folder.

## Naming

Use Shopify’s default folder name, e.g. `theme_export__<store>__<date>`, so snapshots stay sortable.

## What to keep in Git

- **US transactional theme** — latest export used to refresh documentation counts.
- **Prior baseline (optional)** — e.g. an older US export to diff against when updating the hub (see [DOCUMENTATION_REFRESH_RUNBOOK](../docs/DOCUMENTATION_REFRESH_RUNBOOK.md)).

Regional CA/UK themes can live here when you need to reconcile template counts; they are not required for every refresh.

## Archives

`*.zip` downloads are ignored here (see `code/.gitignore`); store zip backups outside Git or re-download from Shopify when needed.
