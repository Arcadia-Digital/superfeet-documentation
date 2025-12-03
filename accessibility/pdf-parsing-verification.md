# PDF Parsing Verification Report
## Comparison of PDF Text vs. Parsed Issues

**Date:** October 22, 2025  
**Purpose:** Verify accuracy of PDF accessibility report parsing

---

## ✅ VERIFIED: Issue Counts Match

| Level         | PDF Reports            | My Parsing | Status        |
| ------------- | ---------------------- | ---------- | ------------- |
| **Level A**   | 25 issues on 101 pages | 25 issues  | ✅ **CORRECT** |
| **Level AA**  | 5 issues on 56 pages   | 5 issues   | ✅ **CORRECT** |
| **Level AAA** | 6 issues on 98 pages   | 6 issues   | ✅ **CORRECT** |
| **Total**     | 36 issues              | 36 issues  | ✅ **CORRECT** |

---

## ✅ VERIFIED: All Issue Types Captured

### Level A Issues (25 total) - All Captured ✅

| #   | PDF Issue Description                                                                                 | Status         | JIRA/CSV Reference                                  |
| --- | ----------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------- |
| 1   | A video plays longer than 5 seconds, without a way to pause                                           | ✅ **RESOLVED** | Confirmed fixed by dev team                         |
| 2   | alt text should not contain placeholders like 'picture' or 'spacer'                                   | 📋 **CSV**      | CSV Row 1 (combined with other alt text issues)     |
| 3   | An element with a role that hides child elements contains focusable child elements                    | 🔄 **JIRA**     | [SUPS25-24] - DONE                                  |
| 4   | An element with the attribute tabindex must not appear as a descendant of an element with role=button | 📋 **CSV**      | CSV Row 9 (Nested Interactive Controls)             |
| 5   | ARIA role=button element is empty and has no accessible name                                          | 📋 **CSV**      | CSV Row 11 (Empty Button Elements)                  |
| 6   | Avoid animated images over 5 seconds long that can't be paused or stopped                             | 📋 **CSV**      | CSV Row 1 (combined with other image issues)        |
| 7   | Decorative and spacer images must not use descriptive alt attributes                                  | 📋 **CSV**      | CSV Row 1 (combined with other alt text issues)     |
| 8   | Element div is missing one or more required attributes (aria-level)                                   | 📋 **CSV**      | CSV Row 2 (Missing ARIA Level Attributes)           |
| 9   | Elements with role=img must have an accessible name                                                   | 📋 **CSV**      | CSV Row 1 (combined with other image issues)        |
| 10  | Headings should not be empty                                                                          | 🔄 **JIRA**     | [SUPS25-150] - Headings & Page Structure            |
| 11  | Identify row and column headers in data tables using th elements                                      | 📋 **CSV**      | CSV Row 3 (Missing Table Headers)                   |
| 12  | iframe and frame elements must have a title attribute                                                 | 📋 **CSV**      | CSV Row 4 (Missing iframe Title Attributes)         |
| 13  | img elements must have an accessible name                                                             | 📋 **CSV**      | CSV Row 1 (combined with other image issues)        |
| 14  | Link uses general text like 'Click Here' with no surrounding text                                     | 📋 **CSV**      | CSV Row 5 (Non-Descriptive Link Text)               |
| 15  | Links must have an accessible name                                                                    | 📋 **CSV**      | CSV Row 6 (Missing Link Names)                      |
| 16  | Several links on a page share the same link text and surrounding context                              | 📋 **CSV**      | CSV Row 7 (Duplicate Link Text)                     |
| 17  | SVG elements with graphic role attributes must have an accessible name                                | 📋 **CSV**      | CSV Row 1 (combined with other image issues)        |
| 18  | The aria-labelledby attribute references a blank element                                              | 📋 **CSV**      | CSV Row 8 (Invalid ARIA References)                 |
| 19  | The aria-owns attribute must point to IDs of elements in the same document                            | 📋 **CSV**      | CSV Row 8 (Invalid ARIA References)                 |
| 20  | The button element must not appear as a descendant of an element with role=button                     | 📋 **CSV**      | CSV Row 9 (Nested Interactive Controls)             |
| 21  | The visual label must appear in the accessible name of links and controls                             | 📋 **CSV**      | CSV Row 10 (Visual Label Not in Accessible Name)    |
| 22  | This button element is empty and has no accessible name                                               | 📋 **CSV**      | CSV Row 11 (Empty Button Elements)                  |
| 23  | This element uses JavaScript to behave like a link                                                    | 📋 **CSV**      | CSV Row 12 (JavaScript Links Without Proper Markup) |
| 24  | Use semantic markup like strong instead of using the CSS font-weight property                         | 📋 **CSV**      | CSV Row 13 (Use Semantic Markup Instead of CSS)     |
| 25  | Use the lang attribute to identify the language of the page                                           | 📋 **CSV**      | CSV Row 14 (Missing Language Attribute)             |

### Level AA Issues (5 total) - All Captured ✅

| #   | PDF Issue Description                                                                            | Status     | JIRA/CSV Reference                                   |
| --- | ------------------------------------------------------------------------------------------------ | ---------- | ---------------------------------------------------- |
| 1   | Cannot use aria-label or aria-labelledby on elements and roles that prohibit naming              | 📋 **CSV**  | CSV Row 15 (Invalid ARIA Naming on Generic Elements) |
| 2   | Ensure that text and background colors have enough contrast                                      | 🔄 **JIRA** | [SUPS25-149] - Color Contrast                        |
| 3   | If you set any of the colors on the body or a elements you must set all of them                  | 📋 **CSV**  | CSV Row 17 (Incomplete Color Definitions)            |
| 4   | Provide two or more ways to reach each page: via links, search, a site map                       | 📋 **CSV**  | CSV Row 18 (Missing Site Navigation Options)         |
| 5   | The CSS outline or border style on this element makes it difficult to see the link focus outline | 📋 **CSV**  | CSV Row 19 (Focus Outline Visibility Issues)         |

### Level AAA Issues (6 total) - All Captured ✅

| #   | PDF Issue Description                                                                                  | Status    | JIRA/CSV Reference                                                 |
| --- | ------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------------------------------ |
| 1   | Avoid specifying a new window as the target of a link with target="_blank"                             | 📋 **CSV** | CSV Row 20 (New Window Links Without Warning)                      |
| 2   | Don't use CSS animations or transitions in interactions without giving the user a way to turn them off | 📋 **CSV** | CSV Row 21 (CSS Animations Without User Control)                   |
| 3   | Ensure that text and background colors have a 7:1 contrast ratio                                       | 📋 **CSV** | CSV Row 22 (Enhanced Color Contrast Requirements)                  |
| 4   | Link uses general text like 'Click Here' which doesn't explain link purpose                            | 📋 **CSV** | CSV Row 23 (Generic Link Text Without Context)                     |
| 5   | Several links on a page share the same link text, but go to different destinations                     | 📋 **CSV** | CSV Row 24 (Duplicate Link Text with Different Destinations - AAA) |
| 6   | This page is hard to read for users with learning disabilities or reading disorders                    | 📋 **CSV** | CSV Row 25 (Reading Level Too High)                                |

---

## ✅ VERIFICATION COMPLETE

**Summary:**
- ✅ **All 36 issues** from PDF correctly identified and mapped
- ✅ **Issue counts** match exactly (25 A + 5 AA + 6 AAA = 36 total)
- ✅ **All issue descriptions** captured accurately
- ✅ **Proper categorization** by WCAG level
- ✅ **Complete mapping** to JIRA tickets and CSV references

**Confidence Level:** 100% - All issues from the PDF have been accurately captured and properly categorized in the status report.

---

*This verification confirms that the accessibility status report for the legal team is complete and accurate.*
