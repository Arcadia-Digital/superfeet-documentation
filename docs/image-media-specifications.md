# Image & Media Specifications

**Superfeet Multi-Region Shopify Plus Platform**

Complete image and media specifications for all content and product template components. Use this guide when creating or sourcing images for the Superfeet eCommerce platform.

---

## Table of Contents

1. [Product Images](#product-images)
2. [Image Banner Section](#image-banner-section)
3. [Image with Text Section](#image-with-text-section)
4. [Featured Product Section](#featured-product-section)
5. [Product Card Images](#product-card-images)
6. [Feature Diagram Section](#feature-diagram-section)
7. [Collection Banner Images](#collection-banner-images)
8. [Icon & Logo Specifications](#icon--logo-specifications)
9. [Video Specifications](#video-specifications)
10. [File Format Guidelines](#file-format-guidelines)
11. [Optimization Best Practices](#optimization-best-practices)

---

## Product Images

### Main Product Images

**Purpose:** Primary product images displayed on product detail pages (PDP).

**Specifications:**
- **Recommended Dimensions:** 2048px × 2048px (square) or 2200px × 2200px
- **Minimum Dimensions:** 1100px × 1100px
- **Maximum Dimensions:** 4096px × 4096px
- **Aspect Ratio:** 1:1 (square) recommended, but theme supports any aspect ratio
- **File Format:** WebP (preferred), JPG, PNG
- **File Size:** < 500KB per image (optimized)

**Responsive Breakpoints:**
The theme automatically generates multiple image sizes:
- 550w (mobile)
- 1100w (tablet)
- 1445w (desktop default)
- 1680w (large desktop)
- 2048w (retina displays)
- 2200w (high-DPI)
- 2890w (ultra-wide)
- 4096w (maximum)

**Usage:**
- Upload via Shopify Admin → Products → Product Images
- First image is the featured image
- Additional images appear in product gallery
- Supports hover/secondary images for product cards

**Important:**
- Use high-quality, professional product photography
- Ensure consistent lighting and background across all product images
- Include multiple angles (front, side, detail shots)
- Product images should show the actual product (not lifestyle shots)

---

## Image Banner Section

**Section:** `image-banner.liquid`

**Purpose:** Full-width hero banners with optional text overlay, used on homepage, landing pages, and collection pages.

### Desktop Images

**Desktop Large Image (Wide Screens):**
- **Recommended Dimensions:** 2800px × 1400px (2:1 aspect ratio)
- **Maximum Width:** 2800px
- **Aspect Ratio:** 2:1 recommended (can vary based on `desktop_max_height` setting)
- **File Format:** WebP (preferred), JPG
- **File Size:** < 800KB (optimized)

**Desktop Image (Standard):**
- **Recommended Dimensions:** 1400px × 700px (2:1 aspect ratio)
- **Maximum Width:** 1400px
- **Aspect Ratio:** 2:1 recommended
- **File Format:** WebP (preferred), JPG
- **File Size:** < 600KB (optimized)

**Desktop Max Height:**
- **Default:** 640px
- **Configurable:** Set in Theme Customizer (Image Banner section → Desktop background area maximum size)
- **Range:** Typically 400px - 1200px

### Mobile Images

**Mobile Image:**
- **Recommended Dimensions:** 800px × 1200px (portrait) or 800px × 1000px
- **Maximum Width:** 400px (theme renders at max 400px width)
- **Aspect Ratio:** 2:3 or 4:5 (portrait) recommended
- **File Format:** WebP (preferred), JPG
- **File Size:** < 300KB (optimized)

**Important:**
- Always provide separate mobile images for optimal mobile experience
- Mobile images can be cropped differently than desktop (portrait vs landscape)
- Theme automatically switches between desktop and mobile images based on screen size

### Video Support

**Video Formats:**
- **Desktop Large Video:** MP4, WebM (for screens 1399px+)
- **Desktop Video:** MP4, WebM (for screens 750px - 1398px)
- **Mobile Video:** MP4, WebM (for screens < 750px)

**Video Specifications:**
- **Resolution:** 1920×1080 (desktop), 1080×1920 (mobile portrait)
- **Codec:** H.264 (MP4) or VP9 (WebM)
- **File Size:** Keep under 10MB for optimal performance
- **Duration:** Recommended 15-60 seconds for background videos

---

## Image with Text Section

**Section:** `image-with-text.liquid`

**Purpose:** Side-by-side image and text content blocks.

### Image Specifications

**Desktop Image:**
- **Recommended Dimensions:** 1200px × 1200px (square) or 1200px × 800px (landscape)
- **Aspect Ratio:** Flexible (1:1, 3:2, 4:3, or 16:9)
- **File Format:** WebP (preferred), JPG
- **File Size:** < 500KB (optimized)

**Mobile Image:**
- **Recommended Dimensions:** 800px × 800px (square) or 800px × 1200px (portrait)
- **Aspect Ratio:** Match desktop or use portrait orientation
- **File Format:** WebP (preferred), JPG
- **File Size:** < 300KB (optimized)

**Image Fit Options:**
- **Cover:** Image fills container, may crop (default)
- **Contain:** Full image visible, may have letterboxing
- **Fill:** Image stretched to fill container

**Desktop Image Width Options:**
- **Small:** Reduced padding, smaller image area
- **Normal:** Standard image width (default)

**Mobile Image Width Options:**
- **Small:** Compact image
- **Medium:** Medium-sized image
- **Large:** Full-width image (default)

**Background Images:**
- **Desktop Background:** Full-width background image (optional)
- **Mobile Background:** Full-width background image for mobile (optional)
- **Recommended:** 1920px × 1080px (desktop), 800px × 1200px (mobile)

---

## Featured Product Section

**Section:** `featured-product.liquid`

**Purpose:** Highlights a single featured product with large image and product card.

### Product Image

**Desktop Image:**
- **Recommended Dimensions:** 1400px × 1400px (square)
- **Maximum Height:** Configurable (default varies)
- **Aspect Ratio:** 1:1 (square) recommended
- **File Format:** WebP (preferred), JPG
- **File Size:** < 600KB (optimized)

**Mobile Image:**
- **Recommended Dimensions:** 800px × 800px (square)
- **Maximum Height:** Configurable (default varies)
- **Aspect Ratio:** 1:1 (square) recommended
- **File Format:** WebP (preferred), JPG
- **File Size:** < 300KB (optimized)

**Background Images:**
- **Desktop Background:** Optional full-width background
- **Mobile Background:** Optional full-width background for mobile
- **Recommended:** 1920px × 1080px (desktop), 800px × 1200px (mobile)

**Product Card Image (within section):**
- **Dimensions:** 312px × 234px (display size)
- **Aspect Ratio:** 1.5:1 (3:2)
- **Source:** Uses product's featured image
- **Responsive:** Theme generates 990px width version

---

## Product Card Images

**Component:** `product-card.liquid` (used in collections, search results, product recommendations)

**Purpose:** Product images displayed in product grids and lists.

### Specifications

**Recommended Dimensions:**
- **Minimum:** 800px × 800px
- **Recommended:** 1200px × 1200px (square)
- **Maximum:** 2048px × 2048px
- **Aspect Ratio:** 1:1 (square) - **CRITICAL for consistent grid layout**

**Responsive Breakpoints:**
Theme generates multiple sizes:
- 493w (small mobile)
- 600w (mobile)
- 713w (tablet)
- 823w (tablet large)
- 990w (desktop)
- 1100w (desktop large)
- 1206w, 1346w, 1426w, 1646w, 1946w (high-DPI)

**Display Size:**
- **Grid View:** Varies by screen size and grid columns
- **Card Aspect Ratio:** Maintains 1:1 square ratio

**Secondary/Hover Images:**
- **Same specifications as primary image**
- **Purpose:** Shows on hover/click for product card
- **Usage:** Second image in product media gallery

**Important:**
- **All product images must be square (1:1 aspect ratio)** for consistent grid display
- Use same dimensions for all product images across the site
- Ensure product is centered and properly framed within square canvas
- White or transparent background recommended

---

## Feature Diagram Section

**Section:** `feature-diagram.liquid`

**Purpose:** Interactive diagrams with feature points (used on product pages and landing pages).

### Main Diagram Image

**Desktop Image:**
- **Recommended Dimensions:** 1488px × 1488px (square) or 1488px × 992px (3:2)
- **Maximum Width:** 744px (display size, theme uses 2x for retina)
- **Aspect Ratio:** 1:1 or 3:2 recommended
- **File Format:** WebP (preferred), PNG (for transparency), JPG
- **File Size:** < 400KB (optimized)

**Mobile Image:**
- **Recommended Dimensions:** 700px × 700px (square) or 700px × 466px (3:2)
- **Maximum Width:** 350px (display size, theme uses 2x for retina)
- **Aspect Ratio:** Match desktop aspect ratio
- **File Format:** WebP (preferred), PNG (for transparency), JPG
- **File Size:** < 200KB (optimized)

### Feature Icons

**Icon Specifications:**
- **Recommended Dimensions:** 120px × 120px (square)
- **Maximum Dimensions:** 160px × 160px (configurable via `icon_width` setting)
- **Aspect Ratio:** 1:1 (square)
- **File Format:** PNG (with transparency), SVG (preferred for scalability)
- **File Size:** < 50KB per icon

**Icon Positioning:**
- Icons are positioned absolutely on diagram using `v_pos` (vertical) and `h_pos` (horizontal) percentages
- Icons should be designed to work at various sizes (60px - 160px)

---

## Collection Banner Images

**Section:** `main-collection-banner.liquid`

**Purpose:** Collection page hero banners.

### Specifications

**Desktop Image:**
- **Recommended Dimensions:** 1920px × 800px (2.4:1 aspect ratio)
- **Aspect Ratio:** 2:1 to 3:1 (wide landscape)
- **File Format:** WebP (preferred), JPG
- **File Size:** < 700KB (optimized)

**Mobile Image:**
- **Recommended Dimensions:** 800px × 600px (4:3 aspect ratio)
- **Aspect Ratio:** 4:3 or 16:9
- **File Format:** WebP (preferred), JPG
- **File Size:** < 300KB (optimized)

---

## Icon & Logo Specifications

### Header Logo

**Desktop Logo:**
- **Recommended Dimensions:** 360px × 180px (2:1 aspect ratio)
- **Maximum Width:** 180px (configurable in Theme Customizer)
- **Aspect Ratio:** 2:1 recommended (can vary)
- **File Format:** PNG (with transparency), SVG (preferred)
- **File Size:** < 100KB

**Mobile Logo:**
- **Recommended Dimensions:** 340px × 170px (2:1 aspect ratio)
- **Maximum Width:** 170px (configurable in Theme Customizer)
- **Sticky Header Width:** 200px × 100px (2:1, configurable)
- **File Format:** PNG (with transparency), SVG (preferred)
- **File Size:** < 80KB

### Footer Logo

**Footer Logo:**
- **Recommended Dimensions:** 300px × 150px (2:1 aspect ratio)
- **Maximum Width:** 200px (typical)
- **Aspect Ratio:** 2:1 recommended
- **File Format:** PNG (with transparency), SVG (preferred)
- **File Size:** < 100KB

### Icon Specifications

**General Icons (Menu, Social, etc.):**
- **Dimensions:** 24px × 24px, 32px × 32px, or 48px × 48px
- **Aspect Ratio:** 1:1 (square)
- **File Format:** SVG (preferred), PNG (with transparency)
- **File Size:** < 10KB per icon

**Feature Icons (Features List Section):**
- **Recommended Dimensions:** 80px × 80px (square)
- **Aspect Ratio:** 1:1 (square)
- **File Format:** SVG (preferred), PNG (with transparency)
- **File Size:** < 30KB per icon

**Product Card Icons (Free Shipping, Returns, etc.):**
- **Dimensions:** 24px × 24px or 32px × 32px
- **Aspect Ratio:** 1:1 (square)
- **File Format:** SVG (preferred), PNG (with transparency)
- **File Size:** < 5KB per icon

---

## Video Specifications

### Background Videos (Image Banner Section)

**Desktop Video:**
- **Resolution:** 1920px × 1080px (Full HD)
- **Aspect Ratio:** 16:9
- **Frame Rate:** 30fps
- **Codec:** H.264 (MP4) or VP9 (WebM)
- **Bitrate:** 5-8 Mbps
- **File Size:** < 10MB (15-60 second videos)
- **Format:** MP4 (primary), WebM (fallback)

**Mobile Video:**
- **Resolution:** 1080px × 1920px (portrait) or 1080px × 1920px
- **Aspect Ratio:** 9:16 (portrait) or 16:9
- **Frame Rate:** 30fps
- **Codec:** H.264 (MP4)
- **Bitrate:** 3-5 Mbps
- **File Size:** < 8MB

### Embedded Videos (YouTube/Vimeo)

**Supported Platforms:**
- YouTube
- Vimeo

**Recommended Settings:**
- **Resolution:** 1080p or 720p minimum
- **Aspect Ratio:** 16:9
- **Embed Type:** Responsive embed (handled by theme)

---

## File Format Guidelines

### WebP (Preferred)

**When to Use:**
- All product images
- All banner images
- All section images
- Any image where file size optimization is critical

**Advantages:**
- 25-35% smaller file size than JPG
- Better quality at same file size
- Supported by all modern browsers
- Shopify automatically generates WebP versions

### JPG

**When to Use:**
- Fallback format
- Images with many colors (photographs)
- When WebP is not available

**Settings:**
- Quality: 80-90%
- Progressive: Enabled
- Optimize: Yes

### PNG

**When to Use:**
- Images requiring transparency
- Icons and logos
- Images with text overlays
- Simple graphics with few colors

**Settings:**
- Compression: Maximum
- Use PNG-8 for simple graphics (< 256 colors)
- Use PNG-24 for complex graphics with transparency

### SVG

**When to Use:**
- Icons
- Logos
- Simple graphics
- Scalable vector graphics

**Advantages:**
- Infinitely scalable
- Small file size
- Crisp at any resolution
- Can be styled with CSS

---

## Optimization Best Practices

### Image Optimization

1. **Compress Before Upload:**
   - Use tools like TinyPNG, ImageOptim, or Squoosh
   - Target 80-90% quality for JPG
   - Target 85-95% quality for WebP

2. **Responsive Images:**
   - Shopify automatically generates multiple sizes
   - Upload at highest needed resolution (2x for retina)
   - Theme handles responsive delivery

3. **Lazy Loading:**
   - Most images lazy load by default
   - First image on page should have `no_lazy_load` enabled for LCP
   - Use `high_fetch_priority` for above-the-fold images

4. **File Naming:**
   - Use descriptive, SEO-friendly names
   - Include product name or purpose
   - Use hyphens, not underscores
   - Example: `all-purpose-cushion-front-view.webp`

### Performance Targets

**File Size Guidelines:**
- **Product Images:** < 500KB per image
- **Banner Images:** < 800KB (desktop), < 300KB (mobile)
- **Icons:** < 50KB per icon
- **Logos:** < 100KB
- **Videos:** < 10MB (15-60 seconds)

**Page Load Performance:**
- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **Total Page Weight:** Keep images under 2MB total per page
- **Above-the-Fold Images:** Optimize for immediate display

### Accessibility

1. **Alt Text:**
   - Always provide descriptive alt text
   - Describe the image content, not decorative purpose
   - Include product names, features, or context
   - Example: "Superfeet All-Purpose Cushion insole, front view showing arch support"

2. **Text Overlays:**
   - Ensure sufficient contrast between text and background images
   - Use text boxes with background opacity for readability
   - Test on various screen sizes and brightness levels

---

## Component-Specific Specifications

### Product Compare Enhanced Section

**Product Images:**
- **Dimensions:** 400px × 400px (square)
- **Aspect Ratio:** 1:1 (square)
- **File Format:** WebP (preferred), JPG
- **File Size:** < 200KB per image
- **Source:** Product featured images

### Shop the Look Section

**Lifestyle Image:**
- **Recommended Dimensions:** 1920px × 1080px (16:9)
- **Aspect Ratio:** 16:9 or 4:3
- **File Format:** WebP (preferred), JPG
- **File Size:** < 600KB

**Product Hotspot Images:**
- Uses product featured images (see Product Images section)

### Multicolumn Section

**Column Images:**
- **Recommended Dimensions:** 800px × 800px (square) or 800px × 600px (4:3)
- **Aspect Ratio:** 1:1 or 4:3
- **File Format:** WebP (preferred), JPG
- **File Size:** < 300KB per image

### Image Accordion Section

**Desktop Images:**
- **Recommended Dimensions:** 1200px × 800px (3:2)
- **Aspect Ratio:** 3:2 or 16:9
- **File Format:** WebP (preferred), JPG
- **File Size:** < 400KB per image

**Mobile Images:**
- **Recommended Dimensions:** 800px × 600px (4:3)
- **Aspect Ratio:** 4:3
- **File Format:** WebP (preferred), JPG
- **File Size:** < 200KB per image

### UGC (User-Generated Content) Section

**Customer Photos:**
- **Recommended Dimensions:** 1200px × 1200px (square)
- **Aspect Ratio:** 1:1 (square)
- **File Format:** JPG, PNG
- **File Size:** < 500KB per image
- **Source:** Yotpo UGC gallery (managed via Yotpo app)

---

## Quick Reference Table

| Component                | Desktop Dimensions | Mobile Dimensions | Aspect Ratio                  | Format   | Max Size    |
| ------------------------ | ------------------ | ----------------- | ----------------------------- | -------- | ----------- |
| **Product Image**        | 2048×2048px        | 2048×2048px       | 1:1 (square)                  | WebP/JPG | 500KB       |
| **Image Banner**         | 1400×700px         | 800×1200px        | 2:1 (desktop), 2:3 (mobile)   | WebP/JPG | 600KB/300KB |
| **Image Banner (Large)** | 2800×1400px        | -                 | 2:1                           | WebP/JPG | 800KB       |
| **Image with Text**      | 1200×1200px        | 800×800px         | 1:1 or flexible               | WebP/JPG | 500KB/300KB |
| **Featured Product**     | 1400×1400px        | 800×800px         | 1:1 (square)                  | WebP/JPG | 600KB/300KB |
| **Product Card**         | 1200×1200px        | 1200×1200px       | 1:1 (square)                  | WebP/JPG | 500KB       |
| **Feature Diagram**      | 1488×1488px        | 700×700px         | 1:1 (square)                  | WebP/PNG | 400KB/200KB |
| **Collection Banner**    | 1920×800px         | 800×600px         | 2.4:1 (desktop), 4:3 (mobile) | WebP/JPG | 700KB/300KB |
| **Logo (Header)**        | 360×180px          | 340×170px         | 2:1                           | SVG/PNG  | 100KB       |
| **Icons**                | 80×80px            | 80×80px           | 1:1 (square)                  | SVG/PNG  | 50KB        |

---

## Additional Resources

- **Theme Architecture:** [theme-architecture.md](./theme-architecture.md)
- **Technical User Guide:** [technical-user-guide.md](./technical-user-guide.md)
- **Shopify Image Guidelines:** https://help.shopify.com/en/manual/products/product-media
- **WebP Conversion:** https://squoosh.app/
- **Image Optimization:** https://tinypng.com/

---

*Last Updated: Based on theme exports from November 2025*  
*Documentation follows ARCDIG-DOCS methodology v1.5.0*

