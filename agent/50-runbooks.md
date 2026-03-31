# Runbooks: Common Workflows and Troubleshooting

## Common Workflows

### Making a Simple Text Change

**Goal:** Update text on a page (e.g., header, footer, section)

**Steps:**
1. **Start Local Development:**
   ```bash
   shopify theme dev --store superfeetww
   ```

2. **Identify the Section:**
   - Check template → find section name
   - Locate section file: `sections/{section-name}.liquid`

3. **Make the Change:**
   - Find text string in section file
   - Edit text
   - Save file

4. **Verify:**
   - Check preview URL (auto-opens)
   - Or visit `http://127.0.0.1:9292`
   - Change should appear immediately

5. **Push to Staging:**
   ```bash
   shopify theme push --unpublished --store superfeetww
   ```

6. **Test on Staging:**
   - Review staging theme preview URL
   - Verify change works correctly

**Reference:** `docs/technical-user-guide-v2.md` - Quick Start

### Adding SearchSpring to a Collection

**Goal:** Enable SearchSpring search and filtering on a collection

**Steps:**
1. **Assign Template Suffix:**
   - Go to **Collections** → Select collection
   - Scroll to **Search engine listing**
   - Set **Template suffix:** `searchspring`
   - Save

2. **Configure in SearchSpring Dashboard:**
   - Open SearchSpring app from Shopify Apps
   - Configure search settings, filters, recommendations
   - Product data syncs automatically

3. **Verify:**
   - Visit collection page on storefront
   - Should see SearchSpring's enhanced search and filtering
   - If default Shopify search appears, check template suffix

**Reference:** `docs/integrations.md` - SearchSpring Setup

### Setting Up Recharge Bundle/Subscription

**Goal:** Enable Recharge bundle or subscription on a product

**Steps:**
1. **Assign Template Suffix:**
   - Go to **Products** → Select product
   - Set **Template suffix:** `recharge-bundle` or `subscription`
   - Save

2. **Configure in Recharge Dashboard:**
   - Open Recharge app from Shopify Apps
   - Configure bundle options or subscription settings
   - Set pricing and product options

3. **Verify:**
   - Visit product page on storefront
   - Should see Recharge bundle or subscription widget
   - If widget doesn't appear, check template suffix and Recharge configuration

**Reference:** `docs/integrations.md` - Recharge Setup

### Updating Product Metafields in Bulk

**Goal:** Update metafield values for multiple products

**Steps:**
1. **Export Products:**
   - Use Matrixify app
   - Export products with all metafield columns
   - Download CSV/Excel file

2. **Modify Metafield Values:**
   - Open exported file
   - Update metafield columns
   - Save file

3. **Import Updated File:**
   - Upload to Matrixify
   - Preview changes
   - Import to store

**Important:** Always backup before bulk changes!

**Reference:** `docs/data-guide.md` - Bulk Data Management

### Multi-Store Theme Update

**Goal:** Deploy theme changes across all stores

**Steps:**
1. **Develop on US Store:**
   - Make changes on `superfeetww` (reference store)
   - Test thoroughly
   - Push to staging

2. **Use Build System (Primary Method):**
   - Process shared codebase through build system
   - Generates store-specific themes for CA and UK
   - Test generated themes on staging

3. **Alternative: Manual File Copy:**
   - Copy updated files to other stores
   - Use Shopify CLI or Matrixify
   - Test on each store's staging

4. **Deploy:**
   - Push to live on each store
   - Verify changes work correctly
   - Check store-specific configurations (SearchSpring, settings)

**Reference:** `docs/theme-architecture-v2.md` - Multi-Region Architecture

## Troubleshooting Checklists

### SearchSpring Not Working

**Problem:** Search not working or showing default Shopify search

**Checklist:**
1. ✅ Check template suffix is `searchspring` (lowercase, no spaces)
2. ✅ Verify SearchSpring dashboard sync status
3. ✅ Check app is active in Shopify Admin
4. ✅ Verify collection is configured in SearchSpring
5. ✅ Contact SearchSpring support if still not working

**Reference:** `docs/integrations.md` - Troubleshooting

### Recharge Widget Not Showing

**Problem:** Bundle or subscription widget not appearing on product page

**Checklist:**
1. ✅ Check template suffix (`recharge-bundle` or `subscription`)
2. ✅ Verify product is configured in Recharge dashboard
3. ✅ Check Recharge app is active
4. ✅ Check browser console for JavaScript errors
5. ✅ Verify mutation observer is working
6. ✅ Contact ReCharge support if still not working

**Reference:** `docs/integrations.md` - Troubleshooting

### Metafields Not Displaying

**Problem:** Metafield values not showing on page

**Checklist:**
1. ✅ Verify metafield exists on product/page/collection
2. ✅ Check metafield namespace is correct (`cql.*`, `custom.*`, etc.)
3. ✅ Verify metafield value is set in Shopify Admin
4. ✅ Check Liquid code for typos
5. ✅ Use `{% if %}` check before accessing metafield
6. ✅ Verify metafield type matches usage (text vs number vs boolean)

**Reference:** `docs/technical-user-guide-v2.md` - Troubleshooting

### Template Not Working

**Problem:** Template changes not appearing or template not loading

**Checklist:**
1. ✅ Verify template suffix is correct (case-sensitive)
2. ✅ Check template file exists in theme
3. ✅ Verify template JSON is valid
4. ✅ Check for missing sections referenced in template
5. ✅ Test with default template to isolate issue
6. ✅ Check browser console for errors

**Reference:** `docs/technical-user-guide-v2.md` - Troubleshooting

### Theme Not Loading

**Problem:** Theme not rendering or showing errors

**Checklist:**
1. ✅ Check Shopify status page (status.shopify.com)
2. ✅ Verify theme is published
3. ✅ Check browser console for errors
4. ✅ Clear browser cache
5. ✅ Check `theme.liquid` for syntax errors
6. ✅ Verify all required files exist
7. ✅ Run `shopify theme check --store superfeetww`

**Reference:** `docs/technical-user-guide-v2.md` - Troubleshooting

## Setup/Validation Procedures

### Development Environment Setup

**Goal:** Set up local development environment

**Steps:**
1. **Install Prerequisites:**
   - Node.js (v16 or higher)
   - Git
   - Shopify CLI: `npm install -g @shopify/cli @shopify/theme`

2. **Authenticate:**
   ```bash
   shopify auth login
   ```
   - Select store: `superfeetww` (US), `superfeet-ca` (Canada), or `superfeet-uk` (UK)

3. **Start Development:**
   ```bash
   shopify theme dev --store superfeetww
   ```

4. **Verify:**
   - Preview URL should open automatically
   - Changes should hot-reload

**Reference:** `docs/technical-user-guide-v2.md` - Development Environment Setup

### Theme Validation

**Goal:** Check theme for errors before deployment

**Steps:**
1. **Run Theme Check:**
   ```bash
   shopify theme check --store superfeetww
   ```

2. **Review Errors:**
   - Fix syntax errors
   - Address warnings
   - Verify file structure

3. **Test Locally:**
   - Use `shopify theme dev`
   - Test key pages and features
   - Check browser console for errors

4. **Test on Staging:**
   - Push to staging theme
   - Test all functionality
   - Verify multi-store compatibility

**Reference:** `docs/technical-user-guide-v2.md` - Troubleshooting

## Safe Change Procedures

### Making Theme Changes

**Best Practices:**
1. **Always work on staging first**
2. **Test thoroughly before deploying to live**
3. **Backup theme before major changes** (use Matrixify export)
4. **Document changes** (what, why, when)
5. **Test on all stores** (US, CA, UK)
6. **Check mobile responsiveness**
7. **Verify integrations still work** (SearchSpring, Recharge, Yotpo)

**Reference:** `docs/technical-user-guide-v2.md` - Development Workflow

### Multi-Store Considerations

**Before Making Changes:**
1. ✅ Understand which stores are affected
2. ✅ Check store-specific configurations
3. ✅ Verify SearchSpring instances are correct
4. ✅ Check market context files (UK store)
5. ✅ Test on each store's staging

**After Making Changes:**
1. ✅ Test on US store first (reference)
2. ✅ Use build system to generate other store themes
3. ✅ Test on each store's staging
4. ✅ Verify store-specific features work
5. ✅ Deploy to live on all stores

**Reference:** `docs/theme-architecture-v2.md` - Multi-Region Architecture

### Integration Changes

**Before Modifying Integrations:**
1. ✅ Understand how integration works
2. ✅ Check integration documentation
3. ✅ Verify app is active
4. ✅ Test on staging first
5. ✅ Contact app support if unsure

**After Modifying Integrations:**
1. ✅ Test integration functionality
2. ✅ Verify tracking/analytics still work
3. ✅ Check for JavaScript errors
4. ✅ Test on all stores
5. ✅ Monitor for issues after deployment

**Reference:** `docs/integrations.md` - Troubleshooting
