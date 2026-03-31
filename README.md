# Superfeet eCommerce Platform Documentation

Comprehensive technical documentation for Superfeet's multi-region Shopify Plus eCommerce platform.

## Platform Overview

Superfeet operates a multi-region eCommerce platform serving customers across North America, the United Kingdom, Europe, and Australia. The platform migrated from Magento to Shopify Plus on October 16, 2024.

### Regional Sites
- **US:** superfeet.com (Primary transactional)
- **Canada:** superfeet.ca (English/French)
- **UK:** superfeet.co.uk (UK, EU, AU customers)
- **EU:** superfeet.eu (Brochure site)
- **Australia:** superfeet.com.au (Brochure site)

### Key Metrics (US store, verified Mar 2026)
- **64 Active Products** - Insoles and footcare accessories
- **44 Collections** - 23 smart + 21 custom
- **29 Installed Apps** - SearchSpring, Klaviyo, Yotpo, Recharge, and more
- **168 Blog Posts** - Foot health and product education content
- **4,400 URL Redirects** - Preserved from Magento migration

## Documentation Structure

### Main Documentation
- **[Business User Guide](business-user-guide.html)** - Content management workflows for business users
- **[Data Guide](data-guide.html)** - Complete reference for all metafields and data structures
- **[Integrations](integrations.html)** - Third-party app documentation and management guides
- **[Image & Media Specifications](image-media-specifications.html)** - Design specifications and requirements
- **[Platform Documentation](superfeet-platform-documentation.html)** - Comprehensive guide covering architecture, operations, and management
- **[Index Page](index.html)** - Navigation hub for all documentation resources

### Supporting Resources
- **[Markdown sources](docs/)** - Canonical `.md` copies of major guides for editing and version control
- **[Documentation refresh runbook](docs/DOCUMENTATION_REFRESH_RUNBOOK.md)** - Theme + Matrixify + hub update workflow (Python scripts included)
- **[Matrixify review runbook](docs/MATRIXIFY_REVIEW_RUNBOOK.md)** - Comparing exports under `data/`
- **[Theme exports (`code/`)](code/README.md)** - Where US/regional theme snapshots live
- **[Store data exports (`data/`)](data/README.md)** - Where Matrixify CSV folders live
- **[Handout files (`resources/`)](resources/)** - One-off PDFs, decks, and checklists (not linked from the public HTML hub)

## Maintaining this repository

When Shopify or catalog data changes materially:

1. Add the new **theme** folder under `code/` and/or **Matrixify** folder under `data/` (see READMEs there; zips inside those dirs stay untracked by design).
2. Run `scripts/diff_theme_exports.py` and/or `scripts/diff_matrixify_exports.py` as in [docs/DOCUMENTATION_REFRESH_RUNBOOK.md](docs/DOCUMENTATION_REFRESH_RUNBOOK.md).
3. Update `docs/*.md` and the matching root `.html` pages, then commit and push.

## Key Features

### Multi-Region Architecture
- Independent Shopify stores for each region
- Geographic redirection via Geo:Pro app
- Localized pricing, inventory, and shipping

### Advanced Functionality
- **SearchSpring Integration** - Enhanced search and filtering
- **Insole Finder Quiz** - Custom product recommendation tool
- **Recharge Subscriptions** - Product bundles and recurring orders
- **Yotpo Reviews** - Cross-region review syndication
- **Advanced Discounting** - Regios Discounts for complex promotions

### Content Management
- Custom CQL Propel theme (v24.3.0)
- 103 theme sections (US March 2026 export baseline) for flexible page building
- Extensive metafields for product data
- Multi-language support (50+ languages)

## Deployment

Documentation can be hosted on GitHub Pages or any static host serving these HTML files.

### Local development
```bash
git clone <repository-url>
cd superfeet-documentation
open index.html
```

### Updating documentation (content only)
1. Prefer editing files under `docs/*.md`, then mirror changes into the matching root `.html` pages (or edit HTML directly if that is your workflow)
2. Test locally, then commit and push

For **evidence-backed** updates after a new theme or Matrixify export, follow the **Maintaining this repository** steps above.

## Documentation Tasks

### Pending documentation
- [ ] **FraudControl App Documentation**
  - [ ] Record short demo of app functionality
  - [ ] Document installation rationale and business case
  - [ ] Document current usage patterns
  - [ ] Add to main platform documentation

## Contact

For questions about this documentation or the Superfeet platform, contact your Superfeet eCommerce team or implementation partner.

---

*Last Updated: March 2026*
