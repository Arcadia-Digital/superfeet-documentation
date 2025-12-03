# Technical User Guide

**Superfeet Multi-Region Shopify Plus Platform**

Developer-focused documentation for working with the Superfeet eCommerce platform.

---

## Table of Contents

1. [Development Environment Setup](#development-environment-setup)
2. [Theme Development Workflow](#theme-development-workflow)
3. [Navigation Implementation](#navigation-implementation)
4. [Template System](#template-system)
5. [Section Development](#section-development)
6. [Snippet Development](#snippet-development)
7. [Code Patterns & Best Practices](#code-patterns--best-practices)
8. [Multi-Store Development](#multi-store-development)
9. [Integration Management](#integration-management)
10. [Troubleshooting](#troubleshooting)

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

### Local Development Server

```bash
# Navigate to theme directory
cd path/to/superfeet-ww-theme

# Start local development server
shopify theme dev --store superfeetww

# This will:
# - Start local server at http://127.0.0.1:9292
# - Watch for file changes
# - Sync changes to Shopify
# - Open theme preview URL
```

---

## Theme Development Workflow

### Development Process

1. **Local Development:**
   ```bash
   shopify theme dev --store superfeetww
   ```

2. **Push to Staging:**
   ```bash
   shopify theme push --unpublished --store superfeetww
   ```

3. **Test on Staging:**
   - Review changes in staging theme
   - Test functionality
   - Verify responsive design

4. **Push to Live:**
   ```bash
   shopify theme push --live --store superfeetww
   ```

**Critical:** Always test on staging before pushing to live!

### Theme Structure

See [Theme Architecture Documentation](./theme-architecture.md) for complete structure overview.

**Key Directories:**
- `sections/` - Page building blocks (101+ files)
- `snippets/` - Reusable components (143+ files)
- `templates/` - Page templates (126+ files in US store)
- `assets/` - CSS, JavaScript, images, fonts
- `config/` - Theme settings

---

## Navigation Implementation

### Header Navigation

**File:** `sections/header.liquid`

**Menu Settings:**
- `section.settings.menu` - Main desktop menu
- `section.settings.mobile_menu` - Mobile menu (optional)
- `section.settings.utility_menu` - Utility menu (optional)

**Code Reference:**
```liquid
{% if section.settings.menu != blank %}
  {% render 'menu-list', menu: section.settings.menu, blocks: section.blocks %}
{% endif %}
```

**Mobile Menu:**
```liquid
{% render 'menu-header-drawer', 
  menu: section.settings.mobile_menu, 
  blocks: section.blocks, 
  secondary_menu: section.settings.utility_menu 
%}
```

**Menu Access in Liquid:**
- Menu object: `section.settings.menu`
- Menu links: `section.settings.menu.links`
- Link properties: `link.url`, `link.title`, `link.active`

### Footer Navigation

**File:** `sections/footer.liquid`

**Footer Menus:** Block-based (not direct settings)

**Code Reference:**
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

**Copyright Menu:**
```liquid
{% if section.settings.copyright_menu %}
  {% for link in section.settings.copyright_menu.links %}
    <!-- Menu items -->
  {% endfor %}
{% endif %}
```

### Announcement Bar Menu

**File:** `sections/announcement-bar.liquid`

**Code Reference:**
```liquid
{% if section.settings.announcement_menu != blank %}
  {% for link in section.settings.announcement_menu.links %}
    <a href="{{ link.url }}">{{ link.title }}</a>
  {% endfor %}
{% endif %}
```

### Menu Snippet System

**Main Menu Snippet:** `snippets/menu-list.liquid`

**Usage:**
```liquid
{% render 'menu-list', menu: link_list, blocks: blocks %}
```

**Menu Header Drawer:** `snippets/menu-header-drawer.liquid`

**Usage:**
```liquid
{% render 'menu-header-drawer', 
  menu: mobile_menu, 
  blocks: blocks, 
  secondary_menu: utility_menu 
%}
```

### Superfeet Mega Menu Implementation

**Mega Menu System:**
- Block type: `desktop_megamenu_promos`
- Parent menu matching: `block.settings.parent_menu_item_name`
- **Case-sensitive matching required** - menu item title must match exactly

**Implementation Details:**

The mega menu system in `snippets/menu-list.liquid` uses a block-based approach where promo blocks are matched to parent menu items:

```liquid
{%- for block in blocks -%}
  {%- if link.title != blank and link.title != block.settings.parent_menu_item_name -%}
    {%- continue -%}
  {%- endif -%}

  {%- case block.type -%}
    {%- when 'desktop_megamenu_promos' -%}
      <details-disclosure>
        <details id="Details-HeaderMenu-{{ forloop.index }}">
          <summary class="header__menu-item header__menu-item--white list-menu__item link focus-inset">
            <a href="{{ link.url }}" class="header__parent-link">{{ link.title | escape }}</a>
          </summary>
          <div class="header__submenu-contents">
            <!-- Mega menu content -->
            {% render 'menu-list-promos', menu_item: link, blocks: blocks, mobile: false, promo_slots: promoCount %}
          </div>
        </details>
      </details-disclosure>
  {%- endcase -%}
{%- endfor -%}
```

**Key Features:**
- Promo slots calculated based on child link count (max 3 links = 1 promo slot, fewer links = 2 promo slots)
- Supports nested menu items (grandchild links)
- Special handling for "BLANK" menu items (used for spacing)
- "Shop All" link option via `block.settings.parent_menu_item_all`
- Grandchild links support "::" separator for title/subtitle display

**Menu Item Formatting:**
- Use "::" separator in grandchild link titles for title/subtitle display:
  - Example: "Product Name::Subtitle text"
  - Renders as: `<span class="header__menu-item--grandchild__title">Product Name</span><span class="header__menu-item--grandchild__subtext">Subtitle text</span>`

**Important Notes:**
- Menu item name matching is **case-sensitive**
- Block must be added to header section in Theme Customizer
- Promo content is rendered via `menu-list-promos` snippet

---

## Template System

### Template Types

**Product Templates:**
- Default: `product.json`
- Variants: `product.*.json` (75+ variants in US store)
- Assignment: Product → Template suffix

**Collection Templates:**
- Default: `collection.json`
- Variants: `collection.*.json` (30+ variants in US store)
- Assignment: Collection → Template suffix

**Page Templates:**
- Default: `page.json`
- Variants: `page.*.json` (50+ variants in US store)
- Assignment: Page → Template suffix

### Template Assignment

**In Shopify Admin:**
1. Navigate to product/collection/page
2. Set "Template suffix" field
3. Template file: `{type}.{suffix}.json`

**Example:**
- Product handle: `all-purpose-cushion`
- Template suffix: `all-purpose-cushion`
- Template file: `product.all-purpose-cushion.json`

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
        }
      }
    }
  },
  "order": ["main"]
}
```

---

## Section Development

### Creating a New Section

1. **Create File:** `sections/my-section.liquid`

2. **Add Schema:**
```liquid
{% schema %}
{
  "name": "My Section",
  "tag": "section",
  "class": "section",
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

3. **Include in Template:**
   - Via Theme Customizer (add section)
   - Or in template JSON

### Section Blocks

**Adding Blocks:**
```liquid
{% schema %}
{
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
  ]
}
{% endschema %}
```

**Rendering Blocks:**
```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when 'text_block' %}
      <div>{{ block.settings.content }}</div>
  {% endcase %}
{% endfor %}
```

---

## Snippet Development

### Creating Snippets

1. **Create File:** `snippets/my-snippet.liquid`

2. **Accept Parameters:**
```liquid
{% comment %}
  Accepts:
  - param1: {String} Description
  - param2: {Number} Description
{% endcomment %}

<div class="my-snippet">
  {{ param1 }}
  {{ param2 }}
</div>
```

3. **Render Snippet:**
```liquid
{% render 'my-snippet', 
  param1: value1, 
  param2: value2 
%}
```

### Best Practices

**Use `{% render %}` not `{% include %}`:**
- `{% render %}` caches snippets (better performance)
- `{% include %}` is deprecated

**Performance:**
- Minimize snippet nesting
- Cache expensive operations
- Use `limit` for loops

---

## Code Patterns & Best Practices

### Liquid Best Practices

**Performance:**
```liquid
{% comment %} Good: Use limit {% endcomment %}
{% for product in collection.products limit: 4 %}
  <!-- Product card -->
{% endfor %}

{% comment %} Good: Use render {% endcomment %}
{% render 'product-card', product: product %}

{% comment %} Avoid: Nested loops {% endcomment %}
{% for collection in collections %}
  {% for product in collection.products %}
    <!-- Avoid this pattern -->
  {% endfor %}
{% endfor %}
```

**Security:**
```liquid
{% comment %} Always escape user input {% endcomment %}
{{ user_input | escape }}

{% comment %} URL parameters {% endcomment %}
{{ url | url_param_escape }}

{% comment %} JSON output {% endcomment %}
{{ data | json }}
```

**Metafield Access:**
```liquid
{% comment %} Check if metafield exists {% endcomment %}
{% if product.metafields.custom.field_name %}
  {{ product.metafields.custom.field_name }}
{% endif %}

{% comment %} JSON metafields {% endcomment %}
{% assign json_data = product.metafields.custom.json_field | parse_json %}
```

### Superfeet-Specific Metafield Patterns

**CQL Namespace Metafields:**

Superfeet uses the `cql.*` namespace extensively for product data:

```liquid
{% comment %} Product information metafields {% endcomment %}
{{ product.metafields.cql.arch_height }}
{{ product.metafields.cql.insole_thickness }}
{{ product.metafields.cql.product_gender }}
{{ product.metafields.cql.product_family }}
{{ product.metafields.cql.underfoot_cushioning }}

{% comment %} Size information {% endcomment %}
{{ product.metafields.cql.men_sizes }}
{{ product.metafields.cql.women_sizes }}
{{ product.metafields.cql.kid_sizes }}

{% comment %} Product attributes (boolean) {% endcomment %}
{% if product.metafields.cql.vegan %}
  <span>Vegan</span>
{% endif %}

{% comment %} Product reference list {% endcomment %}
{% for comparison_product in product.metafields.cql.comparison_products.value %}
  {{ comparison_product.title }}
{% endfor %}

{% comment %} Metaobject reference {% endcomment %}
{% assign faq_group = product.metafields.cql.faq_group.value %}
{{ faq_group.title }}
```

**Page Metafields:**

RX microsite detection:
```liquid
{% if page.metafields.cql.rx_microsite %}
  {% assign isMicrositePage = true %}
{% endif %}
```

**Best Practices:**
- Always check metafield existence before accessing
- Use `.value` for list and metaobject references
- Check boolean metafields with `{% if %}` before display
- Use namespace consistently (`cql.*` for product data, `custom.*` for custom features)

### JavaScript Best Practices

**Namespace Pattern:**
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

**Performance:**
- Minimize DOM queries
- Cache selectors
- Use event delegation
- Defer non-critical scripts

---

## Multi-Store Development

### Development Workflow

1. **Make changes on one store** (usually US first)
2. **Test thoroughly**
3. **Export/replicate to other stores**
4. **Test on each store**

### Theme Sync Methods

**Manual File Copy:**
- Copy changed files between stores
- Update via Shopify CLI or admin

**Matrixify:**
- Export theme from one store
- Import to other stores
- Preserves settings

**Shopify CLI:**
```bash
# Push to multiple stores
shopify theme push --store superfeetww
shopify theme push --store superfeet-ca
shopify theme push --store superfeet-uk
```

### Store-Specific Considerations

**Settings Differences:**
- Review `config/settings_data.json` per store
- Pricing, shipping, tax configurations differ
- Language/localization settings vary

**Template Differences:**
- **US Store:** 123 templates (most comprehensive)
- **Canada Store:** 82 templates
- **UK Store:** 90 templates
- Store-specific template assignments
- Regional customizations

**SearchSpring Instance Configuration:**
- Each store has different SearchSpring instance settings
- US: `searchspring_instance = "us"`
- UK: `searchspring_instance = "uk"`
- CA English: `searchspring_instance = "ca-en"`
- CA French: `searchspring_instance = "ca-fr"`

**Regional Settings:**
- `settings.searchspring_region` - Used for SearchSpring filtering
- Language settings differ (CA has English/French)
- Currency settings per store

### UK Store Market-Specific Development

**Shopify Markets Implementation:**

The UK store uses Shopify Markets to serve three regions:
- **UK Market:** Transactional (shows buy buttons, prices, cart)
- **EU Market:** Brochure-only (hides buy buttons, prices, cart)
- **AU Market:** Brochure-only (hides buy buttons, prices, cart)

**Market Context Files:**

Market-specific templates use context files that override base templates:
- Base: `product.json` (UK market - full functionality)
- EU Override: `product.context.eu.json` (disables transactional blocks)
- AU Override: `product.context.au.json` (disables transactional blocks)

**Market Context File Structure:**

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

**Development Considerations:**
- Market context files inherit from base templates
- Disabled blocks hide transactional elements for brochure markets
- SearchSpring recommendations filter by market (`mfield_cql_market`)
- Template edits in Theme Customizer require market context selection

**Testing:**
- Test UK market (transactional functionality)
- Test EU market (brochure-only, no buy buttons)
- Test AU market (brochure-only, no buy buttons)
- Verify SearchSpring filtering works per market

---

## Superfeet-Specific Features

### RX Microsite Implementation

**Purpose:** Create branded microsite experiences within the main Superfeet site (e.g., RX microsite for healthcare professionals).

**How It Works:**

The RX microsite uses a metafield-based routing system in `layout/theme.liquid`:

```liquid
<!-- Microsite logic (RX site) -->
{% assign isMicrositePage = false %}

{% if page.metafields.cql.rx_microsite != blank and page.metafields.cql.rx_microsite != false %}
  {% assign isMicrositePage = true %}
{% endif %}
```

**Header/Footer Routing:**

```liquid
{% if isMicrositePage %}
  {% sections 'header-group-microsite' %}
{% else %}
  {% sections 'header-group' %}
{% endif %}

<!-- Main content -->

{% if isMicrositePage %}
  {% sections 'footer-group-microsite' %}
{% else %}
  {% sections 'footer-group' %}
{% endif %}
```

**Setup:**
1. Create page in Shopify Admin
2. Set metafield `cql.rx_microsite` to `true` (boolean)
3. Configure `header-group-microsite` and `footer-group-microsite` sections in Theme Customizer
4. Create microsite-specific menus (e.g., `rx-main-menu`, `rx-main-menu-mobile`)

**Files:**
- `layout/theme.liquid` - Microsite routing logic
- `sections/header-group-microsite.json` - Microsite header configuration
- `sections/footer-group-microsite.json` - Microsite footer configuration

**Important:** All pages with `cql.rx_microsite = true` share the same header/footer configuration. Changes to microsite header/footer affect all microsite pages.

### Insole Finder Quiz

**Purpose:** Custom product recommendation quiz guiding customers to the right insole.

**Implementation:**

**Layout:** `layout/theme.insole-finder.liquid`
- Dedicated layout file separate from main theme
- Uses microsite header/footer groups
- Custom app integration (built by Born West & Superfeet)

**Section:** `sections/insole-finder-2.liquid`
- Quiz interface section
- Product recommendation display
- Custom app JavaScript integration

**Template:** `page.insole-finder-2.json`
- Page template for Insole Finder pages
- Assign via Template suffix: `insole-finder-2`

**Setup:**
1. Create page in Shopify Admin
2. Set Template suffix: `insole-finder-2`
3. Configure `insole-finder-2` section in Theme Customizer
4. Quiz logic handled by custom app (contact Born West for changes)

**Important:** Work with Michael Sullivan, Heather Allerdice-Gerow, and Born West team for quiz logic changes. Theme changes only affect UI/styling.

### Product Compare Section

**Purpose:** Display product comparison table on product pages using metafield-based product references.

**Section:** `sections/product-compare.liquid`

**Implementation:**

The section uses the `cql.comparison_products` metafield (list.product_reference) to display comparison products:

```liquid
{%- assign metafields = product.metafields.cql -%}
{%- assign compare_products = metafields.comparison_products.value -%}

{%- if compare_products != blank -%}
  {%- tablerow compare_product in compare_products limit: 3 -%}
    {% render 'product-compare-column', 
      compare_product: compare_product, 
      hide_product_prices: section.settings.hide_product_prices 
    %}
  {%- endtablerow -%}
{% endif %}
```

**Metafields Used:**
- `cql.comparison_products` [list.product_reference] - Products to compare
- `cql.arch_height` - Arch height specification
- `cql.insole_thickness` - Insole thickness
- `cql.underfoot_cushioning` - Cushioning level
- `cql.target_use_activity` - Target activity
- `cql.fits_best_in` - Fit description

**Features:**
- Displays current product + up to 3 comparison products
- Option to hide/show current product (`do_not_feature_current_product` setting)
- Expandable rows (shows primary rows, expand button for additional)
- Row count calculated dynamically based on available metafield data
- Price display toggle (`hide_product_prices` setting)

**Snippet:** `snippets/product-compare-column.liquid`
- Renders individual product column in comparison table
- Handles metafield display logic
- Supports current product vs comparison product styling

**Usage:**
1. Add `product-compare` section to product template
2. Set product metafield `cql.comparison_products` with product references
3. Configure section settings (heading, row count, price display)

### Feature Diagram Section

**Purpose:** Display interactive feature diagrams on product pages using metaobject references.

**Section:** `sections/feature-diagram.liquid`

**Implementation:**

The section checks for feature diagram metafields on the current template object:

```liquid
{% assign current_template = template | split: '.' | first %}
{% assign template_object = '' %}

{% case current_template %}
  {% when 'product' %}
    {% assign template_object = product %}
  {% when 'page' %}
    {% assign template_object = page %}
  {% when 'blog' %}
    {% assign template_object = blog %}
  {% when 'collection' %}
    {% assign template_object = collection %}
{% endcase %}

{% if template_object.metafields.custom.feature_diagram or template_object.metafields.cql.feature_diagram %}
  <!-- Feature diagram content -->
{% endif %}
```

**Metafields:**
- `custom.feature_diagram` [metaobject_reference] - Feature diagram metaobject
- `cql.feature_diagram` [metaobject_reference] - Alternative namespace

**Features:**
- Animated diagram display
- Interactive hotspot functionality
- Responsive image handling
- Customizable animation timing

**Usage:**
1. Create feature diagram metaobject in Shopify Admin
2. Assign metaobject to product/page via metafield
3. Add `feature-diagram` section to template
4. Configure section settings (animation timing, styling)

### Shop the Look Section

**Purpose:** Display "shop the look" product groupings with lifestyle imagery.

**Section:** `sections/shop-the-look.liquid`

**Features:**
- Lifestyle image with product hotspots
- Product cards overlay
- Responsive layout
- Customizable styling

**Usage:**
1. Add `shop-the-look` section to page template
2. Configure lifestyle image
3. Add product blocks with positioning
4. Configure styling settings

### UGC (User-Generated Content) Section

**Purpose:** Display user-generated content feeds.

**Section:** `sections/ugc.liquid`

**Features:**
- Social media feed integration
- Content moderation
- Responsive grid layout

---

## Integration Management

### SearchSpring Integration

**Purpose:** Enhanced product search, filtering, and recommendations beyond Shopify's default search.

**Section:** `sections/searchspring-recommendations.liquid`  
**Snippet:** `snippets/searchspring-script.liquid`

**SearchSpring Script Snippet:**

The `searchspring-script.liquid` snippet initializes SearchSpring context:

```liquid
<script src="{{ 'searchspring.bundle.js' | asset_url }}" id="searchspring-context">
  {% if collection.handle and collection.handle != 'shop' %}
    collection = {
      id: "{{ collection.id }}",
      name: "{{ collection.title }}",
      handle: "{{ collection.handle }}",
    };
  {% endif %}
  {% if blog.handle %}
    blog = {
      id: "{{ blog.id }}",
      name: "{{ blog.title }}",
      handle: "{{ blog.handle }}",
    };
  {% endif %}
  myShopifyDomain = {
    url: "{{ shop.permanent_domain }}"
  };
  {% if current_tags %}tags = "{{ current_tags | join: "," }}";{% endif %}
  {% if template %}template = "{{ template }}";{% endif %}
  {% if collection.handle and collection.handle == 'shop' %}searchPage = true;{% endif %}
  {% if customer %}shopper = { id: "{{ customer.id }}" };{% endif %}
  region = '{{ settings.searchspring_region }}';
</script>
```

**SearchSpring Recommendations Section:**

The recommendations section supports multiple instances and regional filtering:

```liquid
<script type="searchspring/personalized-recommendations" profile="{{ block.settings.profile_id }}">
  options = {
    {% if section.settings.searchspring_instance == "us" %}
      siteId: window.Resources.searchspring.siteIds.productFeeds.usEnglish,
    {% elsif section.settings.searchspring_instance == "uk" %}
      siteId: window.Resources.searchspring.siteIds.productFeeds.ukEnglish,
    {% elsif section.settings.searchspring_instance == "ca-en" %}
      siteId: window.Resources.searchspring.siteIds.productFeeds.caEnglish,
    {% elsif section.settings.searchspring_instance == "ca-fr" %}
      siteId: window.Resources.searchspring.siteIds.productFeeds.caFrench,
    {% endif %}
    
    {% if canonical_url contains ".uk" %}
      filters: [
        {
          type: 'value',
          field: 'mfield_cql_market',
          value: 'UK'
        }
      ]
    {% elsif canonical_url contains ".au" %}
      filters: [
        {
          type: 'value',
          field: 'mfield_cql_market',
          value: 'AU'
        }
      ]
    {% elsif canonical_url contains ".eu" %}
      filters: [
        {
          type: 'value',
          field: 'mfield_cql_market',
          value: 'EU'
        }
      ]
    {% endif %}
    
    batched: false,
    limit: {{ block.settings.max_recommendations }},
  };
</script>
```

**Key Features:**
- Multi-instance support (US, UK, CA-EN, CA-FR)
- Regional filtering for UK/EU/AU markets
- Product and blog feed support
- Cart-based recommendations
- Cookie/DoNotTrack detection (hides section if disabled)

**Regional Filtering:**
- UK market: Filters by `mfield_cql_market = 'UK'`
- AU market: Filters by `mfield_cql_market = 'AU'`
- EU market: Filters by `mfield_cql_market = 'EU'`

**Section Settings:**
- `searchspring_instance` - Select instance (us, uk, ca-en, ca-fr)
- `feed_selection` - Product or blog feed
- `heading` - Section heading text
- `heading_size` - Heading size class
- `background_color` - Section background
- `text_color` - Text color
- Padding settings (desktop/mobile)

**Block Settings:**
- `profile_id` - SearchSpring recommendation profile ID
- `max_recommendations` - Maximum products to display
- `tab_title` - Tab title (if multiple blocks)

**Important:** 
- Essential A/B Testing app is **incompatible** with SearchSpring
- Section automatically hides if cookies disabled or DoNotTrack enabled
- Regional filtering ensures correct products show for UK/EU/AU markets

### Recharge Subscriptions

**Purpose:** Product bundles and subscription orders.

**Snippets:**
- `snippets/recharge-choose-your-bundle-customizations.liquid` - Bundle customization UI
- `snippets/recharge-subscription-customizations.liquid` - Subscription customization UI

**Templates:**
- `product.recharge-bundle.json` - Bundle products
- `product.subscription.json` - Subscription products

**Recharge Bundle Implementation:**

The bundle snippet includes mutation observers to handle Recharge app loading:

```liquid
{{ 'component-recharge-customizations.css' | asset_url | stylesheet_tag }}

<script>
  function initRechargeCustomizations(e) {
    // Mutation observer waiting for recharge to load fully
    const targetNode = document.querySelector("#recharge-bundles");
    const observer = new MutationObserver(function(mutations) {
      // Re-run event listeners on recharge app mutation
    });
    observer.observe(targetNode, { childList: true, subtree: true });
  }
  
  document.addEventListener("DOMContentLoaded", initRechargeCustomizations);
</script>
```

**Recharge Subscription Implementation:**

```liquid
{{ 'component-recharge-subscriptions.css' | asset_url | stylesheet_tag }}
{{ 'recharge-subscription-mutations.js' | asset_url | script_tag }}
{{ 'recharge-subscription-functions.js' | asset_url | script_tag }}

<div class="recharge-subscription__custom-modal hidden" role="dialog" aria-modal="true">
  <div class="recharge-subscription__inner">
    <div class="recharge-subscription__details"></div>
  </div>
</div>
```

**Global Resources:**

Recharge configuration is stored in `snippets/cql-head-content.liquid`:

```liquid
window.Resources = {
  recharge: {
    bundles: {
      selectAVariant: "{{ 'general.recharge.bundles.select_a_variant' | t }}",
      soldOutButtonText: "{{ 'general.recharge.bundles.sold_out_button_text' | t }}",
    },
    subscriptions: {
      closeModal: "{{ 'general.recharge.subscriptions.close_modal' | t }}"
    }
  }
};
```

**Usage:**
1. Install Recharge app in Shopify Admin
2. Configure bundle/subscription products in Recharge dashboard
3. Assign template suffix (`recharge-bundle` or `subscription`)
4. Recharge widgets automatically load on product pages

**Important:** 
- Recharge JavaScript loads asynchronously
- Mutation observers ensure customizations apply after Recharge loads
- Bundle layout template controlled by `rc_bundles.layout_template` metafield

### Elevar Tracking

**Implementation:**
- Elevar JavaScript loaded in `theme.liquid`
- Server-side event tracking
- Connected to GA4, Facebook, Klaviyo, Google Ads

**Code Location:** Check `layout/theme.liquid` for Elevar includes

**Important:** Don't remove Elevar scripts - they're critical for conversion tracking across all marketing channels.

### Yotpo Reviews

**Implementation:**
- Yotpo widgets in product templates
- Review syndication (US → UK/CA)
- ExpertVoice reviews → US

**Metafields:**
- `yotpo.reviews_average` [single_line_text_field] - Average rating
- `yotpo.reviews_count` [single_line_text_field] - Review count
- `yotpo.richsnippetshtml` [single_line_text_field] - Rich snippets HTML

**Important:** 
- Don't break review syndication when modifying product templates
- US reviews automatically syndicated to UK and CA stores
- ExpertVoice reviews syndicated to US store
- Yotpo widgets must remain in product template structure

---

## Troubleshooting

### Common Issues

**Theme Not Loading:**
1. Check Shopify status page
2. Verify theme is published
3. Check browser console for errors
4. Clear browser cache
5. Check `theme.liquid` for syntax errors

**Menu Not Displaying:**
1. Verify menu is assigned in Theme Customizer
2. Check menu exists in Shopify Admin
3. Verify menu has links
4. Check `sections/header.liquid` or `sections/footer.liquid`

**Tracking Not Working:**
1. Check Elevar dashboard for event status
2. Verify Elevar script is loading (browser console)
3. Check destination connections
4. Review server-side event logs

**Performance Issues:**
1. Check Calibreapp for metrics
2. Run PageSpeed Insights
3. Check for large images/assets
4. Review JavaScript bundle size
5. Check for render-blocking resources

### Debugging Tools

**Browser Console:**
- Open DevTools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for failed requests

**Shopify Admin:**
- Settings → Notifications
- Check for system notifications

**Theme Inspector:**
- Use Shopify Theme Inspector browser extension
- Inspect section settings
- Debug Liquid variables

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Shopify Theme Development:** https://shopify.dev/themes
- **Liquid Documentation:** https://shopify.dev/api/liquid
- **Shopify CLI:** https://shopify.dev/themes/tools/cli

---

*Last Updated: Based on theme exports from November 2025*

