# Superfeet eCommerce Platform Documentation

Comprehensive technical documentation for Superfeet's multi-region Shopify Plus eCommerce platform, built and maintained by Arcadia Digital.

## Platform Overview

Superfeet operates a sophisticated multi-region eCommerce platform serving customers across North America, the United Kingdom, Europe, and Australia. The platform successfully migrated from Magento to Shopify Plus on October 16, 2024, with Arcadia Digital leading ongoing operations and optimization.

### Regional Sites
- **US:** superfeet.com (Primary transactional)
- **Canada:** superfeet.ca (English/French)
- **UK:** superfeet.co.uk (UK, EU, AU customers)
- **EU:** superfeet.eu (Brochure site)
- **Australia:** superfeet.com.au (Brochure site)

### Key Metrics
- **57 Active Products** - Insoles and footcare accessories
- **38 Collections** - Smart and custom collections
- **29 Installed Apps** - SearchSpring, Klaviyo, Yotpo, Recharge, and more
- **150 Blog Posts** - Foot health and product education content
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
- **[Data Exports](data/)** - Complete Matrixify export from US store
- **[Theme Source Code](code/)** - All three regional theme exports
- **[Client Artifacts](artifacts/)** - Project presentations and materials
- **[Downloads](downloads/)** - Additional resources and process documents

### Project Analysis & Case Studies
- **[Superfeet Case Study](SUPERFEET_CASE_STUDY.md)** - Comprehensive analysis of the migration project and business outcomes
- **[Project Retrospective](SUPERFEET_RETROSPECTIVE.md)** - Internal analysis of project execution, challenges, and process improvements
- **[ARCDIG-DOCS Improvements](ARCDIG_DOCS_IMPROVEMENTS.md)** - Process enhancements based on Superfeet project learnings

### Offboarding & Handoff Documentation
- **[Offboarding Checklist](OFFBOARDING_CHECKLIST.md)** - Comprehensive checklist for project handoff covering third-party services, access transfer, documentation, and knowledge transfer
- **[AI Handoff Documentation](handoff-documentation/ai-handoff.md)** - Technical context for AI coding assistants (Cursor, Claude Code, GitHub Copilot)
- **[Developer Handoff Documentation](handoff-documentation/developer-handoff.md)** - Detailed technical documentation for developers taking over platform maintenance

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
- 101+ theme sections for flexible page building
- Extensive metafields for product data
- Multi-language support (50+ languages)

## Deployment

This documentation is deployed to GitHub Pages at:
**https://petebuzzell-ad.github.io/superfeet-documentation/**

### Local Development
```bash
# Clone the repository
git clone https://github.com/petebuzzell-ad/superfeet-documentation.git
cd superfeet-documentation

# Open in browser
open index.html
```

### Updating Documentation
1. Edit HTML files directly
2. Test changes locally
3. Commit and push to main branch
4. Changes auto-deploy via GitHub Pages

## Documentation Tasks

### Pending Documentation
- [ ] **FraudControl App Documentation**
  - [ ] Record Loom video demonstrating app functionality
  - [ ] Document installation rationale and business case
  - [ ] Document current usage patterns and effectiveness
  - [ ] Create integration guide for technical team
  - [ ] Add to main platform documentation

## Contact

For questions about this documentation or the Superfeet platform:
- **Email:** hello@arcadiadigital.com
- **Repository:** https://github.com/petebuzzell-ad/superfeet-documentation

---

*Last Updated: October 17, 2025 | Arcadia Digital*
