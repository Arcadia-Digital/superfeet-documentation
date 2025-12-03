# Superfeet Platform - Developer Handoff Documentation

**Purpose:** Comprehensive technical documentation for developers taking over maintenance and development of the Superfeet Shopify Plus platform.

**Last Updated:** [Date]  
**Handoff From:** Arcadia Digital  
**Handoff To:** [Developer Team]

---

## Table of Contents

1. [Platform Architecture](#platform-architecture)
2. [Development Environment Setup](#development-environment-setup)
3. [Theme Customization Guide](#theme-customization-guide)
4. [App Integration Details](#app-integration-details)
5. [Data Management](#data-management)
6. [Performance Optimization](#performance-optimization)
7. [Analytics & Tracking](#analytics--tracking)
8. [SEO & Marketing](#seo--marketing)
9. [Troubleshooting Guide](#troubleshooting-guide)
10. [Emergency Procedures](#emergency-procedures)

---

## Platform Architecture

### Multi-Store Architecture

Superfeet operates **five separate Shopify stores** rather than a single multi-currency store:

| Store     | Handle             | Domain           | Purpose        | Transactional |
| --------- | ------------------ | ---------------- | -------------- | ------------- |
| US        | `superfeetww`      | superfeet.com    | Primary        | Yes           |
| Canada    | `superfeet-ca`     | superfeet.ca     | English/French | Yes           |
| UK        | `superfeet-uk`     | superfeet.co.uk  | UK/EU/AU       | Yes           |
| EU        | `superfeet.eu`     | superfeet.eu     | Brochure       | No            |
| Australia | `superfeet.com.au` | superfeet.com.au | Brochure       | No            |

**Why Multiple Stores?**

This architecture was chosen for:
- **Performance:** Each store optimized independently
- **Scalability:** Independent scaling per region
- **Localization:** True localization without conflicts
- **Maintenance:** Easier to manage regional differences
- **Flexibility:** Regional customization without affecting other regions

### Regional Configuration Differences

**Pricing:**
- Each store has independent pricing
- Currency: USD (US), CAD (Canada), GBP (UK)
- Pricing managed per store in Shopify admin

**Inventory:**
- Inventory tracked independently per store
- Can sync via Matrixify if needed
- Fulfillment locations differ per region

**Shipping:**
- Shipping methods configured per store
- US uses Shipfy app for complex shipping rules (PO Boxes, USPS-only)
- UK/CA have standard Shopify shipping configuration

**Tax:**
- Avalara Tax Compliance app on all three transactional stores
- Automatic tax calculation based on location
- Configuration per store in Avalara dashboard

### Geo-Redirection

**Geo:Pro App** installed on US store automatically redirects visitors:
- US visitors → superfeet.com
- Canadian visitors → superfeet.ca
- UK/EU/AU visitors → superfeet.co.uk
- Other regions → appropriate site

**Implementation:** JavaScript-based redirection. Don't implement manual geolocation - Geo:Pro handles this.

---

## Development Environment Setup

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Git
- Shopify CLI (latest version)
- Code editor (VS Code recommended)

### Shopify CLI Installation

```bash
# Install Shopify CLI globally
npm install -g @shopify/cli @shopify/theme

# Verify installation
shopify version
```

### Authentication

```bash
# Login to Shopify
shopify auth login

# Select appropriate store during login
# US: superfeetww
# Canada: superfeet-ca
# UK: superfeet-uk
```

### Theme Development Setup

```bash
# Clone or navigate to theme directory
cd path/to/superfeet-ww-theme

# Start local development server
shopify theme dev --store superfeetww

# This will:
# - Start local server at http://127.0.0.1:9292
# - Watch for file changes
# - Sync changes to Shopify
# - Open theme preview URL
```

### Theme Structure

```
theme-root/
├── assets/              # Static assets (CSS, JS, images, fonts)
│   ├── *.css           # Stylesheets
│   ├── *.js            # JavaScript files
│   ├── *.otf           # Font files
│   └── *.svg           # SVG assets
├── config/             # Theme configuration
│   ├── settings_data.json      # Current theme settings
│   └── settings_schema.json    # Theme settings schema
├── layout/             # Base layouts
│   ├── theme.liquid            # Main theme layout
│   ├── checkout.liquid         # Checkout layout
│   ├── password.liquid         # Password page layout
│   └── theme.insole-finder.liquid  # Insole Finder layout
├── locales/            # Translation files (50+ languages)
│   └── *.json
├── sections/           # Page sections (101+ files)
│   ├── *.liquid
│   └── *.json
├── snippets/           # Reusable components (143+ files)
│   └── *.liquid
└── templates/          # Page templates
    ├── *.liquid        # Liquid templates
    └── *.json          # JSON templates (for theme editor)
```

### Working with Multiple Stores

**Important:** Changes often need to be made across multiple stores. Workflow:

1. Make changes on one store (usually US first)
2. Test thoroughly
3. Export theme changes or manually replicate to other stores
4. Test on each store after deployment

**Theme Sync:**
- Themes are independent per store
- Use Matrixify or manual copy for theme code sync
- Settings may differ per store - review `settings_data.json` differences

### Staging vs Production

**Development Workflow:**
1. Develop locally using `shopify theme dev`
2. Push to unpublished theme: `shopify theme push --unpublished`
3. Test on staging theme
4. Push to live: `shopify theme push --live`

**Always test on staging before going live!**

---

## Theme Customization Guide

### Section Development

**Sections** are the building blocks of Shopify themes. They can be added, removed, and reordered in the theme customizer.

**Creating a New Section:**

1. Create file: `sections/my-section.liquid`
2. Add schema for theme editor customization
3. Include in template via JSON or theme editor

**Section Schema Example:**

```liquid
{% schema %}
{
  "name": "My Section",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Hello World"
    }
  ],
  "presets": [
    {
      "name": "My Section"
    }
  ]
}
{% endschema %}
```

### Snippet Development

**Snippets** are reusable Liquid components included via `{% render %}`.

**Creating a Snippet:**

1. Create file: `snippets/my-snippet.liquid`
2. Accept parameters if needed
3. Render in templates/sections:

```liquid
{% render 'my-snippet', 
  parameter1: value1, 
  parameter2: value2 
%}
```

### Asset Management

**CSS:**
- Main stylesheet likely in `assets/theme.css` or similar
- Modular CSS files can be created and imported
- Use Shopify asset filters: `{{ 'style.css' | asset_url | stylesheet_tag }}`

**JavaScript:**
- Custom JS files in `assets/`
- Include in `theme.liquid` or specific templates
- Use asset filters: `{{ 'script.js' | asset_url | script_tag }}`

**Images:**
- Upload via Shopify admin or include in theme
- Reference: `{{ 'image.jpg' | asset_url | img_tag }}`
- Use `image_url` filter for product/collection images

### Custom JavaScript Best Practices

1. **Avoid Global Variables:** Use namespaced objects or modules
2. **Event Delegation:** Use for dynamically added elements
3. **Performance:** Minimize DOM queries, cache selectors
4. **Compatibility:** Test across supported browsers
5. **jQuery:** Theme likely uses jQuery - check before adding vanilla JS

**Example Pattern:**

```javascript
(function() {
  'use strict';
  
  const SuperfeetNamespace = {
    init: function() {
      this.bindEvents();
    },
    
    bindEvents: function() {
      // Event bindings
    }
  };
  
  document.addEventListener('DOMContentLoaded', function() {
    SuperfeetNamespace.init();
  });
})();
```

### Liquid Template Best Practices

**Performance:**
- Avoid nested loops
- Use `{% render %}` not `{% include %}` (render caches better)
- Minimize filter usage on large datasets
- Use `limit` and `offset` for pagination

**Security:**
- Always escape user input: `{{ user_input | escape }}`
- Use `| url_param_escape` for URLs in links
- Use `| json` for JSON output to prevent XSS

**Readability:**
- Use meaningful variable names
- Add comments for complex logic
- Keep templates focused (extract complex logic to snippets)

---

## App Integration Details

### Major Apps

#### Elevar Conversion Tracking

**Purpose:** Server-side conversion tracking bypassing ad blockers.

**Stores:** US, UK, CA

**Configuration:**
- App installed via Shopify App Store
- Configuration in Elevar dashboard
- Connected to: GA4, Facebook Pixel, Klaviyo, Google Ads

**Theme Integration:**
- Elevar JavaScript loaded in `theme.liquid`
- Look for Elevar script includes
- Events automatically tracked via Elevar SDK

**Key Events:**
- Purchase
- Add to Cart
- Begin Checkout
- Custom events as needed

**Troubleshooting:**
1. Check Elevar dashboard for event status
2. Verify script is loading (browser console)
3. Check Elevar → destination connections
4. Review server-side event logs

**Vendor Support:** Elevar support team

---

#### SearchSpring

**Purpose:** Enhanced product search and filtering.

**Stores:** US, UK, CA

**Configuration:**
- App installed and configured via SearchSpring dashboard
- Product data synced to SearchSpring
- Search UI replaces default Shopify search

**Theme Integration:**
- SearchSpring JavaScript SDK loaded
- Custom search templates may exist
- Search results rendered via SearchSpring

**Important Notes:**
- Essential A/B Testing app is **incompatible** with SearchSpring
- Don't modify SearchSpring integration without understanding full implementation
- SearchSpring has its own dashboard for configuration

**Troubleshooting:**
- Check SearchSpring dashboard for sync status
- Verify JavaScript SDK is loading
- Check browser console for errors
- Contact SearchSpring support for integration issues

---

#### Recharge Subscriptions

**Purpose:** Product bundles and subscription orders.

**Stores:** US, UK, CA

**Configuration:**
- Recharge app installed
- Subscription products configured in Recharge dashboard
- Checkout flow modified for subscriptions

**Theme Integration:**
- Recharge-specific templates for subscription products
- Custom subscription UI components
- Checkout modifications via Recharge app

**Key Files to Review:**
- Product templates for subscription products
- Checkout modifications
- Recharge-specific snippets

**Documentation:** Recharge has extensive documentation for theme customization

---

#### Yotpo Product Reviews

**Purpose:** Product reviews and user-generated content.

**Stores:** US, UK, CA

**Configuration:**
- Reviews collected on US store
- **US reviews automatically syndicated to UK and CA stores**
- ExpertVoice reviews syndicated to US store
- Moderation settings in Yotpo dashboard

**Theme Integration:**
- Yotpo widgets in product templates
- Review display components
- Review request automation

**Important:** Don't break review syndication when modifying product templates!

**Troubleshooting:**
- Check Yotpo dashboard for review sync status
- Verify widgets are loading on product pages
- Check browser console for JavaScript errors

---

#### Klaviyo

**Purpose:** Email and SMS marketing automation.

**Stores:** US, UK, CA

**Configuration:**
- Klaviyo app installed
- Connected to Shopify customer and order data
- Email/SMS campaigns configured in Klaviyo dashboard

**Theme Integration:**
- Klaviyo JavaScript snippet in `theme.liquid`
- Custom forms may use Klaviyo signup
- Event tracking via Klaviyo (also via Elevar)

**Event Tracking:**
- Elevar sends server-side events to Klaviyo
- Client-side events also tracked via Klaviyo JavaScript

**Troubleshooting:**
- Check Klaviyo dashboard for event delivery
- Verify Klaviyo script is loading
- Check event tracking in Klaviyo debug mode

---

#### Matrixify

**Purpose:** Bulk data import/export and backups.

**Stores:** US, UK, CA

**Usage:**
- Bulk product updates
- Inventory management
- Data backups
- Cross-store data sync

**Important:** Matrixify has "Big Plan" - verify plan status before large operations.

**Common Workflows:**
1. Export products for backup
2. Import product updates
3. Sync inventory across stores
4. Bulk metafield updates

---

#### Geo:Pro Geolocation

**Purpose:** Automatic regional redirection.

**Store:** US only (superfeetww)

**Configuration:**
- App installed on US store
- Redirect rules configured in Geo:Pro dashboard
- JavaScript-based redirection

**How It Works:**
- Detects visitor location
- Redirects to appropriate regional site
- US visitors stay on superfeet.com
- Others redirected to superfeet.ca or superfeet.co.uk

**Important:** Don't implement manual geolocation - Geo:Pro handles this.

---

#### Shipfy: Shipping Rules

**Purpose:** Complex shipping rule management (PO Boxes, USPS-only).

**Store:** US only (superfeetww)

**Configuration:**
- Shipping rules configured in Shipfy dashboard
- Integrates with Shopify shipping settings
- Handles edge cases (PO Boxes, military addresses, etc.)

---

#### Regios Discounts

**Purpose:** Advanced discount logic beyond Shopify's default.

**Store:** US only (superfeetww)

**Usage:**
- Complex promotional rules
- Regional discounts
- Advanced discount stacking

---

### Other Installed Apps

- **Osano Cookie Consent** - GDPR/CCPA compliance
- **StoreRocket Store Locator** - Physical store finder
- **Awin** - Affiliate marketing
- **Avalara Tax Compliance** - Tax calculation
- **GOVX ID Exclusive Discounts** - Military/veteran discounts
- **Fraud Control** - Customer service tool for blocking problematic customers
- **Shopcodes** - QR code generation (evaluating)
- **Essential Preorder** - Preorder functionality (roadmap)

**Apps to Investigate:**
- **Statlas** - Purpose unclear, needs documentation
- **GRIN Influencer Marketing** - May be inactive, replaced by Awin

---

## Data Management

### Product Management

**Product Count:** 57 active products

**Product Structure:**
- Products have multiple variants (typically sizes)
- Extensive metafields for additional data
- Images per variant
- Cross-references and related products

**Metafields:**
- Metafield definitions in Shopify admin
- Access in Liquid: `product.metafields.namespace.key`
- JSON metafields: `product.metafields.custom.json_field | parse_json`

**Bulk Updates:**
- Use Matrixify for bulk product updates
- Export → Modify → Import workflow
- Always backup before bulk changes

### Collection Management

**Total Collections:** 38

**Types:**
- **Smart Collections:** Dynamic based on product conditions
- **Custom Collections:** Manually curated

**Collection Structure:**
- Products can belong to multiple collections
- Collections used for navigation and merchandising
- Collection pages have custom templates

### Inventory Management

**Multi-Store Inventory:**
- Inventory tracked independently per store
- Can sync via Matrixify if needed
- Fulfillment locations differ per region

**Inventory Sync:**
- Manual sync via Matrixify export/import
- Or automated via third-party integration (if configured)

### Matrixify Workflows

**Export:**
1. Install Matrixify app
2. Configure export (products, inventory, etc.)
3. Download CSV/Excel file

**Import:**
1. Modify exported file
2. Upload to Matrixify
3. Preview changes
4. Import to store

**Backups:**
- Regular Matrixify exports for backup
- Export before major changes
- Keep backups for at least 30 days

### URL Redirects

**Critical:** 4,400+ redirects from Magento migration

**Management:**
- Redirects in Shopify admin: Online Store → Navigation → URL Redirects
- **Do not modify without careful testing**
- Each redirect preserves SEO value
- Test redirects after any changes

**Adding Redirects:**
- Via Shopify admin
- Or bulk import via CSV
- Always test redirect after adding

---

## Performance Optimization

### Core Web Vitals Targets

**Current Performance (as of last check):**
- **LCP (Largest Contentful Paint):** 1.67s (GOOD) - Target: < 2.5s
- **CLS (Cumulative Layout Shift):** 0.05 (GOOD) - Target: < 0.1
- **INP (Interaction to Next Paint):** 144ms (GOOD) - Target: < 200ms

**Monitoring:**
- Calibreapp provides daily monitoring
- Performance budgets set in Calibreapp (must be managed by Superfeet team)
- Alerts configured for performance degradation

### Performance Best Practices

**Images:**
- Use Shopify's image CDN and responsive images
- Format: `{{ product.featured_image | image_url: width: 800 | image_tag }}`
- Use appropriate image sizes (don't load 2000px images for thumbnails)
- Lazy load images below the fold

**JavaScript:**
- Minimize JavaScript bundle size
- Defer non-critical scripts
- Use async/defer attributes appropriately
- Remove unused JavaScript

**CSS:**
- Minimize CSS
- Remove unused styles
- Use CSS custom properties for theming
- Avoid excessive specificity

**Fonts:**
- Font files in `assets/` directory
- Use font-display: swap for web fonts
- Preload critical fonts

### Calibreapp Monitoring

**Purpose:** Performance monitoring and Core Web Vitals tracking

**Setup:**
- Daily monitoring configured
- Happy Path monitoring (key user journeys)
- Competitor monitoring

**Access:**
- Calibreapp dashboard
- Performance budgets (must be set by Superfeet team)
- Alert configuration

**Important:** Calibreapp is currently owned by Arcadia Digital - ownership needs to be transferred during offboarding.

---

## Analytics & Tracking

### Google Analytics 4 (GA4)

**Setup:**
- GA4 property configured
- Server-side tracking via Elevar
- Custom events and conversions configured

**Access:**
- GA4 dashboard
- Elevar sends server-side events to GA4

**Key Events:**
- Purchase
- Add to Cart
- Begin Checkout
- Custom events as configured

**Debugging:**
- Use GA4 DebugView for real-time event tracking
- Check Elevar dashboard for event delivery status
- Verify events in GA4 Real-time reports

### Elevar Server-Side Tracking

**Purpose:** Bypass ad blockers and iOS 14.5+ restrictions

**Connected Services:**
- GA4
- Facebook Pixel
- Klaviyo
- Google Ads

**How It Works:**
- Events tracked server-side via Elevar
- More accurate than client-side tracking
- Better attribution data

**Configuration:**
- Elevar dashboard
- Event mapping and transformations
- Destination configuration

**Troubleshooting:**
1. Check Elevar dashboard for event status
2. Verify Elevar script is loading
3. Check server-side event logs
4. Verify destination connections

### Facebook Pixel / Meta Pixel

**Setup:**
- Pixel configured via Elevar
- Server-side event tracking
- Custom conversions configured

**Access:**
- Meta Business Manager
- Facebook Events Manager

### Klaviyo Event Tracking

**Setup:**
- Events sent via Elevar (server-side)
- Also client-side tracking via Klaviyo JavaScript

**Events Tracked:**
- Purchases
- Add to Cart
- Product Views
- Custom events

### Google Ads Conversion Tracking

**Setup:**
- Conversions tracked via Elevar
- Server-side tracking for accuracy

**Access:**
- Google Ads account
- Conversion actions configured

---

## SEO & Marketing

### URL Structure

**Product URLs:**
- `/products/product-handle`
- Handle format: lowercase, hyphens

**Collection URLs:**
- `/collections/collection-handle`

**Page URLs:**
- `/pages/page-handle`

**Blog URLs:**
- `/blogs/blog-handle/article-handle`

### Meta Tags

**Management:**
- Per-product meta tags in Shopify admin
- Template-level defaults
- Open Graph tags for social sharing

**Important:**
- Meta descriptions should be unique and compelling
- Title tags optimized per page
- Canonical URLs set correctly

### Structured Data

**Implementation:**
- Product schema in product templates
- Organization schema in theme
- Breadcrumb schema
- Review schema (via Yotpo)

**Testing:**
- Google Rich Results Test
- Schema.org validator

### Google Search Console

**Properties:**
- superfeet.com
- superfeet.ca
- superfeet.co.uk
- (Other domains as applicable)

**Access:**
- Google Search Console dashboard
- Ownership verification
- Sitemap submission

**Important:** Access needs to be transferred during offboarding.

### Google Merchant Center

**Purpose:** Product feed for Google Shopping

**Configuration:**
- Product feed configured
- Feed updates automatic or scheduled
- Product data synced from Shopify

**Access:**
- Google Merchant Center dashboard
- Feed management
- Product approval status

### Sitemaps

**Automatically Generated:**
- Shopify generates sitemaps automatically
- Located at: `/sitemap.xml`
- Submitted to Google Search Console

### Redirects (Critical!)

**4,400+ redirects** from Magento migration

**Management:**
- Shopify admin: Online Store → Navigation → URL Redirects
- Bulk management via CSV import/export
- **Do not modify without careful consideration**

**Testing:**
- Test redirects after any changes
- Verify 301 status codes
- Check redirect chains (avoid multiple hops)

---

## Troubleshooting Guide

### Common Issues

#### Theme Not Loading
1. Check Shopify status page
2. Verify theme is published
3. Check browser console for errors
4. Clear browser cache
5. Check theme.liquid for syntax errors

#### Tracking Not Working
1. Check Elevar dashboard for event status
2. Verify Elevar script is loading (browser console)
3. Check destination connections (GA4, Facebook, etc.)
4. Review server-side event logs
5. Test in incognito mode (ad blockers)

#### Search Not Working
1. Check SearchSpring dashboard for sync status
2. Verify SearchSpring JavaScript is loading
3. Check browser console for errors
4. Verify SearchSpring app is active
5. Contact SearchSpring support if needed

#### Performance Issues
1. Check Calibreapp for performance metrics
2. Run PageSpeed Insights
3. Check for large images/assets
4. Review JavaScript bundle size
5. Check for render-blocking resources

#### Multi-Store Sync Issues
1. Verify changes were made to all stores
2. Check store-specific settings
3. Use Matrixify for data sync if needed
4. Verify regional configurations

### Error Logs

**Shopify Admin:**
- Settings → Notifications
- Check for system notifications

**Browser Console:**
- Open DevTools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for failed requests

**Server Logs:**
- Some apps provide server-side logs
- Elevar dashboard for tracking logs
- App-specific dashboards

### Support Escalation

**Shopify Support:**
- Shopify Plus support (priority support)
- Live chat or phone
- Support topics: billing, apps, themes, API

**App Vendor Support:**
- Each app has its own support
- Check app documentation
- Contact via app dashboard or email

**Emergency Contacts:**
- [Document emergency contacts here]

---

## Emergency Procedures

### Theme Rollback

**If theme changes break the site:**

1. **Quick Fix - Unpublish Theme:**
   - Shopify admin → Online Store → Themes
   - Click "..." on previous theme version
   - Select "Publish"

2. **Recover from Backup:**
   - Download theme backup (if available)
   - Upload via Shopify admin or CLI
   - Publish recovered theme

3. **Fix and Redeploy:**
   - Make fixes in local development
   - Test thoroughly
   - Deploy to staging first
   - Then deploy to live

### Disable Problematic Apps

**If an app is causing issues:**

1. Go to Apps in Shopify admin
2. Find problematic app
3. Click "..." → "Uninstall" or "Disable"
4. **Warning:** Uninstalling may remove data - check app documentation first

**Apps Critical to Business:**
- Elevar (tracking breaks)
- SearchSpring (search breaks)
- Klaviyo (email marketing breaks)
- Recharge (subscriptions break)
- Yotpo (reviews disappear)

**Test app removal on staging first if possible.**

### Restore from Backups

**Matrixify Backups:**
1. Export current data first (backup current state)
2. Import previous Matrixify backup
3. Verify data is correct
4. Test site functionality

**Theme Backups:**
1. Download theme from Shopify admin
2. Or use Git repository if available
3. Upload and publish backup theme

### Contact Information

**Critical Vendor Contacts:**
- Shopify Plus Support: [Contact info]
- Elevar Support: [Contact info]
- SearchSpring Support: [Contact info]
- [Add other critical vendors]

**Internal Contacts:**
- Superfeet IT: [Contact info]
- Superfeet E-commerce Manager: [Contact info]
- [Add other relevant contacts]

---

## Additional Resources

### Documentation
- Main Platform Documentation: `/superfeet-platform-documentation.html`
- Case Study: `/SUPERFEET_CASE_STUDY.md`
- README: `/README.md`

### Shopify Resources
- [Shopify Theme Development](https://shopify.dev/themes)
- [Liquid Documentation](https://shopify.dev/api/liquid)
- [Shopify CLI Documentation](https://shopify.dev/themes/tools/cli)

### External Resources
- [Elevar Documentation](https://docs.getelevar.com/)
- [SearchSpring Documentation](https://support.searchspring.com/)
- [Recharge Documentation](https://support.rechargepayments.com/)
- [Yotpo Documentation](https://docs.yotpo.com/)

---

*This document should be updated as the platform evolves. Keep it current with actual implementation details and add lessons learned.*

