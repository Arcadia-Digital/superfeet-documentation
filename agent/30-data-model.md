# Data Model: Metafields and Metaobjects

## Key Namespaces

### CQL Namespace (`cql.*`)

**Primary namespace for product data and business logic.**

**Product Information:**
- `cql.arch_height` - Arch height (e.g., "Medium", "High")
- `cql.insole_thickness` - Insole thickness (e.g., "Mid", "Thin")
- `cql.product_gender` - Product gender (e.g., "Unisex", "Men's", "Women's")
- `cql.product_family` - Product family (e.g., "All-Purpose", "Run Support")
- `cql.underfoot_cushioning` - Cushioning level (e.g., "Soft", "Medium")
- `cql.target_use_activity` - Target activity (e.g., "All-Purpose", "Running")
- `cql.fits_best_in` - Fit description
- `cql.insole_technology` - Technology description
- `cql.badge` - Badge text (e.g., "Best Seller")
- `cql.best_for` - Best use case description
- `cql.short_description` - Short product description (multi-line)

**Size Information:**
- `cql.kid_sizes` - Kids size range
- `cql.men_sizes` - Men's size range
- `cql.women_sizes` - Women's size range
- `cql.skate_sizes` - Skate size range

**Product Attributes:**
- `cql.vegan` [boolean] - Vegan product indicator
- `cql.latex_free` [boolean] - Latex-free product indicator
- `cql.low_stock_threshold` [number] - Low stock threshold

**Product Relationships:**
- `cql.comparison_products` [list.product_reference] - Related/comparison products
- `cql.shop_for` - Shop for category (e.g., "Men, Women, Kids")

**Metaobject References:**
- `cql.faq_group` [metaobject_reference] - FAQ group metaobject
- `cql.arch_height_info` [metaobject_reference] - Arch height information
- `cql.thickness_info` [metaobject_reference] - Thickness information
- `cql.cushion_info` [metaobject_reference] - Cushion information

**Reference:** `docs/data-guide.md` - Product Metafields

### Custom Namespace (`custom.*`)

**Custom features and extensions.**

- `custom.feature_diagram` [metaobject_reference] - Feature diagram metaobject
- `custom.insole_finder_header_text` [single_line_text_field] - Insole Finder header text
- `custom.hsa_fsa_eligible` [boolean] - HSA/FSA eligibility indicator

**Reference:** `docs/data-guide.md` - Product Metafields

### SEO Namespace (`seo.*`)

**SEO and search visibility.**

- `seo_title` [single_line_text_field] - Custom SEO title
- `seo_desc` [single_line_text_field] - Custom SEO description
- `seo.hidden` [number_integer] - Hide from search (0 = visible, 1 = hidden)

**Reference:** `docs/data-guide.md` - Product Metafields

### Reviews Namespace (`reviews.*`)

**Review and rating data.**

- `reviews.rating_count` [number_integer] - Review count
- `reviews.rating` [rating] - Average rating

**Reference:** `docs/data-guide.md` - Product Metafields

### Yotpo Namespace (`yotpo.*`)

**Yotpo review integration (auto-generated).**

- `yotpo.reviews_average` [single_line_text_field] - Average review rating
- `yotpo.reviews_count` [single_line_text_field] - Review count
- `yotpo.richsnippetshtml` [single_line_text_field] - Rich snippets HTML

**Reference:** `docs/data-guide.md` - Product Metafields

### Google Shopping Namespace (`mm-google-shopping.*`)

**Google Shopping feed data.**

- `mm-google-shopping.custom_product` [boolean] - Custom product flag
- `mm-google-shopping.google_product_category` [string] - Google product category

**Reference:** `docs/data-guide.md` - Product Metafields

### Facebook Namespace (`mc-facebook.*`)

**Facebook catalog data.**

- `mc-facebook.google_product_category` [string] - Facebook product category

**Reference:** `docs/data-guide.md` - Product Metafields

### Recharge Namespace (`rc_bundles.*`)

**Recharge bundle configuration.**

- `rc_bundles.layout_template` [single_line_text_field] - Bundle layout template

**Reference:** `docs/data-guide.md` - Product Metafields

## Critical Metafields

### High-Value Product Metafields

**For Product Display:**
- `cql.arch_height` - Used in product filtering and display
- `cql.insole_thickness` - Used in product filtering and display
- `cql.product_gender` - Used in product filtering
- `cql.badge` - Displays badges on product cards
- `cql.short_description` - Product description text
- `cql.best_for` - Use case description

**For Product Relationships:**
- `cql.comparison_products` - Powers product comparison features
- `cql.product_family` - Groups related products

**For Metaobjects:**
- `cql.faq_group` - Links to FAQ content
- `cql.arch_height_info` - Links to arch height icons/info
- `cql.thickness_info` - Links to thickness icons/info
- `cql.cushion_info` - Links to cushion icons/info
- `custom.feature_diagram` - Links to feature diagram content

**Reference:** `docs/data-guide.md` - Product Metafields

## Metaobject Types

### Product Feature Groups

**Type:** `product_feature_groups`  
**Reference:** `cql.faq_group` [metaobject_reference]  
**Purpose:** Reusable FAQ content for products  
**Example:** `product_feature_groups.ap-cushion`

**Reference:** `docs/data-guide.md` - Metaobjects

### Arch Height Icons

**Type:** `arch_height_icons`  
**Reference:** `cql.arch_height_info` [metaobject_reference]  
**Purpose:** Arch height information and icon references  
**Example:** `arch_height_icons.mid`

**Reference:** `docs/data-guide.md` - Metaobjects

### Thickness Icons

**Type:** `thickness_icons`  
**Reference:** `cql.thickness_info` [metaobject_reference]  
**Purpose:** Thickness information and icon references  
**Example:** `thickness_icons.medium`

**Reference:** `docs/data-guide.md` - Metaobjects

### Cushion Icons

**Type:** `cushion_icons`  
**Reference:** `cql.cushion_info` [metaobject_reference]  
**Purpose:** Cushion information and icon references  
**Example:** `cushion_icons.soft`

**Reference:** `docs/data-guide.md` - Metaobjects

### Feature Diagrams

**Type:** `feature_diagrams` (inferred)  
**Reference:** `custom.feature_diagram` [metaobject_reference]  
**Purpose:** Feature diagram data for product displays

**Reference:** `docs/data-guide.md` - Metaobjects

## Data Relationships

### Product → Variants

**Relationship:** One-to-many  
**Access:** `product.variants`  
**Variant Metafields:** Google Shopping labels, size system, gender, condition

**Reference:** `docs/data-guide.md` - Variant Metafields

### Product → Metafields

**Relationship:** One-to-many  
**Access:** `product.metafields.{namespace}.{key}`  
**Namespaces:** `cql.*`, `custom.*`, `seo.*`, `reviews.*`, `yotpo.*`, etc.

**Reference:** `docs/data-guide.md` - Data Access Patterns

### Product → Comparison Products

**Relationship:** Many-to-many (via metafield)  
**Metafield:** `cql.comparison_products` [list.product_reference]  
**Purpose:** Links to related products for comparison features

**Reference:** `docs/data-guide.md` - Data Relationships

### Product → Metaobjects

**Relationship:** One-to-one (via metafield)  
**Metafields:**
- `cql.faq_group` → FAQ metaobject
- `cql.arch_height_info` → Arch height metaobject
- `cql.thickness_info` → Thickness metaobject
- `cql.cushion_info` → Cushion metaobject
- `custom.feature_diagram` → Feature diagram metaobject

**Reference:** `docs/data-guide.md` - Data Relationships

## Practical Debugging Rules

### Finding Metafield Values

1. **In Shopify Admin:**
   - Go to Products → Select product
   - Scroll to Metafields section
   - Metafields organized by namespace

2. **In Liquid Templates:**
   ```liquid
   {{ product.metafields.cql.arch_height }}
   {{ product.metafields.custom.hsa_fsa_eligible }}
   ```

3. **Via Matrixify Export:**
   - Export products with all metafield columns
   - View in CSV/Excel format

**Reference:** `docs/data-guide.md` - Using Metafields in Shopify Admin

### Understanding Metafield Types

**Single Line Text Field:**
- Short text values
- Examples: `cql.arch_height`, `cql.badge`

**Multi-Line Text Field:**
- Longer text content
- Example: `cql.short_description`

**Boolean:**
- True/false values
- Examples: `cql.vegan`, `custom.hsa_fsa_eligible`

**Number:**
- Numeric values
- Example: `cql.low_stock_threshold`

**Product Reference:**
- Links to another product
- Example: `cql.addon_product`

**Product Reference List:**
- Links to multiple products
- Example: `cql.comparison_products`

**Metaobject Reference:**
- Links to a metaobject
- Examples: `cql.faq_group`, `cql.arch_height_info`

**File Reference:**
- Links to uploaded file
- Example: `cql.image_with_feature`

**Reference:** `docs/data-guide.md` - Understanding Metafield Types

### Bulk Data Management

**Matrixify Workflow:**
1. Export products with metafields
2. Modify metafield values in CSV/Excel
3. Import updated file
4. Preview changes before applying

**Important:** Always backup before bulk changes!

**Reference:** `docs/data-guide.md` - Bulk Data Management
