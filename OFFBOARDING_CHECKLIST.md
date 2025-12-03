# Superfeet Platform Offboarding Checklist

**Client:** Superfeet Worldwide  
**Platform:** Shopify Plus Multi-Region eCommerce  
**Offboarding Date:** [Date TBD]  
**Completed By:** [Name]

---

## Overview

This checklist ensures all platform access, third-party services, documentation, and knowledge transfer is completed before project handoff. Use this document to track progress and confirm completion of each item.

**Status Legend:**
- [ ] Not Started
- [🔄] In Progress
- [✅] Complete
- [⚠️] Blocked / Needs Attention

---

## 1. Third-Party App & Service Ownership Transfer

### 1.1 Shopify App Ownership

Transfer app ownership/access for all installed Shopify apps. Document billing contacts and admin access.

**Priority Apps (Installed on Multiple Stores):**
- [ ] **AfterShip Order Tracking** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Matrixify** (superfeetww, superfeet-uk, superfeet-ca) - Big Plan
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Elevar Conversion Tracking** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - GA4, Facebook, Klaviyo, Google Ads connections verified
  - Notes: ________________

- [ ] **Recharge Subscriptions** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Yotpo Product Reviews** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Review syndication settings documented
  - Admin access granted to client team
  - Notes: ________________

- [ ] **SearchSpring** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Klaviyo** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **StoreRocket Store Locator** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Osano Cookie Consent** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

- [ ] **Avalara Tax Compliance** (superfeetww, superfeet-uk, superfeet-ca)
  - Ownership transfer completed
  - Billing migrated to client account
  - Admin access granted to client team
  - Notes: ________________

**US-Only Apps:**
- [ ] **Regios Discounts** (superfeetww)
- [ ] **Shopcodes** (superfeetww)
- [ ] **Essential Preorder** (superfeetww)
- [ ] **Geo:Pro Geolocation** (superfeetww)
- [ ] **Awin** (superfeetww)
- [ ] **Shipfy: Shipping Rules** (superfeetww)
- [ ] **Fraud Control** (superfeetww)
- [ ] **GOVX ID Exclusive Discounts** (superfeetww)
- [ ] **Insole Finder Quiz** (superfeetww, superfeet-uk, superfeet-ca) - Custom app by Born West & Superfeet

**Apps Requiring Investigation:**
- [ ] **Statlas** - Purpose and usage to be documented
- [ ] **GRIN Influencer Marketing** - Confirm if still active or replaced by Awin
- [ ] **Essential A/B Testing** - Currently incompatible with SearchSpring, needs resolution

**Unused Apps to Remove:**
- [ ] **Bagpiper Data Export** - Replaced by Matrixify
- [ ] **Forms** - Not in use

### 1.2 External Service Ownership Transfer

Transfer ownership and access for external services not installed via Shopify app store.

- [ ] **AfterShip** (Order Tracking)
  - Account ownership transferred
  - Billing information updated
  - Admin credentials shared securely
  - API keys documented (if applicable)
  - Notes: ________________

- [ ] **Google Search Console**
  - Property ownership verified/transferred
  - Client email added as owner
  - Verification confirmed
  - Access granted for all properties (superfeet.com, superfeet.ca, superfeet.co.uk, etc.)
  - Notes: ________________

- [ ] **Google Merchant Center**
  - Account ownership transferred
  - Billing information updated
  - Product feed access granted
  - Client team trained on feed management
  - Notes: ________________

- [ ] **Microsoft Clarity** (Analytics)
  - Account ownership transferred
  - Admin access granted
  - Recording settings documented
  - Notes: ________________

- [ ] **SEMRush / Ahrefs** (SEO Tools)
  - Account ownership transferred
  - Billing migrated
  - Project access granted
  - Historical data export completed (if needed)
  - Notes: ________________

- [ ] **Calibreapp** (Performance Monitoring)
  - Account ownership transferred
  - Currently owned by Arcadia Digital - needs transfer
  - Performance budgets documented
  - Monitoring settings documented
  - Alert recipients updated
  - Notes: ________________

- [ ] **Google Analytics 4 (GA4)**
  - Property ownership transferred
  - Admin access granted
  - Elevar server-side tracking configuration documented
  - Custom events and conversions documented
  - Notes: ________________

- [ ] **Facebook Business Manager / Meta Pixel**
  - Pixel ownership verified
  - Business Manager access granted
  - Elevar server-side tracking configuration documented
  - Notes: ________________

- [ ] **Google Ads**
  - Account ownership transferred
  - Billing migrated
  - Conversion tracking via Elevar documented
  - Notes: ________________

### 1.3 Domain & DNS Management

- [ ] Domain registrar access (superfeet.com, superfeet.ca, superfeet.co.uk, superfeet.eu, superfeet.com.au)
- [ ] DNS management access
- [ ] SSL certificate renewal process documented
- [ ] DNS records documented (A records, CNAMEs, TXT records for verification, etc.)

### 1.4 Code Repository Access

- [ ] GitHub/GitLab repository access (if custom theme development)
- [ ] Repository ownership transferred or client added as collaborator
- [ ] CI/CD pipeline access (if applicable)
- [ ] Deployment credentials documented

---

## 2. Documentation Handoff

### 2.1 AI Assistant Handoff Documentation

Create comprehensive documentation that enables AI coding assistants (Cursor, Claude Code, GitHub Copilot) to understand and work with the Superfeet platform.

**Location:** Create in `/handoff-documentation/ai-handoff.md` or similar

- [ ] **Platform Architecture Overview**
  - Multi-store architecture explanation
  - Regional store structure (US, CA, UK, EU, AU)
  - Theme structure and organization
  - Key integrations and data flows

- [ ] **Codebase Structure**
  - Theme file organization
  - Custom snippets and sections
  - Asset management
  - Template structure

- [ ] **Development Workflow**
  - Local development setup
  - Theme deployment process
  - Testing procedures
  - Code review guidelines

- [ ] **Key Integrations & APIs**
  - Elevar server-side tracking implementation
  - SearchSpring integration points
  - Recharge subscription flows
  - Klaviyo event tracking
  - Custom Insole Finder app architecture

- [ ] **Common Tasks & Code Patterns**
  - Product data management
  - Collection management
  - Metafield usage
  - Liquid template best practices
  - JavaScript customizations

- [ ] **Testing & Debugging**
  - How to test multi-region functionality
  - How to debug tracking issues
  - Performance testing procedures
  - Browser compatibility requirements

- [ ] **Known Issues & Technical Debt**
  - Essential A/B Testing incompatibility with SearchSpring
  - Areas requiring future refactoring
  - Browser-specific quirks or workarounds

### 2.2 Developer Handoff Documentation

Create detailed documentation for human developers taking over the platform.

**Location:** Create in `/handoff-documentation/developer-handoff.md` or similar

- [ ] **Platform Architecture Deep Dive**
  - Multi-store setup rationale
  - Regional configuration differences
  - Inventory and pricing management across stores
  - Shipping and tax configuration

- [ ] **Development Environment Setup**
  - Shopify CLI setup
  - Theme development workflow
  - Local testing environment
  - Staging/production deployment process

- [ ] **Theme Customization Guide**
  - Section development
  - Snippet creation and usage
  - Asset management
  - Custom JavaScript structure
  - CSS architecture

- [ ] **App Integration Details**
  - For each major app:
    - Configuration locations
    - Custom integration points
    - API usage and rate limits
    - Troubleshooting common issues
    - Upgrade/maintenance procedures

- [ ] **Data Management**
  - Product import/export procedures
  - Matrixify workflows
  - Metafield management
  - Inventory sync processes
  - Review syndication (Yotpo)

- [ ] **Performance Optimization**
  - Core Web Vitals monitoring
  - Performance budget management (Calibreapp)
  - Image optimization practices
  - JavaScript bundle optimization
  - Caching strategies

- [ ] **Analytics & Tracking**
  - Elevar configuration and event tracking
  - GA4 custom events
  - Conversion tracking setup
  - Debugging tracking issues
  - Server-side vs client-side tracking

- [ ] **SEO & Marketing**
  - URL redirect management (4,400+ redirects)
  - Meta tag management
  - Structured data implementation
  - Google Merchant Center feed management

- [ ] **Troubleshooting Guide**
  - Common issues and solutions
  - Error logs and where to find them
  - Support escalation paths
  - App vendor contact information

- [ ] **Emergency Procedures**
  - How to rollback theme changes
  - How to disable problematic apps
  - How to restore from backups
  - Contact information for critical vendors

### 2.3 Business User Documentation

Ensure existing documentation is up-to-date for client business users.

- [ ] Review and update `/superfeet-platform-documentation.html`
- [ ] Verify all screenshots and examples are current
- [ ] Update any outdated procedures
- [ ] Add any missing workflows discovered during offboarding
- [ ] Ensure documentation is accessible to client team
- [ ] Provide training session or recorded walkthroughs (if needed)

---

## 3. Access & Credentials

### 3.1 Shopify Store Access

- [ ] **US Store (superfeetww)**
  - Client team has admin access
  - Staff accounts created for key users
  - Roles and permissions configured
  - Two-factor authentication enforced

- [ ] **Canada Store (superfeet-ca)**
  - Client team has admin access
  - Staff accounts created for key users
  - Roles and permissions configured
  - Two-factor authentication enforced

- [ ] **UK Store (superfeet-uk)**
  - Client team has admin access
  - Staff accounts created for key users
  - Roles and permissions configured
  - Two-factor authentication enforced

### 3.2 Credential Documentation

**⚠️ Security Note:** Store credentials in a secure password manager, not in documentation files. Reference where credentials are stored.

- [ ] **Shopify Admin Credentials**
  - Location: ________________
  - Last updated: ________________

- [ ] **Domain Registrar Credentials**
  - Location: ________________
  - Last updated: ________________

- [ ] **Third-Party Service Credentials**
  - Location: ________________
  - Last updated: ________________

- [ ] **API Keys & Tokens**
  - Location: ________________
  - Last updated: ________________
  - Note: Document which keys are used where, but never commit actual keys to repositories

### 3.3 Shared Resources

- [ ] Shared password manager vault created (1Password, LastPass, etc.)
- [ ] Client team has access to shared vault
- [ ] All credentials migrated to shared vault
- [ ] Access audit completed (remove old/unauthorized access)

---

## 4. Knowledge Transfer Sessions

### 4.1 Technical Team Handoff

- [ ] **Architecture Overview Session**
  - Multi-store architecture
  - Key technical decisions and rationale
  - Integration points
  - Q&A session

- [ ] **Development Workflow Session**
  - Local development setup
  - Deployment process
  - Testing procedures
  - Code review process

- [ ] **App Management Session**
  - Major app configurations
  - Custom integrations
  - Troubleshooting common issues
  - Vendor relationships

### 4.2 Business User Training

- [ ] **Content Management Training**
  - Product management
  - Collection management
  - Page editing
  - Blog post management

- [ ] **Marketing Tools Training**
  - Klaviyo campaign setup
  - Discount code management
  - SearchSpring merchandising
  - Yotpo review management

- [ ] **Analytics & Reporting Training**
  - GA4 navigation and reporting
  - Calibreapp performance monitoring
  - Shopify analytics basics
  - Custom report creation

---

## 5. Operational Handoff

### 5.1 Ongoing Maintenance

- [ ] **Theme Updates**
  - Update schedule documented
  - Review process for Shopify OS updates
  - Custom code compatibility checks

- [ ] **App Updates**
  - Update review process
  - Testing procedures before updates
  - Rollback procedures

- [ ] **Backup Procedures**
  - Matrixify backup schedule
  - Theme backup procedures
  - Data export procedures
  - Recovery testing

### 5.2 Support & Escalation

- [ ] **Support Contacts Documented**
  - Shopify Plus support
  - Major app vendor support
  - Domain/DNS support
  - Emergency escalation path

- [ ] **Support SLAs Documented**
  - Response time expectations
  - Resolution timeframes
  - After-hours support procedures

- [ ] **Issue Tracking**
  - System for tracking known issues
  - Process for reporting new issues
  - Priority classification system

### 5.3 Monitoring & Alerts

- [ ] **Performance Monitoring (Calibreapp)**
  - Alert recipients updated
  - Performance budgets reviewed
  - Monitoring frequency confirmed

- [ ] **Uptime Monitoring**
  - Setup monitoring for all storefronts
  - Alert recipients configured
  - Escalation procedures documented

- [ ] **Error Monitoring**
  - JavaScript error tracking setup
  - Server error monitoring
  - Alert configuration

---

## 6. Financial & Billing

### 6.1 Billing Transfers

- [ ] **Shopify Plus Subscription**
  - Billing contact updated
  - Payment method updated
  - Invoices forwarded to client

- [ ] **App Subscriptions**
  - All app billing transferred to client
  - Subscription details documented
  - Renewal dates documented

- [ ] **External Services**
  - All third-party service billing transferred
  - Cancellation of Arcadia-managed subscriptions
  - Final invoice reconciliation

### 6.2 Budget & Cost Documentation

- [ ] **Monthly Operating Costs Documented**
  - Shopify Plus fees
  - App subscription costs
  - External service costs
  - Estimated annual costs

- [ ] **Cost Optimization Recommendations**
  - Apps that could be consolidated
  - Services that could be optimized
  - Future cost considerations

---

## 7. Final Checklist Items

### 7.1 Documentation Completeness

- [ ] All documentation links are accessible
- [ ] All screenshots are current and accurate
- [ ] All procedures have been tested
- [ ] Contact information is up-to-date
- [ ] Version numbers and dates are accurate

### 7.2 Client Readiness

- [ ] Client team confirms access to all systems
- [ ] Client team has completed necessary training
- [ ] Client team knows how to access documentation
- [ ] Client team understands escalation procedures
- [ ] Client team has backup contacts for critical vendors

### 7.3 Arcadia Digital Cleanup

- [ ] Remove Arcadia staff from Shopify stores (unless retainer relationship)
- [ ] Remove Arcadia access from third-party services
- [ ] Cancel Arcadia-managed subscriptions
- [ ] Archive project files appropriately
- [ ] Final project retrospective completed (if applicable)

---

## 8. Post-Offboarding Support

### 8.1 Transition Period

- [ ] **30-Day Support Window**
  - Response time commitment: ________________
  - Scope of support: ________________
  - Communication channel: ________________

- [ ] **Knowledge Base Access**
  - Client has access to all documentation
  - Documentation is self-service friendly
  - Search functionality works

### 8.2 Retainer Options (if applicable)

- [ ] Retainer scope discussed and documented
- [ ] Ongoing support structure defined
- [ ] Response time SLAs agreed upon
- [ ] Billing structure established

---

## Notes & Open Items

**Add any notes, concerns, or items that need follow-up:**

- ________________
- ________________
- ________________

---

## Completion Sign-Off

**Client Approval:**
- Name: ________________
- Date: ________________
- Signature: ________________

**Arcadia Digital:**
- Name: ________________
- Date: ________________
- Signature: ________________

---

*This checklist should be reviewed and updated throughout the offboarding process. Final version should be saved as a completed record.*

