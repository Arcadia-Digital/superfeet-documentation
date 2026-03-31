# Matrixify export diff — US store (superfeetww)

**New export:** `data/EVERYTHING-Export-forAI_2026-03-31_154533` (job finished 2026-03-31)  
**Baseline:** `data/SFUS-EVERYTHING-Export_2025-10-16_184845`

## Executive summary

Counts below use **unique resource `ID`s** in each CSV (not row counts). Row counts swing with Matrixify column presets (e.g. linked products on collections, discount code expansion).

| Resource (US) | Oct 2025 baseline | Mar 2026 forAI export |
|-----------------|-------------------|------------------------|
| Products | 57 | **64** |
| Smart collections | 18 | **23** |
| Custom collections | 20 | **21** |
| Collections total | 38 | **44** |
| Pages | 63 | **67** |
| Blog posts | 150 | **168** |
| Metaobjects | 259 | **277** |
| Menus | 15 | 15 (unique menu IDs; item rows differ slightly) |

**Export scope:** This **forAI** job is a narrower column preset than the Oct 2025 full store export (e.g. fewer inventory/location columns). Documentation hub metrics do not depend on redirect or file export sheets.

**Products column drift:** The new export drops category/inventory-market columns from Oct 2025 and adds Shopify standard metafields (`shopify.*` lists), `Metafield: avalara.taxcode`, `custom.personalized_option_media`, and variant shipping profile fields—see “Column set differences” below.

**Discounts:** `Export Summary` reports **910** discount *entities* exported in the new job vs **872** in the old; the CSV has hundreds of thousands of **rows** because codes/eligibility expand—do not use raw row count as “number of discounts.”

---

- **Baseline:** `/Users/pete/dev/shopify/superfeet-documentation/data/SFUS-EVERYTHING-Export_2025-10-16_184845`
- **New:** `/Users/pete/dev/shopify/superfeet-documentation/data/EVERYTHING-Export-forAI_2026-03-31_154533`

## File inventory

| File | Old rows | New rows | Delta | Header match |
|------|----------|----------|-------|--------------|
| Blog Posts.csv | 150 | 168 | +18 | yes |
| Custom Collections.csv | 182 | 193 | +11 | NO — columns differ |
| Discounts.csv | 180820 | 202802 | +21982 | NO — columns differ |
| Export Summary.csv | 10 | 9 | -1 | yes |
| Menus.csv | 116 | 115 | -1 | yes |
| Metaobjects.csv | 1362 | 1425 | +63 | yes |
| Pages.csv | 63 | 67 | +4 | yes |
| Products.csv | 350 | 417 | +67 | NO — columns differ |
| Smart Collections.csv | 316 | 36 | -280 | NO — columns differ |

## Added CSV files (1)

- `Shop.csv`

## Removed CSV files (2)

- `Files.csv`
- `Redirects.csv`

## Column set differences

### `Custom Collections.csv`
- Only in **old**: ['Products Count']

### `Discounts.csv`
- Only in **old**: ['Buy X Get Y: Customer Buys Type', 'Buy X Get Y: Customer Buys Values', 'Buy X Get Y: Customer Gets Quantity', 'Combines with Order Discounts', 'Combines with Product Discounts', 'Combines with Shipping Discounts', 'Eligibility: Customer Type', 'Eligibility: Customer Values', 'Free Shipping: Country Codes', 'Free Shipping: Over Amount', 'Purchase Type', 'Purchase Type: Recurring Subscription Limit']

### `Products.csv`
- Only in **old**: ['Category', 'Category: ID', 'Category: Name', 'Compare At Price / United States', 'Custom Collections', 'Included / United States', 'Inventory Available Adjust: Quiet Atlanta Warehouse', 'Inventory Available Adjust: Quiet La Palma Warehouse', 'Inventory Available Adjust: Superfeet Worldwide LLC', 'Inventory Available: Quiet Atlanta Warehouse', 'Inventory Available: Quiet La Palma Warehouse', 'Inventory Available: Superfeet Worldwide LLC', 'Inventory Committed: Quiet Atlanta Warehouse', 'Inventory Committed: Quiet La Palma Warehouse', 'Inventory Committed: Superfeet Worldwide LLC', 'Inventory Damaged Adjust: Quiet Atlanta Warehouse', 'Inventory Damaged Adjust: Quiet La Palma Warehouse', 'Inventory Damaged Adjust: Superfeet Worldwide LLC', 'Inventory Damaged: Quiet Atlanta Warehouse', 'Inventory Damaged: Quiet La Palma Warehouse', 'Inventory Damaged: Superfeet Worldwide LLC', 'Inventory Incoming: Quiet Atlanta Warehouse', 'Inventory Incoming: Quiet La Palma Warehouse', 'Inventory Incoming: Superfeet Worldwide LLC', 'Inventory On Hand Adjust: Quiet Atlanta Warehouse', 'Inventory On Hand Adjust: Quiet La Palma Warehouse', 'Inventory On Hand Adjust: Superfeet Worldwide LLC', 'Inventory On Hand: Quiet Atlanta Warehouse', 'Inventory On Hand: Quiet La Palma Warehouse', 'Inventory On Hand: Superfeet Worldwide LLC', 'Inventory Quality Control Adjust: Quiet Atlanta Warehouse', 'Inventory Quality Control Adjust: Quiet La Palma Warehouse', 'Inventory Quality Control Adjust: Superfeet Worldwide LLC', 'Inventory Quality Control: Quiet Atlanta Warehouse', 'Inventory Quality Control: Quiet La Palma Warehouse', 'Inventory Quality Control: Superfeet Worldwide LLC', 'Inventory Reserved: Quiet Atlanta Warehouse', 'Inventory Reserved: Quiet La Palma Warehouse', 'Inventory Reserved: Superfeet Worldwide LLC', 'Inventory Safety Stock Adjust: Quiet Atlanta Warehouse', 'Inventory Safety Stock Adjust: Quiet La Palma Warehouse', 'Inventory Safety Stock Adjust: Superfeet Worldwide LLC', 'Inventory Safety Stock: Quiet Atlanta Warehouse', 'Inventory Safety Stock: Quiet La Palma Warehouse', 'Inventory Safety Stock: Superfeet Worldwide LLC', 'Price / United States', 'Smart Collections', 'Variant Cost', 'Variant Country of Origin', 'Variant HS Code']…
- Only in **new**: ['Metafield: avalara.taxcode [single_line_text_field]', 'Metafield: custom.personalized_option_media [list.metaobject_reference]', 'Metafield: shopify.activity [list.metaobject_reference]', 'Metafield: shopify.age-group [list.metaobject_reference]', 'Metafield: shopify.clothing-accessory-material [list.metaobject_reference]', 'Metafield: shopify.color-pattern [list.metaobject_reference]', 'Metafield: shopify.material [list.metaobject_reference]', 'Metafield: shopify.shoe-size [list.metaobject_reference]', 'Metafield: shopify.target-gender [list.metaobject_reference]', 'Variant Metafield: custom.material [metaobject_reference]', 'Variant Shipping Profile']

### `Smart Collections.csv`
- Only in **old**: ['Product: Handle', 'Product: ID', 'Product: Position', 'Products Count']

