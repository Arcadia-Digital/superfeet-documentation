# Technical User Guide

**Superfeet Multi-Region Shopify Plus Platform**

Comprehensive developer documentation for building, maintaining, and extending the Superfeet eCommerce platform.

**Who This Guide Is For:** Developers working on the Superfeet Shopify Plus platform. This guide assumes familiarity with Liquid templating, JavaScript, CSS, and Shopify theme development. For business user workflows, see the [Business User Guide](./business-user-guide.md).

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Development Environment Setup](#development-environment-setup)
3. [Theme Development Workflow](#theme-development-workflow)
4. [Code Architecture](#code-architecture)
5. [Template System](#template-system)
6. [Section Development](#section-development)
7. [Snippet Development](#snippet-development)
8. [Navigation Implementation](#navigation-implementation)
9. [Superfeet-Specific Features](#superfeet-specific-features)
10. [Multi-Store Development](#multi-store-development)
11. [Common Development Tasks](#common-development-tasks)
12. [Code Patterns & Best Practices](#code-patterns--best-practices)
13. [Integration Management](#integration-management)
14. [Troubleshooting & Debugging](#troubleshooting--debugging)
15. [Additional Resources](#additional-resources)

---

## Quick Start

### Your First Change (5-Minute Guide)

**Goal:** Make a simple text change to verify your development environment is working.

1. **Start Local Development:**
   ```bash
   shopify theme dev --store superfeetww
   ```

2. **Find a Section to Edit:**
   - Open `sections/header.liquid` or `sections/footer.liquid`
   - Look for a heading or text string
   - Make a small change (add "TEST" to a heading)

3. **Verify the Change:**
   - Check the preview URL that opened automatically
   - Or visit `http://127.0.0.1:9292`
   - Your change should appear immediately

4. **Push to Staging:**
   ```bash
   shopify theme push --unpublished --store superfeetww
   ```

5. **Test on Staging:**
   - Review the staging theme preview URL
   - Verify your change works correctly

**✅ Success!** Your development environment is working.

### Common Commands Cheat Sheet

```bash
# Start local development
shopify theme dev --store superfeetww

# Push to staging theme
shopify theme push --unpublished --store superfeetww

# Push to live theme (USE WITH CAUTION)
shopify theme push --live --store superfeetww

# Pull from live theme
shopify theme pull --live --store superfeetww

# List available themes
shopify theme list --store superfeetww

# Check theme status
shopify theme info --store superfeetww
```

### Key Files to Know

**Critical Files (Don't Modify Without Testing):**
- `layout/theme.liquid` - Base layout, loads all sections
- `sections/header.liquid` - Site navigation
- `sections/footer.liquid` - Site footer
- `sections/announcement-bar.liquid` - Top announcement bar

**Configuration Files:**
- `config/settings_data.json` - Current theme settings
- `config/settings_schema.json` - Theme settings schema

**Reference Documentation:**
- [Theme Architecture](./theme-architecture.md) - Complete theme structure
- [Data Guide](./data-guide.md) - Metafields reference
- [Integrations](./integrations.md) - App integration details

---

## Development Environment Setup

### Prerequisites

**Required:**
- Node.js (v16 or higher) - [Download](https://nodejs.org/)
- Git - [Download](https://git-scm.com/)
- Shopify CLI (latest version) - See installation below
- Code editor (VS Code recommended with Liquid extension)

**Recommended VS Code Extensions:**
- Shopify Liquid (by Shopify)
- Prettier (code formatting)
- ESLint (JavaScript linting)
- GitLens (Git integration)

### Shopify CLI Installation

```bash
# Install Shopify CLI globally
npm install -g @shopify/cli @shopify/theme

# Verify installation
shopify version

# Should output: @shopify/cli version X.X.X
```

**Troubleshooting Installation:**
- If `shopify` command not found, check your PATH
- On macOS/Linux, you may need to use `sudo` for global installs
- Alternative: Use `npx @shopify/cli` instead of global install

### Authentication

```bash
# Login to Shopify
shopify auth login

# You'll be prompted to:
# 1. Select a store (or enter store URL)
# 2. Authorize the CLI in your browser
# 3. Confirm authentication

# Store handles:
# - US: superfeetww
# - Canada: superfeet-ca
# - UK: superfeet-uk
```

**Multiple Store Access:**
- You can authenticate with multiple stores
- Switch stores using: `shopify auth logout` then `shopify auth login`
- Or specify store in each command: `shopify theme dev --store superfeetww`

### Local Development Server

```bash
# Navigate to theme directory
cd path/to/superfeet-ww-theme

# Start local development server
shopify theme dev --store superfeetww

# This will:
# - Start local server at http://127.0.0.1:9292
# - Watch for file changes and auto-sync
# - Open theme preview URL in browser
# - Show live reload in terminal
```

**Development Server Features:**
- **Hot Reload:** Changes sync automatically to Shopify preview
- **Live Preview:** See changes on actual Shopify storefront
- **Error Detection:** Syntax errors shown in terminal
- **File Watching:** Automatically detects file changes

**Stopping the Server:**
- Press `Ctrl+C` in terminal
- Or close the terminal window

### Git Setup (Recommended)

```bash
# Initialize git repository (if not already)
git init

# Create .gitignore
echo "node_modules/
.DS_Store
*.log
.env" > .gitignore

# Make initial commit
git add .
git commit -m "Initial commit"
```

**Git Workflow Best Practices:**
- Commit frequently with descriptive messages
- Create branches for features: `git checkout -b feature/new-section`
- Test on staging before merging to main
- Never commit sensitive data (API keys, passwords)

---

## Theme Development Workflow

### Standard Development Process

**1. Local Development:**
```bash
shopify theme dev --store superfeetww
```
- Make changes locally
- Test in browser at `http://127.0.0.1:9292`
- Verify changes appear in Shopify preview

**2. Push to Staging:**
```bash
shopify theme push --unpublished --store superfeetww
```
- Creates or updates staging theme
- Get staging theme URL from terminal output
- Test thoroughly on staging

**3. Quality Assurance:**
- Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- Test responsive design (mobile, tablet, desktop)
- Test functionality (forms, cart, checkout flow)
- Verify no console errors
- Check performance (PageSpeed Insights)

**4. Push to Live:**
```bash
shopify theme push --live --store superfeetww
```
- **⚠️ CRITICAL:** Only push to live after thorough staging testing
- Verify live theme is correct after push
- Monitor for errors or issues

### Theme Structure Overview

See [Theme Architecture Documentation](./theme-architecture.md) for complete structure.

**Key Directories:**
- `sections/` - Page building blocks (101+ files)
- `snippets/` - Reusable components (143+ files)
- `templates/` - Page templates (123+ files in US store)
- `assets/` - CSS, JavaScript, images, fonts
- `config/` - Theme settings
- `layout/` - Base layouts
- `locales/` - Translation files (52 languages)

### Working with Staging Themes

**Finding Your Staging Theme:**
```bash
# List all themes
shopify theme list --store superfeetww

# Look for themes with "Development" or "Staging" in name
# Or themes that are unpublished
```

**Staging Theme Best Practices:**
- Use descriptive theme names: "Staging - Feature Name"
- Keep staging themes organized
- Delete old staging themes periodically
- Always test on staging before live

### Version Control Strategy

**Recommended Approach:**
1. **Main Branch:** Production-ready code
2. **Feature Branches:** New features or fixes
3. **Staging Deployment:** Test feature branches
4. **Production Deployment:** Merge to main after testing

**Example Workflow:**
```bash
# Create feature branch
git checkout -b feature/new-product-section

# Make changes
# ... edit files ...

# Commit changes
git add .
git commit -m "Add new product section with comparison table"

# Push to staging
shopify theme push --unpublished --store superfeetww

# After testing, merge to main
git checkout main
git merge feature/new-product-section
git push origin main

# Deploy to live
shopify theme push --live --store superfeetww
```

---

## Code Architecture

### CSS Architecture

**File Organization:**

The theme uses a component-based CSS architecture:

```
assets/
├── base.css                    # Base styles, resets, typography
├── component-*.css             # Component-specific styles (50+ files)
├── section-*.css               # Section-specific styles (40+ files)
├── template-*.css              # Template-specific styles
└── [feature].css               # Feature-specific styles (e.g., insole-finder-2.css)
```

**CSS Naming Conventions:**

The theme appears to use a BEM-like naming convention:

```css
/* Component */
.component-name { }

/* Element */
.component-name__element { }

/* Modifier */
.component-name--modifier { }
```

**Example from theme:**
```css
.header__menu-item { }
.header__menu-item--white { }
.header__menu-item--grandchild__title { }
```

**CSS Loading Strategy:**

CSS files are loaded in `layout/theme.liquid`:
- Base styles loaded first
- Component styles loaded as needed
- Section styles loaded per section
- Critical CSS should be inlined for performance

**Responsive Design:**

The theme uses mobile-first responsive design:
- Base styles target mobile
- Media queries for tablet/desktop
- Breakpoints: Check `base.css` for exact values

**CSS Best Practices:**
- Use component classes, avoid inline styles
- Follow existing naming conventions
- Test responsive behavior at all breakpoints
- Minimize CSS specificity conflicts
- Use CSS custom properties (variables) when available

### JavaScript Architecture

**File Organization:**

```
assets/
├── global.js                   # Global functionality, initialization
├── constants.js                # Constants and configuration
├── pubsub.js                   # Event pub/sub system
├── component-*.js              # Component-specific JavaScript
├── [feature].js                # Feature-specific JavaScript
└── [vendor].js                 # Third-party libraries
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
      }
    }
  },
  recharge: {
    bundles: { /* ... */ },
    subscriptions: { /* ... */ }
  }
};
```

**JavaScript Module Pattern:**

Most JavaScript uses IIFE (Immediately Invoked Function Expression) pattern:

```javascript
(function() {
  'use strict';
  
  const ComponentName = {
    init: function() {
      this.bindEvents();
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

**Event Handling:**

The theme uses event delegation and pub/sub patterns:
- `pubsub.js` provides event system
- Components publish/subscribe to events
- Reduces coupling between components

**Third-Party Libraries:**

- **jQuery 3.6.0:** Used for DOM manipulation (legacy support)
- **Flickity:** Carousel/slider functionality
- **Swiper:** Alternative carousel library
- **SearchSpring Bundle:** Search and recommendations

**JavaScript Best Practices:**
- Use modern JavaScript (ES6+) when possible
- Avoid global variables (use namespaces)
- Use event delegation for dynamic content
- Defer non-critical scripts
- Minimize DOM queries (cache selectors)

### Asset Management

**Asset Loading:**

Assets are loaded via Liquid filters:
```liquid
{{ 'component-name.css' | asset_url | stylesheet_tag }}
{{ 'component-name.js' | asset_url | script_tag }}
```

**Asset Optimization:**

- **Images:** Use WebP/AVIF when possible, optimize file sizes
- **CSS:** Minify for production (Shopify handles this)
- **JavaScript:** Minify for production (Shopify handles this)
- **Fonts:** Use `font-display: swap` for better performance

**Image Assets:**

- SVG icons stored in `assets/` (87+ files in US store)
- Product images managed in Shopify Admin
- Lifestyle images uploaded per section

**Font Management:**

- Custom fonts: `proximanova_black.ttf`, `proximanova_regular.ttf`
- Fonts loaded via CSS `@font-face`
- Consider font subsetting for performance

**Performance Considerations:**

- Lazy load images below the fold
- Defer non-critical JavaScript
- Use `preload` for critical resources
- Minimize HTTP requests (combine CSS/JS when possible)

### Code Organization Principles

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

**Blog Templates:**
- `article.json` - Article template
- `blog.json` - Blog listing template
- Article variants: `article.*.json`

**System Templates:**
- `404.json` - 404 error page
- `cart.json` - Cart page
- `search.json` - Search results
- `password.json` - Password page

### Template Assignment

**In Shopify Admin:**
1. Navigate to product/collection/page
2. Scroll to **Search engine listing** section
3. Set **Template suffix** field
4. Template file: `{type}.{suffix}.json`

**Example:**
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
        "buy_buttons": {
          "type": "buy_buttons"
        }
      },
      "settings": {
        "enable_sticky_info": true
      }
    },
    "product-compare": {
      "type": "product-compare",
      "settings": {
        "heading": "Compare Products"
      }
    }
  },
  "order": ["main", "product-compare"]
}
```

**Template Sections:**
- Sections define page structure
- Order array controls section display order
- Sections can have blocks and settings
- Sections are editable in Theme Customizer

### Template Inheritance

**Base Templates:**
- Default templates (`product.json`, `collection.json`, etc.)
- Used when no template suffix is specified
- Can be customized per store

**Template Variants:**
- Custom templates for specific products/collections/pages
- Inherit from base template structure
- Can override section order and settings

**Market Context Files (UK Store):**
- Base: `product.json` (UK market)
- EU Override: `product.context.eu.json`
- AU Override: `product.context.au.json`
- Context files disable transactional blocks for brochure markets

### Creating New Templates

**When to Create a New Template:**
- Product needs unique layout
- Collection needs special sections
- Page needs custom structure
- Multiple products/collections share same layout

**Steps to Create:**
1. Copy existing template (e.g., `product.json`)
2. Rename to `product.{suffix}.json`
3. Modify sections and order
4. Test on staging
5. Assign to products via template suffix

**Template Naming:**
- Use descriptive suffixes: `product-bundle.json`
- Use kebab-case: `product-all-purpose-cushion.json`
- Avoid special characters or spaces

---

## Section Development

### Understanding Sections

**What Are Sections?**
- Building blocks of Shopify themes
- Can be added/removed/reordered in Theme Customizer
- Each section is a self-contained component
- Sections can have settings and blocks

**Section Files:**
- Liquid file: `sections/my-section.liquid`
- Contains HTML, Liquid logic, and schema
- Schema defines settings and blocks

### Creating a New Section

**1. Create the File:**
```bash
# Create file in sections directory
touch sections/my-section.liquid
```

**2. Add Basic Structure:**
```liquid
<div class="section my-section">
  <div class="page-width">
    <h2>{{ section.settings.heading }}</h2>
    <p>{{ section.settings.description }}</p>
  </div>
</div>

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
    },
    {
      "type": "richtext",
      "id": "description",
      "label": "Description"
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

**3. Add Styling:**
- Create `assets/section-my-section.css`
- Load in section: `{{ 'section-my-section.css' | asset_url | stylesheet_tag }}`

**4. Add JavaScript (if needed):**
- Create `assets/my-section.js`
- Load in section: `{{ 'my-section.js' | asset_url | script_tag }}`

**5. Test the Section:**
- Add section to a template via Theme Customizer
- Verify it displays correctly
- Test responsive behavior

### Section Settings

**Common Setting Types:**
- `text` - Single line text
- `textarea` - Multi-line text
- `richtext` - Rich text editor
- `html` - HTML content
- `image_picker` - Image selector
- `color` - Color picker
- `range` - Number slider
- `select` - Dropdown menu
- `checkbox` - Boolean toggle
- `radio` - Radio buttons
- `url` - URL input
- `product` - Product picker
- `collection` - Collection picker
- `page` - Page picker

**Setting Example:**
```liquid
{
  "type": "select",
  "id": "heading_size",
  "label": "Heading Size",
  "options": [
    {
      "value": "small",
      "label": "Small"
    },
    {
      "value": "medium",
      "label": "Medium"
    },
    {
      "value": "large",
      "label": "Large"
    }
  ],
  "default": "medium"
}
```

**Accessing Settings:**
```liquid
{{ section.settings.heading }}
{{ section.settings.heading_size }}
```

### Section Blocks

**What Are Blocks?**
- Flexible content within sections
- Users can add/remove/reorder blocks
- Each block type has its own settings
- Useful for repeating content

**Adding Blocks to Schema:**
```liquid
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
        },
        {
          "type": "image_picker",
          "id": "image",
          "label": "Image"
        }
      ]
    },
    {
      "type": "button_block",
      "name": "Button",
      "settings": [
        {
          "type": "text",
          "id": "button_text",
          "label": "Button Text"
        },
        {
          "type": "url",
          "id": "button_link",
          "label": "Button Link"
        }
      ]
    }
  ],
  "max_blocks": 10
}
```

**Rendering Blocks:**
```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when 'text_block' %}
      <div class="text-block">
        {{ block.settings.content }}
        {% if block.settings.image %}
          <img src="{{ block.settings.image | image_url }}" alt="">
        {% endif %}
      </div>
    {% when 'button_block' %}
      <a href="{{ block.settings.button_link }}" class="button">
        {{ block.settings.button_text }}
      </a>
  {% endcase %}
{% endfor %}
```

**Block Limits:**
- Set `max_blocks` in schema to limit block count
- Useful for performance and UX

### Section Presets

**What Are Presets?**
- Pre-configured section instances
- Appear in Theme Customizer "Add section" menu
- Can have default settings and blocks
- Makes sections easier to use

**Preset Example:**
```liquid
{
  "presets": [
    {
      "name": "My Section",
      "settings": {
        "heading": "Default Heading",
        "heading_size": "large"
      },
      "blocks": [
        {
          "type": "text_block",
          "settings": {
            "content": "<p>Default content</p>"
          }
        }
      ]
    },
    {
      "name": "My Section - With Image",
      "settings": {
        "heading": "Image Section",
        "show_image": true
      }
    }
  ]
}
```

### Section Best Practices

**Performance:**
- Minimize Liquid logic in sections
- Use `limit` for loops
- Cache expensive operations
- Lazy load images below the fold

**Accessibility:**
- Use semantic HTML
- Include proper ARIA labels
- Ensure keyboard navigation works
- Test with screen readers

**Responsive Design:**
- Test on mobile, tablet, desktop
- Use mobile-first CSS
- Test touch interactions
- Verify text readability

**Maintainability:**
- Use descriptive class names
- Comment complex logic
- Follow existing patterns
- Document custom sections

---

## Snippet Development

### Understanding Snippets

**What Are Snippets?**
- Reusable Liquid components
- Included via `{% render %}` tag
- Can accept parameters
- Shared across sections and templates

**When to Use Snippets:**
- Repeated markup across multiple sections
- Complex components used in multiple places
- Product cards, buttons, icons
- Navigation menus, forms

### Creating Snippets

**1. Create the File:**
```bash
touch snippets/my-snippet.liquid
```

**2. Add Content:**
```liquid
{% comment %}
  Renders: [Description of what this snippet does]
  
  Accepts:
  - product: {Product} Product object
  - show_price: {Boolean} Whether to show price
  - class: {String} Additional CSS classes
{% endcomment %}

<div class="product-card {{ class }}">
  <a href="{{ product.url }}">
    <img src="{{ product.featured_image | image_url }}" alt="{{ product.title }}">
    <h3>{{ product.title }}</h3>
    {% if show_price %}
      <p class="price">{{ product.price | money }}</p>
    {% endif %}
  </a>
</div>
```

**3. Render the Snippet:**
```liquid
{% render 'my-snippet', 
  product: product, 
  show_price: true, 
  class: 'featured-product' 
%}
```

### Snippet Parameters

**Passing Parameters:**
- Parameters are passed as key-value pairs
- Parameters are available as variables in snippet
- Use descriptive parameter names
- Document parameters in comments

**Default Values:**
```liquid
{% assign show_price = show_price | default: true %}
{% assign class = class | default: '' %}
```

**Parameter Types:**
- Objects: `product`, `collection`, `page`
- Strings: `heading`, `class`, `id`
- Numbers: `limit`, `index`
- Booleans: `show_price`, `is_featured`
- Arrays: `items`, `links`

### Common Snippet Patterns

**Product Card Snippet:**
```liquid
{% comment %}
  Renders: Product card component
  
  Accepts:
  - product: {Product} Product object
  - show_vendor: {Boolean} Show vendor name
  - image_ratio: {String} Image aspect ratio
{% endcomment %}

<div class="card-product">
  <a href="{{ product.url }}">
    {% render 'image', 
      image: product.featured_image, 
      ratio: image_ratio 
    %}
    <div class="card-product__info">
      <h3>{{ product.title }}</h3>
      {% if show_vendor %}
        <p class="vendor">{{ product.vendor }}</p>
      {% endif %}
      <p class="price">{{ product.price | money }}</p>
    </div>
  </a>
</div>
```

**Icon Snippet:**
```liquid
{% comment %}
  Renders: SVG icon
  
  Accepts:
  - icon: {String} Icon name (e.g., 'cart', 'search')
  - class: {String} Additional CSS classes
{% endcomment %}

<svg class="icon icon-{{ icon }} {{ class }}" aria-hidden="true">
  <use href="#icon-{{ icon }}"></use>
</svg>
```

### Snippet Best Practices

**Performance:**
- Use `{% render %}` not `{% include %}` (render caches snippets)
- Minimize snippet nesting (avoid deep nesting)
- Cache expensive operations
- Use `limit` for loops in snippets

**Reusability:**
- Make snippets flexible with parameters
- Avoid hardcoded values
- Support optional features via parameters
- Document all parameters

**Maintainability:**
- Use descriptive snippet names
- Comment complex logic
- Follow naming conventions
- Group related snippets

**Error Handling:**
```liquid
{% if product %}
  {% render 'product-card', product: product %}
{% else %}
  <p>Product not found</p>
{% endif %}
```

---

## Navigation Implementation

### Header Navigation

**File:** `sections/header.liquid`

**Menu Settings:**
- `section.settings.menu` - Main desktop menu
- `section.settings.mobile_menu` - Mobile menu (optional, falls back to main menu)
- `section.settings.utility_menu` - Utility menu (optional)

**Code Reference:**
```liquid
{% if section.settings.menu != blank %}
  {% render 'menu-list', 
    menu: section.settings.menu, 
    blocks: section.blocks 
  %}
{% endif %}
```

**Mobile Menu:**
```liquid
{% render 'menu-header-drawer', 
  menu: section.settings.mobile_menu | default: section.settings.menu, 
  blocks: section.blocks, 
  secondary_menu: section.settings.utility_menu 
%}
```

**Menu Access in Liquid:**
- Menu object: `section.settings.menu`
- Menu links: `section.settings.menu.links`
- Link properties: `link.url`, `link.title`, `link.active`, `link.links` (children)

### Footer Navigation

**File:** `sections/footer.liquid`

**Footer Menus:** Block-based (not direct settings)

**Code Reference:**
```liquid
{% for block in section.blocks %}
  {% if block.type == 'link_list' %}
    {% if block.settings.menu != blank %}
      <div class="footer-menu">
        <h3>{{ block.settings.heading }}</h3>
        <ul>
          {% for link in block.settings.menu.links %}
            <li>
              <a href="{{ link.url }}">{{ link.title }}</a>
            </li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
  {% endif %}
{% endfor %}
```

**Copyright Menu:**
```liquid
{% if section.settings.copyright_menu %}
  <div class="footer-copyright">
    {% for link in section.settings.copyright_menu.links %}
      <a href="{{ link.url }}">{{ link.title }}</a>
    {% endfor %}
  </div>
{% endif %}
```

### Announcement Bar Menu

**File:** `sections/announcement-bar.liquid`

**Code Reference:**
```liquid
{% if section.settings.announcement_menu != blank %}
  <div class="announcement-bar-menu">
    {% for link in section.settings.announcement_menu.links %}
      <a href="{{ link.url }}">{{ link.title }}</a>
    {% endfor %}
  </div>
{% endif %}
```

### Menu Snippet System

**Main Menu Snippet:** `snippets/menu-list.liquid`

**Usage:**
```liquid
{% render 'menu-list', 
  menu: link_list, 
  blocks: blocks 
%}
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
            {% render 'menu-list-promos', 
              menu_item: link, 
              blocks: blocks, 
              mobile: false, 
              promo_slots: promoCount 
            %}
          </div>
        </details>
      </details-disclosure>
  {%- endcase -%}
{%- endfor -%}
```

**Key Features:**
- Promo slots calculated based on child link count
  - Max 3 links = 1 promo slot
  - Fewer links = 2 promo slots
- Supports nested menu items (grandchild links)
- Special handling for "BLANK" menu items (used for spacing)
- "Shop All" link option via `block.settings.parent_menu_item_all`
- Grandchild links support "::" separator for title/subtitle display

**Menu Item Formatting:**
- Use "::" separator in grandchild link titles for title/subtitle display
- Example: "Product Name::Subtitle text"
- Renders as: 
  ```html
  <span class="header__menu-item--grandchild__title">Product Name</span>
  <span class="header__menu-item--grandchild__subtext">Subtitle text</span>
  ```

**Important Notes:**
- Menu item name matching is **case-sensitive**
- Block must be added to header section in Theme Customizer
- Promo content is rendered via `menu-list-promos` snippet
- Mega menu only appears on desktop (mobile uses drawer menu)

### Navigation Best Practices

**Menu Structure:**
- Keep menu hierarchy shallow (max 3 levels)
- Use descriptive menu item names
- Test menu on all devices
- Ensure all links work correctly

**Performance:**
- Minimize menu items for better performance
- Use lazy loading for mega menu content
- Cache menu structure when possible

**Accessibility:**
- Use semantic HTML (`<nav>`, `<ul>`, `<li>`)
- Include ARIA labels for screen readers
- Ensure keyboard navigation works
- Test with screen readers

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

**Important:** 
- All pages with `cql.rx_microsite = true` share the same header/footer configuration
- Changes to microsite header/footer affect all microsite pages
- Microsite pages can use any page template
- Microsite header/footer are configured separately from main site

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

**Assets:**
- `assets/insole-finder-2.css` - Quiz styling
- `assets/insole-finder-2.js` - Quiz functionality

**Setup:**
1. Create page in Shopify Admin
2. Set Template suffix: `insole-finder-2`
3. Configure `insole-finder-2` section in Theme Customizer
4. Quiz logic handled by custom app (contact Born West for changes)

**Important:** 
- Work with Michael Sullivan, Heather Allerdice-Gerow, and Born West team for quiz logic changes
- Theme changes only affect UI/styling
- Quiz results link to specific product pages automatically
- Quiz uses custom app API for recommendations

### Product Compare Section

**Purpose:** Display product comparison table on product pages using metafield-based product references.

**Section:** `sections/product-compare.liquid`

**Implementation:**

The section uses the `cql.comparison_products` metafield (list.product_reference) to display comparison products:

```liquid
{%- assign metafields = product.metafields.cql -%}
{%- assign compare_products = metafields.comparison_products.value -%}

{%- if compare_products != blank -%}
  <div class="product-compare">
    <h2>{{ section.settings.heading }}</h2>
    <table class="compare-table">
      {%- tablerow compare_product in compare_products limit: 3 -%}
        {% render 'product-compare-column', 
          compare_product: compare_product, 
          hide_product_prices: section.settings.hide_product_prices 
        %}
      {%- endtablerow -%}
    </table>
  </div>
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

**CSS:** `assets/section-product-compare.css`

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
  {% assign diagram = template_object.metafields.custom.feature_diagram.value | default: template_object.metafields.cql.feature_diagram.value %}
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

**CSS:** `assets/section-feature-diagram.css`

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

**CSS:** `assets/section-shop-the-look.css`

### UGC (User-Generated Content) Section

**Purpose:** Display user-generated content feeds.

**Section:** `sections/ugc.liquid`

**Features:**
- Social media feed integration
- Content moderation
- Responsive grid layout
- Yotpo UGC integration

**Usage:**
1. Add `ugc` section to collection or page template
2. Configure UGC source (Yotpo, Instagram, etc.)
3. Set display settings (grid columns, image size)

**CSS:** `assets/section-ugc.css`

---

## Multi-Store Development

### Development Workflow

**Standard Process:**
1. **Make changes on one store** (usually US first)
2. **Test thoroughly** on staging
3. **Export/replicate to other stores**
4. **Test on each store** after deployment

**Why US First?**
- US store has most comprehensive template set (123 templates)
- Most features are developed/tested on US first
- US store is primary reference for other stores

### Theme Sync Methods

**Method 1: Manual File Copy**
- Copy changed files between stores
- Update via Shopify CLI or admin
- **Pros:** Selective, controlled
- **Cons:** Time-consuming, error-prone

**Method 2: Matrixify**
- Export theme from one store
- Import to other stores
- Preserves settings
- **Pros:** Complete sync, preserves settings
- **Cons:** Requires Matrixify app, may overwrite store-specific changes

**Method 3: Shopify CLI**
```bash
# Push to multiple stores
shopify theme push --store superfeetww
shopify theme push --store superfeet-ca
shopify theme push --store superfeet-uk
```
- **Pros:** Fast, reliable
- **Cons:** Pushes entire theme, may overwrite store-specific changes

**Recommended Approach:**
- Use Shopify CLI for new sections/snippets (shared code)
- Use manual copy for store-specific templates
- Use Matrixify for complete theme syncs (major updates)

### Store-Specific Considerations

**Settings Differences:**
- Review `config/settings_data.json` per store
- Pricing, shipping, tax configurations differ
- Language/localization settings vary
- Store-specific branding may differ

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
- Shipping zones differ per store

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
- Test all three markets when making template changes

**Testing:**
- Test UK market (transactional functionality)
- Test EU market (brochure-only, no buy buttons)
- Test AU market (brochure-only, no buy buttons)
- Verify SearchSpring filtering works per market
- Verify prices are hidden for EU/AU markets

### Multi-Store Deployment Checklist

**Before Deployment:**
- [ ] Test changes on US store staging
- [ ] Verify responsive design works
- [ ] Check browser console for errors
- [ ] Test all affected pages/templates
- [ ] Verify integrations still work

**During Deployment:**
- [ ] Push to US store staging first
- [ ] Test on US staging thoroughly
- [ ] Push to US live (if approved)
- [ ] Push to Canada store staging
- [ ] Test on Canada staging
- [ ] Push to Canada live
- [ ] Push to UK store staging
- [ ] Test UK market (transactional)
- [ ] Test EU market (brochure)
- [ ] Test AU market (brochure)
- [ ] Push to UK live

**After Deployment:**
- [ ] Monitor for errors (browser console, Shopify logs)
- [ ] Verify functionality on all stores
- [ ] Check performance metrics
- [ ] Document any store-specific issues

---

## Common Development Tasks

### Adding a New Section

**Scenario:** Create a new "Testimonials" section for product pages.

**Steps:**
1. **Create Section File:**
   ```bash
   touch sections/testimonials.liquid
   ```

2. **Add Basic Structure:**
   ```liquid
   <div class="section testimonials">
     <div class="page-width">
       <h2>{{ section.settings.heading }}</h2>
       {% for block in section.blocks %}
         <div class="testimonial">
           <p>{{ block.settings.quote }}</p>
           <p class="author">- {{ block.settings.author }}</p>
         </div>
       {% endfor %}
     </div>
   </div>

   {% schema %}
   {
     "name": "Testimonials",
     "settings": [
       {
         "type": "text",
         "id": "heading",
         "label": "Heading",
         "default": "Customer Testimonials"
       }
     ],
     "blocks": [
       {
         "type": "testimonial",
         "name": "Testimonial",
         "settings": [
           {
             "type": "richtext",
             "id": "quote",
             "label": "Quote"
           },
           {
             "type": "text",
             "id": "author",
             "label": "Author"
           }
         ]
       }
     ],
     "presets": [
       {
         "name": "Testimonials"
       }
     ]
   }
   {% endschema %}
   ```

3. **Add CSS:**
   ```bash
   touch assets/section-testimonials.css
   ```
   ```css
   .testimonials {
     padding: 4rem 0;
   }
   .testimonial {
     margin-bottom: 2rem;
   }
   ```

4. **Load CSS in Section:**
   ```liquid
   {{ 'section-testimonials.css' | asset_url | stylesheet_tag }}
   ```

5. **Add to Template:**
   - Via Theme Customizer: Add section to product template
   - Or in template JSON: Add to sections object

6. **Test:**
   - Verify section appears correctly
   - Test responsive design
   - Add testimonials via blocks

### Modifying an Existing Section

**Scenario:** Add a "Show More" button to the product description section.

**Steps:**
1. **Locate Section File:**
   - Find section in `sections/` directory
   - Or search for section name in templates

2. **Backup First:**
   ```bash
   cp sections/main-product.liquid sections/main-product.liquid.backup
   ```

3. **Make Changes:**
   - Add new setting for "Show More" toggle
   - Add JavaScript for expand/collapse functionality
   - Add CSS for styling

4. **Test on Staging:**
   - Push to staging theme
   - Test functionality
   - Verify no regressions

5. **Deploy:**
   - Push to live after testing

**Important:** Always test on staging before live!

### Debugging a Broken Template

**Scenario:** Product page not displaying correctly.

**Debugging Steps:**

1. **Check Browser Console:**
   - Open DevTools (F12)
   - Check Console tab for JavaScript errors
   - Check Network tab for failed requests

2. **Check Liquid Syntax:**
   ```bash
   # Use Shopify CLI to check for syntax errors
   shopify theme check --store superfeetww
   ```

3. **Verify Template Assignment:**
   - Check product has correct template suffix
   - Verify template file exists
   - Check template JSON is valid

4. **Check Section Settings:**
   - Verify sections are configured correctly
   - Check for missing required settings
   - Verify blocks are set up correctly

5. **Test with Default Template:**
   - Remove template suffix from product
   - See if default template works
   - This helps isolate the issue

6. **Check Metafields:**
   - Verify required metafields exist
   - Check metafield values are correct
   - Use `{% if %}` checks for optional metafields

### Adding a New Product Template

**Scenario:** Create a template for bundle products with special layout.

**Steps:**
1. **Copy Existing Template:**
   ```bash
   cp templates/product.json templates/product.bundle.json
   ```

2. **Modify Template:**
   - Add/remove sections as needed
   - Reorder sections
   - Configure section settings

3. **Test Template:**
   - Assign to a test product
   - Verify layout works correctly
   - Test responsive design

4. **Deploy:**
   - Push to staging
   - Test thoroughly
   - Deploy to live

### Fixing a Menu Issue

**Scenario:** Menu not displaying on mobile.

**Debugging Steps:**
1. **Check Menu Assignment:**
   - Verify menu is assigned in Theme Customizer
   - Check `section.settings.mobile_menu` or `section.settings.menu`

2. **Check Menu Exists:**
   - Go to Shopify Admin → Navigation
   - Verify menu exists and has links

3. **Check Snippet:**
   - Verify `menu-header-drawer.liquid` is being called
   - Check snippet for errors

4. **Check CSS:**
   - Verify mobile menu styles are loading
   - Check for CSS conflicts
   - Test with browser DevTools

5. **Check JavaScript:**
   - Verify menu drawer JavaScript is loading
   - Check for JavaScript errors
   - Test menu toggle functionality

### Common Gotchas

**1. Template Suffix Case Sensitivity:**
- Template suffixes are case-sensitive
- `product.Bundle.json` ≠ `product.bundle.json`
- Always use lowercase with hyphens

**2. Metafield Namespace:**
- Always check metafield namespace
- `cql.*` vs `custom.*` vs `yotpo.*`
- Wrong namespace = metafield not found

**3. Section Block Limits:**
- Check `max_blocks` in section schema
- Users can't add more blocks than limit
- Increase limit if needed

**4. Market Context Files:**
- UK store market context files override base templates
- Changes to base template may not affect EU/AU markets
- Always test all three markets

**5. SearchSpring Incompatibility:**
- Essential A/B Testing app conflicts with SearchSpring
- Don't run A/B tests on SearchSpring-powered collections
- Use native template for A/B testing

**6. Snippet Caching:**
- Use `{% render %}` not `{% include %}`
- Render caches snippets (better performance)
- Include is deprecated

**7. Multi-Store Template Differences:**
- Templates may not exist in all stores
- Check template exists before assigning
- Create template in other stores if needed

---

## Code Patterns & Best Practices

### Liquid Best Practices

**Performance:**
```liquid
{% comment %} Good: Use limit {% endcomment %}
{% for product in collection.products limit: 4 %}
  {% render 'card-product', product: product %}
{% endfor %}

{% comment %} Good: Use render {% endcomment %}
{% render 'product-card', product: product %}

{% comment %} Avoid: Nested loops {% endcomment %}
{% for collection in collections %}
  {% for product in collection.products %}
    <!-- Avoid this pattern - very slow -->
  {% endfor %}
{% endfor %}

{% comment %} Better: Flatten the data {% endcomment %}
{% assign all_products = collections.featured.products %}
{% for product in all_products limit: 20 %}
  <!-- Process products -->
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

{% comment %} HTML content (if trusted) {% endcomment %}
{{ trusted_html | strip_html }}
```

**Metafield Access:**
```liquid
{% comment %} Always check if metafield exists {% endcomment %}
{% if product.metafields.custom.field_name %}
  {{ product.metafields.custom.field_name }}
{% endif %}

{% comment %} JSON metafields {% endcomment %}
{% assign json_data = product.metafields.custom.json_field | parse_json %}
{% if json_data.property %}
  {{ json_data.property }}
{% endif %}

{% comment %} List metafields {% endcomment %}
{% assign product_list = product.metafields.cql.comparison_products.value %}
{% if product_list != blank %}
  {% for item in product_list %}
    {{ item.title }}
  {% endfor %}
{% endif %}
```

### Superfeet-Specific Metafield Patterns

**CQL Namespace Metafields:**

Superfeet uses the `cql.*` namespace extensively for product data. See [Data Guide](./data-guide.md) for complete reference.

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
  <span class="badge">Vegan</span>
{% endif %}

{% comment %} Product reference list {% endcomment %}
{% for comparison_product in product.metafields.cql.comparison_products.value %}
  {% render 'card-product', product: comparison_product %}
{% endfor %}

{% comment %} Metaobject reference {% endcomment %}
{% assign faq_group = product.metafields.cql.faq_group.value %}
{% if faq_group %}
  <h3>{{ faq_group.title }}</h3>
  {% for faq in faq_group.faqs.value %}
    <div class="faq">
      <h4>{{ faq.question }}</h4>
      <p>{{ faq.answer }}</p>
    </div>
  {% endfor %}
{% endif %}
```

**Page Metafields:**

RX microsite detection:
```liquid
{% assign isMicrositePage = false %}
{% if page.metafields.cql.rx_microsite != blank and page.metafields.cql.rx_microsite != false %}
  {% assign isMicrositePage = true %}
{% endif %}
```

**Best Practices:**
- Always check metafield existence before accessing
- Use `.value` for list and metaobject references
- Check boolean metafields with `{% if %}` before display
- Use namespace consistently (`cql.*` for product data, `custom.*` for custom features)
- Reference [Data Guide](./data-guide.md) for complete metafield documentation

### JavaScript Best Practices

**Namespace Pattern:**
```javascript
(function() {
  'use strict';
  
  const SuperfeetComponent = {
    init: function() {
      this.cacheElements();
      this.bindEvents();
    },
    
    cacheElements: function() {
      this.$container = document.querySelector('.component-container');
      this.$button = this.$container.querySelector('.component-button');
    },
    
    bindEvents: function() {
      if (this.$button) {
        this.$button.addEventListener('click', this.handleClick.bind(this));
      }
    },
    
    handleClick: function(e) {
      e.preventDefault();
      // Handle click
    }
  };
  
  document.addEventListener('DOMContentLoaded', function() {
    SuperfeetComponent.init();
  });
})();
```

**Performance:**
- Minimize DOM queries (cache selectors)
- Use event delegation for dynamic content
- Defer non-critical scripts
- Use `requestAnimationFrame` for animations
- Avoid blocking the main thread

**Event Delegation Example:**
```javascript
// Instead of binding to each element
document.querySelectorAll('.product-card').forEach(card => {
  card.addEventListener('click', handleClick);
});

// Use event delegation
document.addEventListener('click', function(e) {
  if (e.target.closest('.product-card')) {
    handleClick(e);
  }
});
```

### CSS Best Practices

**Component-Based Styling:**
```css
/* Component */
.component-name {
  /* Base styles */
}

/* Element */
.component-name__element {
  /* Element styles */
}

/* Modifier */
.component-name--modifier {
  /* Modified styles */
}

/* State */
.component-name.is-active {
  /* Active state */
}
```

**Responsive Design:**
```css
/* Mobile-first approach */
.component {
  /* Mobile styles */
}

@media screen and (min-width: 750px) {
  .component {
    /* Tablet styles */
  }
}

@media screen and (min-width: 990px) {
  .component {
    /* Desktop styles */
  }
}
```

**Performance:**
- Minimize CSS specificity
- Avoid deep nesting (max 3 levels)
- Use CSS custom properties for theming
- Minimize use of `!important`
- Use `will-change` sparingly

---

## Integration Management

### SearchSpring Integration

**Purpose:** Enhanced product search, filtering, and recommendations beyond Shopify's default search.

**Section:** `sections/searchspring-recommendations.liquid`  
**Snippet:** `snippets/searchspring-script.liquid`

**Key Implementation Details:**

The SearchSpring integration uses a global `window.Resources` namespace for configuration:

```javascript
window.Resources.searchspring = {
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
};
```

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

**Important:** 
- Essential A/B Testing app is **incompatible** with SearchSpring
- Section automatically hides if cookies disabled or DoNotTrack enabled
- Regional filtering ensures correct products show for UK/EU/AU markets
- See [Integrations Guide](./integrations.md) for operational details

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
    if (!targetNode) return;
    
    const observer = new MutationObserver(function(mutations) {
      // Re-run event listeners on recharge app mutation
      // Customizations apply after Recharge loads
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

**Important:** 
- Recharge JavaScript loads asynchronously
- Mutation observers ensure customizations apply after Recharge loads
- Bundle layout template controlled by `rc_bundles.layout_template` metafield
- See [Integrations Guide](./integrations.md) for operational details

### Elevar Tracking

**Implementation:**
- Elevar JavaScript loaded in `layout/theme.liquid`
- Server-side event tracking
- Connected to GA4, Facebook Pixel, Klaviyo, Google Ads

**Code Location:** Check `layout/theme.liquid` for Elevar includes

**Important:** 
- Don't remove Elevar scripts - they're critical for conversion tracking
- Elevar handles server-side event tracking (more reliable than client-side)
- All marketing channel tracking depends on Elevar
- Contact marketing team before modifying Elevar configuration

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
- See [Integrations Guide](./integrations.md) for operational details

**Integration Reference:**
For complete integration documentation including setup, configuration, and troubleshooting, see the [Integrations Guide](./integrations.md).

---

## Troubleshooting & Debugging

### Debugging Workflow

**Step 1: Identify the Problem**
- What's not working?
- When did it stop working?
- What changed recently?
- Does it affect all stores or just one?

**Step 2: Check Browser Console**
- Open DevTools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for failed requests
- Look for 404 errors (missing files)

**Step 3: Check Liquid Syntax**
```bash
# Use Shopify CLI to check for syntax errors
shopify theme check --store superfeetww
```

**Step 4: Verify File Changes**
- Check if files were saved correctly
- Verify file paths are correct
- Check for typos in file names

**Step 5: Test on Staging**
- Push changes to staging theme
- Test functionality on staging
- Compare staging vs live behavior

### Common Issues

**Theme Not Loading:**
1. Check Shopify status page (status.shopify.com)
2. Verify theme is published
3. Check browser console for errors
4. Clear browser cache
5. Check `theme.liquid` for syntax errors
6. Verify all required files exist

**Menu Not Displaying:**
1. Verify menu is assigned in Theme Customizer
2. Check menu exists in Shopify Admin → Navigation
3. Verify menu has links
4. Check `sections/header.liquid` or `sections/footer.liquid`
5. Verify menu snippet is being called
6. Check for JavaScript errors preventing menu render

**Template Not Working:**
1. Verify template suffix is correct (case-sensitive)
2. Check template file exists in theme
3. Verify template JSON is valid
4. Check for missing sections referenced in template
5. Test with default template to isolate issue

**Metafields Not Displaying:**
1. Verify metafield exists on product/page/collection
2. Check metafield namespace is correct
3. Verify metafield value is set
4. Check Liquid code for typos
5. Use `{% if %}` check before accessing metafield

**Tracking Not Working:**
1. Check Elevar dashboard for event status
2. Verify Elevar script is loading (browser console)
3. Check destination connections (GA4, Facebook, etc.)
4. Review server-side event logs
5. Check for ad blockers interfering
6. Verify customer consent (Osano) is not blocking

**Performance Issues:**
1. Check Calibreapp for metrics
2. Run PageSpeed Insights
3. Check for large images/assets
4. Review JavaScript bundle size
5. Check for render-blocking resources
6. Verify lazy loading is working
7. Check for excessive DOM queries

**SearchSpring Not Working:**
1. Check SearchSpring dashboard for sync status
2. Verify collection has `searchspring` template suffix
3. Check SearchSpring script is loading
4. Verify `window.Resources.searchspring` is defined
5. Check browser console for SearchSpring errors
6. Verify correct SearchSpring instance is selected

**Recharge Widget Not Showing:**
1. Verify product has correct template suffix (`recharge-bundle` or `subscription`)
2. Check Recharge dashboard for product configuration
3. Verify Recharge app is active
4. Check for JavaScript errors in console
5. Verify mutation observer is working
6. Check Recharge script is loading

### Debugging Tools

**Browser DevTools:**
- **Console:** JavaScript errors, log messages
- **Network:** Failed requests, slow resources
- **Elements:** Inspect HTML, test CSS
- **Sources:** Debug JavaScript, set breakpoints
- **Application:** Check localStorage, cookies, cache

**Shopify CLI:**
```bash
# Check theme for errors
shopify theme check --store superfeetww

# List themes
shopify theme list --store superfeetww

# Get theme info
shopify theme info --store superfeetww
```

**Shopify Admin:**
- **Settings → Notifications:** System notifications
- **Online Store → Themes:** Theme management
- **Online Store → Navigation:** Menu management
- **Settings → Apps:** App status and configuration

**Theme Inspector:**
- Use Shopify Theme Inspector browser extension
- Inspect section settings
- Debug Liquid variables
- View theme structure

**Liquid Debugging:**
```liquid
{% comment %} Output variable for debugging {% endcomment %}
{{ product.metafields.cql.arch_height }}

{% comment %} Check if variable exists {% endcomment %}
{% if product.metafields.cql.arch_height %}
  <!-- Variable exists -->
{% else %}
  <!-- Variable doesn't exist -->
{% endif %}

{% comment %} Output entire object (be careful with large objects) {% endcomment %}
{{ product | json }}
```

### Performance Debugging

**Identify Performance Issues:**
1. Run PageSpeed Insights
2. Check Core Web Vitals (LCP, CLS, INP)
3. Use browser Performance tab
4. Check Network tab for slow requests
5. Review JavaScript execution time

**Common Performance Problems:**
- Large images not optimized
- Too many HTTP requests
- Render-blocking resources
- Excessive JavaScript execution
- Large CSS files
- Unoptimized fonts

**Performance Optimization:**
- Optimize images (WebP, compression)
- Minimize HTTP requests (combine files)
- Defer non-critical JavaScript
- Use lazy loading for images
- Minimize CSS (remove unused styles)
- Use font subsetting

### Getting Help

**When to Ask for Help:**
- Issue persists after troubleshooting
- Error is unclear or confusing
- Change affects multiple stores
- Integration is broken
- Performance issue can't be identified

**Information to Provide:**
- What you're trying to do
- What's not working
- Error messages (screenshot or copy)
- Browser console errors
- Steps to reproduce
- What you've already tried

**Resources:**
- [Shopify Theme Development Docs](https://shopify.dev/themes)
- [Liquid Documentation](https://shopify.dev/api/liquid)
- [Theme Architecture Guide](./theme-architecture.md)
- [Integrations Guide](./integrations.md)
- [Data Guide](./data-guide.md)

---

## Additional Resources

### Documentation
- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md) - Complete theme structure and organization
- **Data Guide:** [data-guide.md](./data-guide.md) - Complete metafields reference
- **Integrations:** [integrations.md](./integrations.md) - App integration details
- **Business User Guide:** [business-user-guide.md](./business-user-guide.md) - Non-technical workflows

### External Resources
- **Shopify Theme Development:** https://shopify.dev/themes
- **Liquid Documentation:** https://shopify.dev/api/liquid
- **Shopify CLI:** https://shopify.dev/themes/tools/cli
- **Shopify Community:** https://community.shopify.com/

### Tools
- **Shopify CLI:** Theme development and deployment
- **Theme Inspector:** Browser extension for debugging
- **PageSpeed Insights:** Performance testing
- **Browser DevTools:** Built-in debugging tools

---

*Last Updated: Based on theme exports from November 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

