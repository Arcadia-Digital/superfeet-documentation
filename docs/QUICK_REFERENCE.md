# Quick Reference Guide

**Superfeet Multi-Region Shopify Plus Platform**

Quick lookup tables and common tasks for fast reference.

**Note:** This guide assumes you're familiar with Shopify Admin basics. For detailed explanations and step-by-step workflows, see the [Business User Guide](./business-user-guide.md).

---

## Store Information

| Store     | Handle           | Domain           | Transactional |
| --------- | ---------------- | ---------------- | ------------- |
| US        | `superfeetww`    | superfeet.com    | Yes           |
| Canada    | `superfeet-ca`   | superfeet.ca     | Yes           |
| UK        | `superfeet-uk`   | superfeet.co.uk  | Yes           |
| EU        | superfeet.eu     | superfeet.eu     | No (Brochure) |
| Australia | superfeet.com.au | superfeet.com.au | No (Brochure) |

---

## Platform Metrics

- **57 Active Products**
- **38 Collections** (Smart and Custom)
- **29 Installed Apps**
- **150 Blog Posts**
- **4,400 URL Redirects** (from Magento migration)
- **101+ Theme Sections**
- **143+ Theme Snippets**
- **123 Templates** (US store, November 2025)

---

## Theme Information

- **Theme:** CQL Propel v24.3.0
- **Theme Type:** Liquid (not headless)
- **Multi-Region:** Independent stores per region

---

## Quick Links

### Documentation
- [Theme Architecture](./theme-architecture.md)
- [Technical User Guide](./technical-user-guide.md)
- [Business User Guide](./business-user-guide.md)
- [Data Guide](./data-guide.md)
- [Integrations](./integrations.md)

### Store URLs
- **US:** https://www.superfeet.com
- **Canada:** https://www.superfeet.ca
- **UK:** https://www.superfeet.co.uk
- **EU:** https://www.superfeet.eu
- **Australia:** https://www.superfeet.com.au

### Shopify Admin
- **US:** https://superfeetww.myshopify.com/admin
- **Canada:** https://superfeet-ca.myshopify.com/admin
- **UK:** https://superfeet-uk.myshopify.com/admin

---

## Common Tasks

### Update Navigation Menu

1. **Shopify Admin → Online Store → Navigation**
2. Create/edit menu
3. Add menu items
4. **Theme Customizer → Header/Footer → Select menu**
5. Save

### Change Header Logo

1. **Theme Customizer → Header**
2. Find **Logo** setting
3. Upload/select new logo
4. Save

### Add Footer Menu

1. **Theme Customizer → Footer**
2. Click **Add block**
3. Select **Link list**
4. Select menu from dropdown
5. Save

### Assign Product Template

1. **Products → Select product**
2. Scroll to **Search engine listing**
3. Enter **Template suffix** (e.g., `recharge-bundle`)
4. Save

### Assign Collection Template

1. **Collections → Select collection**
2. Scroll to **Search engine listing**
3. Enter **Template suffix** (e.g., `searchspring`)
4. Save

### Bulk Update Products

1. **Matrixify app → Export**
2. Download CSV
3. Modify data
4. **Matrixify → Import**
5. Preview changes
6. Import

---

## Menu-to-Section Quick Reference

| Menu Location         | Theme Customizer Path                 |
| --------------------- | ------------------------------------- |
| Header - Main Menu    | Header → Menu                         |
| Header - Mobile Menu  | Header → Mobile menu                  |
| Header - Utility Menu | Header → Utility menu                 |
| Announcement Bar      | Announcement bar → Menu               |
| Footer Menu 1         | Footer → Add block → Link list → Menu |
| Footer Menu 2+        | Footer → Add block → Link list → Menu |
| Footer Copyright      | Footer → Copyright → Menu             |

---

## Template Suffix Reference

### Product Templates
- `recharge-bundle` - Recharge bundle products
- `subscription` - Subscription products
- `all-purpose-cushion` - Product-specific template
- (75+ product template variants)

### Collection Templates
- `searchspring` - SearchSpring-powered collections
- `native` - Native Shopify collections
- `category-landing` - Category landing pages
- (30+ collection template variants)

### Page Templates
- `store-locator` - Store locator page
- `insole-finder-2` - Insole Finder quiz
- `about` - About page
- (50+ page template variants)

---

## Key Metafields Quick Reference

### Product Metafields (CQL Namespace)
- `cql.arch_height` - Arch height
- `cql.product_gender` - Gender
- `cql.product_family` - Product family
- `cql.badge` - Badge text
- `cql.men_sizes` - Men's sizes
- `cql.women_sizes` - Women's sizes
- `cql.vegan` - Vegan indicator
- `cql.latex_free` - Latex-free indicator

### SEO Metafields
- `seo_title` - Custom SEO title
- `seo_desc` - Custom SEO description

### Reviews Metafields
- `yotpo.reviews_average` - Average rating
- `yotpo.reviews_count` - Review count

---

## App Quick Reference

### Major Apps
- **SearchSpring** - Enhanced search (US, UK, CA)
- **Recharge** - Bundles & subscriptions (US, UK, CA)
- **Yotpo** - Product reviews (US, UK, CA)
- **Elevar** - Server-side tracking (US, UK, CA)
- **Klaviyo** - Email/SMS marketing (US, UK, CA)
- **Matrixify** - Bulk data management (US, UK, CA)

### US-Only Apps
- **Regios Discounts** - Advanced discounts
- **Geo:Pro** - Regional redirection
- **Shipfy** - Shipping rules
- **GOVX ID** - Military discounts
- **Fraud Control** - Customer blocking

---

## Development Commands

### Shopify CLI

```bash
# Login
shopify auth login

# Local development
shopify theme dev --store superfeetww

# Push to staging
shopify theme push --unpublished --store superfeetww

# Push to live
shopify theme push --live --store superfeetww

# Pull from live
shopify theme pull --live --store superfeetww
```

---

## Troubleshooting Quick Reference

### Menu Not Showing
- Verify menu assigned in Theme Customizer
- Check menu has items
- Verify correct section (Header/Footer)

### Template Not Applying
- Check template file exists
- Verify template suffix spelling (case-sensitive)
- Check template is valid JSON

### Search Not Working
- Check SearchSpring dashboard
- Verify `collection.searchspring.json` template
- Check browser console for errors

### Reviews Not Showing
- Check Yotpo dashboard
- Verify Yotpo blocks in template
- Check review syndication settings

---

## Contact & Support

### Arcadia Digital
- **Email:** hello@arcadiadigital.com
- **Website:** https://arcadiadigital.com

### Shopify Support
- **Plus Support:** Priority support via Shopify admin
- **Live Chat:** Available in Shopify admin

### App Support
- Each app has its own support channel
- Check app dashboard for support links

---

## Important Notes

- **Multi-Store Setup:** Superfeet uses **three independent Shopify stores** (US, Canada, UK). Changes made in one store do NOT automatically appear in other stores. You must make changes separately in each store.

- **UK Store Markets:** The UK store serves EU and Australia as brochure-only markets (no buy buttons). To edit EU/AU content, select the market in Theme Customizer before making changes.

- **URL Redirects:** 4,400+ redirects from Magento migration - do not modify without careful testing and coordination with development team.

- **SearchSpring:** Essential A/B Testing app is incompatible with SearchSpring. Don't run A/B tests on collections using the `searchspring` template.

- **Template Suffixes:** Always use lowercase, no spaces, hyphens for word separation. Template suffixes are case-sensitive.

- **Backups:** Use Matrixify for regular data backups before making bulk changes.

---

*Last Updated: November 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

