# Documentation folder (`docs/`)

Markdown sources for the Superfeet platform documentation hub. Root-level `.html` files are the primary published pages; keep them in sync when you edit here.

## Files in this directory

1. **theme-architecture.md** / **theme-architecture-v2.md** - Theme architecture
2. **technical-user-guide.md** / **technical-user-guide-v2.md** - Developer workflows
3. **business-user-guide.md** - Content management and regional stores
4. **data-guide.md** - Metafields and data structures
5. **integrations.md** - Installed apps and integrations
6. **image-media-specifications.md** - Media specifications
7. **QUICK_REFERENCE.md** - Quick lookup
8. **MATRIXIFY_REVIEW_RUNBOOK.md** - Reconciling Matrixify exports with these docs

## Theme inventory baseline (US, March 2026)

Verified from a US theme export: **135** JSON templates, **103** sections, **144** snippets (recursive counts under `templates/` and top-level `sections/` / `snippets/`). Re-export from **Shopify Admin → Online Store → Themes** when you need to re-verify.

## Configuration notes

- **Password protection (optional):** If `component-loader.js` gates the site, set the `PASSWORD` constant before deployment.

---

*Last Updated: March 2026*
