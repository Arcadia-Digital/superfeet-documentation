# Blank Accessibility Fields Inventory - Template JSON Files

## Overview
This document identifies all accessibility-specific fields (aria-label, etc.) in **template JSON files** that are currently blank and require content to be filled in.

---

## Summary Count
Based on analysis of all template JSON files in the theme:

| Field Type                       | Total   | Blank   | Filled | % Blank   |
| -------------------------------- | ------- | ------- | ------ | --------- |
| `button_aria_label` (single)     | 121     | 78      | 43     | 64.5%     |
| `button_aria_label_1` (button 1) | 47      | 30      | 17     | 63.8%     |
| `button_aria_label_2` (button 2) | 47      | 31      | 16     | 66.0%     |
| **TOTAL**                        | **215** | **139** | **76** | **64.7%** |

---

## Templates Requiring Updates

The following **32 template JSON files** contain blank accessibility fields and need to be updated:

### Collection Templates (15 files)
1. `collection.all-purpose-collection.json`
2. `collection.bundle-collection.json`
3. `collection.casual-dress-collection.json`
4. `collection.cleat-sports-collection.json`
5. `collection.court-sports-collection.json`
6. `collection.fit-train-collection.json`
7. `collection.golf-collection.json`
8. `collection.hiking-collection.json`
9. `collection.hockey-skates-collection.json`
10. `collection.json`
11. `collection.pain-relief-collection.json`
12. `collection.racquet-sports-collection.json`
13. `collection.ski-snowboard-collection.json`
14. `collection.walking-collection.json`
15. `collection.work-collection.json`

### Index Templates (1 file)
16. `index.ea-vpo1ey.json`

### Page Templates (9 files)
17. `page.b2b-personalized-fit.json`
18. `page.case-study.json`
19. `page.comfort-science.json`
20. `page.pain-relief.json`
21. `page.qr-pages.json`
22. `page.qr-work.json`
23. `page.rx-otc-orthotics.json`
24. `page.rx-supporting.json`
25. `page.why-superfeet.json`

### Product Templates (6 files)
26. `product.casual-pain-relief.json`
27. `product.fixed-bundle.json`
28. `product.json`
29. `product.run-pain-relief.json`
30. `product.subscription.json`
31. `product.work-cushion.json`

### Search Templates (1 file)
32. `search.json`

**Total: 32 template files (15 collections + 1 index + 9 pages + 6 products + 1 search)**

---

## Where These Fields Appear

These fields appear in template JSON files across various section types:

- **image-banner** sections (buttons)
- **image-with-text** sections (buttons)
- **image-with-text-alternate** sections (buttons)
- **rich-text** sections (buttons)
- **info-carousel** sections (testimonial buttons)
- **video** sections (buttons)
- **image-accordion** sections (CTA buttons)
- **banner-grid** sections (buttons)
- **multicolumn** sections (links)
- And other section types with button/CTA functionality

---

## Action Required

**139 blank accessibility fields** need to be filled in across all template JSON files to improve screen reader support.

### Next Steps
1. Review each blank `button_aria_label` field
2. Add descriptive, contextual aria-label text (e.g., "Shop Run Pacer Elite product page" instead of just leaving it blank)
3. Ensure aria-labels are unique and informative
4. Consider button text context when writing aria-labels

---

## Historical Context: Section Files (Reference)

**Note:** The sections below document the original template/section definitions, not the live JSON data.

### Sections with Optional Accessibility Fields

### 1. **image-accordion.liquid**
**Field:** `section.settings.cta_aria_label`
- **Type:** Text field
- **Usage:** Applied to CTA link at bottom of accordion
- **Total instances:** 1 per section
- **Lines:** 82-84, 237-241

---

### 2. **multicolumn.liquid**
**Fields:** 
- `block.settings.link_aria_label` (appears on block links)
- `section.settings.link_aria_label` (appears on section-wide CTA)

**Usage:** Applied to multiple link types:
- Entire card links (lines 100, 242, 266, 444)
- Image links (lines 266, 444)
- Individual link labels (lines 242, 444)
- Section-level CTA (line 461)

**Total instances:** 4+ per block (entire card, image link, link label) + 1 per section
- **Lines:** 99-101, 241-243, 265-267, 443-445, 461

---

### 3. **banner-grid.liquid**
**Field:** `section.settings.section_button_aria_label`
- **Type:** Text field
- **Usage:** Applied to all buttons (hero, landscape, square cards, section-level CTA)
- **Total instances:** Up to 5 per section (4 card buttons + 1 section button)
- **Lines:** 65, 97, 129, 161, 180, 207-212

---

### 4. **info-carousel.liquid**
**Field:** `block.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to carousel content block buttons
- **Total instances:** 2 per block (mobile and desktop variations)
- **Lines:** 99, 174

---

### 5. **rich-text.liquid**
**Field:** `block.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to rich text block buttons
- **Total instances:** 2 per block
- **Lines:** 97, 108

---

### 6. **image-with-features.liquid**
**Field:** `block.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to feature block buttons
- **Total instances:** Unknown (need to check file)

---

### 7. **video.liquid**
**Field:** `section.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to video section buttons
- **Total instances:** 2 per section (lines 45, 52)

---

### 8. **slideshow.liquid**
**Field:** `section.settings.accessibility_info`
- **Type:** Text field
- **Usage:** Applied to main slideshow aria-label
- **Total instances:** 1 per section
- **Lines:** 58

---

### 9. **featured-products.liquid**
**Field:** `block.settings.button_aria_label`
- **Type:** Text field  
- **Usage:** Applied to featured product block buttons
- **Total instances:** 1 per block
- **Lines:** 97

---

### 10. **scrolling-features.liquid**
**Field:** `section.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to scrolling features buttons
- **Total instances:** 1 per section
- **Lines:** 124

---

### 11. **featured-collections.liquid**
**Field:** `block.settings.button_aria_label`
- **Type:** Text field
- **Usage:** Applied to collection block buttons
- **Total instances:** 1 per block

---

### 12-14. **Other sections** (lifestyle.liquid, image-banner.liquid, image-with-text.liquid, image-with-text-alternate.liquid)
**Field:** Various button and link aria-label fields
**Details:** Need to review these files for exact field names and usage

---

## Accessible Components Already Hardcoded (No Issues)

These components use translation keys or hardcoded values and don't require content filling:

- Customer account repos (aria-label values use translation keys)
- Cart drawer (uses translation keys)
- Product media gallery (uses translation keys)
- Search modals (uses translation keys)
- Pagination (uses translation keys)
- Gift card forms (uses translation keys)
- Product compare columns (uses translation keys)

---

## Recommendations

### High Priority
1. **multicolumn.liquid** - Has the most instances (4+ per block)
2. **banner-grid.liquid** - Used on multiple button instances
3. **image-accordion.liquid** - Simple single instance, easy fix

### Medium Priority
4. **info-carousel.liquid** - Used in multiple places
5. **slideshow.liquid** - Important for carousel accessibility
6. **rich-text.liquid** - Flexible content sections

### Documentation Needed
- Review actual live theme data to see which sections/blocks are actively used
- Determine how many of each section type exist
- Prioritize based on page traffic/importance

---

## File Locations
All files located in:
`accessibility/code/theme_export__www-superfeet-com-release-10-01-25-production__28OCT2025-0158pm/sections/`

---

## Notes
- All identified fields are **optional** (marked with `!= blank` checks)
- Fields are only rendered if they have content
- No validation errors occur when fields are left empty
- Theme uses conditional rendering: `{% if field != blank %} aria-label="{{ field }}" {% endif %}`
