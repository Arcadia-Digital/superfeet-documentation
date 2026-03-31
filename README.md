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
- **[Matrixify review runbook](docs/MATRIXIFY_REVIEW_RUNBOOK.md)** - How to compare new Matrixify exports and refresh metrics

**Not in this repository:** Theme source exports, Matrixify CSV dumps, and large project artifacts are kept outside Git (local secure storage or Shopify Admin export). Use Admin or your implementation partner for theme and bulk data files.

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

### Updating documentation
1. Prefer editing files under `docs/*.md`, then mirror changes into the matching root `.html` pages (or edit HTML directly if that is your workflow)
2. Test locally, then commit and push

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
