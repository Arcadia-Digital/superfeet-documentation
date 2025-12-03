# Superfeet Platform - AI Assistant Handoff Documentation

**Purpose:** This document provides context for AI coding assistants (Cursor, Claude Code, GitHub Copilot) to understand and work effectively with the Superfeet Shopify Plus platform.

**Last Updated:** [Date]

---

## Platform Overview

Superfeet operates a multi-region Shopify Plus eCommerce platform serving customers across North America, the United Kingdom, Europe, and Australia.

### Regional Store Architecture

- **US Store:** `superfeetww` - superfeet.com (Primary transactional store)
- **Canada Store:** `superfeet-ca` - superfeet.ca (English/French bilingual)
- **UK Store:** `superfeet-uk` - superfeet.co.uk (UK, EU, AU customers)
- **EU Store:** superfeet.eu (Non-transactional brochure site)
- **Australia Store:** superfeet.com.au (Non-transactional brochure site)

**Key Architectural Decision:** Each region operates as an independent Shopify store rather than a single multi-currency store. This enables:
- Better performance optimization per region
- Independent inventory management
- Regional customization without conflicts
- Simplified maintenance and scaling

### Theme Information

- **Theme:** Custom CQL Propel Theme (v24.3.0)
- **Theme Type:** Liquid (not headless)
- **Sections:** 101+ customizable sections
- **Snippets:** 143+ reusable snippets
- **Templates:** 126+ templates (product, collection, page, etc.)

---

## Codebase Structure

### Theme File Organization

```
theme-root/
├── assets/           # CSS, JavaScript, fonts, images
│   ├── *.css        # Theme stylesheets
│   ├── *.js         # JavaScript functionality
│   ├── *.otf        # Font files
│   └── *.svg        # SVG assets
├── config/          # Theme settings
│   ├── settings_data.json
│   └── settings_schema.json
├── layout/          # Base layouts
│   ├── theme.liquid
│   ├── checkout.liquid
│   ├── password.liquid
│   └── theme.insole-finder.liquid
├── locales/         # Translation files (50+ languages)
├── sections/        # Page sections (101+ files)
│   ├── *.liquid
│   └── *.json
├── snippets/        # Reusable components (143+ files)
│   └── *.liquid
└── templates/       # Page templates
    ├── *.liquid
    └── *.json
```

### Key Directories

- **`sections/`** - Page building blocks. Each section can be added/removed/reordered in theme customizer
- **`snippets/`** - Reusable Liquid components included in templates/sections via `{% render 'snippet-name' %}`
- **`templates/`** - Page type templates (product, collection, page, article, etc.)
- **`assets/`** - Static files served directly (CSS, JS, images)

---

## Development Workflow

### Local Development Setup

```bash
# Install Shopify CLI
npm install -g @shopify/cli @shopify/theme

# Login to Shopify
shopify auth login

# Connect to theme
cd path/to/theme
shopify theme dev --store superfeetww
```

### Theme Deployment

```bash
# Push to staging theme
shopify theme push --unpublished --store superfeetww

# Push to live theme
shopify theme push --live --store superfeetww

# Pull from live
shopify theme pull --live --store superfeetww
```

**Important:** Always test on staging/unpublished theme before pushing to live.

---

## Key Integrations & Technical Patterns

### 1. Elevar Server-Side Tracking

**Purpose:** Bypasses ad blockers and iOS 14.5+ restrictions by tracking conversions server-side.

**Implementation:**
- Elevar app installed on all three stores
- Sends events to: GA4, Facebook Pixel, Klaviyo, Google Ads
- Located in theme: Look for Elevar JavaScript includes in `theme.liquid`

**Key Events Tracked:**
- `purchase` - Order completion
- `add_to_cart` - Product added to cart
- `begin_checkout` - Checkout started
- Custom events as needed

**Debugging:** Check Elevar dashboard for event delivery status.

### 2. SearchSpring Integration

**Purpose:** Enhanced product search and filtering beyond Shopify's default search.

**Implementation:**
- SearchSpring JavaScript SDK loaded in theme
- Search results replace default Shopify search
- Product data synchronized via SearchSpring dashboard

**Key Files:**
- Search functionality likely in custom search templates
- SearchSpring scripts in `theme.liquid` or dedicated asset file

**Important:** Essential A/B Testing app is incompatible with SearchSpring. If A/B testing is needed, consider alternatives.

### 3. Recharge Subscriptions

**Purpose:** Handles product bundles and (future) subscription orders.

**Implementation:**
- Recharge app installed on all stores
- Custom subscription UI components
- Checkout flow modified for subscription products

**Code Location:** Look for Recharge-specific templates and snippets, subscription product templates.

### 4. Custom Insole Finder Quiz

**Purpose:** Custom product recommendation tool to guide customers to the right insole.

**Implementation:**
- Custom app built by Born West & Superfeet
- Installed on all three stores
- Has dedicated layout: `theme.insole-finder.liquid`

**Files:**
- Layout: `layout/theme.insole-finder.liquid`
- Quiz logic in dedicated snippets or JavaScript files

### 5. Yotpo Review Syndication

**Purpose:** US reviews automatically syndicated to UK and CA stores for social proof.

**Implementation:**
- Yotpo app configuration handles syndication
- Review widgets in product templates
- ExpertVoice reviews syndicated to US store

**Code Location:** Yotpo widgets in product template files.

### 6. Multi-Region Redirects (Geo:Pro)

**Purpose:** Automatically redirect visitors to appropriate regional site.

**Implementation:**
- Geo:Pro app installed on US store (superfeetww)
- JavaScript-based redirection based on visitor location
- Redirects non-US visitors to superfeet.ca or superfeet.co.uk

**Important:** Don't implement manual geolocation - Geo:Pro handles this.

---

## Common Tasks & Code Patterns

### Product Data Management

**Metafields:**
- Products use extensive metafields for additional data
- Metafield definitions in Shopify admin
- Access in Liquid: `product.metafields.namespace.key`

**Product Variants:**
- Products have size variants (e.g., insoles come in multiple sizes)
- Variant inventory tracked per store
- Variant images managed per variant

### Collection Management

**Types:**
- **Smart Collections:** Dynamic based on conditions
- **Custom Collections:** Manually curated
- **38 total collections** across platform

**Code Pattern:**
```liquid
{% for collection in collections %}
  {% if collection.products_count > 0 %}
    <!-- Collection content -->
  {% endif %}
{% endfor %}
```

### Metafield Usage

**Access Pattern:**
```liquid
{{ product.metafields.custom.field_name }}
{{ collection.metafields.custom.field_name }}
```

**JSON Metafields:**
```liquid
{% assign json_data = product.metafields.custom.json_field | parse_json %}
```

### Liquid Best Practices

**Performance:**
- Avoid nested loops where possible
- Use `{% render %}` for snippets, not `{% include %}` (render is faster)
- Minimize filters on large datasets

**Security:**
- Always escape user input: `{{ user_input | escape }}`
- Use `| url_param_escape` for URLs
- Use `| json` for JSON output

### JavaScript Customizations

**Theme JavaScript Location:**
- Custom JS files in `assets/` directory
- Included in `theme.liquid` via `<script src="{{ 'filename.js' | asset_url }}"></script>`
- Or inline in templates/sections when needed

**jQuery Usage:**
- Theme likely uses jQuery (check `theme.liquid` for jQuery include)
- Modern JavaScript (ES6+) also acceptable if browser support is sufficient

**Event Tracking:**
- Use Elevar for conversion tracking, not direct pixel fires
- Check Elevar documentation for event syntax

---

## Testing & Debugging

### Multi-Region Testing

When testing functionality:
1. Test on US store (superfeetww) first
2. Test same functionality on CA store (superfeet-ca)
3. Test same functionality on UK store (superfeet-uk)
4. Verify regional differences (pricing, inventory, shipping) work correctly

### Performance Testing

**Core Web Vitals:**
- Monitor via Calibreapp (performance monitoring service)
- Target metrics:
  - LCP (Largest Contentful Paint): < 2.5s
  - CLS (Cumulative Layout Shift): < 0.1
  - INP (Interaction to Next Paint): < 200ms

**Testing Tools:**
- Google PageSpeed Insights
- Calibreapp dashboard
- Chrome DevTools Lighthouse

### Debugging Tracking Issues

**Elevar:**
1. Check Elevar dashboard for event status
2. Verify events are firing in browser console
3. Check server-side event logs in Elevar

**GA4:**
1. Use GA4 DebugView in Google Analytics
2. Check Elevar → GA4 connection status
3. Verify events appear in GA4 Real-time reports

### Browser Compatibility

**Supported Browsers:**
- Chrome (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Edge (latest 2 versions)
- Mobile: iOS Safari, Chrome Mobile

**Testing:**
- Test on actual devices, not just responsive mode
- Use BrowserStack or similar for cross-browser testing

---

## Known Issues & Technical Debt

### Current Issues

1. **Essential A/B Testing Incompatibility**
   - Essential A/B Testing app doesn't work with SearchSpring
   - Alternative A/B testing solution needed if testing is required
   - Consider Shopify native experiments or alternative app

2. **Unused Apps**
   - Bagpiper Data Export - replaced by Matrixify, can be removed
   - Forms app - not in use, could be removed or implemented

3. **Apps Requiring Investigation**
   - Statlas - purpose unclear, needs documentation
   - GRIN Influencer Marketing - may be inactive, replaced by Awin

### Technical Debt

- **URL Redirects:** 4,400+ redirects from Magento migration - these are critical for SEO and should not be modified without careful testing
- **Theme Version:** CQL Propel v24.3.0 - check for updates but test thoroughly before upgrading
- **JavaScript Organization:** Some custom JavaScript may need refactoring for better maintainability

---

## Important Notes for AI Assistants

### Code Generation Guidelines

1. **Liquid Syntax:** Always use correct Liquid syntax. Shopify Liquid has specific syntax that differs from other templating languages.

2. **Performance First:** Consider performance impact of any code changes. Avoid heavy operations in loops.

3. **Multi-Store Awareness:** Remember that changes might need to be made across multiple stores (US, CA, UK). Document which stores are affected.

4. **Metafields:** Always check if metafields exist before accessing them:
   ```liquid
   {% if product.metafields.custom.field_name %}
     {{ product.metafields.custom.field_name }}
   {% endif %}
   ```

5. **Testing Required:** Any code changes should be tested on staging before deployment.

6. **Documentation:** When adding new features, update relevant documentation.

### Common Pitfalls to Avoid

- Don't modify redirect rules without understanding SEO impact
- Don't remove unused apps without confirming they're truly unused
- Don't change Elevar tracking without testing event delivery
- Don't modify SearchSpring integration without understanding the full implementation
- Don't break Yotpo review syndication when modifying product templates

---

## Quick Reference

### Store URLs
- US: https://www.superfeet.com
- Canada: https://www.superfeet.ca
- UK: https://www.superfeet.co.uk
- EU: https://www.superfeet.eu
- Australia: https://www.superfeet.com.au

### Key Metrics
- 57 Active Products
- 38 Collections
- 29 Installed Apps
- 150 Blog Posts
- 4,400 URL Redirects

### Theme Version
- CQL Propel Theme v24.3.0

### Documentation Links
- Platform Documentation: `/superfeet-platform-documentation.html`
- Case Study: `/SUPERFEET_CASE_STUDY.md`
- README: `/README.md`

---

*This document should be updated as the platform evolves. Keep it current with actual implementation details.*

