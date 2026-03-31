# Integrations Map

## Integration Classification

### Theme-Integrated Apps

These apps require theme code integration or template assignments:

#### SearchSpring
**Type:** Theme-integrated  
**Stores:** US, UK, Canada  
**Template Requirement:** `searchspring` suffix on collections  
**Theme Files:**
- `assets/searchspring.bundle.js` (store-specific configuration)
- Template: `collection.searchspring.json`

**Configuration:**
- Assign `searchspring` template suffix to collections
- Configure in SearchSpring dashboard (not Shopify Admin)
- Each store has its own SearchSpring instance

**Important:** Incompatible with Essential A/B Testing - don't run A/B tests on SearchSpring collections

**Reference:** `docs/integrations.md` - SearchSpring

#### Recharge Subscriptions
**Type:** Theme-integrated  
**Stores:** US, UK, Canada  
**Template Requirements:**
- `recharge-bundle` suffix for bundle products
- `subscription` suffix for subscription products

**Theme Files:**
- Templates: `product.recharge-bundle.json`, `product.subscription.json`
- Recharge widget loads automatically on product pages

**Configuration:**
- Assign template suffix in Shopify Admin
- Configure bundle/subscription options in Recharge dashboard
- Bundle pricing managed in Recharge (not Shopify)

**Note:** Subscriptions available but not currently activated

**Reference:** `docs/integrations.md` - Recharge Subscriptions

#### Yotpo Product Reviews
**Type:** Theme-integrated  
**Stores:** US, UK, Canada  
**Theme Files:**
- Yotpo blocks in product templates
- Review widgets render on product pages
- UGC gallery sections available

**Metafields:**
- `yotpo.reviews_average` [auto-generated]
- `yotpo.reviews_count` [auto-generated]
- `yotpo.richsnippetshtml` [auto-generated]

**Configuration:**
- Reviews sync automatically between stores
- Moderate reviews in Yotpo dashboard
- Add UGC gallery via Theme Customizer

**Reference:** `docs/integrations.md` - Yotpo Product Reviews

#### Insole Finder
**Type:** Theme-integrated (custom app)  
**Stores:** US, UK, Canada  
**Theme Files:**
- `layout/theme.insole-finder.liquid` - Custom layout
- Insole Finder-specific assets

**Template Requirement:** `insole-finder-2` suffix on pages  
**Purpose:** Custom product recommendation quiz  
**Built by:** Born West & Superfeet (separate app)

**Reference:** `docs/theme-architecture-v2.md` - Custom Features

### Backend-Only Apps

These apps run automatically with no theme code integration:

#### Matrixify
**Purpose:** Bulk data import/export and backups  
**Stores:** US, UK, CA  
**Integration:** App-only, no theme code  
**Usage:** Bulk product updates, inventory management, data backups

#### Elevar Conversion Tracking
**Purpose:** Server-side conversion tracking  
**Stores:** US, UK, CA  
**Integration:** JavaScript loaded via `{{ content_for_header }}`  
**Connected Services:** GA4, Facebook Pixel, Klaviyo, Google Ads

#### Klaviyo
**Purpose:** Email and SMS marketing automation  
**Stores:** US, UK, CA  
**Integration:** JavaScript loaded via `{{ content_for_header }}`

#### Regios Discounts
**Purpose:** Advanced discount logic  
**Stores:** US only  
**Integration:** App-only, no theme code

#### Geo:Pro Geolocation
**Purpose:** Automatic regional redirection  
**Stores:** US only  
**Integration:** JavaScript-based redirection (app handles)  
**Note:** Don't implement manual geolocation - Geo:Pro handles this

#### Shipfy: Shipping Rules
**Purpose:** Complex shipping rule management  
**Stores:** US only  
**Integration:** App-only, no theme code

#### StoreRocket Store Locator
**Purpose:** Physical store finder  
**Stores:** US, UK, CA  
**Integration:** App-only, no theme code

#### Avalara Tax Compliance
**Purpose:** Tax calculation  
**Stores:** US, UK, CA  
**Integration:** App-only, no theme code

#### AfterShip Order Tracking
**Purpose:** Order tracking  
**Stores:** US, UK, CA  
**Integration:** App-only, no theme code

#### Osano Cookie Consent
**Purpose:** GDPR/CCPA cookie consent  
**Stores:** US, UK, CA  
**Integration:** JavaScript loaded via app  
**Note:** Banner appears automatically on all pages

#### Google Shopping (mm-google-shopping)
**Purpose:** Google Merchant Center product feed  
**Stores:** US, UK, CA  
**Integration:** Metafield-based  
**Metafields:** Product and variant metafields populate feed

#### Facebook (mc-facebook)
**Purpose:** Facebook product catalog  
**Stores:** US, UK, CA  
**Integration:** Metafield-based  
**Metafields:** Product metafields populate catalog

**Reference:** `docs/integrations.md` - Apps without Theme Integration

## High-Signal Integrations

### SearchSpring
**Why Important:** Powers enhanced search and filtering on major collections  
**Theme Touchpoints:**
- `assets/searchspring.bundle.js` (store-specific)
- `templates/collection.searchspring.json`
- Collection template suffix assignment

**Debugging:**
- Check template suffix is `searchspring` (lowercase)
- Verify SearchSpring dashboard sync status
- Check app is active in Shopify Admin

**Reference:** `docs/integrations.md` - SearchSpring

### Recharge
**Why Important:** Enables product bundles and subscriptions  
**Theme Touchpoints:**
- `templates/product.recharge-bundle.json`
- `templates/product.subscription.json`
- Product template suffix assignment

**Debugging:**
- Check template suffix (`recharge-bundle` or `subscription`)
- Verify Recharge dashboard configuration
- Check app is active in Shopify Admin

**Reference:** `docs/integrations.md` - Recharge Subscriptions

### Yotpo
**Why Important:** Product reviews and UGC  
**Theme Touchpoints:**
- Yotpo blocks in product templates
- UGC gallery sections
- Auto-generated metafields

**Debugging:**
- Check Yotpo dashboard for review sync
- Verify reviews are approved
- Check product template includes Yotpo blocks

**Reference:** `docs/integrations.md` - Yotpo Product Reviews

## Integration Debugging Patterns

### Template Suffix Issues

**Problem:** App feature not appearing on page

**Checklist:**
1. Verify template suffix is assigned correctly
2. Check suffix spelling (case-sensitive, no spaces)
3. Verify template file exists (`templates/{type}.{suffix}.json`)
4. Check app is active in Shopify Admin
5. Clear browser cache and test

**Reference:** `docs/integrations.md` - Troubleshooting

### App Configuration Issues

**Problem:** App feature not working as expected

**Checklist:**
1. Check app dashboard for configuration
2. Verify app is synced (if applicable)
3. Check app-specific settings
4. Review app documentation
5. Contact app support if needed

**Reference:** `docs/integrations.md` - Configuration & Setup

### Multi-Store Considerations

**Problem:** Integration works on one store but not others

**Checklist:**
1. Verify app is installed on all stores
2. Check store-specific configurations (e.g., SearchSpring instance)
3. Verify template assignments are consistent
4. Check store-specific settings in app dashboard

**Reference:** `docs/theme-architecture-v2.md` - Multi-Region Architecture

## Integration Setup Workflows

### Setting Up SearchSpring on a Collection

1. Go to **Collections** → Select collection
2. Scroll to **Search engine listing**
3. Set **Template suffix:** `searchspring`
4. Save
5. Configure in SearchSpring dashboard
6. Verify on storefront

**Reference:** `docs/integrations.md` - SearchSpring Setup

### Setting Up Recharge Bundle/Subscription

1. Go to **Products** → Select product
2. Set **Template suffix:** `recharge-bundle` or `subscription`
3. Save
4. Configure in Recharge dashboard
5. Set pricing and options in Recharge
6. Verify on storefront

**Reference:** `docs/integrations.md` - Recharge Setup
