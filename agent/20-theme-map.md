# Theme Architecture Mental Model

## Theme Export Root Path

**Note:** Theme code files are not in this repository (excluded via `.gitignore`). The theme structure follows standard Shopify theme organization. Access theme files via Shopify CLI or theme export.

**Standard Theme Structure:**
```
theme-root/
├── layout/theme.liquid          # Main layout (entry point)
├── sections/                     # 103 section files (US Mar 2026 export)
├── snippets/                     # 144 snippet files
├── templates/                    # 135 JSON templates (US store, recursive)
├── assets/                       # CSS, JS, fonts, images
└── config/                       # Theme settings
```

## Primary Entrypoints

### 1. Main Layout: `layout/theme.liquid`

**Purpose:** Base structure for all pages  
**Key Features:**
- Loads header group (`{% sections 'header-group' %}`)
- Loads footer group (`{% sections 'footer-group' %}`)
- Handles microsite detection via `page.metafields.cql.rx_microsite`
- Routes to microsite header/footer if applicable
- Loads global JavaScript config (`snippets/cql-head-content.liquid`)

**Reference:** `docs/theme-architecture-v2.md` - Layout System

### 2. Header System: `sections/header-group.json`

**Purpose:** Defines header structure  
**Components:**
- Announcement bar section
- Header section (navigation, logo, cart)
- Mobile menu handling

**Reference:** `docs/theme-architecture-v2.md` - Section Architecture

### 3. Footer System: `sections/footer-group.json`

**Purpose:** Defines footer structure  
**Components:**
- Footer links and navigation
- Social media links
- Store information

**Reference:** `docs/theme-architecture-v2.md` - Section Architecture

### 4. Template System: `templates/*.json`

**Purpose:** Page templates for products, collections, pages  
**Key Templates:**
- `product.json` - Base product template
- `product.bundle.json` - Recharge bundle products
- `product.subscription.json` - Recharge subscription products
- `collection.json` - Base collection template
- `collection.searchspring.json` - SearchSpring-powered collections
- `page.json` - Base page template

**Template Suffix Rules:**
- Products: `bundle`, `subscription`, `insole-finder`
- Collections: `searchspring`
- Pages: Custom suffixes for special layouts

**Reference:** `docs/theme-architecture-v2.md` - Template System

## Major Custom Systems

### 1. Insole Finder Quiz

**Layout:** `layout/theme.insole-finder.liquid`  
**Purpose:** Custom product recommendation tool  
**Integration:** Built by Born West & Superfeet (separate app)  
**Features:**
- Multi-step quiz flow
- Product recommendations based on answers
- Custom header/footer (microsite style)

**Reference:** `docs/theme-architecture-v2.md` - Custom Features

### 2. SearchSpring Integration

**Template Suffix:** `searchspring`  
**Asset:** `assets/searchspring.bundle.js` (store-specific)  
**Purpose:** Enhanced search and filtering  
**Usage:**
- Assign `searchspring` template suffix to collections
- SearchSpring replaces default Shopify search
- Store-specific bundle configuration

**Reference:** `docs/integrations.md` - SearchSpring

### 3. Recharge Integration

**Template Suffixes:** `bundle`, `subscription`  
**Purpose:** Product bundles and subscriptions  
**Usage:**
- Assign `recharge-bundle` suffix for bundles
- Assign `subscription` suffix for subscriptions
- Configuration in Recharge dashboard (not Shopify)

**Reference:** `docs/integrations.md` - Recharge Subscriptions

### 4. Multi-Region Architecture

**Build System:** Processes shared codebase → generates store-specific themes  
**Stores:**
- US: `superfeetww` (reference store)
- Canada: `superfeet-ca` (bilingual)
- UK: `superfeet-uk` (UK/EU/AU markets)

**Store-Specific Files:**
- `config/settings_data.json` - Store settings
- `assets/searchspring.bundle.js` - SearchSpring config
- `templates/` - Template assignments
- `locales/` - Language files

**Reference:** `docs/theme-architecture-v2.md` - Multi-Region Architecture

### 5. UK Store Markets

**Market Context Files:**
- `product.context.eu.json` - EU market (brochure-only)
- `product.context.au.json` - AU market (brochure-only)
- Base `product.json` - UK market (transactional)

**Purpose:** Disable transactional elements for EU/AU markets  
**Implementation:** Template blocks disabled via context files

**Reference:** `docs/theme-architecture-v2.md` - UK Store Markets Architecture

## Template Suffix Rules

### Product Templates

- **Default:** `product.json` - Standard product page
- **Bundle:** `product.bundle.json` or `product.recharge-bundle.json` - Recharge bundle products
- **Subscription:** `product.subscription.json` - Recharge subscription products
- **Insole Finder:** `product.insole-finder.json` - Insole Finder quiz results

### Collection Templates

- **Default:** `collection.json` - Standard collection page
- **SearchSpring:** `collection.searchspring.json` - SearchSpring-powered search/filtering

### Page Templates

- **Default:** `page.json` - Standard page template
- **Custom:** Various suffixes for special page layouts

**Reference:** `docs/technical-user-guide-v2.md` - Template System

## Where to Start for Changes

### Making a Text Change

1. **Identify the section:** Check template → find section name
2. **Locate section file:** `sections/{section-name}.liquid`
3. **Edit text:** Find text string, make change
4. **Test:** Use `shopify theme dev --store superfeetww`

### Adding a New Section

1. **Create section file:** `sections/{new-section}.liquid`
2. **Add section CSS:** `assets/section-{new-section}.css` (if needed)
3. **Add to template:** Edit template JSON, add section
4. **Test:** Verify section appears and functions correctly

### Modifying Navigation

1. **Header navigation:** `sections/header.liquid` or `sections/header-group.json`
2. **Footer navigation:** `sections/footer.liquid` or `sections/footer-group.json`
3. **Menu structure:** Managed in Shopify Admin → Navigation
4. **Menu rendering:** Check snippets that render menus

### Changing Product Page Layout

1. **Identify template:** Check product's template suffix
2. **Edit template:** `templates/product.json` or `templates/product.{suffix}.json`
3. **Modify sections:** Add/remove/reorder sections in template JSON
4. **Test:** Verify changes on product page

### Multi-Store Considerations

1. **Develop on US store first:** `superfeetww` is the reference store
2. **Use build system:** Generate other store themes from shared codebase
3. **Test store-specific:** Verify SearchSpring config, settings, templates
4. **Check market context:** For UK store, verify EU/AU market behavior

**Reference:** `docs/technical-user-guide-v2.md` - Multi-Store Development

## File Organization Patterns

### CSS Architecture

- `assets/base.css` - Base styles, resets, typography
- `assets/component-*.css` - Component styles (50+ files)
- `assets/section-*.css` - Section styles (40+ files)
- `assets/template-*.css` - Template styles

### JavaScript Architecture

- `assets/global.js` - Global initialization
- `assets/constants.js` - Constants and config
- `assets/pubsub.js` - Event system
- `assets/component-*.js` - Component JavaScript
- `assets/{feature}.js` - Feature-specific JS

### Section Dependencies

- Sections load their own CSS/JS assets
- Sections use snippets for reusable markup
- Sections can reference other sections (via blocks)

### Snippet Dependencies

- Snippets are independent (no dependencies on other snippets)
- Snippets can accept parameters from sections
- Snippets render HTML, no CSS/JS of their own

**Reference:** `docs/theme-architecture-v2.md` - Asset Architecture
