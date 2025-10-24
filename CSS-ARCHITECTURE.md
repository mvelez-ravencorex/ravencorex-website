# CSS Architecture - RavencoreX Website v2

## Current State (Problems Identified)

### Files Overview
1. **normalize.css** (7.6KB) - CSS reset/normalization
2. **webflow.css** (38KB) - Webflow framework styles
3. **ravencorex-6ba78a.webflow.css** (127KB) - Webflow exported styles (MAIN STYLES)
4. **responsive-enhancements.css** (13KB) - Custom responsive overrides

### Problems
- **Conflicting specificity**: `responsive-enhancements.css` uses `!important` to override base styles
- **Duplicate definitions**: Same classes defined in multiple files
- **Unclear hierarchy**: Not clear which file should contain what
- **Hard to maintain**: Changes require updating multiple files
- **No clear override strategy**: Mix of inline styles, !important, and specificity wars

## Proposed New Architecture

### Loading Order (in HTML `<head>`)
```html
1. normalize.css          <!-- Browser resets -->
2. webflow.css            <!-- Webflow framework -->
3. ravencorex-6ba78a.webflow.css  <!-- Base design system -->
4. custom-variables.css   <!-- CSS custom properties/variables -->
5. custom-overrides.css   <!-- Specific customizations -->
```

### File Responsibilities

#### 1. normalize.css
- Browser CSS resets
- **DO NOT MODIFY**

#### 2. webflow.css
- Webflow framework utilities
- **DO NOT MODIFY**

#### 3. ravencorex-6ba78a.webflow.css
- Webflow exported component styles
- Base design system
- **MINIMIZE MODIFICATIONS** (only when re-exporting from Webflow)

#### 4. custom-variables.css (NEW)
- CSS custom properties (variables)
- Design tokens (colors, spacing, typography)
- Media query breakpoints
- Reusable values

#### 5. custom-overrides.css (NEW - replaces responsive-enhancements.css)
- All custom modifications
- Component-specific overrides
- Page-specific styles
- Clear commenting structure

## File Structure

### custom-variables.css
```css
:root {
  /* Colors */
  --color-primary: #4d65ff;
  --color-text: #000000;
  --color-background: #ffffff;

  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --space-xl: 3rem;

  /* Typography */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;

  /* Layout */
  --hero-height: 400px;
  --navbar-gap: 0.25rem;
}
```

### custom-overrides.css Structure
```css
/* ===================================
   NAVIGATION
   =================================== */

/* Navbar spacing */
.navbar1_menu-links {
  gap: var(--navbar-gap);
}

.navbar1_link {
  padding: 0.5rem var(--space-xs);
}

/* ===================================
   HERO SECTIONS
   =================================== */

/* Contact page hero */
.section_header55 {
  height: var(--hero-height);
  min-height: var(--hero-height);
}

/* ... etc */
```

## Migration Strategy

1. ✅ Create `custom-variables.css` with all design tokens
2. ✅ Create `custom-overrides.css` with organized sections
3. ✅ Move all customizations from `ravencorex-6ba78a.webflow.css` to `custom-overrides.css`
4. ✅ Replace `responsive-enhancements.css` with new structure
5. ✅ Update all HTML files to use new CSS loading order
6. ✅ Test all pages
7. ✅ Document all custom classes

## Benefits

- **Clear separation of concerns**: Each file has a specific purpose
- **Easy to scale**: Add new overrides in predictable locations
- **Better maintainability**: Find and modify styles quickly
- **Version control friendly**: Clear diff when changes are made
- **No specificity wars**: Proper cascade order eliminates need for !important
- **Reusable values**: CSS variables make global changes easy

## Next Steps

1. Implement new architecture
2. Test on all pages (contact-page.html, index.html, etc.)
3. Create component documentation
4. Set up CSS linting rules
