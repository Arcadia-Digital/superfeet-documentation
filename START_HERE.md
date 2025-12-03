# START HERE - New Client Engagement Guide

## Team Setup

### Initial Setup (One-Time)
1. **Review the methodology:**
   - Read `README.md` for overview (when cloning for reference)
   - Review `PROCESS.md` for methodology
   - Study case studies in `case-studies/` directory
   - Review `CHANGELOG.md` for methodology evolution

2. **Set up your workspace:**
   ```bash
   # Create your working directory for client projects
   mkdir ~/client-documentation-projects
   cd ~/client-documentation-projects
   ```

## For New Client Engagements

### 1. Setup New Client Directory
**Create your client project directory:**
```bash
# From your client-documentation-projects directory
mkdir [CLIENT_NAME]-docs
cd [CLIENT_NAME]-docs
```

### 2. Clone ARCDIG-DOCS to Temporary Location
**Clone the framework to a temporary directory:**
```bash
# Clone ARCDIG-DOCS to temporary location
git clone https://github.com/petebuzzell-ad/arcdig-docs.git /tmp/arcdig-docs

# Copy templates (includes arcadia-style.css and assets directory)
cp -r /tmp/arcdig-docs/templates/* .

# Remove temporary ARCDIG-DOCS directory
rm -rf /tmp/arcdig-docs
```

**Alternative: Use a local temp directory if you prefer:**
```bash
# Clone to local temp directory
git clone https://github.com/petebuzzell-ad/arcdig-docs.git ./temp-arcdig-docs

# Copy templates (includes arcadia-style.css and assets directory)
cp -r ./temp-arcdig-docs/templates/* .

# Remove temp directory
rm -rf ./temp-arcdig-docs
```

**What's Included:**
- Template HTML files (header-template.html, footer-template.html, html-template.html)
- `arcadia-style.css` - Complete Arcadia branding stylesheet
- `assets/` directory - All required icons and images (except client logo)
- `component-loader.js` - Dynamic header/footer loader
- `enhanced-toc/` - Enhanced table of contents system

**Note:** You can also reference the repository online at https://github.com/petebuzzell-ad/arcdig-docs.git for documentation and methodology reference without cloning.

### 3. Run Discovery Phase
**Note:** If you need the discovery prompts, you can reference them from the ARCDIG-DOCS repository online or clone temporarily.

Use prompts from the ARCDIG-DOCS `prompts/01-discovery.md` to:
- Analyze technical landscape
- Audit existing documentation
- Identify user needs and pain points

### 4. Create Documentation
**Note:** If you need the documentation prompts, you can reference them from the ARCDIG-DOCS repository online or clone temporarily.

Use prompts from the ARCDIG-DOCS `prompts/02-documentation.md` to:
- Write executive summary
- Document technical architecture
- Create operational procedures

### 5. Setup Header and Footer Components
**Copy and customize template files:**
```bash
# Copy header template and customize
cp header-template.html header.html
# Edit header.html - replace all [PLACEHOLDER] values with client-specific content

# Copy footer template and customize  
cp footer-template.html footer.html
# Edit footer.html - replace all [PLACEHOLDER] values with client-specific content
```

**Required customizations:**
- **header.html:** Replace `[CLIENT_NAME]`, `[CLIENT_LOGO]`, `[CLIENT_WEBSITE]`, `[DOC_TITLE]`, `[DOC_SUBTITLE]`, and customize menu items
- **footer.html:** Replace `[CREATED_DATE]`, `[LAST_UPDATED]`, and optionally add GitHub repository link

### 6. Setup Assets Directory
The `assets/` directory is already included when you copy templates. Just add your client logo:

```bash
# Assets directory is already copied with templates
# Just add your client logo:
# cp [CLIENT_LOGO] assets/[client-logo].png
```

**Included Assets (already in templates/assets/):**
- `favicon.webp` - Favicon (update with client favicon if needed)
- `home-icon-svgrepo-com.svg` - Home icon for header
- `burger-menu-svgrepo-com.svg` - Mobile menu icon
- `Green_Arcadia Digital.png` - Arcadia Digital logo for footer

**Client-Specific (you need to add):**
- Client logo - Add to `assets/` directory (update header.html to reference it)

### 7. Apply Arcadia Branding
- `arcadia-style.css` is already copied to project root when you copy templates
- Customize CSS variables in `:root` for brand colors if needed
- Test visual presentation and responsiveness
- Enhanced TOC styling is included automatically in `arcadia-style.css`

### 8. Add Client-Side Authentication (Optional)
**If your documentation needs password protection:**

1. **Review Security Requirements:**
   - Is client-side protection sufficient? (See `PROCESS.md` Phase 3.1 for details)
   - Appropriate for: Documentation protection, proprietary content
   - NOT appropriate for: Financial data, PII, highly sensitive data

2. **Implement Authentication:**
   - Add authentication code to `component-loader.js` (before component loading logic)
   - See `learnings/AUTHENTICATION_LEARNINGS.md` for complete implementation guide
   - Includes: Session storage, password prompt, content flash prevention, accessibility

3. **Configure Password:**
   - Choose strong, unique password
   - Update password constant in `component-loader.js`
   - Document password securely for authorized users

4. **Test Authentication:**
   - Test password prompt appears on first visit
   - Test session persists across page navigation
   - Test content doesn't flash before authentication
   - Test error handling and accessibility

**Note:** Authentication is optional. Only implement if documentation contains proprietary content that needs protection.

### 9. Build Documentation Pages
**Option A: Index Page (Documentation Hub)**
- Use the INDEX PAGE STRUCTURE in html-template.html
- Remove TOC sidebar and two-column layout
- List all documentation links and resources

**Option B: Documentation Page with Enhanced TOC**
- Use the DOCUMENTATION PAGE structure in html-template.html
- Customize TOC sidebar to match your content sections
- Ensure each `<section>` has an `id` matching TOC links
- Enhanced TOC will automatically highlight current section as users scroll

### 10. Test Component Loading
Before deploying, verify:
- Header loads correctly (check browser console for errors)
- Footer loads correctly
- Mobile menu toggle works
- Enhanced TOC highlights sections as you scroll
- All links navigate correctly

### 11. Deploy and Handoff
- Create GitHub repository for client
- Deploy to GitHub Pages
- Transfer ownership to client
- Provide maintenance documentation

## Key Success Factors

1. **Start with business context** - Understand client goals and user needs
2. **Use systematic approach** - Follow the process phases
3. **Focus on visual quality** - Professional presentation matters
4. **Plan for handoff** - Design for client ownership and maintenance
5. **Iterate based on feedback** - Validate with actual users

## Template Features

The ARCDIG-DOCS template system includes:

- **Dynamic Header/Footer:** Component loader automatically loads header.html and footer.html
- **Enhanced TOC:** Scroll-based section highlighting with smooth navigation
- **Mobile Responsive:** Header menu toggle and responsive TOC sidebar
- **Client Branding:** Easy customization through template placeholders
- **Professional Presentation:** Arcadia Digital branding with client-specific elements

## Common Pitfalls to Avoid

- **Keeping ARCDIG-DOCS repo in client project** - Remove temporary clone after copying templates
- **Forgetting to customize templates** - Must copy header-template.html → header.html and footer-template.html → footer.html
- **Missing section IDs** - Enhanced TOC requires each section to have an id matching TOC links
- **Not testing component loading** - Verify header/footer load correctly before deployment
- **Technical jargon** - Write for business users
- **Poor visual design** - Invest in professional presentation
- **Incomplete handoff** - Ensure client can maintain documentation
- **One-size-fits-all** - Customize for each client's specific needs
- **Rushing the process** - Take time to understand the technical landscape

