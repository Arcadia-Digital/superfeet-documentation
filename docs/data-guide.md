# Data Guide

**Superfeet Multi-Region Shopify Plus Platform**

Complete reference documentation for all metafields, metaobjects, and data structures.

**Who This Guide Is For:** This guide helps you understand and manage metafields (custom data fields) in Shopify Admin. You don't need to know code to use this guide - it focuses on how to work with metafields through the Shopify interface and Matrixify for bulk updates.

---

## Table of Contents

1. [Product Metafields](#product-metafields)
2. [Variant Metafields](#variant-metafields)
3. [Collection Metafields](#collection-metafields)
4. [Page Metafields](#page-metafields)
5. [Metaobjects](#metaobjects)
6. [Data Access Patterns](#data-access-patterns)
7. [Bulk Data Management](#bulk-data-management)

---

## Product Metafields

### CQL Namespace (`cql.*`)

**Product Information:**
- `cql.arch_height` [single_line_text_field] - Arch height (e.g., "Medium", "High")
- `cql.insole_thickness` [single_line_text_field] - Insole thickness (e.g., "Mid", "Thin")
- `cql.product_gender` [single_line_text_field] - Product gender (e.g., "Unisex", "Men's", "Women's")
- `cql.product_family` [single_line_text_field] - Product family (e.g., "All-Purpose", "Run Support")
- `cql.underfoot_cushioning` [single_line_text_field] - Cushioning level (e.g., "Soft", "Medium")
- `cql.target_use_activity` [single_line_text_field] - Target activity (e.g., "All-Purpose", "Running")
- `cql.fits_best_in` [single_line_text_field] - Fit description (e.g., "Roomy to moderate fitting footwear")
- `cql.insole_technology` [single_line_text_field] - Technology description (e.g., "A.C.T. (Adaptive Comfort Technology)")
- `cql.insole_heel_cup_depth` [single_line_text_field] - Heel cup depth (e.g., "Max")
- `cql.previously_named` [single_line_text_field] - Previous product name
- `cql.badge` [single_line_text_field] - Badge text (e.g., "Best Seller")
- `cql.best_for` [single_line_text_field] - Best use case (e.g., "Everyday footwear, athletic shoes, active use")
- `cql.short_description` [multi_line_text_field] - Short product description
- `cql.discount_summary` [single_line_text_field] - Discount summary text
- `cql.bundle_type` [single_line_text_field] - Bundle type identifier

**Size Information:**
- `cql.kid_sizes` [single_line_text_field] - Kids size range
- `cql.men_sizes` [single_line_text_field] - Men's size range (e.g., "5.5 - 7, 7.5 - 9, 9.5 - 11, 11.5 - 13")
- `cql.women_sizes` [single_line_text_field] - Women's size range (e.g., "4.5 - 6, 6.5 - 8, 8.5 - 10, 10.5 - 12, 12.5 - 14")
- `cql.skate_sizes` [single_line_text_field] - Skate size range

**Product Attributes:**
- `cql.vegan` [boolean] - Vegan product indicator
- `cql.latex_free` [boolean] - Latex-free product indicator
- `cql.low_stock_threshold` [number_integer] - Low stock threshold number

**Product Relationships:**
- `cql.comparison_products` [list.product_reference] - Related/comparison products
- `cql.shop_for` [single_line_text_field] - Shop for category (e.g., "Men, Women, Kids")

**Metaobject References:**
- `cql.faq_group` [metaobject_reference] - FAQ group metaobject
- `cql.arch_height_info` [metaobject_reference] - Arch height information metaobject
- `cql.thickness_info` [metaobject_reference] - Thickness information metaobject
- `cql.cushion_info` [metaobject_reference] - Cushion information metaobject

**Media:**
- `cql.image_with_feature` [file_reference] - Image with feature overlay

### Custom Namespace (`custom.*`)

- `custom.feature_diagram` [metaobject_reference] - Feature diagram metaobject
- `custom.insole_finder_header_text` [single_line_text_field] - Insole Finder header text
- `custom.hsa_fsa_eligible` [boolean] - HSA/FSA eligibility indicator

### SEO Namespace (`seo.*`)

- `seo_title` [single_line_text_field] - Custom SEO title
- `seo_desc` [single_line_text_field] - Custom SEO description
- `seo.hidden` [number_integer] - Hide from search (0 = visible, 1 = hidden)

### Reviews Namespace (`reviews.*`)

- `reviews.rating_count` [number_integer] - Review count
- `reviews.rating` [rating] - Average rating

### Yotpo Namespace (`yotpo.*`)

- `yotpo.reviews_average` [single_line_text_field] - Average review rating
- `yotpo.reviews_count` [single_line_text_field] - Review count
- `yotpo.richsnippetshtml` [single_line_text_field] - Rich snippets HTML

### Google Shopping Namespace (`mm-google-shopping.*`)

- `mm-google-shopping.custom_product` [boolean] - Custom product flag
- `mm-google-shopping.google_product_category` [string] - Google product category

### Facebook Namespace (`mc-facebook.*`)

- `mc-facebook.google_product_category` [string] - Facebook product category

### Recharge Namespace (`rc_bundles.*`)

- `rc_bundles.layout_template` [single_line_text_field] - Bundle layout template

### Standard Metafields

- `title_tag` [string] - Page title tag
- `description_tag` [string] - Meta description tag

---

## Variant Metafields

### Google Shopping Variant Metafields (`mm-google-shopping.*`)

- `mm-google-shopping.custom_label_0` [single_line_text_field] - Custom label 0
- `mm-google-shopping.custom_label_1` [single_line_text_field] - Custom label 1
- `mm-google-shopping.custom_label_2` [single_line_text_field] - Custom label 2
- `mm-google-shopping.custom_label_3` [single_line_text_field] - Custom label 3
- `mm-google-shopping.custom_label_4` [single_line_text_field] - Custom label 4
- `mm-google-shopping.size_system` [single_line_text_field] - Size system
- `mm-google-shopping.size_type` [single_line_text_field] - Size type
- `mm-google-shopping.mpn` [single_line_text_field] - Manufacturer part number
- `mm-google-shopping.gender` [single_line_text_field] - Gender
- `mm-google-shopping.condition` [single_line_text_field] - Product condition
- `mm-google-shopping.age_group` [single_line_text_field] - Age group

---

## Collection Metafields

Collection metafields are used for collection-specific configurations and content. Common namespaces include:
- `cql.*` - Custom collection data
- `custom.*` - Custom collection settings
- `seo.*` - SEO settings

**Note:** Specific collection metafields should be verified in Shopify Admin or via data exports.

---

## Page Metafields

### CQL Namespace (`cql.*`)

- `cql.rx_microsite` [boolean] - RX microsite indicator (used for microsite layout)

**Note:** Additional page metafields may exist. Verify in Shopify Admin or data exports.

---

## Metaobjects

### Product Feature Groups

**Reference:** `cql.faq_group` [metaobject_reference]

Product FAQ groups stored as metaobjects for reusable FAQ content.

**Example:** `product_feature_groups.ap-cushion`

### Arch Height Icons

**Reference:** `cql.arch_height_info` [metaobject_reference]

Arch height information and icon references.

**Example:** `arch_height_icons.mid`

### Thickness Icons

**Reference:** `cql.thickness_info` [metaobject_reference]

Thickness information and icon references.

**Example:** `thickness_icons.medium`

### Cushion Icons

**Reference:** `cql.cushion_info` [metaobject_reference]

Cushion information and icon references.

**Example:** `cushion_icons.soft`

### Feature Diagrams

**Reference:** `custom.feature_diagram` [metaobject_reference]

Feature diagram data for product displays.

---

## Using Metafields in Shopify Admin

### Finding Metafields on Products

**In Product Edit Screen:**
1. Go to **Products** → Select a product
2. Scroll down to the **Metafields** section
3. Metafields are organized by namespace (e.g., all `cql.*` metafields appear together)
4. Click on a metafield to edit its value
5. Click **Save** to save changes

### Understanding Metafield Types

**Single Line Text Field:**
- Use for short text values (e.g., "Medium", "High", "Best Seller")
- Examples: `cql.arch_height`, `cql.badge`, `cql.product_gender`

**Multi-Line Text Field:**
- Use for longer text content (e.g., product descriptions)
- Supports basic formatting
- Example: `cql.short_description`

**Boolean (True/False):**
- Use for yes/no indicators
- Examples: `cql.vegan`, `cql.latex_free`, `custom.hsa_fsa_eligible`
- Check the box for "true", leave unchecked for "false"

**Number:**
- Use for numeric values
- Example: `cql.low_stock_threshold` (enter a number like 10)

**Product Reference:**
- Links to another product
- Use the product picker to select a product
- Example: `cql.addon_product`

**Product Reference List:**
- Links to multiple products
- Click "Add product" to add multiple products
- Examples: `cql.comparison_products`, `cql.associated_products`

**Metaobject Reference:**
- Links to a metaobject (reusable content)
- Use the metaobject picker to select
- Examples: `cql.faq_group`, `cql.arch_height_info`

**File Reference:**
- Links to an uploaded file (image, PDF, etc.)
- Use the file picker to upload or select
- Example: `cql.image_with_feature`

---

## Bulk Data Management

### Matrixify Export/Import

**Exporting Products with Metafields:**
1. Install Matrixify app
2. Configure export (select Products)
3. Include all metafield columns
4. Download CSV/Excel file

**Importing Products with Metafields:**
1. Modify exported file
2. Update metafield values
3. Upload to Matrixify
4. Preview changes
5. Import to store

**Important:** Always backup before bulk changes!

### Metafield Updates

**Via Shopify Admin:**
1. Navigate to product/page/collection
2. Scroll to metafields section
3. Edit metafield values
4. Save

**Via Matrixify:**
1. Export products
2. Modify metafield columns
3. Import updated file

**Via Shopify API:**
- Use GraphQL Admin API
- Update metafield definitions and values
- Requires API access

---

## Data Relationships

### Product Relationships

**Comparison Products:**
- Metafield: `cql.comparison_products` [list.product_reference]
- Links to related products for comparison features

**Product Families:**
- Metafield: `cql.product_family` [single_line_text_field]
- Groups products by family (e.g., "All-Purpose", "Run Support")

### Metaobject Relationships

**FAQ Groups:**
- Products reference FAQ metaobjects
- Reusable FAQ content across products

**Icon References:**
- Products reference icon metaobjects
- Arch height, thickness, cushion icons
- Consistent iconography across site

---

## Common Use Cases

### Product Organization

**Using Product Family:**
- Set `cql.product_family` to group related products (e.g., "All-Purpose", "Run Support")
- Helps organize products for collections and filtering
- Used internally for product recommendations and related products

**Using Product Gender:**
- Set `cql.product_gender` to categorize products (e.g., "Unisex", "Men's", "Women's")
- Used for filtering and collection organization
- Helps customers find gender-specific products

**Using Arch Height:**
- Set `cql.arch_height` to specify arch support level (e.g., "Medium", "High", "Low/Medium/High")
- Displays on product pages with an icon
- Used for product comparison and filtering

### Product Display on Storefront

**Product Badges:**
- Set `cql.badge` to add badges like "Best Seller", "New", or "Limited Edition"
- Badge appears as an overlay on product images
- Use sparingly - only for special promotions or highlights

**Short Description:**
- Set `cql.short_description` to customize the product description that appears on product pages
- This replaces the standard product description
- Supports basic formatting (bold, italic, lists)
- For Recharge bundles, this displays as an "Includes:" list when configured

**Size Information:**
- Set `cql.men_sizes`, `cql.women_sizes`, or `cql.kid_sizes` to specify size ranges
- Used for filtering and product organization
- Format: "5.5 - 7, 7.5 - 9, 9.5 - 11" (comma-separated ranges)

### SEO Optimization

**Custom SEO Titles:**
- Set `seo_title` to override the default page title for search engines
- Appears in browser tabs and search engine results
- If not set, uses the product title

**Custom SEO Descriptions:**
- Set `seo_desc` to override the default meta description
- Appears in search engine results below the title
- Keep it under 160 characters for best results

**Hide from Search:**
- Set `seo.hidden` to `1` to prevent products from appearing in search results
- Use for test products, discontinued items, or products not ready for sale
- Set to `0` or leave empty to show in search

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **Shopify Metafields:** https://help.shopify.com/en/manual/metafields

---

*Last Updated: Based on data exports from October 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

