# Integrations Documentation

**Superfeet Multi-Region Shopify Plus Platform**

Complete documentation of all third-party apps and how to manage them in your day-to-day work.

---

## Table of Contents

1. [Major Apps You'll Use Daily](#major-apps-youll-use-daily)
2. [Apps with Special Template Requirements](#apps-with-special-template-requirements)
3. [Apps with Metafield Integration](#apps-with-metafield-integration)
4. [Apps That Run Automatically](#apps-that-run-automatically)
5. [Configuration & Setup](#configuration--setup)
6. [Troubleshooting](#troubleshooting)

---

## Major Apps You'll Use Daily

### SearchSpring

**What It Does:** Enhanced product search and filtering that's much more powerful than Shopify's default search. Provides better search results, filtering options, and product recommendations.

**Stores:** US, UK, Canada (all three stores)

**How You Use It:**
1. **Assign SearchSpring Template to Collections:**
   - Go to **Collections** → Select a collection
   - Scroll to **Search engine listing**
   - Set **Template suffix:** `searchspring`
   - Save

2. **Configure in SearchSpring Dashboard:**
   - Access SearchSpring dashboard (link in Shopify Apps)
   - Configure search settings, filters, and recommendations
   - Product data syncs automatically from Shopify

3. **What Happens:**
   - SearchSpring replaces the default Shopify search on that collection
   - Customers get better search results and filtering
   - Product recommendations appear automatically

**Important Notes:**
- **Essential A/B Testing app is incompatible** - Don't run A/B tests on SearchSpring-powered collections
- SearchSpring has its own dashboard for configuration - you don't configure it in Shopify Admin
- Each store (US, UK, CA) has its own SearchSpring instance

**When to Use SearchSpring:**
- Main product collections where customers need to filter and search
- Collections with many products where filtering is important
- When you want advanced product recommendations

**When NOT to Use SearchSpring:**
- Simple collections with few products
- Collections that don't need advanced search
- Collections where you're running A/B tests (Essential A/B Testing conflicts)

**Troubleshooting:**
- If search isn't working, check SearchSpring dashboard for sync status
- Verify the collection has `searchspring` template suffix assigned
- Contact SearchSpring support if you see sync errors

---

### Recharge Subscriptions

**What It Does:** Enables product bundles (customizable product sets) and subscription orders (recurring orders).

**Stores:** US, UK, Canada (all three stores)

**How You Use It:**

**For Bundle Products:**
1. Go to **Products** → Select product
2. Set **Template suffix:** `recharge-bundle`
3. Configure bundle options in **Recharge app dashboard** (not in Shopify)
4. The bundle widget appears automatically on the product page

**For Subscription Products:**
1. Go to **Products** → Select product
2. Set **Template suffix:** `subscription`
3. Configure subscription options in **Recharge app dashboard**
4. The subscription widget appears automatically on the product page

**Important Notes:**
- Bundle and subscription configuration happens in the **Recharge app dashboard**, not in Shopify Admin
- The template suffix just tells the theme to show the Recharge widget
- Bundle pricing and options are managed in Recharge
- **Subscriptions are available but not currently activated** - work with ReCharge support team and your development partner when ready to launch

**ReCharge Documentation:**
- Bundle documentation: https://support.getrecharge.com/hc/en-us/sections/6981308041623-Bundles
- Subscription management: https://support.getrecharge.com/hc/en-us/categories/360000578374-Subscription-Management

---

### Yotpo Product Reviews

**What It Does:** Manages product reviews and customer photos (user-generated content) across all stores.

**Stores:** US, UK, Canada (all three stores)

**How It Works:**
- Reviews are collected on the **US store**
- **US reviews automatically appear on UK and Canada stores** (this is called "syndication")
- ExpertVoice reviews also sync to the US store
- Reviews appear automatically on product pages - you don't need to do anything

**What You Manage:**
- **Review Moderation:** Approve/reject reviews in Yotpo dashboard
- **Review Settings:** Configure review display, email requests, etc. in Yotpo dashboard
- **UGC Galleries:** Add Yotpo UGC sections to collection pages in Theme Customizer

**Metafields (Automatic):**
- `yotpo.reviews_average` - Average rating (updated automatically)
- `yotpo.reviews_count` - Review count (updated automatically)
- These are updated automatically - you don't need to manage them

**Important Notes:**
- Reviews sync automatically between stores - don't worry about managing this
- If reviews aren't showing, check Yotpo dashboard for sync status
- Review widgets are built into product templates - they appear automatically
- You can add UGC galleries to collection pages via Theme Customizer

**Troubleshooting:**
- If reviews aren't appearing, check Yotpo dashboard for sync status
- Verify product template includes Yotpo blocks (they should by default)
- Contact Yotpo support if you see sync errors

---

### Osano Cookie Consent

**What It Does:** Manages cookie consent for GDPR/CCPA compliance. Shows a cookie consent banner to visitors and manages their cookie preferences.

**Stores:** US, UK, Canada (all three stores)

**How It Works:**
- Cookie consent banner appears automatically to visitors
- Visitors can accept or customize cookie preferences
- Osano manages which cookies are allowed based on consent
- Different rules apply based on visitor location (GDPR for EU, CCPA for California, etc.)

**What You Manage:**
- **Cookie Policy:** Update cookie policy text in Osano dashboard
- **Consent Settings:** Configure which cookies require consent in Osano dashboard
- **Regional Rules:** Set up different rules for different regions (EU, US, etc.) in Osano dashboard

**Important Notes:**
- Osano runs automatically - the banner appears on all pages
- Configuration happens in Osano dashboard, not in Shopify
- You don't need to do anything in Shopify Admin for this to work
- If the banner isn't appearing, check Osano dashboard for configuration issues

---

### Insole Finder Quiz

**What It Does:** Custom quiz that asks customers questions about their feet and activity level, then recommends the best insole products for them.

**Stores:** US, UK, Canada (all three stores)

**How You Use It:**
1. **Create Insole Finder Page:**
   - Go to **Online Store → Pages**
   - Create new page or edit existing Insole Finder page
   - Set **Template suffix:** `insole-finder-2`
   - Save

2. **Configure Quiz in Theme Customizer:**
   - Go to **Theme Customizer**
   - Select the Insole Finder page
   - Find **Insole Finder 2** section
   - Configure quiz questions and product recommendations

3. **Link to Quiz:**
   - Add link in navigation menus
   - Link from product pages
   - Link from homepage or landing pages

**Important Notes:**
- Quiz logic and product recommendations are managed by a custom app built by Born West & Superfeet
- For changes to quiz questions or logic, work with **Michael Sullivan, Heather Allerdice-Gerow, and the team at Born West**
- The quiz uses a special page template that has a simplified header/footer design
- Quiz results link to specific product pages automatically

---

## Apps with Metafield Integration

### Google Shopping (mm-google-shopping)

**Purpose:** Google Merchant Center product feed integration.

**Metafields:**
- Product: `mm-google-shopping.custom_product` [boolean]
- Product: `mm-google-shopping.google_product_category` [string]
- Variant: `mm-google-shopping.custom_label_0-4` [single_line_text_field]
- Variant: `mm-google-shopping.size_system` [single_line_text_field]
- Variant: `mm-google-shopping.size_type` [single_line_text_field]
- Variant: `mm-google-shopping.mpn` [single_line_text_field]
- Variant: `mm-google-shopping.gender` [single_line_text_field]
- Variant: `mm-google-shopping.condition` [single_line_text_field]
- Variant: `mm-google-shopping.age_group` [single_line_text_field]

**Configuration:**
- Google Merchant Center dashboard
- Product feed synchronization
- Metafield values populate feed

---

### Facebook (mc-facebook)

**Purpose:** Facebook product catalog integration.

**Metafields:**
- Product: `mc-facebook.google_product_category` [string]

**Configuration:**
- Facebook Business Manager
- Product catalog synchronization

---

## Apps without Theme Integration

These apps are installed and functional but have no theme code integration:

### Matrixify
- **Purpose:** Bulk data import/export and backups
- **Stores:** US, UK, CA
- **Integration:** App-only, no theme code
- **Usage:** Bulk product updates, inventory management, data backups

### Elevar Conversion Tracking
- **Purpose:** Server-side conversion tracking
- **Stores:** US, UK, CA
- **Integration:** JavaScript loaded via app (not in theme code)
- **Connected Services:** GA4, Facebook Pixel, Klaviyo, Google Ads
- **Note:** Elevar script loaded via `{{ content_for_header }}` in theme.liquid

### Klaviyo
- **Purpose:** Email and SMS marketing automation
- **Stores:** US, UK, CA
- **Integration:** JavaScript loaded via app (not in theme code)
- **Note:** Klaviyo script loaded via `{{ content_for_header }}` in theme.liquid

### Regios Discounts
- **Purpose:** Advanced discount logic
- **Stores:** US only
- **Integration:** App-only, no theme code

### Geo:Pro Geolocation
- **Purpose:** Automatic regional redirection
- **Stores:** US only
- **Integration:** JavaScript-based redirection (app handles)
- **Note:** Don't implement manual geolocation - Geo:Pro handles this

### Shipfy: Shipping Rules
- **Purpose:** Complex shipping rule management
- **Stores:** US only
- **Integration:** App-only, no theme code

### StoreRocket Store Locator
- **Purpose:** Physical store finder
- **Stores:** US, UK, CA
- **Integration:** App-only, no theme code

### Avalara Tax Compliance
- **Purpose:** Tax calculation
- **Stores:** US, UK, CA
- **Integration:** App-only, no theme code

### AfterShip Order Tracking
- **Purpose:** Order tracking
- **Stores:** US, UK, CA
- **Integration:** App-only, no theme code

### GOVX ID Exclusive Discounts
- **Purpose:** Military/veteran discounts
- **Stores:** US only
- **Integration:** App-only, no theme code

### Fraud Control
- **Purpose:** Customer service tool for blocking problematic customers
- **Stores:** US only
- **Integration:** App-only, no theme code

### Awin
- **Purpose:** Affiliate marketing
- **Stores:** US only
- **Integration:** App-only, no theme code

### Shopcodes
- **Purpose:** QR code generation (evaluating)
- **Stores:** US only
- **Integration:** App-only, no theme code
- **Status:** Roadmap - evaluating

### Essential Preorder
- **Purpose:** Preorder functionality
- **Stores:** US only
- **Integration:** App-only, no theme code
- **Status:** Roadmap - planned for future product releases

### Forms
- **Purpose:** Native Shopify Forms
- **Stores:** Not in use
- **Integration:** Not implemented
- **Status:** Roadmap - would like to replace embedded Cognito forms

### Essential A/B Testing
- **Purpose:** A/B testing for product pages, collections, templates, and themes
- **Stores:** Installed but incompatible
- **Integration:** Creates collection templates with "ea-" prefix (e.g., `ea-9zkhwx`, `ea-aklu3g`) for A/B test variants
- **Template Creation:** Automatically creates test variant templates when running A/B tests on collections
- **Important:** Not compatible with SearchSpring - cannot use Essential A/B Testing on SearchSpring-powered collections
- **Status:** Looking for alternative
- **Documentation:** [Essential A/B Testing App](https://essential-apps.com/essential-shopify-ab-testing-app/)
- **Note:** EA-prefixed templates are automatically managed by the app and should not be manually assigned to collections

### Bagpiper Data Export
- **Purpose:** Data export (replaced by Matrixify)
- **Stores:** Not in use
- **Status:** Replaced by Matrixify, can be removed

### GRIN Influencer Marketing
- **Purpose:** Influencer marketing
- **Stores:** Installed
- **Status:** May be inactive, replaced by Awin

### Statlas
- **Purpose:** Unknown
- **Stores:** Installed
- **Status:** Needs investigation/documentation

### Shopify Native Apps
- **Flow** - Automation workflows
- **Launchpad** - Scheduled sales and promotions
- **Theme Access** - Theme access management
- **Shopify GraphiQL App** - GraphQL API testing
- **Translate & Adapt** - Translation management

---

## Apps with Special Template Requirements

Some apps require you to assign specific templates to products or collections for them to work properly. Here's a quick reference:

### SearchSpring
- **Collection Template:** `searchspring`
- **Where to Set:** Collections → Search engine listing → Template suffix
- **What It Does:** Enables SearchSpring search and filtering on that collection

### Recharge
- **Bundle Products:** Template suffix `recharge-bundle`
- **Subscription Products:** Template suffix `subscription`
- **Where to Set:** Products → Search engine listing → Template suffix
- **What It Does:** Shows Recharge bundle or subscription widget on product page

### Insole Finder
- **Page Template:** `insole-finder-2`
- **Where to Set:** Pages → Template suffix
- **What It Does:** Enables the quiz interface and special layout

---

## Configuration & Setup

### SearchSpring Setup (For New Collections)

1. **Assign Template:**
   - Go to **Collections** → Select collection
   - Set **Template suffix:** `searchspring`
   - Save

2. **Configure in SearchSpring Dashboard:**
   - Open SearchSpring app from Shopify Apps
   - Configure search settings, filters, and recommendations
   - Product data syncs automatically

3. **Verify It's Working:**
   - Visit the collection page on the storefront
   - You should see SearchSpring's enhanced search and filtering
   - If you see default Shopify search, check the template suffix

### Recharge Setup (For Bundle/Subscription Products)

1. **Assign Template:**
   - Go to **Products** → Select product
   - Set **Template suffix:** `recharge-bundle` or `subscription`
   - Save

2. **Configure in Recharge Dashboard:**
   - Open Recharge app from Shopify Apps
   - Configure bundle options or subscription settings
   - Set pricing and product options

3. **Verify It's Working:**
   - Visit the product page on the storefront
   - You should see the Recharge bundle or subscription widget
   - If widget doesn't appear, check template suffix and Recharge configuration

### Yotpo Setup (Usually Already Configured)

- Reviews are already set up and working
- Reviews sync automatically between stores
- You mainly need to moderate reviews in Yotpo dashboard
- To add UGC gallery to a collection page, add Yotpo UGC section in Theme Customizer

### Osano Setup (Usually Already Configured)

- Cookie consent is already configured and working
- Banner appears automatically on all pages
- Update cookie policy or consent settings in Osano dashboard if needed

---

## Troubleshooting

### SearchSpring Issues

**Problem:** Search not working or showing default Shopify search.

**Solution:**
1. **Check Template Assignment:**
   - Go to Collections → Select the collection
   - Verify **Template suffix** is set to `searchspring` (lowercase, no spaces)
   - Save if needed

2. **Check SearchSpring Dashboard:**
   - Open SearchSpring app
   - Check sync status - products should be synced
   - Verify the collection is configured in SearchSpring

3. **Verify App is Active:**
   - Go to **Settings → Apps and sales channels**
   - Find SearchSpring app
   - Make sure it's installed and active

4. **Still Not Working?**
   - Contact SearchSpring support (they have excellent support)
   - Provide them with the collection URL and store name

### Recharge Issues

**Problem:** Bundle or subscription widget not showing on product page.

**Solution:**
1. **Check Template Assignment:**
   - Go to Products → Select the product
   - Verify **Template suffix** is set correctly:
     - `recharge-bundle` for bundle products
     - `subscription` for subscription products
   - Save if needed

2. **Check Recharge Dashboard:**
   - Open Recharge app
   - Verify the product is configured in Recharge
   - Check that bundle/subscription options are set up

3. **Verify App is Active:**
   - Go to **Settings → Apps and sales channels**
   - Find Recharge app
   - Make sure it's installed and active

4. **Still Not Working?**
   - Contact ReCharge support
   - They can help troubleshoot widget display issues

### Yotpo Issues

**Problem:** Reviews not displaying on product pages.

**Solution:**
1. **Check Yotpo Dashboard:**
   - Open Yotpo app
   - Check review sync status
   - Verify reviews exist for the product

2. **Verify Product Has Reviews:**
   - Check if the product has any approved reviews
   - Reviews need to be approved before they display

3. **Check Template:**
   - Product templates should include Yotpo blocks by default
   - If reviews still don't show, contact Yotpo support

### Osano Issues

**Problem:** Cookie consent banner not appearing.

**Solution:**
1. **Check Osano Dashboard:**
   - Open Osano app
   - Verify banner is enabled
   - Check regional settings

2. **Clear Browser:**
   - Clear browser cookies
   - Try incognito/private browsing mode
   - Banner might not show if you've already accepted cookies

3. **Check Ad Blockers:**
   - Some ad blockers can interfere with cookie consent banners
   - Try disabling ad blockers to test

4. **Still Not Working?**
   - Contact Osano support
   - They can help troubleshoot banner display

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **SearchSpring Documentation:** https://support.searchspring.com/
- **Recharge Documentation:** https://support.rechargepayments.com/
- **Yotpo Documentation:** https://docs.yotpo.com/

---

*Last Updated: March 2026 (theme export context; verify app versions in Admin)*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

