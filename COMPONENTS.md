# Elara Aerospace Website Components

This document describes the optimized component structure for the Elara Aerospace Jekyll website.

## New Components Created

### 1. Social Media Component (`_includes/social-media.html`)
**Usage:** `{% include social-media.html %}`
- **Parameters:**
  - `show_labels`: true/false (default: false) - Show social media platform names
  - `class`: CSS class for container (default: "social-links")
  - `icon_class`: CSS class for icons (default: "fa-brands")

**Example:**
```liquid
{% include social-media.html class="home-social" show_labels=true %}
```

### 2. Schema.org Component (`_includes/schema-org.html`)
**Usage:** `{% include schema-org.html %}`
- Centralized organization schema markup
- Automatically uses site configuration variables

### 3. Team Member Card Component (`_includes/team-member-card.html`)
**Usage:** `{% include team-member-card.html member=member %}`
- **Parameters:**
  - `member`: Team member object from `_data/team/`

**Example:**
```liquid
{% for member in team_members %}
  {% include team-member-card.html member=member %}
{% endfor %}
```

### 4. CTA Buttons Component (`_includes/cta-buttons.html`)
**Usage:** `{% include cta-buttons.html %}`
- **Parameters:**
  - `primary_text`: Text for primary button (default: "Join Us")
  - `primary_link`: Link for primary button (default: "/apply/")
  - `secondary_text`: Text for secondary button (default: "Learn More")
  - `secondary_link`: Link for secondary button (default: "/about/")
  - `primary_class`: CSS class for primary button (default: "btn btn--primary")
  - `secondary_class`: CSS class for secondary button (default: "btn btn--stroke")

### 5. Statistics Counter Component (`_includes/stats-counter.html`)
**Usage:** `{% include stats-counter.html title="Title" count=count link=link %}`
- **Parameters:**
  - `title`: Title for the stat
  - `count`: The number to display
  - `link`: Optional link for the stat (default: "#")
  - `class`: Optional CSS class (default: "stats__count tektur")

## CSS Optimizations

### Team Page Styles (`assets/css/team.css`)
- Moved all inline styles from `team.html` to dedicated CSS file
- Added responsive design improvements
- Better organization and maintainability

## Optimizations Made

### 1. Eliminated Duplicate Code
- **Social Media Links**: Removed duplicate social media links from 4+ files
- **Schema.org Markup**: Consolidated duplicate schema markup
- **Team Member Cards**: Created reusable component for team member display

### 2. Improved Maintainability
- Centralized social media configuration
- Reusable components reduce code duplication
- Better separation of concerns (HTML vs CSS)

### 3. Performance Improvements
- Reduced HTML file sizes by removing duplicate code
- Better CSS organization
- Improved loading times through component reuse

### 4. Accessibility Improvements
- Consistent aria-labels across all social media links
- Better alt text for team member images
- Improved semantic structure

## Files Updated

### Components Created:
- `_includes/social-media.html`
- `_includes/schema-org.html`
- `_includes/team-member-card.html`
- `_includes/cta-buttons.html`
- `_includes/stats-counter.html`
- `assets/css/team.css`

### Files Optimized:
- `_includes/navigation.html`
- `_includes/intro.html`
- `_includes/footer.html`
- `_layouts/default.html`
- `team.html`
- `index.html`

## Benefits

1. **Reduced Code Duplication**: ~200 lines of duplicate code eliminated
2. **Easier Maintenance**: Changes to social media links only need to be made in one place
3. **Better Performance**: Smaller file sizes and faster loading
4. **Improved Consistency**: All social media links now have consistent styling and behavior
5. **Enhanced Accessibility**: Better semantic structure and aria-labels

## Future Improvements

1. **Image Optimization**: Consider implementing lazy loading for all images
2. **CSS Minification**: Minify CSS files for production
3. **JavaScript Optimization**: Consolidate and minify JavaScript files
4. **Component Library**: Expand component library for other common patterns
5. **Documentation**: Add more detailed documentation for each component 