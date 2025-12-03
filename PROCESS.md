# Client Documentation Process

## Phase 1: Discovery & Analysis

### 1.1 Stakeholder Mapping
**Goal:** Create comprehensive stakeholder map before beginning documentation

**Process:**
1. **Identify All User Types:** Technical, business, and end-user stakeholders
2. **Conduct Formal Interviews:** Structured interviews with each stakeholder group
3. **Document Pain Points:** Current system limitations and user frustrations
4. **Define Success Criteria:** Clear metrics for project success

**Stakeholder Analysis Template:**
- Role: [Technical/Business/End-User]
- Current System Usage: [Primary functions]
- Pain Points: [Specific challenges]
- Success Criteria: [What success looks like]
- Documentation Needs: [Specific content requirements]

**Output:** Comprehensive stakeholder map with interview findings

### 1.2 Technical Landscape Mapping
**Goal:** Understand the complete technical ecosystem

**Key Questions:**
- What are the core systems and platforms?
- How do they integrate with each other?
- What are the data flows and dependencies?
- Who are the different user types and their needs?

**Process:**
1. **System Mapping:** Document all current integrations and dependencies
2. **Performance Baseline:** Establish current performance metrics (when applicable)
3. **Data Flow Analysis:** Map data flows between all systems
4. **Migration Complexity Assessment:** Identify technical challenges early (for migrations)

**Multi-Instance/Multi-Region Analysis (XeroShoes):**
For multi-instance or multi-region platforms:
1. **Codebase Comparison:** Analyze similarities and differences between instances
2. **App Integration Analysis:** Document app differences per instance
3. **Configuration Variations:** Document region-specific settings
4. **Pre-Launch Documentation:** Document pre-launch state with post-launch update plan

**Output:** Technical architecture overview with migration complexity scoring (if applicable) and multi-instance comparison (if applicable)

### 1.3 Content Audit
**Goal:** Catalog existing documentation and knowledge

**Key Questions:**
- What documentation already exists?
- What's missing or outdated?
- What are the pain points for users?
- What information is most critical?

**Output:** Content inventory and gaps analysis

## Phase 2: Documentation Creation

### 2.1 Structure Planning
**Goal:** Organize information for maximum clarity

**Key Principles:**
- **Business-first** - Write for business users, not just developers
- **Progressive disclosure** - Start high-level, drill down to details
- **Use case driven** - Organize around what users need to accomplish
- **Visual hierarchy** - Clear headings, sections, and navigation

**Documentation-First Development:**
- Begin documentation during development, not post-launch
- Create documentation alongside development (parallel process)
- Developer documentation: Technical team documents as they build
- Business documentation: Business team documents processes as they learn
- Integration testing: Document testing procedures during development

**Benefits:**
- Higher quality documentation
- Reduced post-launch support burden
- Better knowledge transfer
- Earlier identification of gaps

### 2.2 Content Development
**Goal:** Create comprehensive, accurate documentation

**Required Documentation Files (Always Generate):**
1. **README.md** - Static memory file for complete project context
2. **docs/theme-architecture.md** - Technical architecture and code structure
3. **docs/technical-user-guide.md** - Developer-focused documentation with code references
4. **docs/business-user-guide.md** - Content management workflows for business users
5. **docs/data-guide.md** - Complete metafield and metaobject reference
6. **docs/integrations.md** - Third-party app integration documentation
7. **docs/QUICK_REFERENCE.md** - Quick lookup tables and common tasks

**Conditional Documentation (Generate When Available):**
- **docs/performance.md** - Generated from prework performance audits
- **docs/accessibility.md** - Generated from prework accessibility audits

**Content Sources:**
- Theme code analysis (sections, snippets, templates)
- Data exports (Matrixify, Shopify exports)
- App list from Shopify admin
- Prework audits (performance, accessibility)
- Theme settings schema

**Audience Separation:**
- **Technical User Guide:** Developer-focused, code-heavy, all page types, template assignments, customizer sections
- **Business User Guide:** Workflow-focused, client-specific features only (exclude generic Shopify documentation)
- **Data Guide:** Reference documentation for all audiences, organized by namespace
- **Integrations Guide:** Technical reference for developers/operations, includes code references

**Visual Documentation Standards:**
- **Screenshots:** Consistent sizing and annotation
- **Diagrams:** Standardized symbols and color coding
- **Flowcharts:** Process flow documentation
- **Architecture Diagrams:** System relationship visualization

**Visual Documentation Tools:**
- Figma for visual mockups
- Lucidchart for process diagrams
- Snagit for screenshot annotation
- Arcadia brand guidelines for consistency

**Evidence-Based Approach (XeroShoes):**
- Base documentation on actual codebase analysis (theme exports, data exports)
- Document only integrations with actual theme code evidence
- Verify all documentation against source material
- Use complete theme exports as source of truth
- Base documentation on actual CSV/data exports
- All documentation verified against source material
- Preserve investigation patterns and failure examples
- Use real error logs and test data for troubleshooting guides

**Investigation Pattern Documentation (Winzer):**
- Date-organized investigation folders (`investigations/DDMMMYYYY[-N]/`)
- Real error logs and test data preserved
- Pattern matching for similar issues
- Evidence-based troubleshooting approach
- Preserves real failure patterns for faster troubleshooting
- Builds knowledge base over time

**Navigation Documentation Standards (RUDIS):**
Navigation documentation must bridge the gap between Shopify Admin (menu creation) and Theme Customizer (menu assignment). This requires explicit mapping and comprehensive section documentation.

**Required Components:**
1. **Menu-to-Section Mapping Table** - Explicit reference table showing:
   - Which menu setting controls which visible element
   - Exact Theme Customizer location (section → setting)
   - Desktop vs. mobile display behavior
   - All configurable elements beyond just menus

2. **Comprehensive Global Section Documentation** - For each global section (Header, Announcement Bar, Footer):
   - Menu assignments (which menu setting controls which menu)
   - All non-menu elements (logo, text blocks, images, social media, etc.)
   - Configuration paths (exact Theme Customizer navigation)
   - Desktop vs. mobile behavior (how elements differ on different devices)
   - Block-based vs. direct assignment methods

3. **Mega Menu Configuration** (if applicable):
   - Menu structure requirements (nested menus in Shopify Admin)
   - Block configuration (mega menu blocks in Theme Customizer)
   - Name matching requirements (case-sensitive matching)
   - Promo content and activity links documentation

4. **Menu Management Guide** - Separate section covering:
   - Creating menus in Shopify Admin
   - Editing menu items
   - Menu item types (Collection, Page, HTTP, etc.)
   - Creating nested menus (submenus)
   - Menu best practices
   - Troubleshooting common issues

**Code Verification Requirements:**
- Verify menu assignments against `sections/header.liquid`, `sections/footer.liquid`, `sections/announcement-bar.liquid`
- Review `config/settings_schema.json` for setting IDs (`menu`, `main_content_menu`, `utility_menu`, etc.)
- Document exact Liquid code showing menu access (`linklists[section.settings.menu]`)
- Verify block types for footer and mega menus
- All menu assignments must match actual theme code

**Key Principles:**
- **Explicit Mapping Over Implicit Understanding:** Never assume users can connect menu creation (Shopify Admin) with menu assignment (Theme Customizer). Explicitly map every menu setting to its visible location.
- **Document All Elements, Not Just Menus:** Navigation areas contain logos, text blocks, images, social media links, newsletter signup, payment icons, country/language selectors. Document the entire section.
- **Desktop vs. Mobile Behavior Matters:** Same menu can display differently on desktop vs. mobile. Always document display behavior for both.
- **Block-Based vs. Direct Assignment:** Different sections use different assignment methods. Document the assignment method for each section.

**Navigation Documentation Checklist:**
- [ ] Create menu-to-section mapping table with all menu assignments
- [ ] Document Header section (menus, logo, options, blocks)
- [ ] Document Announcement Bar (menu, blocks)
- [ ] Document Footer (menus as blocks, logo, text, images, social, newsletter, SMS, copyright, payment, selectors, apps, color scheme)
- [ ] Document mega menu configuration (if applicable)
- [ ] Document menu management in Shopify Admin
- [ ] Verify all menu assignments against theme code
- [ ] Document non-menu elements in each section
- [ ] Test with business users (can they find which menu controls which element?)

## Phase 3: Design & Presentation

### 3.1 Client-Side Authentication (Optional)
**Goal:** Protect proprietary documentation with lightweight password protection

**When to Use:**
- Documentation contains proprietary content
- Static site hosting (GitHub Pages, Netlify, Vercel)
- Basic protection sufficient (not for highly sensitive data)
- Want to avoid server-side infrastructure costs

**When NOT to Use:**
- Highly sensitive data (financial, PII)
- Compliance requires encryption
- Need user-specific access
- Need audit logging or password reset

**Implementation Approach:**
1. **Session Storage Authentication:** Use `sessionStorage` for authentication state
   - Clears when browser tab closes (security)
   - Persists across page navigation (UX)
   - No server required (static site compatible)

2. **Content Flash Prevention:** Hide body immediately on page load
   - Use `visibility: hidden` (not `display: none`) to preserve layout
   - Show content only after successful authentication
   - Prevents unauthorized content viewing

3. **Password Prompt Interface:**
   - Accessible form structure with ARIA attributes
   - Hidden username field for browser compatibility
   - Keyboard navigation support (Enter to submit)
   - Clear error messaging
   - Focus management for accessibility

4. **Integration with Component Loading:**
   - Check authentication state first
   - If not authenticated → show password prompt
   - If authenticated → load components immediately
   - After successful authentication → load components

**Security Considerations:**
- **Appropriate For:** Documentation protection, proprietary content, internal team access
- **Not Appropriate For:** Financial data, PII, highly sensitive data, compliance-required encryption
- **Limitations:** Client-side only, password visible in source code, no server validation
- **Mitigation:** Use strong passwords, HTTPS required, regular password rotation, code obfuscation (optional)

**Implementation Checklist:**
- [ ] Define security requirements (is client-side sufficient?)
- [ ] Choose strong, unique password
- [ ] Add authentication check to component loader
- [ ] Create password prompt overlay with accessibility features
- [ ] Prevent content flash (hide body on load)
- [ ] Test authentication flow and error handling
- [ ] Test session persistence across pages
- [ ] Test across browsers
- [ ] Document password securely
- [ ] Deploy with HTTPS

**Code Integration:**
Authentication code should be added to `component-loader.js` before component loading logic. See `learnings/AUTHENTICATION_LEARNINGS.md` for complete implementation details and code template.

### 3.2 Visual Design
**Goal:** Professional presentation with Arcadia branding

**Brand Integration:**
1. **Brand Audit:** Analyze client's visual identity and tone
2. **Style Guide Creation:** Develop documentation-specific style guide
3. **Template Customization:** Adapt ARCDIG-DOCS templates to client brand
4. **Visual Hierarchy:** Ensure documentation reflects client's visual standards

**Key Elements:**
- Arcadia color palette and typography
- Consistent navigation and layout
- Visual hierarchy and spacing
- Interactive elements and hover effects
- Mobile-responsive design

### 3.2 Content Organization
**Goal:** Easy navigation and information discovery

**Key Elements:**
- Clear table of contents
- Cross-referenced sections
- Download options for offline use
- Contact information and support

**Responsive Documentation:**
- Mobile-responsive HTML documentation
- PDF versions for offline access
- Interactive elements for better engagement
- Search functionality within documentation

## Phase 4: Client Handoff

### 4.1 Repository Strategy
**Goal:** Clean separation and easy handoff

**Key Decisions:**
- **Separate repos per client** - Complete isolation
- **HTML-based documentation** - Easier maintenance
- **Client-specific branding** - Professional presentation
- **Transfer ownership** - Client gets full control

### 4.2 Handoff Documentation
**Goal:** Enable client self-sufficiency

**Key Elements:**
- Setup and deployment instructions
- Content update procedures
- Technical contact information
- Ongoing support process

**Multi-Audience Approach:**
- **AI Assistants:** Static memory file (comprehensive README), structured context files
- **Developers:** Architecture guides, setup instructions, code READMEs
- **Operations:** Runbooks, incident procedures, troubleshooting guides
- **Business Users:** Documentation hub with clear navigation

**Static Memory File (XeroShoes):**
- Comprehensive README serving as complete project context
- Repository structure and file organization
- Technical architecture overview
- Documentation philosophy and content strategy
- Data sources and evidence-based approach
- Security considerations and update processes
- Enables immediate productivity without additional handoff
- Reduces onboarding time for AI assistants
- Serves as complete project context in single document

**Structured Training Program:**
**Components:**
1. **Role-Based Training:** Different training tracks for different user types
2. **Hands-On Workshops:** Practical exercises with real platform
3. **Documentation Walkthrough:** Guided tour of all documentation
4. **Q&A Sessions:** Structured question and answer periods

**Training Tracks:**
- **Technical Users:** Platform administration and troubleshooting
- **Business Users:** Content management and basic operations
- **End Users:** Platform usage and common tasks

**Ongoing Support Structure:**
**Support Levels:**
1. **Level 1:** Self-service documentation and FAQ
2. **Level 2:** Email support for common issues
3. **Level 3:** Phone support for complex issues
4. **Level 4:** On-site support for critical issues

**Escalation Matrix:**
- Response time commitments by issue severity
- Clear escalation paths for unresolved issues
- Regular support reviews and process improvements

## Phase 5: Quality Assurance

### 5.1 Documentation Review Process
**Goal:** Formal review process for all documentation

**Review Stages:**
1. **Technical Review:** Accuracy and completeness verification
2. **Business Review:** Clarity and usability assessment
3. **Client Review:** Stakeholder feedback and approval
4. **Final Review:** Quality assurance and consistency check

**Review Checklist:**
- [ ] Technical accuracy verified
- [ ] Business clarity confirmed
- [ ] Visual consistency maintained
- [ ] Brand guidelines followed
- [ ] Accessibility standards met
- [ ] Client approval obtained

### 5.2 Testing Protocols
**Goal:** Comprehensive testing procedures for all deliverables

**Testing Types:**
1. **Functional Testing:** Verify all documented procedures work
2. **User Testing:** Test documentation with actual users
3. **Cross-Platform Testing:** Verify compatibility across devices
4. **Performance Testing:** Ensure documentation loads quickly

### 5.3 Client Feedback
**Goal:** Validate with actual users

**Key Activities:**
- Client review and feedback
- User testing with business stakeholders
- Iteration based on feedback
- Final approval and sign-off

---

## Process Templates

### Project Kickoff Template
```
ARCDIG-DOCS Project Kickoff
- Project Overview
- Stakeholder Analysis
- Technical Architecture Assessment
- Documentation Scope
- Timeline and Milestones
- Success Criteria
- Risk Assessment
```

### Documentation Plan Template
```
Documentation Plan
- Content Outline
- Visual Requirements
- Review Schedule
- Approval Process
- Delivery Format
- Maintenance Plan
```

### Quality Assurance Checklist
```
QA Checklist
- Technical Accuracy
- Business Clarity
- Visual Consistency
- Brand Compliance
- Accessibility
- Client Approval
```

---

## Metrics and KPIs

### Documentation Quality Metrics
- **Completeness:** Percentage of required content delivered
- **Accuracy:** Error rate in technical documentation
- **Usability:** User satisfaction scores
- **Adoption:** Usage rates of documentation

### Process Efficiency Metrics
- **Timeline Adherence:** Percentage of milestones met on time
- **Budget Management:** Actual vs. planned costs
- **Client Satisfaction:** Net Promoter Score
- **Team Productivity:** Documentation output per hour

### Business Impact Metrics
- **Support Reduction:** Decrease in support tickets
- **Training Efficiency:** Time to competency for new users
- **Knowledge Retention:** Long-term knowledge retention rates
- **Platform Adoption:** User adoption rates of new platform
