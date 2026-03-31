# Matrixify export review runbook

Use this when a new Matrixify “everything” export arrives so documentation stays aligned with live store data and with the theme review in [internal_THEME_DELTA_MAR2026.md](./internal_THEME_DELTA_MAR2026.md).

## Baselines in this repo (current)

| Region | Folder under `data/` | Export date (from folder name) | Notes |
|--------|----------------------|--------------------------------|--------|
| US (full, Oct 2025) | `SFUS-EVERYTHING-Export_2025-10-16_184845` | 2025-10-16 | Includes Redirects, Files |
| US (forAI, Mar 2026) | `EVERYTHING-Export-forAI_2026-03-31_154533` | 2026-03-31 | Current catalog snapshot; no Redirects/Files — see [internal_MATRIXIFY_DELTA_US_2026-03-31.md](./internal_MATRIXIFY_DELTA_US_2026-03-31.md) |
| CA | `SFCA_EVERYTHING_Export_2025-11-11_150447` | 2025-11-11 | |
| UK | `SFUK_Export_2025-11-11_152620` | 2025-11-11 | |

After you add the new export folder (keep the Matrixify naming pattern), run:

```bash
python3 scripts/diff_matrixify_exports.py \
  data/SFUS-EVERYTHING-Export_2025-10-16_184845 \
  data/<NEW_SFUS_FOLDER> \
  > docs/internal_MATRIXIFY_DELTA_US_2026-03-31.md
```

Repeat per region with the appropriate baseline folder.

## What to do with the diff

1. **Row deltas** — Large swings in `Products.csv`, `Metaobjects.csv`, `Pages.csv`, or `Menus.csv` usually deserve a quick sanity check in Admin, not necessarily doc edits.
2. **New columns** — Update [data-guide.md](./data-guide.md) when new metafield namespaces or important columns appear in `Products.csv` / metaobject sheets.
3. **Cross-check theme** — If the dump includes definitions that mirror theme usage (e.g. metaobject types), spot-check against Liquid from the latest US theme export in `code/theme_export__www-superfeet-com-us-spring-sale-3-25-3-31__31MAR2026-0344pm/`.
4. **Hub metrics** — If [README.md](../README.md) or [business-user-guide.md](./business-user-guide.md) cite product/collection counts as facts, refresh them from the new export or label them “as of &lt;date&gt;”.

## Deliverable

- `docs/internal_MATRIXIFY_DELTA_<REGION>.md` (generated; can be committed or kept local)
- Edits to `docs/data-guide.md` and any HTML mirrors (`data-guide.html` if present) when schema or workflows change

*Last Updated: March 2026*
