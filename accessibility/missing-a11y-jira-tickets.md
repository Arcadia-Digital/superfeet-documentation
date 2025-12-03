# Missing Accessibility JIRA Tickets

Based on comparison between the August 2025 accessibility report and existing JIRA tickets, the following issues require new tickets to be created:

## High Priority (Level A - Critical)

### 1. Missing or Invalid Alt Text and Image Accessible Names
**Title:** `Accessibility - Missing or Invalid Alt Text and Image Accessible Names`

**Description:**
Multiple issues with image accessibility including placeholder alt text, missing accessible names for images, missing alt text, and missing SVG accessible names. These issues prevent screen reader users from understanding image content.

**Technical Details:**
- **WCAG Reference:** 1.1.1 (Non-text Content), 1.2.1 (Audio-only and Video-only)
- **Section 508 Reference:** A F30, A F65, A 1.1.1
- **Pages Affected:** Multiple pages across the site
- **Specific Issues:**
  - Alt text contains placeholders like 'picture' or 'spacer' (https://www.superfeet.com/ Line 7912)
  - Elements with role=img missing accessible names (https://tracking.superfeet.com/ Line 290)
  - img elements missing alt attributes (https://www.superfeet.com/pages/new-product-releases Line 2780)
  - SVG elements with graphic role missing accessible names (https://www.superfeet.com/ Line 4600)

**Solution:**
- For purely decorative images and spacers use alt=''
- For images of text use the text content
- For other images use a descriptive alt attribute
- For elements with role=img add aria-label or aria-labelledby attributes
- For SVG elements add accessible names using title elements or ARIA labels
- Purely decorative images should use role=presentation

**Priority:** High (Level A violation)

---

### 3. Missing ARIA Level Attributes
**Title:** `Accessibility - Missing ARIA Level Attributes on Headings`

**Description:**
Element div is missing one or more required attributes. Missing aria-level attributes on heading elements.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A 4.1.2
- **Pages Affected:** 14 pages (blog pages)

**Solution:**
Add appropriate aria-level attributes to heading elements to maintain proper heading hierarchy.

**Priority:** High (Level A violation)

---

### 2. Table Headers Missing
**Title:** `Accessibility - Missing Table Headers`

**Description:**
Identify row and column headers in data tables using th elements, and mark layout tables with role=presentation. Data tables allow screen reader users to understand column and row relationships.

**Technical Details:**
- **WCAG Reference:** 1.3.1 (Info and Relationships)
- **Section 508 Reference:** A F91
- **Pages Affected:** 4 pages
  - https://www.superfeet.com/pages/accessibility-policy (Line 2765)
  - https://www.superfeet.com/pages/ccpa-privacy-policy (Lines 2769, 2812, 2831)
  - https://www.superfeet.com/pages/privacy-policy (Lines 2793, 2862)
  - https://www.superfeet.com/pages/u-s-shipping-policy (Line 2764)

**Solution:**
If a data table has headers marked up using td, then change these to th. If a data table has no headers, add th elements describing each row and/or column. If the table is only used for layout add role=presentation to the table element.

**Priority:** High (Level A violation)

---

### 7. Missing iframe Titles
**Title:** `Accessibility - Missing iframe Title Attributes`

**Description:**
iframe and frame elements must have a title attribute. Without a title some screen readers read out the frame filename, which is usually meaningless.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A 4.1.2
- **Pages Affected:** 2 pages
  - https://www.superfeet.com/ (Line 8501)
  - https://www.superfeet.com/blogs/company-news/superfeet-hockey-insoles-the-ultimate-assist (Line 2791)

**Solution:**
Add a title attribute or ARIA label to each iframe and frame element (e.g. title='Main Content').

**Priority:** High (Level A violation)

---

### 7. Non-Descriptive Link Text
**Title:** `Accessibility - Non-Descriptive Link Text`

**Description:**
Link uses general text like 'Click Here' with no surrounding text explaining link purpose. Screen reader users use text around links to help understand what the link does.

**Technical Details:**
- **WCAG Reference:** 2.4.4 (Link Purpose, In Context), 2.4.9 (Link Purpose, Link Only)
- **Section 508 Reference:** A F63
- **Pages Affected:** 17 pages (various collection pages)

**Solution:**
Either use a descriptive link label (which helps all users) or add an aria-label or aria-describedby to the link (which helps screen reader users).

**Priority:** High (Level A violation)

---

### 10. Missing Link Names
**Title:** `Accessibility - Missing Link Names`

**Description:**
Links must have an accessible name. A link name allows screen readers to voice what the links does. If there is no link content, or the link content is hidden by CSS, screen readers have nothing to read.

**Technical Details:**
- **WCAG Reference:** 2.4.4 (Link Purpose, In Context), 2.4.9 (Link Purpose, Link Only), 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A F89
- **Pages Affected:** 35 pages

**Solution:**
Add text between the a element start and end tags, add an aria-label attribute, add an aria-labelledby attribute, or add an img alt attribute labeling the link if it contains an img element.

**Priority:** High (Level A violation)

---

### 11. Duplicate Link Text
**Title:** `Accessibility - Duplicate Link Text with Different Destinations`

**Description:**
Several links on a page share the same link text and surrounding context, but go to different destinations. This is confusing for screen reader users.

**Technical Details:**
- **WCAG Reference:** 2.4.4 (Link Purpose, In Context), 2.4.9 (Link Purpose, Link Only)
- **Section 508 Reference:** A F63
- **Pages Affected:** 94 pages

**Solution:**
Make the link text unique for each target page (which helps all users) or add an aria-label or aria-describedby to the link (which helps screen reader users).

**Priority:** High (Level A violation)

---

### 10. Invalid ARIA References
**Title:** `Accessibility - Invalid ARIA References`

**Description:**
The aria-labelledby attribute references a blank element, and the aria-owns attribute must point to IDs of elements in the same document. These IDs weren't found: predictive-search-results-list.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value), 1.3.1 (Info and Relationships)
- **Section 508 Reference:** A 4.1.2, A 1.3.1
- **Pages Affected:** 95 pages

**Solution:**
Make sure aria-labelledby references an element containing text, and ensure aria-owns points to valid element IDs in the same document.

**Priority:** High (Level A violation)

---

### 14. Nested Interactive Controls
**Title:** `Accessibility - Nested Interactive Controls`

**Description:**
The button element must not appear as a descendant of an element with role=button. An interactive control nested inside another interactive control is not voiced correctly by screen readers.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A 4.1.2
- **Pages Affected:** 1 page
  - https://www.superfeet.com/ (Lines 7827, 7851, 7875, 7899)

**Solution:**
Restructure the HTML to avoid nesting interactive controls within each other.

**Priority:** High (Level A violation)

---

### 15. Visual Label Mismatch
**Title:** `Accessibility - Visual Label Not in Accessible Name`

**Description:**
The visual label must appear in the accessible name of links and controls. People who use speech control rely on being able to select elements using the visual label displayed on screen.

**Technical Details:**
- **WCAG Reference:** 2.5.3 (Label in Name)
- **Section 508 Reference:** A F96
- **Pages Affected:** 23 pages

**Solution:**
Ensure the visual label text is included in the accessible name of interactive elements.

**Priority:** High (Level A violation)

---

### 16. Empty Button Elements
**Title:** `Accessibility - Empty Button Elements`

**Description:**
This button element is empty and has no accessible name. A programmatically determined name allows screen readers to tell users what the control does.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A 4.1.2
- **Pages Affected:** 32 pages

**Solution:**
Add text between the button start and end tags, add a title attribute, add an aria-label attribute, add an aria-labelledby attribute, or add an img alt attribute if the button contains an img element.

**Priority:** High (Level A violation)

---

### 17. JavaScript Links
**Title:** `Accessibility - JavaScript Links Without Proper Markup`

**Description:**
This element uses JavaScript to behave like a link. Links like this cannot be tabbed to from the keyboard and are not read out when screen readers list the links on a page.

**Technical Details:**
- **WCAG Reference:** 1.3.1 (Info and Relationships), 2.1.1 (Keyboard), 2.1.3 (Keyboard, No Exception), 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** A F42
- **Pages Affected:** 97 pages

**Solution:**
Use an a or area element with a fallback link target in the href attribute, to ensure it receive keyboard focus and behaves like a link.

**Priority:** High (Level A violation)

---

### 18. Semantic Markup Issues
**Title:** `Accessibility - Use Semantic Markup Instead of CSS`

**Description:**
Use semantic markup like strong instead of using the CSS font-weight property. Use the strong element instead of the span element for bold text.

**Technical Details:**
- **WCAG Reference:** 1.3.1 (Info and Relationships)
- **Section 508 Reference:** A F2
- **Pages Affected:** 27 pages

**Solution:**
Replace span elements with font-weight CSS with proper semantic strong elements.

**Priority:** High (Level A violation)

---

### 19. Missing Language Attribute
**Title:** `Accessibility - Missing Language Attribute`

**Description:**
Use the lang attribute to identify the language of the page. This allows screen readers to pronounce words correctly.

**Technical Details:**
- **WCAG Reference:** 3.1.1 (Language of Page)
- **Section 508 Reference:** A 3.1.1
- **Pages Affected:** 3 pages (web-pixels pages)

**Solution:**
In HTML add a lang attribute containing a language code to the html tag.

**Priority:** High (Level A violation)

---

## Medium Priority (Level AA)

### 20. Invalid ARIA Naming
**Title:** `Accessibility - Invalid ARIA Naming on Generic Elements`

**Description:**
Cannot use aria-label or aria-labelledby on elements and roles that prohibit naming. The div and span elements have an implicit role of generic and cannot be named unless they have a role attribute.

**Technical Details:**
- **WCAG Reference:** 4.1.2 (Name, Role, Value)
- **Section 508 Reference:** AA 4.1.2
- **Pages Affected:** 28 pages

**Solution:**
Remove aria-label or aria-labelledby from generic elements, or add appropriate role attributes if naming is required.

**Priority:** Medium (Level AA violation)

---

### 21. Insufficient Color Contrast
**Title:** `Accessibility - Insufficient Color Contrast`

**Description:**
Ensure that text and background colors have enough contrast. Some users find it hard to read light gray text on a white background, dark gray text on a black background and white text on a red background.

**Technical Details:**
- **WCAG Reference:** 1.4.3 (Contrast, Minimum), 1.4.6 (Contrast, Enhanced)
- **Section 508 Reference:** AA 1.4.3
- **Pages Affected:** 34 pages
- **Contrast Issues:**
  - 1.52 ratio with color: rgb(45,45,45); background: rgb(0,0,0)
  - 1.84 ratio with color: rgb(191,191,191); background: rgb(255,255,255)
  - 3.20 ratio with color: rgb(0,146,255); background: rgb(255,255,255)

**Solution:**
The contrast ratio should be 3.0 or more for 18 point text, or larger; 3.0 or more for 14 point bold text, or larger; 4.5 or more for all other text.

**Priority:** Medium (Level AA violation)

---

### 22. Incomplete Color Definitions
**Title:** `Accessibility - Incomplete Color Definitions`

**Description:**
If you set any of the colors on the body or a elements you must set all of them. Some users have browser defaults set to white text on a black background, so setting one color without setting the others can result in black text on a black background.

**Technical Details:**
- **WCAG Reference:** 1.4.3 (Contrast, Minimum), 1.4.6 (Contrast, Enhanced), 1.4.8 (Visual Presentation)
- **Section 508 Reference:** AA F24
- **Pages Affected:** 28 pages

**Solution:**
Set all color attributes (text, bgcolor, link, alink, vlink in HTML or color and background-color in CSS) to ensure consistent appearance across different user settings.

**Priority:** Medium (Level AA violation)

---

### 23. Missing Site Navigation
**Title:** `Accessibility - Missing Site Navigation Options`

**Description:**
Provide two or more ways to reach each page: via links, search, a site map or table of contents. You should provide a link labeled 'Site Map' or 'Sitemap' or the equivalent in your language, or a search option on every page, or links to all pages from the home page.

**Technical Details:**
- **WCAG Reference:** 2.4.5 (Multiple Ways)
- **Section 508 Reference:** AA 2.4.5
- **Pages Affected:** 1 page
  - https://tracking.superfeet.com/

**Solution:**
Add a site map, search functionality, or comprehensive navigation to provide multiple ways to access content.

**Priority:** Medium (Level AA violation)

---

### 24. Focus Outline Issues
**Title:** `Accessibility - Focus Outline Visibility Issues`

**Description:**
The CSS outline or border style on this element makes it difficult or impossible to see the link focus outline. Do not remove the default outline style, and change any border styles to avoid obscuring the focus outline around focusable elements.

**Technical Details:**
- **WCAG Reference:** 2.4.7 (Focus Visible)
- **Section 508 Reference:** AA F78
- **Pages Affected:** 16 pages

**Solution:**
Do not remove the default outline style, and change any border styles to avoid obscuring the focus outline around focusable elements. See :focus-visible for more information.

**Priority:** Medium (Level AA violation)

---

## Low Priority (Level AAA)

### 25. New Window Links
**Title:** `Accessibility - New Window Links Without Warning`

**Description:**
Avoid specifying a new window as the target of a link with target="_blank". Displaying new windows without warning can be very confusing to non-sighted and mobile users.

**Technical Details:**
- **WCAG Reference:** 3.2.5 (Change on Request)
- **Section 508 Reference:** AAA F22
- **Pages Affected:** 71 pages

**Solution:**
If you cannot avoid displaying a new window, insert an "opens in a new window" warning into the link text or add the warning to the link using a title attribute or aria-describedby attribute.

**Priority:** Low (Level AAA violation)

---

### 26. CSS Animation Issues
**Title:** `Accessibility - CSS Animations Without User Control`

**Description:**
Don't use CSS animations or transitions in interactions without giving the user a way to turn them off. Use the @media (prefers-reduced-motion) media query to respect user preferences.

**Technical Details:**
- **WCAG Reference:** 2.3.3 (Animation from Interactions)
- **Section 508 Reference:** AAA 2.3.3
- **Pages Affected:** 1 page
  - https://www.superfeet.com/ (Lines 7204, 7205, 7206, 7207)

**Solution:**
Use the @media (prefers-reduced-motion) media query to respect user preferences for reduced motion.

**Priority:** Low (Level AAA violation)

---

### 27. Enhanced Color Contrast
**Title:** `Accessibility - Enhanced Color Contrast Requirements`

**Description:**
Ensure that text and background colors have a 7:1 contrast ratio. The text color to background color contrast ratio after composition is: 3.20 with color: rgb(0,146,255); background: rgb(255,255,255); font-size: 14.40pt; font-weight: 700.

**Technical Details:**
- **WCAG Reference:** 1.4.6 (Contrast, Enhanced)
- **Section 508 Reference:** AAA 1.4.6
- **Pages Affected:** 1 page
  - https://www.superfeet.com/pages/ccpa-privacy-policy (Line 2752)

**Solution:**
The contrast ratio should be 7.0 or more for all text to meet AAA standards.

**Priority:** Low (Level AAA violation)

---

### 28. Generic Link Text
**Title:** `Accessibility - Generic Link Text Without Context`

**Description:**
Link uses general text like 'Click Here' which doesn't explain link purpose. Screen reader users often tab from one link to the next, or use the 'Next Link' command.

**Technical Details:**
- **WCAG Reference:** 2.4.9 (Link Purpose, Link Only)
- **Section 508 Reference:** AAA F84
- **Pages Affected:** 26 pages

**Solution:**
Change the link text, or add an aria-label, so the link makes sense when read without the surrounding text.

**Priority:** Low (Level AAA violation)

---

### 29. Duplicate Link Text (AAA)
**Title:** `Accessibility - Duplicate Link Text with Different Destinations (AAA)`

**Description:**
Several links on a page share the same link text, but go to different destinations. Make the link text unique for each target, or add additional text using aria-label.

**Technical Details:**
- **WCAG Reference:** 2.4.9 (Link Purpose, Link Only)
- **Section 508 Reference:** AAA 2.4.9
- **Pages Affected:** 94 pages

**Solution:**
Make the link text unique for each target, or add additional text using aria-label.

**Priority:** Low (Level AAA violation)

---

### 30. Reading Level Issues
**Title:** `Accessibility - Reading Level Too High`

**Description:**
This page is hard to read for users with learning disabilities or reading disorders like dyslexia. For improved readability use simpler words and shorter sentences.

**Technical Details:**
- **WCAG Reference:** 3.1.5 (Reading Level)
- **Section 508 Reference:** AAA 3.1.5
- **Pages Affected:** 83 pages
- **Reading Age:** 4-7 years (Flesch Reading Ease Score: 53-62)

**Solution:**
Use simpler words and shorter sentences. The reading age should be appropriate for the target audience.

**Priority:** Low (Level AAA violation)

---

## Summary

**Total Missing Tickets:** 25
- **High Priority (Level A):** 14 tickets
- **Medium Priority (Level AA):** 5 tickets  
- **Low Priority (Level AAA):** 6 tickets

These tickets should be created in JIRA to ensure comprehensive coverage of all accessibility issues identified in the August 2025 report that are not already addressed by existing tickets.
