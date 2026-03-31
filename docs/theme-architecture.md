# Theme Architecture Documentation

**Superfeet Multi-Region Shopify Plus Platform**

## Overview

Superfeet operates a multi-region eCommerce platform using the **CQL Propel Theme (v24.3.0)** across three primary transactional stores. This documentation provides a comprehensive technical overview of the theme architecture, structure, and customization guidelines.

**Theme Version:** CQL Propel v24.3.0  
**Theme Type:** Liquid (not headless)  
**Regional Stores:** US (superfeetww), Canada (superfeet-ca), UK (superfeet-uk)

---

## Theme Structure

### Directory Organization

```
theme-root/
├── assets/              # Static assets (CSS, JS, fonts, images)
│   ├── *.css           # Theme stylesheets (119 files)
│   ├── *.js            # JavaScript functionality (35 files)
│   ├── *.otf           # Font files (13 files)
│   └── *.svg           # SVG assets (87 files in US store)
├── config/             # Theme settings
│   ├── settings_data.json      # Current theme settings
│   └── settings_schema.json   # Theme settings schema
├── layout/             # Base layouts
│   ├── theme.liquid            # Main theme layout
│   ├── checkout.liquid         # Checkout layout
│   ├── password.liquid         # Password page layout
│   └── theme.insole-finder.liquid  # Insole Finder custom layout
├── locales/          # Translation files (52 languages)
│   └── *.json
├── sections/          # Page sections (103 in US Mar 2026 export)
│   ├── *.liquid       # Section Liquid files
│   └── *.json         # Section JSON configuration
├── snippets/          # Reusable components (144 in US Mar 2026 export)
│   └── *.liquid
└── templates/         # Page templates
    ├── *.liquid       # Liquid templates
    └── *.json         # JSON templates (for theme editor)
```

### File Counts by Store

| Store                 | Sections | Snippets | Templates |
| --------------------- | -------- | -------- | --------- |
| US (superfeetww)      | 103      | 144      | 135       |
| Canada (superfeet-ca) | 101      | 143      | 75        |
| UK (superfeet-uk)     | 101      | 143      | 84        |

**Note:** US counts from March 2026 export; CA/UK template counts from theme folders in `code/` (Oct 2025 exports). See [internal_THEME_DELTA_MAR2026.md](./internal_THEME_DELTA_MAR2026.md).

---

## Multi-Region Architecture

### Store Configuration

Superfeet uses **independent Shopify stores** for each region rather than a single multi-currency store:

| Store  | Handle         | Domain          | Purpose        | Transactional |
| ------ | -------------- | --------------- | -------------- | ------------- |
| US     | `superfeetww`  | superfeet.com   | Primary        | Yes           |
| Canada | `superfeet-ca` | superfeet.ca    | English/French | Yes           |
| UK     | `superfeet-uk` | superfeet.co.uk | UK/EU/AU       | Yes           |

### Theme Differences

**Common Elements:**
- Same base theme (CQL Propel v24.3.0)
- Shared Propel patterns; US Mar 2026 export in `code/` is ahead of older CA/UK folders here until those themes are re-exported
- Layout files follow the same structure across stores (verify when merging changes)

**Regional Variations:**
- Template assignments differ per store
- Settings configurations vary (pricing, shipping, tax)
- Language/localization settings differ
- Store-specific customizations in templates

**Key Files to Compare:**
- `config/settings_data.json` - Store-specific settings
- `templates/` - Different template assignments per store
- `locales/` - Language files may differ

---

## Layout System

### Main Layout: `theme.liquid`

The main theme layout (`layout/theme.liquid`) provides the base structure for all pages:

**Key Components:**
- Header group (`{% sections 'header-group' %}`)
- Main content area (`{{ content_for_layout }}`)
- Footer group (`{% sections 'footer-group' %}`)
- Cart drawer (if enabled)
- Store details drawer (if enabled)

**Microsite Support:**
- Conditional microsite header/footer groups
- Microsite detection via page metafields: `page.metafields.cql.rx_microsite`

**Code Reference:**
```liquid
{% if isMicrositePage %}
  {% sections 'header-group-microsite' %}
{% else %}
  {% sections 'header-group' %}
{% endif %}
```

### Custom Layouts

**Insole Finder Layout** (`layout/theme.insole-finder.liquid`):
- Dedicated layout for Insole Finder quiz pages
- Custom app integration (built by Born West & Superfeet)
- Separate from main theme layout

**Checkout Layout** (`layout/checkout.liquid`):
- Shopify checkout customization
- Limited customization options (Shopify Plus restrictions)

**Password Layout** (`layout/password.liquid`):
- Password-protected store pages
- Pre-launch or private store access

---

## Section Architecture

### Section Types

Sections are the building blocks of Shopify themes. They can be added, removed, and reordered in the Theme Customizer.

**Total Sections:** 103 in US Mar 2026 export; re-export other regions to confirm.

**Section Categories:**

1. **Global Sections:**
   - `header.liquid` - Site header with navigation
   - `footer.liquid` - Site footer with menus and content
   - `announcement-bar.liquid` - Top announcement bar

2. **Main Content Sections:**
   - `main-product.liquid` - Product page content
   - `main-collection-product-grid.liquid` - Collection product grid
   - `main-page.liquid` - Page content
   - `main-article.liquid` - Blog article content
   - `main-blog.liquid` - Blog listing

3. **Content Sections:**
   - `image-with-text.liquid` - Image and text combinations
   - `image-banner.liquid` - Banner images
   - `rich-text.liquid` - Rich text content
   - `featured-collection.liquid` - Collection displays
   - `featured-product.liquid` - Product highlights

4. **Custom Sections:**
   - `shop-the-look.liquid` - Shop the look functionality
   - `insole-finder-2.liquid` - Insole Finder integration
   - `searchspring-recommendations.liquid` - SearchSpring integration
   - `product-compare.liquid` - Product comparison
   - `lifestyle.liquid` - Lifestyle content display

5. **App Sections:**
   - `apps.liquid` - App block container
   - Various app-specific sections

### Section Groups

**Header Group** (`sections/header-group.json`):
- Combines header section with announcement bar
- Standard and microsite variants

**Footer Group** (`sections/footer-group.json`):
- Combines footer section
- Standard and microsite variants

### Section Schema

All sections include a `{% schema %}` block defining:
- Section name and settings
- Block types (for flexible content)
- Presets (for quick section addition)

**Example Schema Structure:**
```liquid
{% schema %}
{
  "name": "Section Name",
  "tag": "section",
  "class": "section",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading"
    }
  ],
  "blocks": [
    {
      "type": "block_type",
      "name": "Block Name"
    }
  ],
  "presets": [
    {
      "name": "Section Name"
    }
  ]
}
{% endschema %}
```

---

## Snippet System

### Snippet Overview

Snippets are reusable Liquid components included via `{% render %}`.

**Total Snippets:** 143 per store

**Snippet Categories:**

1. **Navigation Snippets:**
   - `menu-list.liquid` - Menu rendering
   - `menu-header-drawer.liquid` - Mobile menu drawer
   - `menu-link-item.liquid` - Individual menu items
   - `menu-utility-links.liquid` - Utility menu links

2. **Product Snippets:**
   - `card-product.liquid` - Product card display
   - `product-media.liquid` - Product media gallery
   - `product-variant-picker.liquid` - Variant selection
   - `buy-buttons.liquid` - Add to cart functionality

3. **Cart Snippets:**
   - `cart-drawer.liquid` - Cart drawer component
   - `cart-notification.liquid` - Cart notification
   - `cart-gift-messaging.liquid` - Gift messaging

4. **Icon Snippets:**
   - `icons.liquid` - Icon rendering system
   - `icon-*.liquid` - Individual icon components (50+ files)

5. **Integration Snippets:**
   - `searchspring-script.liquid` - SearchSpring integration
   - `osano-shopify.liquid` - Osano cookie consent
   - `recharge-*.liquid` - Recharge subscription components

6. **Utility Snippets:**
   - `image.liquid` - Image rendering
   - `button.liquid` - Button component
   - `price.liquid` - Price display
   - `pagination.liquid` - Pagination controls

### Snippet Usage Pattern

```liquid
{% render 'snippet-name', 
  parameter1: value1, 
  parameter2: value2 
%}
```

**Best Practice:** Use `{% render %}` instead of `{% include %}` for better performance (render caches snippets).

---

## Template System

### Template Types

Templates define the structure and sections for different page types.

**Template Categories:**

1. **Product Templates:**
   - `product.json` - Default product template
   - `product.*.json` - Product template variants (75+ variants in US store)
   - Examples: `product.recharge-bundle.json`, `product.subscription.json`

2. **Collection Templates:**
   - `collection.json` - Default collection template
   - `collection.*.json` - Collection template variants (30+ variants in US store)
   - Examples: `collection.searchspring.json`, `collection.native.json`

3. **Page Templates:**
   - `page.json` - Default page template
   - `page.*.json` - Page template variants (50+ variants in US store)
   - Examples: `page.store-locator.json`, `page.insole-finder-2.json`

4. **Blog Templates:**
   - `article.json` - Default article template
   - `article.*.json` - Article template variants
   - `blog.json` - Blog listing template

5. **System Templates:**
   - `404.json` - 404 error page
   - `cart.json` - Cart page
   - `search.json` - Search results
   - `password.json` - Password page

### Template Assignment

Templates are assigned in Shopify Admin:
- **Products:** Product → Template suffix
- **Collections:** Collection → Template suffix
- **Pages:** Page → Template suffix

**Template Suffix Pattern:**
- Product handle: `all-purpose-cushion`
- Template suffix: `all-purpose-cushion`
- Template file: `product.all-purpose-cushion.json`

---

## Custom Features

### Insole Finder Quiz

**Layout:** `layout/theme.insole-finder.liquid`  
**Section:** `sections/insole-finder-2.liquid`  
**Custom App:** Built by Born West & Superfeet

**Purpose:** Custom product recommendation tool guiding customers to the right insole.

**Implementation:**
- Dedicated layout for quiz pages
- Custom app integration
- Installed on all three stores

### SearchSpring Integration

**Section:** `sections/searchspring-recommendations.liquid`  
**Snippet:** `snippets/searchspring-script.liquid`

**Purpose:** Enhanced product search and filtering beyond Shopify's default search.

**Implementation:**
- SearchSpring JavaScript SDK loaded
- Custom search templates
- Product recommendations section

**Important:** Essential A/B Testing app is incompatible with SearchSpring.

### Recharge Subscriptions

**Snippets:**
- `snippets/recharge-choose-your-bundle-customizations.liquid`
- `snippets/recharge-subscription-customizations.liquid`

**Purpose:** Product bundles and subscription orders.

**Implementation:**
- Recharge-specific templates
- Custom subscription UI components
- Checkout flow modifications

---

## Theme Customization Guidelines

### Adding New Sections

1. Create file: `sections/my-section.liquid`
2. Add schema for Theme Customizer settings
3. Include in template via JSON or Theme Customizer
4. Test on staging theme before publishing

### Modifying Existing Sections

1. **Always test on staging first**
2. Backup theme before major changes
3. Use version control (Git) if available
4. Document changes for multi-store deployment

### Multi-Store Deployment

**Workflow:**
1. Make changes on one store (usually US first)
2. Test thoroughly
3. Export theme changes or manually replicate
4. Test on each store after deployment

**Sync Methods:**
- Manual file copy
- Matrixify theme export/import
- Shopify CLI theme push (per store)

### Performance Considerations

**Best Practices:**
- Minimize JavaScript bundle size
- Use lazy loading for images
- Defer non-critical scripts
- Optimize CSS delivery
- Use `{% render %}` instead of `{% include %}`

**Current Performance:**
- LCP: 1.67s (GOOD) - Target: < 2.5s
- CLS: 0.05 (GOOD) - Target: < 0.1
- INP: 144ms (GOOD) - Target: < 200ms

---

## Code References

### Header Menu Access

**Location:** `sections/header.liquid`

```liquid
{% if section.settings.menu != blank %}
  {% render 'menu-list', menu: section.settings.menu, blocks: section.blocks %}
{% endif %}
```

**Menu Settings:**
- `section.settings.menu` - Main desktop menu
- `section.settings.mobile_menu` - Mobile menu
- `section.settings.utility_menu` - Utility menu

### Footer Menu Access

**Location:** `sections/footer.liquid`

```liquid
{% for block in section.blocks %}
  {% if block.type == 'link_list' %}
    {% if block.settings.menu != blank %}
      {% for link in block.settings.menu.links %}
        <!-- Menu items -->
      {% endfor %}
    {% endif %}
  {% endif %}
{% endfor %}
```

**Footer Menus:** Block-based (not direct settings)

### Announcement Bar Menu

**Location:** `sections/announcement-bar.liquid`

```liquid
{% if section.settings.announcement_menu != blank %}
  {% for link in section.settings.announcement_menu.links %}
    <!-- Menu items -->
  {% endfor %}
{% endif %}
```

---

## Regional Theme Differences

### US Store (superfeetww)
- 135 JSON templates (March 2026 export)
- Full feature set
- All integrations active

### Canada Store (superfeet-ca)
- 75 templates (`code/superfeet-ca-theme`, Oct 2025 export in repo)
- Bilingual support (English/French)
- Regional pricing and shipping

### UK Store (superfeet-uk)
- 84 templates (`code/superfeet-uk-theme`, Oct 2025 export in repo)
- UK/EU/AU customer focus
- Regional pricing and shipping

**Key Differences:**
- Template counts vary
- Settings configurations differ
- Language/localization settings
- Store-specific customizations

---

## Development Workflow

### Local Development

```bash
# Install Shopify CLI
npm install -g @shopify/cli @shopify/theme

# Login to Shopify
shopify auth login

# Start development server
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

**Important:** Always test on staging before pushing to live!

---

## Maintenance Notes

### Theme Updates

**Current Version:** CQL Propel v24.3.0

**Update Considerations:**
- Test thoroughly before upgrading
- Check for breaking changes
- Review CQL Propel changelog
- Test on staging first
- Coordinate multi-store updates

### Critical Files

**Do Not Modify Without Testing:**
- `layout/theme.liquid` - Base layout
- `sections/header.liquid` - Navigation
- `sections/footer.liquid` - Footer
- `sections/announcement-bar.liquid` - Announcement bar

**URL Redirects:**
- 4,400+ redirects from Magento migration
- Critical for SEO
- Do not modify without careful testing

---

## Additional Resources

- **Theme Documentation:** CQL Propel theme documentation
- **Shopify Theme Development:** https://shopify.dev/themes
- **Liquid Documentation:** https://shopify.dev/api/liquid
- **Shopify CLI:** https://shopify.dev/themes/tools/cli

---

*Last Updated: Based on theme exports from October 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

