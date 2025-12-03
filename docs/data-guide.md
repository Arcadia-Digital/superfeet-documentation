# Data Guide

**Superfeet Multi-Region Shopify Plus Platform**

Complete reference documentation for all metafields, metaobjects, and data structures.

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

## Data Access Patterns

### Liquid Template Access

**Product Metafields:**
```liquid
{% comment %} Single line text {% endcomment %}
{{ product.metafields.cql.arch_height }}

{% comment %} Boolean {% endcomment %}
{% if product.metafields.cql.vegan %}
  <span>Vegan</span>
{% endif %}

{% comment %} Multi-line text {% endcomment %}
{{ product.metafields.cql.short_description }}

{% comment %} Number {% endcomment %}
{{ product.metafields.cql.low_stock_threshold }}

{% comment %} Product reference list {% endcomment %}
{% for comparison_product in product.metafields.cql.comparison_products.value %}
  {{ comparison_product.title }}
{% endfor %}

{% comment %} Metaobject reference {% endcomment %}
{% assign faq_group = product.metafields.cql.faq_group.value %}
{{ faq_group.title }}
```

**Variant Metafields:**
```liquid
{{ variant.metafields.mm-google-shopping.gender }}
{{ variant.metafields.mm-google-shopping.size_system }}
```

**Page Metafields:**
```liquid
{% if page.metafields.cql.rx_microsite %}
  {% assign isMicrositePage = true %}
{% endif %}
```

**JSON Metafields:**
```liquid
{% assign json_data = product.metafields.custom.json_field | parse_json %}
{{ json_data.property }}
```

### Checking Metafield Existence

**Best Practice:** Always check if metafield exists before accessing:
```liquid
{% if product.metafields.cql.arch_height %}
  {{ product.metafields.cql.arch_height }}
{% endif %}
```

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

### Product Filtering

**By Arch Height:**
```liquid
{% if product.metafields.cql.arch_height == "Medium" %}
  <!-- Display medium arch product -->
{% endif %}
```

**By Gender:**
```liquid
{% if product.metafields.cql.product_gender == "Unisex" %}
  <!-- Display unisex product -->
{% endif %}
```

### Product Display

**Size Ranges:**
```liquid
{% if product.metafields.cql.men_sizes %}
  <p>Men's Sizes: {{ product.metafields.cql.men_sizes }}</p>
{% endif %}
```

**Product Badges:**
```liquid
{% if product.metafields.cql.badge %}
  <span class="badge">{{ product.metafields.cql.badge }}</span>
{% endif %}
```

### SEO Optimization

**Custom SEO Titles:**
```liquid
{% if product.metafields.seo_title %}
  <title>{{ product.metafields.seo_title }}</title>
{% else %}
  <title>{{ product.title }}</title>
{% endif %}
```

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **Shopify Metafields:** https://help.shopify.com/en/manual/metafields

---

*Last Updated: Based on data exports from October 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

