# Integrations Documentation

**Superfeet Multi-Region Shopify Plus Platform**

Complete documentation of all third-party app integrations and their theme code implementations.

---

## Table of Contents

1. [Apps with Theme Code Integration](#apps-with-theme-code-integration)
2. [Apps with Metafield Integration](#apps-with-metafield-integration)
3. [Apps without Theme Integration](#apps-without-theme-integration)
4. [Integration Code References](#integration-code-references)
5. [Configuration & Setup](#configuration--setup)
6. [Troubleshooting](#troubleshooting)

---

## Apps with Theme Code Integration

### SearchSpring

**Purpose:** Enhanced product search and filtering beyond Shopify's default search.

**Stores:** US (superfeetww), UK (superfeet-uk), Canada (superfeet-ca)

**Theme Integration:**

**Section:**
- `sections/searchspring-recommendations.liquid` - SearchSpring product recommendations section

**Snippet:**
- `snippets/searchspring-script.liquid` - SearchSpring JavaScript SDK loader

**Layout Integration:**
- `layout/theme.liquid` - SearchSpring Intellisuggest script loaded:
  ```liquid
  <script type="text/javascript" src="//cdn.searchspring.net/intellisuggest/is.min.js"></script>
  ```

**Template Usage:**
- `collection.searchspring.json` - Collection template using SearchSpring
- `main-collection-product-grid-ss.liquid` - SearchSpring product grid section
- `main-search.liquid` - Search results using SearchSpring

**Code Reference:**
```liquid
{% render 'searchspring-script' %}
```

**Configuration:**
- SearchSpring dashboard for product data sync
- Theme settings: `settings.searchspring_region` for regional configuration
- SearchSpring JavaScript SDK replaces default Shopify search

**Important Notes:**
- Essential A/B Testing app is **incompatible** with SearchSpring
- Don't modify SearchSpring integration without understanding full implementation
- SearchSpring has its own dashboard for configuration

**Troubleshooting:**
- Check SearchSpring dashboard for sync status
- Verify JavaScript SDK is loading (browser console)
- Check browser console for errors
- Contact SearchSpring support for integration issues

---

### Recharge Subscriptions

**Purpose:** Product bundles and subscription orders.

**Stores:** US (superfeetww), UK (superfeet-uk), Canada (superfeet-ca)

**Theme Integration:**

**Snippets:**
- `snippets/recharge-choose-your-bundle-customizations.liquid` - Bundle customization UI
- `snippets/recharge-subscription-customizations.liquid` - Subscription customization UI

**Template Usage:**
- `product.recharge-bundle.json` - Recharge bundle product template
- `product.subscription.json` - Subscription product template

**Code Reference:**
```liquid
{% render 'recharge-choose-your-bundle-customizations' %}
{% render 'recharge-subscription-customizations' %}
```

**Template Block:**
```json
{
  "type": "shopify://apps/recharge-subscriptions/blocks/bundles-widget/..."
}
```

**Configuration:**
- Recharge app installed via Shopify App Store
- Subscription products configured in Recharge dashboard
- Checkout flow modified for subscriptions

**Documentation:** Recharge has extensive documentation for theme customization

---

### Yotpo Product Reviews

**Purpose:** Product reviews and user-generated content.

**Stores:** US (superfeetww), UK (superfeet-uk), Canada (superfeet-ca)

**Theme Integration:**

**Template Blocks:**
- Yotpo star rating blocks in product templates:
  ```json
  {
    "type": "shopify://apps/yotpo-product-reviews/blocks/star-rating/..."
  }
  ```

**Template Usage:**
- Product templates include Yotpo review widgets
- Collection templates include Yotpo UGC galleries:
  ```liquid
  <div class="yotpo yotpo-pictures-widget" data-gallery-id="..."></div>
  ```

**Metafields:**
- `yotpo.reviews_average` [single_line_text_field] - Average rating
- `yotpo.reviews_count` [single_line_text_field] - Review count
- `yotpo.richsnippetshtml` [single_line_text_field] - Rich snippets HTML

**Configuration:**
- Reviews collected on US store
- **US reviews automatically syndicated to UK and CA stores**
- ExpertVoice reviews syndicated to US store
- Moderation settings in Yotpo dashboard

**Important:** Don't break review syndication when modifying product templates!

**Troubleshooting:**
- Check Yotpo dashboard for review sync status
- Verify widgets are loading on product pages
- Check browser console for JavaScript errors

---

### Osano Cookie Consent

**Purpose:** GDPR/CCPA compliance cookie consent management.

**Stores:** US (superfeetww), UK (superfeet-uk), Canada (superfeet-ca)

**Theme Integration:**

**Snippet:**
- `snippets/osano-shopify.liquid` - Osano Shopify integration

**Layout Integration:**
- `layout/theme.liquid` - Osano script loaded:
  ```liquid
  <script async src="https://cmp.osano.com/16BR7lSlwnVOl4Jfg/c078783c-4b7d-4855-9d77-f20cbb796003/osano.js"></script>
  ```

**Code Reference:**
```liquid
{% render 'osano-shopify' %}
```

**Configuration:**
- Osano dashboard for consent management
- Cookie policy configuration
- Regional compliance settings

---

### Insole Finder Quiz

**Purpose:** Custom product recommendation tool guiding customers to the right insole.

**Stores:** US (superfeetww), UK (superfeet-uk), Canada (superfeet-ca)

**Theme Integration:**

**Layout:**
- `layout/theme.insole-finder.liquid` - Dedicated layout for Insole Finder pages

**Section:**
- `sections/insole-finder-2.liquid` - Insole Finder section

**Template:**
- `page.insole-finder-2.json` - Insole Finder page template

**Custom App:** Built by Born West & Superfeet

**Configuration:**
- Custom app configuration
- Product recommendation logic
- Quiz flow management

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

## Integration Code References

### SearchSpring Integration

**Section File:** `sections/searchspring-recommendations.liquid`

**Snippet File:** `snippets/searchspring-script.liquid`

**Layout Integration:** `layout/theme.liquid` (line 82)
```liquid
<script type="text/javascript" src="//cdn.searchspring.net/intellisuggest/is.min.js"></script>
```

**Collection Template:** `collection.searchspring.json`

**Search Template:** `main-search.liquid`

### Recharge Integration

**Snippet Files:**
- `snippets/recharge-choose-your-bundle-customizations.liquid`
- `snippets/recharge-subscription-customizations.liquid`

**Product Templates:**
- `product.recharge-bundle.json`
- `product.subscription.json`

### Yotpo Integration

**Template Blocks:**
- Product templates include Yotpo app blocks
- Collection templates include Yotpo UGC widgets

**Example:**
```json
{
  "type": "shopify://apps/yotpo-product-reviews/blocks/star-rating/eb7dfd7d-db44-4334-bc49-c893b51b36cf"
}
```

### Osano Integration

**Snippet File:** `snippets/osano-shopify.liquid`

**Layout Integration:** `layout/theme.liquid` (line 23)
```liquid
<script async src="https://cmp.osano.com/16BR7lSlwnVOl4Jfg/c078783c-4b7d-4855-9d77-f20cbb796003/osano.js"></script>
```

---

## Configuration & Setup

### SearchSpring Setup

1. Install SearchSpring app
2. Configure in SearchSpring dashboard
3. Sync product data
4. Configure search instance per store (US, UK, CA)
5. Assign `collection.searchspring.json` template to collections

### Recharge Setup

1. Install Recharge app
2. Configure subscription products in Recharge dashboard
3. Assign `product.recharge-bundle.json` or `product.subscription.json` templates
4. Configure bundle options

### Yotpo Setup

1. Install Yotpo app
2. Configure review collection settings
3. Set up review syndication (US → UK/CA)
4. Add Yotpo blocks to product templates
5. Configure UGC galleries for collections

### Osano Setup

1. Install Osano app
2. Configure cookie policy
3. Set regional compliance settings
4. Osano script loads automatically via theme

---

## Troubleshooting

### SearchSpring Issues

**Problem:** Search not working or showing default Shopify search.

**Solution:**
1. Check SearchSpring dashboard for sync status
2. Verify SearchSpring JavaScript is loading (browser console)
3. Check collection template is `collection.searchspring.json`
4. Verify SearchSpring app is active
5. Contact SearchSpring support

### Recharge Issues

**Problem:** Bundle or subscription options not showing.

**Solution:**
1. Verify product template is `product.recharge-bundle.json` or `product.subscription.json`
2. Check Recharge dashboard for product configuration
3. Verify Recharge app is active
4. Check browser console for JavaScript errors

### Yotpo Issues

**Problem:** Reviews not displaying or syndication not working.

**Solution:**
1. Check Yotpo dashboard for review sync status
2. Verify Yotpo blocks are in product templates
3. Check browser console for JavaScript errors
4. Verify review syndication settings in Yotpo

### Osano Issues

**Problem:** Cookie consent not appearing.

**Solution:**
1. Verify Osano script is loading (browser console)
2. Check Osano dashboard for configuration
3. Clear browser cookies and test
4. Check if ad blockers are interfering

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **SearchSpring Documentation:** https://support.searchspring.com/
- **Recharge Documentation:** https://support.rechargepayments.com/
- **Yotpo Documentation:** https://docs.yotpo.com/

---

*Last Updated: Based on theme exports from November 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

