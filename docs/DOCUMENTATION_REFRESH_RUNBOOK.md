# Documentation refresh runbook

Use this when a **new Shopify theme export** and/or **new Matrixify dump** lands and you need to update the documentation hub (markdown + root HTML pages) the same way the platform was last reviewed.

## Prerequisites

- Python 3.9+ (`python3 --version`)
- This repository cloned locally
- **Older baseline** theme folder under `code/` (optional but recommended for diffs)
- **Newer** theme folder under `code/`
- Matrixify CSV folders under `data/` (optional, for catalog metrics)

## 1. Add evidence to the repo

1. **Theme:** Download from Shopify → unzip into `code/` (see [code/README.md](../code/README.md)).
2. **Matrixify:** Export from the app → unzip into `data/` (see [data/README.md](../data/README.md)).

Commit those folders on a branch so reviewers can see raw evidence alongside doc edits.

## 2. Theme diff (inventory + changed files)

Compare the previous baseline export to the new one:

```bash
python3 scripts/diff_theme_exports.py \
  code/superfeetww-theme-NOV2025 \
  code/theme_export__YOUR-NEW-EXPORT-FOLDER \
  > docs/internal_THEME_DELTA.md
```

Open `docs/internal_THEME_DELTA.md`: note new/removed templates, sections, snippets, and changed assets.

Update counts in:

- [README.md](../README.md) (if you surface section/template metrics)
- [docs/theme-architecture-v2.md](./theme-architecture-v2.md), [docs/QUICK_REFERENCE.md](./QUICK_REFERENCE.md)
- [docs/business-user-guide.md](./business-user-guide.md) (template counts)
- Matching root `*.html` files

## 3. Matrixify diff (catalog / columns)

Pick **baseline** and **new** export folders under `data/`:

```bash
python3 scripts/diff_matrixify_exports.py \
  data/SFUS-EVERYTHING-Export_2025-10-16_184845 \
  data/YOUR_NEW_US_EXPORT_FOLDER \
  > docs/internal_MATRIXIFY_DELTA_US.md
```

Use unique resource **IDs** in the CSVs (not raw row counts) when updating product/collection/blog/metaobject numbers. See the executive-summary pattern in any existing `docs/internal_MATRIXIFY_*.md`.

Refresh hub metrics in README, [business-user-guide.md](./business-user-guide.md), [data-guide.md](./data-guide.md), and HTML mirrors.

## 4. Internal delta docs

- Keep `docs/internal_THEME_DELTA*.md` / `docs/internal_MATRIXIFY*.md` as **optional** engineering notes; they can be committed or regenerated each cycle.
- Prefer stable filenames or date-stamp new files so history stays clear.

## 5. Ship

1. Proofread markdown ↔ HTML for pages you touched.
2. Commit: evidence (`code/`, `data/`) + script output + documentation edits.
3. Push; redeploy GitHub Pages (or your static host) if applicable.

## Optional: knowledge pack

If you use Arcadia’s `agent/` layout and `scripts/build_agent_pack.py`, restore those from your implementation partner; they were not required for theme/Matrixify refresh.

*Last updated: March 2026*
