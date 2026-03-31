# Theme Architecture Documentation

**Superfeet Multi-Region Shopify Plus Platform**

Comprehensive technical overview of the Superfeet theme architecture, structure, system design, and how all components work together.

**Who This Guide Is For:** Developers who need to understand the overall theme structure, how components interact, and the architectural decisions behind the Superfeet platform. For practical development workflows, see the [Technical User Guide](./technical-user-guide.md).

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Theme Structure](#theme-structure)
4. [Multi-Region Architecture](#multi-region-architecture)
5. [Layout System](#layout-system)
6. [Section Architecture](#section-architecture)
7. [Snippet System](#snippet-system)
8. [Template System](#template-system)
9. [Asset Architecture](#asset-architecture)
10. [Performance Architecture](#performance-architecture)
11. [Custom Features](#custom-features)
12. [Development Patterns](#development-patterns)
13. [Code References](#code-references)
14. [Regional Theme Differences](#regional-theme-differences)
15. [Maintenance & Updates](#maintenance--updates)

---

## Overview

### Platform Summary

Superfeet operates a multi-region eCommerce platform using the **CQL Propel Theme (v24.3.0)** across three primary transactional stores. The platform successfully migrated from Magento to Shopify Plus on October 16, 2024.

**Theme Version:** CQL Propel v24.3.0  
**Theme Type:** Liquid (not headless)  
**Regional Stores:** US (superfeetww), Canada (superfeet-ca), UK (superfeet-uk)

### Key Platform Metrics

- **64 Active Products (US)** - Insoles and footcare accessories (Matrixify Mar 2026)
- **44 Collections (US)** - 23 smart + 21 custom (Matrixify Mar 2026)
- **29 Installed Apps** - SearchSpring, Klaviyo, Yotpo, Recharge, and more
- **168 Blog Posts (US)** - Foot health and product education content (Matrixify Mar 2026)
- **4,400 URL Redirects** - Preserved from Magento migration
- **103 Theme Sections** - Flexible page building blocks (US export, March 2026)
- **144 Theme Snippets** - Reusable components
- **135 Templates** - US store (March 2026; all `templates/**/*.json`)

### Architecture Principles

**Component-Based Design:**
- Sections are self-contained building blocks
- Snippets provide reusable components
- Templates compose sections into pages
- Assets are organized by component/feature

**Performance-First:**
- Mobile-first responsive design
- Lazy loading for images and content
- Optimized asset delivery
- Minimal render-blocking resources

**Multi-Store Consistency:**
- Shared base theme across all stores
- Store-specific customizations via templates
- Regional settings and configurations
- Consistent user experience across regions

---

## System Architecture

### How It All Fits Together

**Request Flow:**
1. User visits storefront URL
2. Shopify routes request to appropriate template
3. `layout/theme.liquid` loads and determines layout structure
4. Template defines which sections to load
5. Sections render HTML using snippets and assets
6. Browser loads CSS and JavaScript
7. Page renders with all functionality

**Data Flow:**
1. Shopify Admin → Product/Collection/Page data
2. Metafields attached to resources
3. Liquid templates access data via objects
4. Sections render data in HTML
5. JavaScript enhances interactivity
6. User interacts with page

**Component Interaction:**
```
Layout (theme.liquid)
  ├── Header Group
  │   ├── Announcement Bar Section
  │   └── Header Section
  │       └── Menu Snippets
  ├── Main Content (from template)
  │   ├── Section 1
  │   │   ├── Snippets
  │   │   └── Assets (CSS/JS)
  │   ├── Section 2
  │   └── Section N
  └── Footer Group
      └── Footer Section
          └── Menu Snippets
```

### Theme File Dependencies

**Critical Dependencies:**
- `layout/theme.liquid` - Loads all other components
- `sections/header-group.json` - Defines header structure
- `sections/footer-group.json` - Defines footer structure
- `snippets/cql-head-content.liquid` - Global JavaScript configuration

**Section Dependencies:**
- Sections load their own CSS/JS assets
- Sections use snippets for reusable markup
- Sections can reference other sections (via blocks)

**Snippet Dependencies:**
- Snippets are independent (no dependencies on other snippets)
- Snippets can accept parameters from sections
- Snippets render HTML, no CSS/JS of their own

### Data Architecture

**Metafield Organization:**
- `cql.*` namespace - Product data, business logic
- `custom.*` namespace - Custom features, extensions
- `yotpo.*` namespace - Review data (auto-generated)
- `mm-google-shopping.*` - Google Shopping feed data
- `mc-facebook.*` - Facebook catalog data

**Metaobjects:**
- Reusable structured content
- Referenced via metafields
- Examples: FAQ groups, feature diagrams, arch height info

**Data Relationships:**
- Products → Variants (one-to-many)
- Products → Metafields (one-to-many)
- Products → Comparison Products (many-to-many via metafield)
- Products → Metaobjects (one-to-one via metafield)

---

## Theme Structure

### Directory Organization

```
theme-root/
├── assets/              # Static assets (CSS, JS, fonts, images)
│   ├── *.css           # Theme stylesheets (119 files)
│   │   ├── base.css                    # Base styles, resets, typography
│   │   ├── component-*.css            # Component styles (50+ files)
│   │   ├── section-*.css              # Section styles (40+ files)
│   │   └── template-*.css              # Template styles
│   ├── *.js            # JavaScript functionality (35 files)
│   │   ├── global.js                  # Global initialization
│   │   ├── constants.js               # Constants and config
│   │   ├── pubsub.js                  # Event system
│   │   ├── component-*.js             # Component JavaScript
│   │   └── [feature].js               # Feature-specific JS
│   ├── *.otf           # Font files (13 files)
│   ├── *.svg           # SVG assets (87 files in US store)
│   └── *.png, *.jpg    # Image assets
├── config/             # Theme settings
│   ├── settings_data.json      # Current theme settings (store-specific)
│   └── settings_schema.json   # Theme settings schema (defines available settings)
├── layout/             # Base layouts
│   ├── theme.liquid            # Main theme layout (loads all pages)
│   ├── checkout.liquid         # Checkout layout (Shopify Plus customization)
│   ├── password.liquid         # Password page layout
│   └── theme.insole-finder.liquid  # Insole Finder custom layout
├── locales/          # Translation files (52 languages)
│   └── *.json        # Language-specific translations
├── sections/          # Page sections (103 in US Mar 2026 export)
│   ├── *.liquid       # Section Liquid files (markup and logic)
│   └── *.json         # Section JSON configuration (for section groups)
├── snippets/          # Reusable components (144 in US Mar 2026 export)
│   └── *.liquid       # Snippet files (reusable markup)
└── templates/         # Page templates
    ├── *.liquid       # Liquid templates (legacy, rarely used)
    └── *.json         # JSON templates (for theme editor, most common)
```

### File Counts by Store

| Store                 | Sections | Snippets | Templates | Notes                         |
| --------------------- | -------- | -------- | --------- | ----------------------------- |
| US (superfeetww)      | 103      | 144      | 135       | US theme export Mar 31, 2026 (reference) |
| Canada (superfeet-ca) | 101      | 143      | 75        | Folder `code/superfeet-ca-theme` (Oct 2025 export in repo) |
| UK (superfeet-uk)     | 101      | 143      | 84        | Folder `code/superfeet-uk-theme` (Oct 2025 export in repo) |

**Note:** Template totals are recursive `templates/**/*.json`. US counts follow [internal_THEME_DELTA_MAR2026.md](./internal_THEME_DELTA_MAR2026.md). CA/UK folders in this repo predate the Mar 2026 US refresh—re-export regional themes to confirm parity.

### File Naming Conventions

**Sections:**
- `section-{name}.css` - Section-specific CSS
- `{name}.liquid` - Section Liquid file
- Examples: `section-header.css`, `header.liquid`

**Snippets:**
- `{name}.liquid` - Snippet file
- Examples: `menu-list.liquid`, `card-product.liquid`

**Templates:**
- `{type}.{suffix}.json` - Template file
- Examples: `product.bundle.json`, `collection.searchspring.json`

**Assets:**
- `component-{name}.css` - Component CSS
- `component-{name}.js` - Component JavaScript
- `section-{name}.css` - Section CSS
- `{feature}.css` / `{feature}.js` - Feature-specific assets

---

## Multi-Region Architecture

### Store Configuration

Superfeet uses **independent Shopify stores** for each region rather than a single multi-currency store. This provides:

- **Complete Isolation:** Each store operates independently
- **Regional Customization:** Store-specific templates and settings
- **Separate Admin Access:** Different logins and permissions
- **Independent Scaling:** Each store can scale separately

| Store  | Handle         | Domain          | Purpose        | Transactional | Markets                              |
| ------ | -------------- | --------------- | -------------- | ------------- | ------------------------------------ |
| US     | `superfeetww`  | superfeet.com   | Primary        | Yes           | US only                              |
| Canada | `superfeet-ca` | superfeet.ca    | English/French | Yes           | Canada (EN/FR)                       |
| UK     | `superfeet-uk` | superfeet.co.uk | UK/EU/AU       | Yes           | UK (transactional), EU/AU (brochure) |

### Theme Synchronization Strategy

**Build System Architecture:**

Superfeet uses a **build system** that processes a single shared codebase and generates store-specific theme files for each region. This build system:

- Takes the shared Superfeet codebase as input
- Adjusts code for `superfeet-ca` (Canada) and `superfeet-uk` (UK) stores
- Modifies assets including `searchspring.bundle.js` for each store's SearchSpring instance
- Generates store-specific theme files ready for deployment

**Important Note:** The build system code is not currently available in this repository, but this is the primary mechanism for theme synchronization across stores. Manual file copy, Matrixify, and Shopify CLI are alternative methods for one-off updates or when the build system is unavailable.

**Shared Components:**
- Base theme files (sections, snippets, layouts)
- Core functionality and features
- Shared CSS and JavaScript
- Common integrations

**Store-Specific (Generated by Build System):**
- SearchSpring bundle configuration (`searchspring.bundle.js`)
- Store-specific asset modifications
- Template assignments
- Theme settings (`config/settings_data.json`)
- Language files (`locales/`)
- Regional customizations

**Synchronization Methods:**
1. **Build System (Primary):** Processes shared codebase → generates store-specific themes
2. **Manual File Copy:** Selective, controlled updates (when build system unavailable)
3. **Matrixify:** Complete theme export/import (backup/restore method)
4. **Shopify CLI:** Push entire theme to multiple stores (alternative method)

**Best Practice:** 
- Use the build system for standard deployments
- Develop on US store first, then use build system to generate other store themes
- Test generated themes on staging before live deployment

### Theme Differences

**Common Elements:**
- Same base theme (CQL Propel v24.3.0)
- Same section and snippet structure (101 sections, 143 snippets)
- Same layout files
- Same core functionality

**Regional Variations:**
- Template assignments differ per store
- Settings configurations vary (pricing, shipping, tax)
- Language/localization settings differ
- Store-specific customizations in templates
- SearchSpring instance configurations differ

**Key Files to Compare:**
- `config/settings_data.json` - Store-specific settings
- `templates/` - Different template assignments per store
- `locales/` - Language files may differ (CA has French)

### UK Store Markets Architecture

**Shopify Markets Implementation:**

The UK store uses Shopify Markets to serve three regions from a single store:

**UK Market (Transactional):**
- Full eCommerce functionality
- Shows prices, buy buttons, cart
- Complete checkout flow
- Uses base templates (e.g., `product.json`)

**EU Market (Brochure-Only):**
- No transactional elements
- Hides prices, buy buttons, cart
- Uses market context files (e.g., `product.context.eu.json`)
- Disables transactional blocks in templates

**AU Market (Brochure-Only):**
- No transactional elements
- Hides prices, buy buttons, cart
- Uses market context files (e.g., `product.context.au.json`)
- Disables transactional blocks in templates

**Market Context Files:**

Market context files override base templates for specific markets:

```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "blocks": {
        "price": {
          "type": "price",
          "disabled": true
        },
        "variant_picker": {
          "type": "variant_picker",
          "disabled": true
        },
        "buy_buttons": {
          "type": "buy_buttons",
          "disabled": true
        }
      }
    }
  }
}
```

**How Market Context Works:**
1. Base template (`product.json`) defines full structure
2. Market context file (`product.context.eu.json`) overrides specific blocks
3. Disabled blocks don't render for that market
4. Other blocks inherit from base template

**Development Considerations:**
- Market context files inherit from base templates
- Changes to base template affect all markets
- Market-specific changes require context file updates
- Template edits in Theme Customizer require market context selection
- SearchSpring recommendations filter by market (`mfield_cql_market`)

---

## Layout System

### Main Layout: `theme.liquid`

The main theme layout (`layout/theme.liquid`) provides the base structure for all pages:

**Key Components:**
- `<head>` section - Meta tags, CSS, JavaScript
- Header group (`{% sections 'header-group' %}`)
- Main content area (`{{ content_for_layout }}`)
- Footer group (`{% sections 'footer-group' %}`)
- Cart drawer (if enabled)
- Store details drawer (if enabled)

**Microsite Support:**
- Conditional microsite header/footer groups
- Microsite detection via page metafields: `page.metafields.cql.rx_microsite`
- Separate header/footer configurations for microsites

**Code Reference:**
```liquid
{% comment %} Microsite detection {% endcomment %}
{% assign isMicrositePage = false %}
{% if page.metafields.cql.rx_microsite != blank and page.metafields.cql.rx_microsite != false %}
  {% assign isMicrositePage = true %}
{% endif %}

{% comment %} Header routing {% endcomment %}
{% if isMicrositePage %}
  {% sections 'header-group-microsite' %}
{% else %}
  {% sections 'header-group' %}
{% endif %}

{% comment %} Main content {% endcomment %}
{{ content_for_layout }}

{% comment %} Footer routing {% endcomment %}
{% if isMicrositePage %}
  {% sections 'footer-group-microsite' %}
{% else %}
  {% sections 'footer-group' %}
{% endif %}
```

**Global Resources:**
- `snippets/cql-head-content.liquid` - Global JavaScript configuration
- Defines `window.Resources` namespace
- Configures SearchSpring, Recharge, and other integrations

### Custom Layouts

**Insole Finder Layout** (`layout/theme.insole-finder.liquid`):
- Dedicated layout for Insole Finder quiz pages
- Uses microsite header/footer groups
- Custom app integration (built by Born West & Superfeet)
- Separate from main theme layout
- Loads Insole Finder-specific assets

**Checkout Layout** (`layout/checkout.liquid`):
- Shopify checkout customization
- Limited customization options (Shopify Plus restrictions)
- Used for checkout page styling
- Cannot modify checkout functionality (Shopify restriction)

**Password Layout** (`layout/password.liquid`):
- Password-protected store pages
- Pre-launch or private store access
- Simplified layout for password pages
- Custom password form styling

### Layout Loading Order

**Page Load Sequence:**
1. `layout/theme.liquid` loads
2. `<head>` section processes (CSS, meta tags)
3. Header group sections load
4. Template sections load (from `{{ content_for_layout }}`)
5. Footer group sections load
6. JavaScript loads (deferred/non-blocking)

**Section Loading:**
- Sections load in order defined by template
- Each section can load its own CSS/JS
- Sections are independent (can't depend on other sections)
- Section settings available via `section.settings`

---

## Section Architecture

### Section Types

Sections are the building blocks of Shopify themes. They can be added, removed, and reordered in the Theme Customizer.

**Total Sections:** 103 in the Mar 2026 US export; regional theme folders in repo may lag until the next export.

### Section Categories

**1. Global Sections:**
These sections appear on every page (or can be configured to):

- `header.liquid` - Site header with navigation
- `footer.liquid` - Site footer with menus and content
- `announcement-bar.liquid` - Top announcement bar

**2. Main Content Sections:**
These sections provide the primary content for specific page types:

- `main-product.liquid` - Product page content
- `main-collection-product-grid.liquid` - Collection product grid
- `main-collection-product-grid-ss.liquid` - SearchSpring collection grid
- `main-page.liquid` - Page content
- `main-article.liquid` - Blog article content
- `main-blog.liquid` - Blog listing
- `main-search.liquid` - Search results

**3. Content Sections:**
Flexible content sections that can be added to any template:

- `image-with-text.liquid` - Image and text combinations
- `image-banner.liquid` - Banner images
- `rich-text.liquid` - Rich text content
- `featured-collection.liquid` - Collection displays
- `featured-product.liquid` - Product highlights
- `multicolumn.liquid` - Multi-column layouts
- `newsletter.liquid` - Email signup forms

**4. Custom Sections:**
Superfeet-specific custom sections:

- `shop-the-look.liquid` - Shop the look functionality
- `insole-finder-2.liquid` - Insole Finder integration
- `searchspring-recommendations.liquid` - SearchSpring integration
- `product-compare.liquid` - Product comparison table
- `product-compare-enhanced.liquid` - Enhanced product comparison
- `lifestyle.liquid` - Lifestyle content display
- `feature-diagram.liquid` - Interactive feature diagrams
- `feature-diagram-inset.liquid` - Inset feature diagrams

**5. App Sections:**
Sections that integrate with third-party apps:

- `apps.liquid` - App block container
- Various app-specific sections (Yotpo, Recharge, etc.)

### Section Groups

**Header Group** (`sections/header-group.json`):
- Combines header section with announcement bar
- Standard and microsite variants
- Defines header structure and order

**Footer Group** (`sections/footer-group.json`):
- Combines footer section
- Standard and microsite variants
- Defines footer structure

**Section Group Structure:**
```json
{
  "sections": {
    "announcement-bar": {
      "type": "announcement-bar"
    },
    "header": {
      "type": "header"
    }
  },
  "order": ["announcement-bar", "header"]
}
```

### Section Schema

All sections include a `{% schema %}` block defining:

- **Section name and tag**
- **Settings** - Configurable options in Theme Customizer
- **Blocks** - Flexible content blocks
- **Presets** - Pre-configured section instances

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
      "label": "Heading",
      "default": "Default Heading"
    },
    {
      "type": "color",
      "id": "background_color",
      "label": "Background Color",
      "default": "#ffffff"
    }
  ],
  "blocks": [
    {
      "type": "text_block",
      "name": "Text Block",
      "settings": [
        {
          "type": "richtext",
          "id": "content",
          "label": "Content"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Section Name",
      "settings": {
        "heading": "Default Heading"
      }
    }
  ]
}
{% endschema %}
```

### Section Dependencies

**CSS Dependencies:**
- Each section can load its own CSS file
- CSS files follow naming: `section-{name}.css`
- Base styles in `base.css`
- Component styles in `component-*.css`

**JavaScript Dependencies:**
- Sections can load their own JavaScript
- JavaScript files follow naming: `{name}.js` or `component-{name}.js`
- Global JavaScript in `global.js`

**Snippet Dependencies:**
- Sections use snippets for reusable markup
- Common snippets: `card-product`, `image`, `button`, `price`
- Navigation snippets: `menu-list`, `menu-header-drawer`

---

## Snippet System

### Snippet Overview

Snippets are reusable Liquid components included via `{% render %}` tag. They provide:

- **Reusability:** Use same markup across multiple sections
- **Maintainability:** Update once, affects all uses
- **Modularity:** Self-contained components
- **Performance:** Cached by Shopify (via `{% render %}`)

**Total Snippets:** 143 per store

### Snippet Categories

**1. Navigation Snippets:**
- `menu-list.liquid` - Menu rendering (desktop)
- `menu-header-drawer.liquid` - Mobile menu drawer
- `menu-link-item.liquid` - Individual menu items
- `menu-utility-links.liquid` - Utility menu links
- `menu-list-promos.liquid` - Mega menu promo content

**2. Product Snippets:**
- `card-product.liquid` - Product card display
- `product-media.liquid` - Product media gallery
- `product-variant-picker.liquid` - Variant selection
- `buy-buttons.liquid` - Add to cart functionality
- `product-compare-column.liquid` - Product comparison column
- `product-info.liquid` - Product information display

**3. Cart Snippets:**
- `cart-drawer.liquid` - Cart drawer component
- `cart-notification.liquid` - Cart notification
- `cart-gift-messaging.liquid` - Gift messaging
- `cart-items.liquid` - Cart items list

**4. Icon Snippets:**
- `icons.liquid` - Icon rendering system
- `icon-*.liquid` - Individual icon components (50+ files)
- Examples: `icon-cart.liquid`, `icon-search.liquid`, `icon-account.liquid`

**5. Integration Snippets:**
- `searchspring-script.liquid` - SearchSpring integration
- `osano-shopify.liquid` - Osano cookie consent
- `recharge-choose-your-bundle-customizations.liquid` - Recharge bundles
- `recharge-subscription-customizations.liquid` - Recharge subscriptions
- `cql-head-content.liquid` - Global JavaScript configuration

**6. Utility Snippets:**
- `image.liquid` - Image rendering with lazy loading
- `button.liquid` - Button component
- `price.liquid` - Price display
- `pagination.liquid` - Pagination controls
- `loading-spinner.liquid` - Loading indicator

### Snippet Usage Pattern

**Basic Usage:**
```liquid
{% render 'snippet-name' %}
```

**With Parameters:**
```liquid
{% render 'snippet-name', 
  parameter1: value1, 
  parameter2: value2 
%}
```

**Real Example:**
```liquid
{% render 'card-product', 
  product: product, 
  show_vendor: true,
  image_ratio: 'square'
%}
```

**Best Practice:** 
- Use `{% render %}` instead of `{% include %}` for better performance
- `{% render %}` caches snippets
- `{% include %}` is deprecated

### Snippet Parameter Patterns

**Common Parameters:**
- Objects: `product`, `collection`, `page`, `block`
- Strings: `heading`, `class`, `id`, `text`
- Numbers: `limit`, `index`, `count`
- Booleans: `show_price`, `is_featured`, `hide_element`
- Arrays: `items`, `links`, `products`

**Parameter Documentation:**
```liquid
{% comment %}
  Renders: [Description of what this snippet does]
  
  Accepts:
  - product: {Product} Product object to display
  - show_price: {Boolean} Whether to show product price (default: true)
  - class: {String} Additional CSS classes
{% endcomment %}
```

---

## Template System

### Template Types

Templates define the structure and sections for different page types.

**Template Categories:**

**1. Product Templates:**
- `product.json` - Default product template
- `product.*.json` - Product template variants (75+ variants in US store)
- Examples: 
  - `product.recharge-bundle.json` - Recharge bundle products
  - `product.subscription.json` - Subscription products
  - `product.all-purpose-cushion.json` - Product-specific template

**2. Collection Templates:**
- `collection.json` - Default collection template
- `collection.*.json` - Collection template variants (30+ variants in US store)
- Examples:
  - `collection.searchspring.json` - SearchSpring-powered collections
  - `collection.native.json` - Native Shopify collections
  - `collection.featured.json` - Featured collections

**3. Page Templates:**
- `page.json` - Default page template
- `page.*.json` - Page template variants (50+ variants in US store)
- Examples:
  - `page.store-locator.json` - Store locator page
  - `page.insole-finder-2.json` - Insole Finder quiz page
  - `page.landing.json` - Landing page template

**4. Blog Templates:**
- `article.json` - Default article template
- `article.*.json` - Article template variants
- `blog.json` - Blog listing template

**5. System Templates:**
- `404.json` - 404 error page
- `cart.json` - Cart page
- `search.json` - Search results
- `password.json` - Password page

### Template Assignment

Templates are assigned in Shopify Admin:

**Products:**
1. Go to Products → Select product
2. Scroll to **Search engine listing**
3. Set **Template suffix** field
4. Template file: `product.{suffix}.json`

**Collections:**
1. Go to Collections → Select collection
2. Scroll to **Search engine listing**
3. Set **Template suffix** field
4. Template file: `collection.{suffix}.json`

**Pages:**
1. Go to Online Store → Pages → Select page
2. Scroll to **Search engine listing**
3. Set **Template suffix** field
4. Template file: `page.{suffix}.json`

**Template Suffix Pattern:**
- Product handle: `all-purpose-cushion`
- Template suffix: `all-purpose-cushion`
- Template file: `product.all-purpose-cushion.json`

**Important Notes:**
- Template suffix is **case-sensitive**
- Use lowercase, hyphens for word separation
- Template must exist in theme files
- If template doesn't exist, default template is used

### Template Structure

**JSON Template Example:**
```json
{
  "sections": {
    "main": {
      "type": "main-product",
      "blocks": {
        "title": {
          "type": "title"
        },
        "price": {
          "type": "price"
        },
        "variant_picker": {
          "type": "variant_picker"
        },
        "buy_buttons": {
          "type": "buy_buttons"
        }
      },
      "settings": {
        "enable_sticky_info": true,
        "media_aspect_ratio": "adapt"
      }
    },
    "product-compare": {
      "type": "product-compare",
      "settings": {
        "heading": "Compare Products",
        "hide_product_prices": false
      }
    },
    "product-recommendations": {
      "type": "product-recommendations",
      "settings": {
        "heading": "You may also like"
      }
    }
  },
  "order": ["main", "product-compare", "product-recommendations"]
}
```

**Template Sections:**
- `sections` object defines section instances
- Each section has `type` (section file name)
- Sections can have `blocks` and `settings`
- `order` array controls section display order

### Template Inheritance

**Base Templates:**
- Default templates (`product.json`, `collection.json`, etc.)
- Used when no template suffix is specified
- Can be customized per store
- Provide fallback structure

**Template Variants:**
- Custom templates for specific products/collections/pages
- Inherit structure from base templates conceptually
- Can override section order and settings
- Store-specific template assignments

**Market Context Files (UK Store):**
- Base: `product.json` (UK market - full functionality)
- EU Override: `product.context.eu.json` (disables transactional blocks)
- AU Override: `product.context.au.json` (disables transactional blocks)
- Context files inherit and override base template

---

## Asset Architecture

### CSS Architecture

**File Organization:**

The theme uses a component-based CSS architecture:

```
assets/
├── base.css                    # Base styles, resets, typography, variables
├── component-*.css             # Component-specific styles (50+ files)
│   ├── component-card.css
│   ├── component-product-grid.css
│   ├── component-cart.css
│   └── ...
├── section-*.css               # Section-specific styles (40+ files)
│   ├── section-header.css
│   ├── section-footer.css
│   ├── section-product-compare.css
│   └── ...
├── template-*.css              # Template-specific styles
│   ├── template-collection.css
│   └── template-search.css
└── [feature].css               # Feature-specific styles
    ├── insole-finder-2.css
    └── ...
```

**CSS Loading Strategy:**

CSS files are loaded in sections or layout:
- Base styles loaded in `layout/theme.liquid`
- Component styles loaded as needed per section
- Section styles loaded per section
- Critical CSS should be inlined for performance

**CSS Naming Conventions:**

The theme uses a BEM-like naming convention:

```css
/* Component */
.component-name { }

/* Element */
.component-name__element { }

/* Modifier */
.component-name--modifier { }

/* State */
.component-name.is-active { }
```

**Example from theme:**
```css
.header__menu-item { }
.header__menu-item--white { }
.header__menu-item--grandchild__title { }
.header__menu-item--grandchild__subtext { }
```

**Responsive Design:**

The theme uses mobile-first responsive design:
- Base styles target mobile
- Media queries for tablet/desktop
- Breakpoints: Check `base.css` for exact values
- Typically: 750px (tablet), 990px (desktop)

**CSS Custom Properties:**

The theme may use CSS custom properties (variables) for theming:
- Check `base.css` for variable definitions
- Use variables for colors, spacing, typography
- Enables easy theme customization

### JavaScript Architecture

**File Organization:**

```
assets/
├── global.js                   # Global functionality, initialization
├── constants.js                 # Constants and configuration
├── pubsub.js                    # Event pub/sub system
├── component-*.js               # Component-specific JavaScript
│   ├── component-cart.js
│   ├── component-product-form.js
│   └── ...
├── [feature].js                 # Feature-specific JavaScript
│   ├── insole-finder-2.js
│   ├── product-form.js
│   └── ...
└── [vendor].js                  # Third-party libraries
    ├── jquery-3.6.0.min.js
    ├── flickity.pkgd.min.js
    ├── swiper-bundle.min.js
    └── searchspring.bundle.js
```

**Global Namespace Pattern:**

The theme uses a `window.Resources` global namespace for configuration:

```javascript
window.Resources = {
  searchspring: {
    siteIds: {
      productFeeds: {
        usEnglish: "...",
        ukEnglish: "...",
        caEnglish: "...",
        caFrench: "..."
      },
      contentFeeds: {
        usEnglish: "..."
      }
    }
  },
  recharge: {
    bundles: {
      selectAVariant: "...",
      soldOutButtonText: "..."
    },
    subscriptions: {
      closeModal: "..."
    }
  },
  colorMap: { /* ... */ }
};
```

**JavaScript Module Pattern:**

Most JavaScript uses IIFE (Immediately Invoked Function Expression) pattern:

```javascript
(function() {
  'use strict';
  
  const ComponentName = {
    init: function() {
      this.cacheElements();
      this.bindEvents();
    },
    
    cacheElements: function() {
      this.$container = document.querySelector('.component-container');
    },
    
    bindEvents: function() {
      // Event bindings
    }
  };
  
  document.addEventListener('DOMContentLoaded', function() {
    ComponentName.init();
  });
})();
```

**Event System:**

The theme uses `pubsub.js` for event communication:
- Components publish events
- Other components subscribe to events
- Reduces coupling between components
- Enables loose component communication

**Third-Party Libraries:**

- **jQuery 3.6.0:** Used for DOM manipulation (legacy support)
- **Flickity:** Carousel/slider functionality
- **Swiper:** Alternative carousel library
- **SearchSpring Bundle:** Search and recommendations
  - **Important:** `searchspring.bundle.js` is modified by the build system for each store
  - US store: Configured for US SearchSpring instance
  - UK store: Configured for UK SearchSpring instance
  - CA store: Configured for CA-EN and CA-FR SearchSpring instances
  - Do not manually modify this file - use the build system
- **BigPicture.js:** Image/video lightbox

### Asset Loading Strategy

**CSS Loading:**
```liquid
{{ 'component-name.css' | asset_url | stylesheet_tag }}
{{ 'section-name.css' | asset_url | stylesheet_tag }}
```

**JavaScript Loading:**
```liquid
{{ 'component-name.js' | asset_url | script_tag }}
{{ 'feature-name.js' | asset_url | script_tag }}
```

**Deferred Loading:**
- Non-critical JavaScript should be deferred
- Use `defer` attribute when possible
- Lazy load images below the fold
- Preload critical resources

**Asset Optimization:**
- Images: Use WebP/AVIF when possible, optimize file sizes
- CSS: Minify for production (Shopify handles this)
- JavaScript: Minify for production (Shopify handles this)
- Fonts: Use `font-display: swap` for better performance

### Image Assets

**Image Management:**
- Product images managed in Shopify Admin
- Lifestyle images uploaded per section
- SVG icons stored in `assets/` (87+ files in US store)
- Logo and branding assets in `assets/`

**Image Optimization:**
- Use appropriate image formats (WebP, AVIF)
- Optimize file sizes before upload
- Use responsive images when possible
- Lazy load images below the fold

### Font Management

**Custom Fonts:**
- `proximanova_black.ttf` - Proxima Nova Black
- `proximanova_regular.ttf` - Proxima Nova Regular
- Fonts loaded via CSS `@font-face`
- Consider font subsetting for performance

**Font Loading:**
- Use `font-display: swap` for better performance
- Preload critical fonts
- Fallback fonts for better loading experience

---

## Performance Architecture

### Current Performance Metrics

**Core Web Vitals (Targets):**
- **LCP (Largest Contentful Paint):** 1.67s (GOOD) - Target: < 2.5s
- **CLS (Cumulative Layout Shift):** 0.05 (GOOD) - Target: < 0.1
- **INP (Interaction to Next Paint):** 144ms (GOOD) - Target: < 200ms

**Performance Strategy:**
- Mobile-first responsive design
- Lazy loading for images and content
- Optimized asset delivery
- Minimal render-blocking resources
- Efficient JavaScript execution

### Optimization Strategies

**Image Optimization:**
- Use WebP/AVIF formats when possible
- Optimize image file sizes
- Lazy load images below the fold
- Use responsive images (`srcset`)
- Proper image dimensions (avoid scaling)

**CSS Optimization:**
- Minimize CSS file size
- Remove unused CSS
- Use CSS custom properties
- Minimize specificity conflicts
- Critical CSS inlined when possible

**JavaScript Optimization:**
- Minimize JavaScript bundle size
- Defer non-critical scripts
- Use event delegation
- Minimize DOM queries (cache selectors)
- Avoid blocking the main thread

**Asset Delivery:**
- Minimize HTTP requests
- Combine files when possible
- Use CDN for assets (Shopify handles this)
- Enable browser caching
- Use compression (gzip/brotli)

### Lazy Loading Implementation

**Images:**
- Lazy load images below the fold
- Use `loading="lazy"` attribute
- Implement intersection observer for custom lazy loading

**Content:**
- Lazy load non-critical sections
- Defer JavaScript execution
- Load third-party scripts asynchronously

**Performance Monitoring:**
- Use PageSpeed Insights for regular checks
- Monitor Core Web Vitals
- Use browser Performance tab
- Check Calibreapp for metrics

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
- Uses microsite header/footer groups

**Assets:**
- `assets/insole-finder-2.css` - Quiz styling
- `assets/insole-finder-2.js` - Quiz functionality

**Files:**
- `layout/theme.insole-finder.liquid` - Custom layout
- `sections/insole-finder-2.liquid` - Quiz section
- `templates/page.insole-finder-2.json` - Page template

**Important:** 
- Quiz logic handled by custom app (contact Born West for changes)
- Theme changes only affect UI/styling
- Work with Michael Sullivan, Heather Allerdice-Gerow, and Born West team

### SearchSpring Integration

**Section:** `sections/searchspring-recommendations.liquid`  
**Snippet:** `snippets/searchspring-script.liquid`

**Purpose:** Enhanced product search and filtering beyond Shopify's default search.

**Implementation:**
- SearchSpring JavaScript SDK loaded
- Custom search templates
- Product recommendations section
- Multi-instance support (US, UK, CA-EN, CA-FR)

**Assets:**
- `assets/searchspring.bundle.js` - SearchSpring SDK

**Key Features:**
- Enhanced search and filtering
- Product recommendations
- Regional filtering for UK/EU/AU markets
- Cart-based recommendations

**Important:** 
- Essential A/B Testing app is incompatible with SearchSpring
- See [Integrations Guide](./integrations.md) for operational details
- See [Technical User Guide](./technical-user-guide.md) for implementation details

### Recharge Subscriptions

**Snippets:**
- `snippets/recharge-choose-your-bundle-customizations.liquid` - Bundle customization UI
- `snippets/recharge-subscription-customizations.liquid` - Subscription customization UI

**Templates:**
- `product.recharge-bundle.json` - Bundle products
- `product.subscription.json` - Subscription products

**Purpose:** Product bundles and subscription orders.

**Implementation:**
- Recharge-specific templates
- Custom subscription UI components
- Mutation observers for async loading
- Checkout flow modifications

**Assets:**
- `assets/component-recharge-customizations.css`
- `assets/component-recharge-subscriptions.css`
- `assets/recharge-subscription-mutations.js`
- `assets/recharge-subscription-functions.js`

**Important:** 
- See [Integrations Guide](./integrations.md) for operational details
- See [Technical User Guide](./technical-user-guide.md) for implementation details

### RX Microsite

**Purpose:** Create branded microsite experiences within the main Superfeet site.

**Implementation:**
- Metafield-based routing in `layout/theme.liquid`
- Separate header/footer groups
- Microsite-specific menus
- Shared header/footer configuration

**Files:**
- `layout/theme.liquid` - Microsite routing logic
- `sections/header-group-microsite.json` - Microsite header
- `sections/footer-group-microsite.json` - Microsite footer

**Metafield:**
- `page.metafields.cql.rx_microsite` [boolean] - Enables microsite layout

---

## Development Patterns

### Component Reuse Patterns

**Product Card Pattern:**
- Snippet: `snippets/card-product.liquid`
- Used across: Collection pages, search results, recommendations
- Consistent product display
- Reusable across templates

**Menu Rendering Pattern:**
- Snippet: `snippets/menu-list.liquid`
- Used in: Header, footer, mobile menu
- Consistent menu structure
- Supports mega menu functionality

**Image Rendering Pattern:**
- Snippet: `snippets/image.liquid`
- Used across: All sections and templates
- Handles lazy loading
- Responsive image support

### Responsive Design Patterns

**Mobile-First Approach:**
- Base styles target mobile
- Media queries for larger screens
- Progressive enhancement
- Touch-friendly interactions

**Breakpoint Strategy:**
- Mobile: Base styles (default)
- Tablet: 750px and up
- Desktop: 990px and up
- Large Desktop: 1200px and up (if needed)

**Responsive Components:**
- Grid systems adapt to screen size
- Navigation changes (desktop menu → mobile drawer)
- Images scale appropriately
- Typography adjusts for readability

### Code Organization Patterns

**Separation of Concerns:**
- **Liquid:** Data and logic
- **CSS:** Styling and layout
- **JavaScript:** Interactivity and behavior

**Component-Based Architecture:**
- Each component has its own CSS and JS files
- Components are reusable across sections
- Components are self-contained when possible

**DRY (Don't Repeat Yourself):**
- Use snippets for repeated markup
- Use CSS classes for repeated styles
- Use JavaScript functions for repeated logic
- Centralize configuration (window.Resources)

### Naming Conventions

**Files:**
- Sections: `{name}.liquid` (e.g., `header.liquid`)
- Snippets: `{name}.liquid` (e.g., `card-product.liquid`)
- Templates: `{type}.{suffix}.json` (e.g., `product.bundle.json`)
- CSS: `section-{name}.css` or `component-{name}.css`
- JavaScript: `{name}.js` or `component-{name}.js`

**CSS Classes:**
- BEM-like naming: `component-name__element--modifier`
- Examples: `header__menu-item--white`
- Consistent naming across theme

**JavaScript:**
- Namespace pattern: `ComponentName`
- Methods: `camelCase`
- Constants: `UPPER_CASE`

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
- `section.settings.mobile_menu` - Mobile menu (optional)
- `section.settings.utility_menu` - Utility menu (optional)

**Menu Object Properties:**
- `menu.links` - Array of menu links
- `link.url` - Link URL
- `link.title` - Link title
- `link.active` - Whether link is active
- `link.links` - Child links (nested menus)

### Footer Menu Access

**Location:** `sections/footer.liquid`

```liquid
{% for block in section.blocks %}
  {% if block.type == 'link_list' %}
    {% if block.settings.menu != blank %}
      {% for link in block.settings.menu.links %}
        <a href="{{ link.url }}">{{ link.title }}</a>
      {% endfor %}
    {% endif %}
  {% endif %}
{% endfor %}
```

**Footer Menus:** Block-based (not direct settings)

**Copyright Menu:**
```liquid
{% if section.settings.copyright_menu %}
  {% for link in section.settings.copyright_menu.links %}
    <a href="{{ link.url }}">{{ link.title }}</a>
  {% endfor %}
{% endif %}
```

### Announcement Bar Menu

**Location:** `sections/announcement-bar.liquid`

```liquid
{% if section.settings.announcement_menu != blank %}
  {% for link in section.settings.announcement_menu.links %}
    <a href="{{ link.url }}">{{ link.title }}</a>
  {% endfor %}
{% endif %}
```

### Global Resources Access

**Location:** `snippets/cql-head-content.liquid`

**JavaScript Access:**
```javascript
// SearchSpring configuration
window.Resources.searchspring.siteIds.productFeeds.usEnglish

// Recharge configuration
window.Resources.recharge.bundles.selectAVariant

// Color map
window.Resources.colorMap
```

**Liquid Access:**
- Resources are defined in Liquid
- Output as JavaScript in `<head>`
- Available globally in JavaScript
- Used by integrations and components

---

## Regional Theme Differences

### US Store (superfeetww)

**Characteristics:**
- 135 templates (most comprehensive)
- Full feature set
- All integrations active
- Primary development store
- Reference for other stores

**Template Count:** 135 (March 2026 US export)

### Canada Store (superfeet-ca)

**Characteristics:**
- 75 templates (recursive JSON in `code/superfeet-ca-theme`, Oct 2025 export in repo)
- Bilingual support (English/French)
- Regional pricing and shipping
- CA-specific customizations

**Template Count:** 75 (re-export to confirm current)

**Language Support:**
- English (primary)
- French (secondary)
- Language switching via Shopify Markets

### UK Store (superfeet-uk)

**Characteristics:**
- 84 templates (recursive JSON in `code/superfeet-uk-theme`, Oct 2025 export in repo)
- UK/EU/AU customer focus
- Regional pricing and shipping
- Market context files for EU/AU

**Template Count:** 84 (re-export to confirm current)

**Market Support:**
- UK Market: Transactional
- EU Market: Brochure-only (via market context)
- AU Market: Brochure-only (via market context)

### Key Differences Summary

**Common:**
- Same base theme (CQL Propel v24.3.0)
- Same layout files
- Same core functionality

**Different:**
- Section counts: US Mar 2026 export has 103 sections / 144 snippets vs 101 / 143 in older regional exports in this repo until themes are synced.
- Template counts vary by store (US 135 vs CA 75 vs UK 84 in current repo folders—see table above)
- Settings configurations differ
- Language/localization settings
- Store-specific customizations
- SearchSpring instance configurations
- Regional pricing and shipping

**Files to Compare:**
- `config/settings_data.json` - Store-specific settings
- `templates/` - Different template assignments
- `locales/` - Language files may differ

---

## Maintenance & Updates

### Theme Updates

**Current Version:** CQL Propel v24.3.0

**Update Considerations:**
- Test thoroughly before upgrading
- Check for breaking changes
- Review CQL Propel changelog
- Test on staging first
- Coordinate multi-store updates
- Backup theme before updating

**Update Process:**
1. Review CQL Propel release notes
2. Test update on staging theme
3. Check for breaking changes
4. Update customizations if needed
5. Test on all stores
6. Deploy to live

### Critical Files

**Do Not Modify Without Testing:**
- `layout/theme.liquid` - Base layout, affects all pages
- `sections/header.liquid` - Navigation, affects all pages
- `sections/footer.liquid` - Footer, affects all pages
- `sections/announcement-bar.liquid` - Announcement bar, affects all pages
- `snippets/cql-head-content.liquid` - Global JavaScript configuration

**High-Risk Files:**
- Files used across multiple templates
- Global CSS/JavaScript files
- Integration snippets
- Core navigation components

### URL Redirects

**Migration Preserved:**
- 4,400+ redirects from Magento migration
- Critical for SEO
- Maintains old URL structure
- Preserves search engine rankings

**Important:**
- Do not modify redirects without careful testing
- Coordinate with SEO team before changes
- Test redirects after any changes
- Monitor for 404 errors

### Backup Strategy

**Before Major Changes:**
1. Backup theme via Shopify Admin
2. Export theme via Matrixify
3. Commit changes to Git
4. Document changes made

**Backup Methods:**
- Shopify Admin: Duplicate theme
- Matrixify: Export theme files
- Git: Version control
- Shopify CLI: `shopify theme pull`

### Performance Monitoring

**Regular Checks:**
- PageSpeed Insights (monthly)
- Core Web Vitals monitoring
- Calibreapp metrics
- Browser Performance tab

**Performance Targets:**
- LCP: < 2.5s
- CLS: < 0.1
- INP: < 200ms
- FCP: < 1.8s

**Optimization Opportunities:**
- Image optimization
- JavaScript bundle size
- CSS optimization
- Lazy loading implementation
- Critical resource prioritization

---

## Additional Resources

### Documentation
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md) - Practical development workflows
- **Data Guide:** [data-guide.md](./data-guide.md) - Complete metafields reference
- **Integrations:** [integrations.md](./integrations.md) - App integration details
- **Business User Guide:** [business-user-guide.md](./business-user-guide.md) - Non-technical workflows

### External Resources
- **Shopify Theme Development:** https://shopify.dev/themes
- **Liquid Documentation:** https://shopify.dev/api/liquid
- **Shopify CLI:** https://shopify.dev/themes/tools/cli
- **CQL Propel Theme:** Theme vendor documentation

### Tools
- **Shopify CLI:** Theme development and deployment
- **Theme Inspector:** Browser extension for debugging
- **PageSpeed Insights:** Performance testing
- **Browser DevTools:** Built-in debugging tools
- **Matrixify:** Theme export/import

---

*Last Updated: Based on US theme export March 31, 2026 ([internal_THEME_DELTA_MAR2026.md](./internal_THEME_DELTA_MAR2026.md))*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

