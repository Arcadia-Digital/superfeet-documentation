# Superfeet Platform Overview

## What This Repository Is

This is the **Superfeet eCommerce Platform Documentation** repository - comprehensive technical and business documentation for Superfeet's multi-region Shopify Plus platform, built and maintained by Arcadia Digital.

## Platform Summary

Superfeet operates a sophisticated multi-region eCommerce platform serving customers across North America, the United Kingdom, Europe, and Australia. The platform successfully migrated from Magento to Shopify Plus on October 16, 2024.

### Regional Sites

- **US:** superfeet.com (Primary transactional store)
- **Canada:** superfeet.ca (English/French bilingual)
- **UK:** superfeet.co.uk (UK, EU, AU customers)
- **EU:** superfeet.eu (Brochure site)
- **Australia:** superfeet.com.au (Brochure site)

### Key Platform Metrics

- **64 Active Products (US)** - Insoles and footcare accessories (Matrixify Mar 2026)
- **44 Collections (US)** - 23 smart + 21 custom (Matrixify Mar 2026)
- **29 Installed Apps** - SearchSpring, Klaviyo, Yotpo, Recharge, and more
- **168 Blog Posts (US)** - Foot health and product education content (Matrixify Mar 2026)
- **4,400 URL Redirects** - Preserved from Magento migration
- **103 Theme Sections** - Flexible page building blocks (US Mar 2026 export)
- **144 Theme Snippets** - Reusable components
- **135 Templates** - US store (March 2026; `templates/**/*.json`)

## What "Evidence" Means

**Theme Code Location:**
- Theme files are **not** in this repository (excluded via `.gitignore`)
- Theme code lives in a separate repository or build system
- Documentation references theme file paths (e.g., `sections/header.liquid`)
- When theme code is needed, it must be accessed via Shopify CLI or theme export

**Available Evidence:**
- Complete documentation files in `docs/`
- Configuration examples
- Code snippets referenced in documentation
- Architecture diagrams and explanations

**Theme Export Path:**
- If theme code is exported, it would follow standard Shopify theme structure:
  - `layout/theme.liquid` - Main layout
  - `sections/` - Page sections (103 files in US Mar 2026 export)
  - `snippets/` - Reusable components (144 files)
  - `templates/` - Page templates (135 JSON files in US store)
  - `assets/` - CSS, JS, fonts, images
  - `config/` - Theme settings

## Repository Layout

```
superfeet-documentation/
├── README.md                    # Platform overview
├── docs/                        # Core documentation
│   ├── theme-architecture-v2.md    # Theme structure
│   ├── technical-user-guide-v2.md   # Development workflows
│   ├── data-guide.md                # Metafields reference
│   ├── integrations.md              # App documentation
│   ├── business-user-guide.md       # Business workflows
│   └── ...
├── agent/                       # Knowledge pack (this directory)
├── scripts/                     # Build scripts
└── dist/                        # Generated outputs
```

## What Makes Superfeet Special

### Multi-Region Architecture
- Independent Shopify stores for each region
- Geographic redirection via Geo:Pro app
- Localized pricing, inventory, and shipping
- Shared base theme with store-specific customizations

### Advanced Features
- **SearchSpring Integration** - Enhanced search and filtering
- **Insole Finder Quiz** - Custom product recommendation tool
- **Recharge Subscriptions** - Product bundles and recurring orders
- **Yotpo Reviews** - Cross-region review syndication
- **Advanced Discounting** - Regios Discounts for complex promotions

### Content Management
- Custom CQL Propel theme (v24.3.0)
- 103 theme sections (US Mar 2026 export) for flexible page building
- Extensive metafields for product data
- Multi-language support (50+ languages)

## How to Answer Common Questions

### "How do I make a theme change?"
1. Reference `docs/technical-user-guide-v2.md` - Development Environment Setup
2. Explain Shopify CLI workflow: `shopify theme dev --store superfeetww`
3. Point to relevant section in theme architecture docs
4. Remind about multi-store considerations

### "What metafield should I use?"
1. Reference `docs/data-guide.md` - Complete metafield catalog
2. Explain namespace organization (cql.*, custom.*, etc.)
3. Provide exact metafield name and type
4. Reference where it's used in theme (if documented)

### "How does [integration] work?"
1. Reference `docs/integrations.md` - Integration documentation
2. Explain theme integration vs backend-only
3. Provide template suffix requirements (if applicable)
4. Reference configuration steps

### "Where is the theme code?"
1. Explain theme code is not in this repo
2. Provide Shopify CLI commands to access theme
3. Reference file paths from documentation
4. Explain build system (if applicable)

## Key Documentation Files

- **README.md** - Start here for platform overview
- **docs/theme-architecture-v2.md** - Complete theme structure
- **docs/technical-user-guide-v2.md** - Development workflows
- **docs/data-guide.md** - All metafields and data structures
- **docs/integrations.md** - Third-party app documentation
- **docs/business-user-guide.md** - Content management workflows
