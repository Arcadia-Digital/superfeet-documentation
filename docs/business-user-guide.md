# Business User Guide

**Superfeet Multi-Region Shopify Plus Platform**

Superfeet-specific customizations and workflows for managing the eCommerce platform.

**Who This Guide Is For:** This guide is written for team members with Shopify Plus experience who manage day-to-day operations, content, and merchandising. It focuses on what you need to know to work effectively in Shopify Admin and Theme Customizer, without requiring technical development knowledge.

**Key Difference from Other Stores:** Superfeet operates **three independent Shopify stores** (US, Canada, UK) rather than a single store with multiple markets. This means many changes need to be made separately in each store. The UK store also uses Shopify Markets to serve EU and Australia as brochure-only sites (non-transactional).

---

## Table of Contents

1. [Menu-to-Section Mapping](#menu-to-section-mapping)
2. [RX Microsite Setup](#rx-microsite-setup)
3. [Insole Finder Quiz](#insole-finder-quiz)
4. [Product Templates & Customizations](#product-templates--customizations)
5. [Collection Templates & SearchSpring](#collection-templates--searchspring)
6. [Custom Sections](#custom-sections)
7. [Image & Media Specifications](#image--media-specifications)
8. [Multi-Store Considerations](#multi-store-considerations)
9. [Managing AU & EU Markets in Theme Customizer](#managing-au--eu-markets-in-theme-customizer)
10. [Troubleshooting](#troubleshooting)

---

## Menu-to-Section Mapping

### Complete Menu Assignment Reference

This table shows exactly which menu setting controls which visible element on the site.

| Visible Element                | Where to Assign Menu               | Theme Customizer Path                                    | Desktop Display      | Mobile Display            |
| ------------------------------ | ---------------------------------- | -------------------------------------------------------- | -------------------- | ------------------------- |
| **Header - Main Desktop Menu** | Direct menu setting                | Theme Customizer → Header → Menu                         | Horizontal menu bar  | Hidden (uses mobile menu) |
| **Header - Mobile Menu**       | Direct menu setting                | Theme Customizer → Header → Mobile menu                  | Hidden               | Hamburger menu drawer     |
| **Header - Utility Menu**      | Direct menu setting                | Theme Customizer → Header → Utility menu                 | Secondary menu items | Included in mobile drawer |
| **Announcement Bar Menu**      | Direct menu setting                | Theme Customizer → Announcement bar → Menu               | Top bar links        | Hidden                    |
| **Footer - Menu Block 1**      | Footer block (add Link list block) | Theme Customizer → Footer → Add block → Link list → Menu | Footer column        | Accordion                 |
| **Footer - Menu Block 2**      | Footer block (add Link list block) | Theme Customizer → Footer → Add block → Link list → Menu | Footer column        | Accordion                 |
| **Footer - Menu Block 3+**     | Footer block (add Link list block) | Theme Customizer → Footer → Add block → Link list → Menu | Footer column        | Accordion                 |
| **Footer - Copyright Menu**    | Direct menu setting                | Theme Customizer → Footer → Copyright → Menu             | Bottom bar links     | Bottom bar links          |

### Key Points

- **Header menus** use direct settings (not blocks)
- **Footer menus** use blocks (add multiple menu blocks)
- **Mobile vs Desktop** behavior differs for header and footer
- **Announcement bar** menu only shows on desktop

---

## RX Microsite Setup

The RX microsite is a custom implementation that uses different header and footer groups for specific pages, creating a separate branded experience within the main Superfeet site.

### How It Works

When a page has the `cql.rx_microsite` metafield set to `true`, the theme automatically:
- Loads `header-group-microsite` instead of `header-group`
- Loads `footer-group-microsite` instead of `footer-group`
- Applies microsite-specific styling and navigation

### Setting Up an RX Microsite Page

**Step 1: Create the Page**
1. Go to **Online Store → Pages** in Shopify Admin
2. Create a new page or edit existing page
3. Add page content as needed

**Step 2: Enable RX Microsite**
1. On the page edit screen, scroll to **Metafields** section
2. Find or create metafield: **Namespace and key:** `cql.rx_microsite`
3. Set **Type:** Boolean
4. Set **Value:** `true`
5. Save the page

**Step 3: Configure Microsite Header/Footer (if needed)**
1. Go to **Theme Customizer**
2. Navigate to **Header Group RX** section (for microsite header)
3. Navigate to **Footer Group RX** section (for microsite footer)
4. Configure menus, logo, and settings specific to RX microsite

### RX Microsite Configuration

**Header Group RX Settings:**
- **Menu:** `rx-main-menu` (default)
- **Mobile menu:** `rx-main-menu-mobile` (default)
- **Utility menu:** `rx-utility-menu-mobile` (default)
- **Search:** Disabled by default
- **Store locator:** Disabled by default
- **Demo button:** "Request Information" (links to contact page)

**Footer Group RX Settings:**
- **Social media:** Uses "microsite" social links
- **Company info:** RX-specific contact information
- **Country/Language selectors:** Disabled by default
- **Payment icons:** Disabled by default

### RX Microsite Menus

Create these menus in **Online Store → Navigation:**
- `rx-main-menu` - Main desktop navigation
- `rx-main-menu-mobile` - Mobile navigation
- `rx-utility-menu-mobile` - Mobile utility menu
- `footer-about-rx` - Footer about menu
- `announcement-bar-menu` - Announcement bar menu (if used)

### Important Notes

- RX microsite pages use the same theme but different header/footer groups
- All RX pages share the same header/footer configuration
- Changes to Header Group RX or Footer Group RX affect all RX microsite pages
- RX microsite can be used for other branded experiences (not just RX)

---

## Insole Finder Quiz

The Insole Finder is a custom quiz application that guides customers to the right insole product.

### How It Works

The Insole Finder uses a special page template that provides a custom experience separate from the main site layout. When you assign the `insole-finder-2` template to a page, it automatically uses a different header and footer design optimized for the quiz experience.

### Setting Up Insole Finder Pages

**Step 1: Create Insole Finder Page**
1. Go to **Online Store → Pages**
2. Create new page or edit existing Insole Finder page
3. Set **Template suffix:** `insole-finder-2`

**Step 2: Configure Insole Finder Section**
1. Go to **Theme Customizer**
2. Select the Insole Finder page
3. Find **Insole Finder 2** section
4. Configure quiz settings, questions, and product recommendations

**Step 3: Link to Insole Finder**
- Link from navigation menus
- Link from product pages
- Link from homepage or landing pages

### Insole Finder Template Details

**Template Suffix:** `insole-finder-2`

**What This Means:**
- When you set the template suffix to `insole-finder-2`, the page uses a special layout
- This layout uses a simplified header and footer (similar to the RX microsite)
- The quiz section appears in the Theme Customizer when you're editing an Insole Finder page

### Important Notes

- Insole Finder uses the microsite header/footer layout
- Quiz logic is handled by custom app (Insole Finder Quiz app)
- Product recommendations are generated based on quiz answers
- Quiz results link to specific product pages
- Work with Michael Sullivan, Heather Allerdice-Gerow, and the team at Born West to make changes to the Insole Finder.

---

## Product Templates & Customizations

### Recharge Bundle Products

**Template:** `product.recharge-bundle.json`

**Setup:**
1. Go to **Products** → Select product
2. Scroll to **Search engine listing**
3. Set **Template suffix:** `recharge-bundle`
4. Save product

**Features:**
- Recharge bundle widget displays on product page
- Customers can customize bundle contents
- Bundle pricing and options managed in Recharge app
- ReCharge bundle documentation - https://support.getrecharge.com/hc/en-us/sections/6981308041623-Bundles

**Recharge Bundle Widget Settings:**
- Theme color: `#00c09e` (default Superfeet green)
- Items per row: 1 (mobile), 3 (desktop)
- These settings are pre-configured in the template - you don't need to change them unless working with a developer

### Subscription Products

**Template:** `product.subscription.json`

**Setup:**
1. Set **Template suffix:** `subscription`
2. Configure subscription options in Recharge app
3. Subscription widget displays on product page

Note: Subscriptions are available but have not been activated. Once SF brand and eComm teams have aligned on an initial subscription offer, rely on the support team at ReCharge, ReCharge documentation - https://support.getrecharge.com/hc/en-us/categories/360000578374-Subscription-Management, and your development partner. 

### Product-Specific Templates

Superfeet has **31 product-specific templates** for custom product page layouts. Each template provides a unique layout and section configuration optimized for specific product types.

**Complete List of Product Templates:**

1. **`all-purpose-cushion`** - All-Purpose Cushion product template
2. **`all-purpose-wide-fit`** - All-Purpose Wide Fit product template
3. **`alternate`** - Alternate product layout template
4. **`ap-support-low-arch`** - All-Purpose Support Low Arch product template
5. **`apma-approved`** - APMA approved products template
6. **`casual-pain-relief`** - Casual Pain Relief product template
7. **`casual-women-s-easy-fit`** - Casual Women's Easy Fit product template
8. **`everyday-pressure-relief`** - Everyday Pressure Relief product template
9. **`fixed-bundle`** - Fixed bundle products template
10. **`gift-card`** - Gift card product template
11. **`hike-cushion`** - Hike Cushion product template
12. **`hike-support`** - Hike Support product template
13. **`hike-women-s-support`** - Hike Women's Support product template
14. **`hockey-cushion`** - Hockey Cushion product template
15. **`hockey-performance`** - Hockey Performance product template
16. **`me3d-max`** - ME3D Max product template
17. **`me3d`** - ME3D product template
18. **`recharge-bundle`** - Recharge bundle products template (includes Recharge bundle widget)
19. **`run-cushion-low`** - Run Cushion Low product template
20. **`run-cushion`** - Run Cushion product template
21. **`run-pacer-elite`** - Run Pacer Elite product template
22. **`run-pain-relief`** - Run Pain Relief product template
23. **`run-support-high-med-low`** - Run Support High/Med/Low product template
24. **`run-support-v1`** - Run Support V1 product template
25. **`run-women-s-support`** - Run Women's Support product template
26. **`sport-ultralight`** - Sport Ultralight product template
27. **`subscription`** - Subscription products template (includes Recharge subscription widget)
28. **`winter-support`** - Winter Support product template
29. **`work-cushion`** - Work Cushion product template
30. **`work-memory-foam`** - Work Memory Foam product template
31. **`work-slim-fit`** - Work Slim Fit product template

**Usage:**
1. Go to **Products** → Select product
2. Scroll to **Search engine listing** section
3. Find **Template suffix** field
4. Enter template suffix (e.g., `all-purpose-cushion` for `product.all-purpose-cushion.json`)
5. Click **Save**

**Important Notes:**
- Template suffix is **case-sensitive** and must match exactly (no spaces, use hyphens)
- If you enter a template suffix that doesn't exist, the page will use the default product template instead
- Templates control which sections and features appear on the product page
- Some templates (like `recharge-bundle` and `subscription`) include special app widgets that only work with those templates
- **Multi-Store Note:** Templates are store-specific. If a template exists in the US store but not in Canada or UK, you'll need to have it created in those stores before you can use it

### Product Metafields for Display

Complete reference of all product metafields, their purpose, and where they display on the storefront.

#### CQL Namespace (`cql.*`)

**Product Information Metafields:**

- **`cql.arch_height`** [single_line_text_field]
  - **Purpose:** Arch height specification (e.g., "Medium", "High", "Low/Medium/High")
  - **Display:** Product page - Icon data rows section (with icon from metaobject)
  - **Usage:** Used for product filtering and comparison features

- **`cql.insole_thickness`** [single_line_text_field]
  - **Purpose:** Insole thickness specification (e.g., "Mid", "Thin")
  - **Display:** Product page - Icon data rows section (with icon from metaobject)
  - **Usage:** Product specification display

- **`cql.product_gender`** [single_line_text_field]
  - **Purpose:** Product gender category (e.g., "Unisex", "Men's", "Women's")
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Internal categorization and filtering

- **`cql.product_family`** [single_line_text_field]
  - **Purpose:** Product family grouping (e.g., "All-Purpose", "Run Support")
  - **Display:** Not directly visible on storefront (used for grouping)
  - **Usage:** Internal organization and related product logic

- **`cql.underfoot_cushioning`** [single_line_text_field]
  - **Purpose:** Cushioning level specification (e.g., "Soft", "Medium")
  - **Display:** Product page - Icon data rows section (with icon from metaobject)
  - **Usage:** Product specification display

- **`cql.target_use_activity`** [single_line_text_field]
  - **Purpose:** Target activity/use case (e.g., "All-Purpose", "Running")
  - **Display:** Not directly visible on storefront (used for filtering)
  - **Usage:** Internal categorization

- **`cql.fits_best_in`** [single_line_text_field]
  - **Purpose:** Fit description (e.g., "Roomy to moderate fitting footwear with removable insoles")
  - **Display:** Product page - Main product section (as metafield block with label "Fits Best In")
  - **Usage:** Helps customers understand shoe compatibility

- **`cql.insole_technology`** [single_line_text_field]
  - **Purpose:** Technology description (e.g., "A.C.T. (Adaptive Comfort Technology)")
  - **Display:** Not directly visible on storefront (used for internal reference)
  - **Usage:** Product information reference

- **`cql.insole_heel_cup_depth`** [single_line_text_field]
  - **Purpose:** Heel cup depth specification (e.g., "Max")
  - **Display:** Not directly visible on storefront (used for internal reference)
  - **Usage:** Product specification reference

- **`cql.previously_named`** [single_line_text_field]
  - **Purpose:** Previous product name (for rebranded products)
  - **Display:** Product page - Main product section (as metafield block with label "Previously Named")
  - **Usage:** Helps customers find products they knew by previous name

- **`cql.badge`** [single_line_text_field]
  - **Purpose:** Badge text (e.g., "Best Seller", "New", "Limited Edition")
  - **Display:** Product page - Product media gallery (badge overlay on product images)
  - **Usage:** Highlights special product attributes

- **`cql.best_for`** [single_line_text_field]
  - **Purpose:** Best use case description (e.g., "Everyday footwear, athletic shoes, active use")
  - **Display:** Product page - Main product section (as metafield block with label "Best For")
  - **Usage:** Helps customers understand product use cases

- **`cql.short_description`** [multi_line_text_field]
  - **Purpose:** Short product description (formatted text)
  - **Display:** Product page - Main product section (as "short_description" block, replaces standard description)
  - **Special Usage:** For Recharge bundles, displays as "Includes:" list when `rc_bundles.layout_template` is set
  - **Usage:** Primary product description on product pages

- **`cql.discount_summary`** [single_line_text_field]
  - **Purpose:** Discount summary text
  - **Display:** Not directly visible on storefront (used for internal reference)
  - **Usage:** Discount information reference

- **`cql.bundle_type`** [single_line_text_field]
  - **Purpose:** Bundle type identifier
  - **Display:** Not directly visible on storefront (used for internal logic)
  - **Usage:** Determines bundle behavior and display

**Size Information Metafields:**

- **`cql.kid_sizes`** [single_line_text_field]
  - **Purpose:** Kids size range
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Size filtering and product organization

- **`cql.men_sizes`** [single_line_text_field]
  - **Purpose:** Men's size range (e.g., "5.5 - 7, 7.5 - 9, 9.5 - 11, 11.5 - 13")
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Size filtering and product organization

- **`cql.women_sizes`** [single_line_text_field]
  - **Purpose:** Women's size range (e.g., "4.5 - 6, 6.5 - 8, 8.5 - 10, 10.5 - 12, 12.5 - 14")
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Size filtering and product organization

- **`cql.skate_sizes`** [single_line_text_field]
  - **Purpose:** Skate size range
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Size filtering for skate-specific products

**Product Attributes:**

- **`cql.vegan`** [boolean]
  - **Purpose:** Vegan product indicator
  - **Display:** Not directly visible on storefront (used for filtering)
  - **Usage:** Product filtering and categorization

- **`cql.latex_free`** [boolean]
  - **Purpose:** Latex-free product indicator
  - **Display:** Not directly visible on storefront (used for filtering)
  - **Usage:** Product filtering and categorization

- **`cql.low_stock_threshold`** [number_integer]
  - **Purpose:** Low stock threshold number
  - **Display:** Product page - Low stock message block (displays when inventory falls below threshold)
  - **Usage:** Triggers low stock warning message on product pages
  - **Note:** Message text configured in product section block settings

**Product Relationships:**

- **`cql.comparison_products`** [list.product_reference]
  - **Purpose:** Related/comparison products for product compare features
  - **Display:** Product compare sections (used to populate comparison tables)
  - **Usage:** Powers product comparison functionality

- **`cql.shop_for`** [single_line_text_field]
  - **Purpose:** Shop for category (e.g., "Men, Women, Kids")
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Product categorization and filtering

- **`cql.addon_product`** [product_reference]
  - **Purpose:** Add-on product for upsell functionality
  - **Display:** Product page - Add-on form section (when addon_product block is present)
  - **Usage:** Displays add-on product selection form

- **`cql.associated_products`** [list.product_reference]
  - **Purpose:** Associated products for cross-sell functionality
  - **Display:** Product page - Associated products section (when associated_products block is present)
  - **Usage:** Displays related product recommendations

**Metaobject References:**

- **`cql.faq_group`** [metaobject_reference]
  - **Purpose:** FAQ group metaobject for reusable FAQ content
  - **Display:** Collection pages - FAQ sections (when faq_group_handle is configured)
  - **Usage:** Powers FAQ sections on collection pages
  - **Example:** `product_feature_groups.ap-cushion`

- **`cql.arch_height_info`** [metaobject_reference]
  - **Purpose:** Arch height information and icon reference
  - **Display:** Product page - Icon data rows section (provides icon image and tooltip)
  - **Usage:** Displays arch height icon and tooltip information
  - **Example:** `arch_height_icons.mid`

- **`cql.thickness_info`** [metaobject_reference]
  - **Purpose:** Thickness information and icon reference
  - **Display:** Product page - Icon data rows section (provides icon image and tooltip)
  - **Usage:** Displays thickness icon and tooltip information
  - **Example:** `thickness_icons.medium`

- **`cql.cushion_info`** [metaobject_reference]
  - **Purpose:** Cushion information and icon reference
  - **Display:** Product page - Icon data rows section (provides icon image and tooltip)
  - **Usage:** Displays cushion icon and tooltip information
  - **Example:** `cushion_icons.soft`

**Media:**

- **`cql.image_with_feature`** [file_reference]
  - **Purpose:** Image with feature overlay
  - **Display:** Product page - Image with features section (when used in template)
  - **Usage:** Displays product image with feature annotations

#### Custom Namespace (`custom.*`)

- **`custom.feature_diagram`** [metaobject_reference]
  - **Purpose:** Feature diagram metaobject for interactive product diagrams
  - **Display:** Product/landing pages - Feature diagram section
  - **Usage:** Powers interactive feature diagram sections

- **`custom.insole_finder_header_text`** [single_line_text_field]
  - **Purpose:** Insole Finder header text
  - **Display:** Insole Finder quiz pages
  - **Usage:** Custom header text for Insole Finder experience

- **`custom.hsa_fsa_eligible`** [boolean]
  - **Purpose:** HSA/FSA eligibility indicator
  - **Display:** Not directly visible on storefront (used for filtering/grouping)
  - **Usage:** Product categorization for HSA/FSA eligible products

#### SEO Namespace (`seo.*`)

- **`seo_title`** [single_line_text_field]
  - **Purpose:** Custom SEO title (overrides default product title)
  - **Display:** Browser tab title and search engine results
  - **Usage:** SEO optimization for search engines

- **`seo_desc`** [single_line_text_field]
  - **Purpose:** Custom SEO description (overrides default product description)
  - **Display:** Search engine results (meta description)
  - **Usage:** SEO optimization for search engines

- **`seo.hidden`** [number_integer]
  - **Purpose:** Hide from search (0 = visible, 1 = hidden)
  - **Display:** Controls search engine indexing
  - **Usage:** Prevents products from appearing in search results

#### Reviews Namespace (`reviews.*`)

- **`reviews.rating_count`** [number_integer]
  - **Purpose:** Review count
  - **Display:** Not directly visible (used for internal logic)
  - **Usage:** Review system integration

- **`reviews.rating`** [rating]
  - **Purpose:** Average rating
  - **Display:** Not directly visible (Yotpo handles review display)
  - **Usage:** Review system integration

#### Yotpo Namespace (`yotpo.*`)

- **`yotpo.reviews_average`** [single_line_text_field]
  - **Purpose:** Average review rating from Yotpo
  - **Display:** Product pages - Yotpo review widgets
  - **Usage:** Powers Yotpo review display

- **`yotpo.reviews_count`** [single_line_text_field]
  - **Purpose:** Review count from Yotpo
  - **Display:** Product pages - Yotpo review widgets
  - **Usage:** Powers Yotpo review display

- **`yotpo.richsnippetshtml`** [single_line_text_field]
  - **Purpose:** Rich snippets HTML for structured data
  - **Display:** Search engine results (structured data)
  - **Usage:** SEO structured data for search engines

#### Google Shopping Namespace (`mm-google-shopping.*`)

- **`mm-google-shopping.custom_product`** [boolean]
  - **Purpose:** Custom product flag for Google Merchant Center
  - **Display:** Not visible on storefront (used for feed generation)
  - **Usage:** Google Shopping feed configuration

- **`mm-google-shopping.google_product_category`** [string]
  - **Purpose:** Google product category for Merchant Center
  - **Display:** Not visible on storefront (used for feed generation)
  - **Usage:** Google Shopping feed categorization

#### Facebook Namespace (`mc-facebook.*`)

- **`mc-facebook.google_product_category`** [string]
  - **Purpose:** Facebook product category for catalog
  - **Display:** Not visible on storefront (used for catalog generation)
  - **Usage:** Facebook catalog configuration

#### Recharge Namespace (`rc_bundles.*`)

- **`rc_bundles.layout_template`** [single_line_text_field]
  - **Purpose:** Bundle layout template identifier
  - **Display:** Product page - Affects bundle widget display and short_description formatting
  - **Usage:** Controls Recharge bundle widget behavior and display
  - **Note:** When set, `cql.short_description` displays as "Includes:" list format

#### Standard Metafields

- **`title_tag`** [string]
  - **Purpose:** Page title tag
  - **Display:** Browser tab title
  - **Usage:** Page title override

- **`description_tag`** [string]
  - **Purpose:** Meta description tag
  - **Display:** Search engine results (meta description)
  - **Usage:** SEO meta description override

---

## Collection Templates & SearchSpring

### SearchSpring Collections

**Template:** `collection.searchspring.json`

**Setup:**
1. Go to **Collections** → Select collection
2. Scroll to **Search engine listing**
3. Set **Template suffix:** `searchspring`
4. Save collection

**Features:**
- Enhanced search and filtering via SearchSpring
- Product recommendations
- Advanced faceted search
- SearchSpring JavaScript SDK loaded automatically

**Important:**
- SearchSpring replaces default Shopify search on these collections
- Essential A/B Testing app is **incompatible** with SearchSpring
- SearchSpring configuration managed in SearchSpring dashboard

### Native Shopify Collections

**Template:** `collection.native.json`

**Usage:**
- Standard Shopify collection functionality
- No SearchSpring integration
- Use for simple collections without advanced search

### Collection-Specific Templates

Superfeet has **28 collection-specific templates** for custom collection page layouts. Each template provides unique section configurations optimized for specific collection types and use cases.

**Complete List of Collection Templates:**

1. **`all-purpose-collection`** - All-Purpose collection template
2. **`bundle-collection`** - Bundle collection template
3. **`casual-dress-collection`** - Casual/Dress collection template
4. **`category-landing`** - Category landing page template
5. **`cleat-sports-collection`** - Cleat Sports collection template
6. **`court-sports-collection`** - Court Sports collection template
7. **`ea-9zkhwx`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
8. **`ea-aklu3g`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
9. **`ea-f4vvc0`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
10. **`ea-fk7mj0`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
11. **`ea-u2m7v1`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
12. **`ea-z40jd9`** - Essential A/B Testing template (created by Essential A/B Testing app for A/B testing)
13. **`fit-train-collection`** - Fitness/Training collection template
14. **`golf-collection`** - Golf collection template
15. **`hiking-collection`** - Hiking collection template
16. **`hockey-skates-collection`** - Hockey Skates collection template
17. **`holiday-gift-guide`** - Holiday Gift Guide collection template
18. **`native`** - Native Shopify collection template (standard Shopify functionality, no SearchSpring)
19. **`pain-relief-collection`** - Pain Relief collection template
20. **`qr-code-promotion-page`** - QR Code Promotion Page collection template
21. **`racquet-sports-collection`** - Racquet Sports collection template
22. **`run-support-sale`** - Run Support Sale collection template
23. **`run-support-sale-2`** - Run Support Sale 2 collection template
24. **`searchspring`** - SearchSpring-powered collection template (enhanced search and filtering)
25. **`ski-snowboard-collection`** - Ski/Snowboard collection template
26. **`tier-2-collection`** - Tier 2 collection template
27. **`walking-collection`** - Walking collection template
28. **`work-collection`** - Work collection template

**Usage:**
1. Go to **Collections** → Select collection
2. Scroll to **Search engine listing** section
3. Find **Template suffix** field
4. Enter template suffix (e.g., `searchspring` for `collection.searchspring.json`)
5. Click **Save**

**Important Notes:**
- Template suffix is **case-sensitive** and must match exactly (no spaces, use hyphens)
- If you enter a template suffix that doesn't exist, the collection will use the default collection template instead
- **SearchSpring template** (`searchspring`): This replaces the default Shopify search with SearchSpring's enhanced search and filtering. Use this for collections where you want advanced search capabilities.
- **Native template** (`native`): This uses standard Shopify collection functionality without SearchSpring. Use this for simple collections that don't need advanced search.
- Templates control which sections appear on the collection page (banners, FAQs, product grids, etc.)
- **Multi-Store Note:** Templates are store-specific. If a template exists in the US store but not in Canada or UK, you'll need to have it created in those stores before you can use it
- **EA-prefixed templates** (e.g., `ea-9zkhwx`): These are automatically created by the Essential A/B Testing app when running A/B tests. **Do not manually assign these** - the app manages them. If you see one assigned to a collection, it means an A/B test is running on that collection.

---

## Custom Sections

### Product Compare Sections

**Two Versions Available:**

1. **Product Compare** (`product-compare.liquid`)
   - Simple product comparison table
   - Configure products via section settings
   - Manual product selection

2. **Product Compare Enhanced** (`product-compare-enhanced.liquid`)
   - Uses metaobjects for product line data
   - Dynamic parameter comparison
   - Visual parameter scales
   - **Requires:** Metaobject with product line entries

**Product Compare Enhanced Setup:**
1. Create metaobject in Shopify Admin
2. Add product line entries with parameters
3. Add **Product Compare Enhanced** section to page
4. Select metaobject in section settings
5. Configure parameter labels and options

### Feature Diagram Section

**Section:** `feature-diagram.liquid`

**Usage:**
- Interactive diagram with feature points
- Clickable feature icons with descriptions
- Carousel support for multiple features
- Used on RX landing pages and product pages

**Setup:**
1. Add **Feature Diagram** section to page
2. Upload diagram base image
3. Add feature carousel blocks
4. Position icons on diagram (vertical/horizontal position)
5. Configure feature descriptions and icons

### Shop the Look Section

**Section:** `shop-the-look.liquid`

**Usage:**
- Display multiple products in lifestyle context
- Product hotspots on lifestyle image
- Click hotspots to view product details
- Used on collection and product pages

### SearchSpring Recommendations

**Section:** `searchspring-recommendations.liquid`

**Usage:**
- Product recommendations powered by SearchSpring
- Displays on product pages, collection pages, cart page
- Automatically hides if cookies disabled or doNotTrack enabled

**Setup:**
1. Add **SearchSpring Recommendations** section
2. Configure display settings
3. SearchSpring handles product selection automatically

### UGC (User-Generated Content) Section

**Section:** `ugc.liquid`

**Usage:**
- Display Yotpo UGC galleries
- Product reviews and customer photos
- Used on product and collection pages

**Setup:**
1. Add **UGC** section
2. Configure gallery ID (from Yotpo)
3. Yotpo handles content display

---

## Image & Media Specifications

For comprehensive image and media specifications for all components, sections, and templates, see the dedicated [Image & Media Specifications Guide](./image-media-specifications.md).

**Quick Reference:**
- **Product Images:** 2048×2048px (square), WebP format, < 500KB
- **Image Banners:** 1400×700px (desktop), 800×1200px (mobile), WebP format
- **Product Cards:** 1200×1200px (square), WebP format, < 500KB
- **Logos:** 360×180px (2:1 ratio), SVG or PNG with transparency
- **Icons:** 80×80px (square), SVG format preferred

**Important:**
- All product images must be **square (1:1 aspect ratio)** for consistent grid display
- Always provide separate mobile images for banners and hero sections
- Use WebP format for optimal performance (Shopify auto-generates from JPG/PNG)
- Optimize all images before upload to meet file size targets

See [Image & Media Specifications Guide](./image-media-specifications.md) for complete specifications, responsive breakpoints, video requirements, and optimization guidelines.

---

## Multi-Store Considerations

### Independent Stores

Superfeet operates **three independent transactional Shopify stores**. This is different from many Shopify Plus setups that use a single store with multiple markets. Here's what this means for you:

| Store      | Handle         | Domain          | Primary Market                    | Currency    | What You Need to Know    |
| ---------- | -------------- | --------------- | --------------------------------- | ----------- | ------------------------ |
| **US**     | `superfeetww`  | superfeet.com   | United States                     | USD         | Main store, most content |
| **Canada** | `superfeet-ca` | superfeet.ca    | Canada (English/French bilingual) | CAD         | Separate admin login     |
| **UK**     | `superfeet-uk` | superfeet.co.uk | UK, EU, Australia                 | GBP/EUR/AUD | Uses Markets for EU/AU   |

**Important:** Each store has its own Shopify Admin login. You'll need to log into each store separately to make changes. Changes made in one store do NOT automatically appear in the other stores.

**UK Store Special Case:** The UK store (`superfeet-uk`) uses Shopify Markets to serve three regions:
- **UK Market:** Full transactional store (shows prices, buy buttons, cart)
- **EU Market:** Brochure-only (hides prices, buy buttons, cart - customers can't purchase)
- **AU Market:** Brochure-only (hides prices, buy buttons, cart - customers can't purchase)

EU and AU are **markets within the same store**, not separate stores. This means you edit EU/AU content in the same Shopify Admin, but you need to select the market context in Theme Customizer. See [Managing AU & EU Markets in Theme Customizer](#managing-au--eu-markets-in-theme-customizer) for details.

### Store-Specific Data Differences

**Product Counts (US Mar 2026 Matrixify; CA/UK from prior regional exports unless noted):**
- **US:** 64 products (Matrixify `EVERYTHING-Export-forAI_2026-03-31_154533`)
- **Canada:** 45 products
- **UK:** 57 products (last from regional export in repo—not refreshed with Mar 2026 US run)

**Collection Counts:**
- **US:** 44 collections (23 smart, 21 custom)
- **Canada:** 32 collections (20 smart, 12 custom)
- **UK:** 32 collections (21 smart, 11 custom)

**Content Counts:**
- **US:** 67 pages, 168 blog posts, 277 metaobjects
- **Canada:** 45 pages, 142 blog posts, 247 metaobjects
- **UK:** 44 pages, 139 blog posts, 236 metaobjects

**Template Counts:**
- **US:** 135 templates (March 2026 US theme export)
- **Canada:** 75 templates (`code/superfeet-ca-theme`, Oct 2025 export in repo)
- **UK:** 84 templates (`code/superfeet-uk-theme`, Oct 2025 export in repo)

**Note:** Template counts differ due to store-specific template assignments and regional customizations. Product, collection, and content counts reflect regional inventory and content strategies.

### Changes Across Stores

**Manual Replication Required:**
- Theme code changes (sections, snippets, templates)
- Navigation menu updates
- Page content updates
- Product template assignments
- Collection template assignments
- Product data and inventory (managed per store)

**Store-Specific Configurations:**
- Header/footer menus (different per store - 15 menus per store)
- Product availability (inventory managed independently per store)
- Pricing (currency per store: USD, CAD, GBP/EUR/AUD)
- Apps (some apps US-only, others installed across all stores)
- Language/localization settings (CA: English/French, UK: English)
- Tax and shipping configurations (regional requirements)

### Regional Considerations

**Canada Store:**
- Bilingual support (English/French)
- CAD currency
- Canadian tax and shipping rules
- Fewer products (45 vs 64 in US; UK count not refreshed Mar 2026)

**UK Store:**
- Serves UK, EU, and Australia markets
- Multi-currency support (GBP, EUR, AUD)
- Regional shipping and tax compliance
- Similar product count to US store historically (verify; US 64 as of Mar 2026 Matrixify)

**US Store:**
- Primary transactional store
- Largest content library (168 blog posts, 67 pages in US Mar 2026 export)
- Most templates (135 templates in US export)
- USD currency

---

## Managing AU & EU Markets in Theme Customizer

### Understanding Markets in the UK Store

The **UK store** (`superfeet-uk`) uses **Shopify Markets** to serve three different regions:
- **UK Market:** United Kingdom (transactional - shows buy buttons, prices, cart)
- **EU Market:** European Union (brochure-only - hides buy buttons, prices, cart)
- **AU Market:** Australia (brochure-only - hides buy buttons, prices, cart)

EU and AU are **markets within the same Shopify store**, not separate stores. This allows the UK store to display different content and functionality based on which market a customer is viewing.

### Why This Is Confusing

Even experienced Shopify admins find market-specific template editing confusing because:

1. **Markets vs. Stores:** Markets are not separate stores - they're different views of the same store
2. **Market Context in Customizer:** The Theme Customizer requires you to **select a market context** before editing templates
3. **Template Inheritance:** Market-specific templates inherit from base templates, so changes can affect multiple markets
4. **Hidden by Default:** Market context selection is not obvious - it's in a dropdown that many users miss

### How Market-Specific Templates Work

**Template Structure:**

The UK store uses **market context files** that override base templates:

- **Base Template:** `product.json` (used for UK market - shows all blocks including price, buy buttons)
- **EU Market Override:** `product.context.eu.json` (inherits from `product.json` but disables transactional blocks)
- **AU Market Override:** `product.context.au.json` (inherits from `product.json` but disables transactional blocks)

**Example: Default Product Template**

The default product template (`product.json`) includes these blocks for UK customers:
- Price block
- Variant picker
- Buy buttons
- Product description
- Other content blocks

For EU and AU markets, the market context files (`product.context.eu.json` and `product.context.au.json`) **disable** these blocks:
- `price` → `disabled: true`
- `variant_picker` → `disabled: true`
- `buy_buttons` → `disabled: true`

This allows EU and AU customers to see product information but not purchase directly, while UK customers see the full transactional experience.

### Editing Templates for Specific Markets

**Step 1: Open Theme Customizer**

1. Go to **Online Store → Themes** in Shopify Admin
2. Click **Customize** on the active theme
3. Theme Customizer opens

**Step 2: Select Market Context**

1. In Theme Customizer, look for the **market selector** dropdown (usually at the top of the left sidebar)
2. Click the dropdown to see available markets:
   - **UK** (default)
   - **EU**
   - **AU**
3. **Select the market** you want to edit (e.g., "EU" or "AU")

**Important:** If you don't select a market context, you're editing the **default template** (UK market). Always verify which market is selected before making changes.

**Step 3: Navigate to Template**

1. Use the page selector at the top of Theme Customizer
2. Navigate to the template you want to edit (e.g., **Products → Default product**)
3. The template now shows the **market-specific version**

**Step 4: Edit Blocks and Sections**

1. Edit blocks and sections as needed
2. **Disable blocks** for brochure markets (EU/AU):
   - Click on a block (e.g., "Price", "Buy buttons")
   - Toggle the block **off** (disable it)
   - This hides the block for that specific market
3. **Enable/configure blocks** as needed
4. Changes apply **only to the selected market**

**Step 5: Save and Publish**

1. Click **Save** to save changes
2. Click **Publish** to make changes live
3. Changes apply only to the market you selected

### Example: Editing Product Template for EU Market

**Scenario:** You want to hide the buy button and price for EU customers but keep them for UK customers.

**Steps:**

1. Open Theme Customizer
2. **Select "EU" from market dropdown** (critical step!)
3. Navigate to **Products → Default product**
4. Find the **"Buy buttons"** block in the left sidebar
5. Click on the block
6. Toggle the block **off** (disable it)
7. Find the **"Price"** block
8. Toggle the block **off** (disable it)
9. **Save** and **Publish**

**Result:**
- EU customers: No buy button, no price (brochure view)
- UK customers: Buy button and price still visible (transactional view)
- AU customers: Unchanged (unless you also edit AU market context)

### Market-Specific Template Files

The UK store has market context files for several templates:

**Product Templates:**
- `product.context.eu.json` - EU market product template
- `product.context.au.json` - AU market product template
- `product.apma-approved.context.eu.json` - EU market APMA template
- `product.apma-approved.context.au.json` - AU market APMA template

**Collection Templates:**
- `collection.context.eu.json` - EU market collection template
- `collection.context.au.json` - AU market collection template

**Page Templates:**
- `index.context.eu.json` - EU market homepage
- `index.context.au.json` - AU market homepage
- `index.context.uk.json` - UK market homepage
- `404.context.eu.json` - EU market 404 page
- `404.context.au.json` - AU market 404 page

**Note:** If a market context file doesn't exist, that market uses the base template (same as UK).

### Best Practices

1. **Always Check Market Context:**
   - Verify which market is selected in Theme Customizer before editing
   - The market selector shows at the top of the left sidebar
   - Default is usually "UK" - don't assume you're editing the right market

2. **Test Across Markets:**
   - After making changes, preview the page for each market
   - Use the market selector to switch between UK, EU, and AU views
   - Verify that brochure markets (EU/AU) hide transactional elements

3. **Document Market-Specific Changes:**
   - Note which blocks are disabled for which markets
   - Keep track of market-specific content differences
   - Document any custom blocks added for specific markets

4. **Understand Template Inheritance:**
   - Market context files inherit from base templates
   - Changes to base templates may affect all markets
   - Market-specific overrides only affect that market

### Common Mistakes

**Mistake 1:** Editing UK template when you meant to edit EU/AU
- **Solution:** Always select the correct market from the dropdown before editing

**Mistake 2:** Assuming changes apply to all markets
- **Solution:** Market-specific changes only apply to the selected market. Edit each market separately if needed.

**Mistake 3:** Not disabling transactional blocks for brochure markets
- **Solution:** For EU/AU markets, disable price, variant_picker, and buy_buttons blocks to create brochure experience

**Mistake 4:** Forgetting to publish changes
- **Solution:** Always click **Publish** after making market-specific changes, not just Save

### Troubleshooting Market-Specific Issues

**Problem:** Changes not appearing for specific market
- **Solution:** Verify you selected the correct market context before editing and clicked **Publish**

**Problem:** Can't find market selector in Theme Customizer
- **Solution:** Market selector is in the left sidebar at the top. If you don't see it, you may not have market-specific templates configured for that page type.

**Problem:** Buy buttons showing on EU/AU sites
- **Solution:** Edit the product template for EU or AU market context and disable the "Buy buttons" block

**Problem:** Want to add market-specific content
- **Solution:** Edit the template for that specific market context and add/enable blocks as needed. Changes only apply to that market.

---

## Troubleshooting

### RX Microsite Not Loading

**Problem:** Page has `cql.rx_microsite` metafield set but still shows regular header/footer.

**Solution:**
1. Verify metafield is set to `true` (boolean, not text "true")
2. Check metafield namespace/key: `cql.rx_microsite`
3. Clear browser cache
4. Verify page is using default `page.json` template (not custom template)

### SearchSpring Not Working

**Problem:** Collection has `searchspring` template suffix but SearchSpring not loading.

**Solution:**
1. Verify template suffix spelling: `searchspring` (lowercase, no spaces)
2. Check SearchSpring dashboard for sync status
3. Verify SearchSpring app is active
4. Check browser console for JavaScript errors
5. Verify cookies are enabled (SearchSpring requires cookies)

### Product Template Not Applying

**Problem:** Template suffix set but product page not using custom template.

**Solution:**
1. Verify template file exists (e.g., `product.recharge-bundle.json`)
2. Check template suffix spelling (case-sensitive, no spaces)
3. Verify template is valid JSON
4. Check browser console for errors
5. Clear theme cache (publish/unpublish theme)

### Menu Not Showing in Footer

**Problem:** Footer menu block added but menu not displaying.

**Solution:**
1. Verify menu is selected in block settings
2. Check menu has menu items (not empty)
3. Verify block is enabled (not disabled)
4. Check mobile vs desktop display settings
5. Verify menu is published in Shopify Admin

### Low Stock Message Not Showing

**Problem:** Product has `cql.low_stock_threshold` metafield but message not displaying.

**Solution:**
1. Verify metafield is number type (not text)
2. Check product section has **Low stock message** block
3. Verify inventory quantity is below threshold
4. Check block is enabled in product template

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **Data Guide:** [data-guide.md](./data-guide.md) - Metafields reference
- **Integrations:** [integrations.md](./integrations.md) - App documentation

---

*Last Updated: Theme structure March 31, 2026 ([internal_THEME_DELTA_MAR2026.md](./internal_THEME_DELTA_MAR2026.md))*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*
