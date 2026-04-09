# AcadPro--Academic Portfolio Template
**A GitHub repository for an academic portfolio template, professor lab website, researcher homepage, and university faculty profile theme.**

![Acadpro Academic Portfolio](https://img.shields.io/badge/Academic-Portfolio-2d5a7b?style=for-the-badge&labelColor=ffffff) ![Version 2.0.2](https://img.shields.io/badge/Version-2.0.2-2d5a7b?style=for-the-badge&labelColor=ffffff) ![License](https://img.shields.io/badge/License-MIT-2d5a7b?style=for-the-badge&labelColor=ffffff)


<div align="center">

[![Live Demo](https://img.shields.io/badge/Live_Demo-acadpro.netlify.app-2d5a7b?style=for-the-badge&labelColor=ffffff&logo=googlechrome&logoColor=2d5a7b)](https://acadpro.netlify.app)

</div>

**Preview**

![Hero Section](screenshots/hero.png)

# AcadPro--Academic Portfolio Template


Acadpro is a modern, JSON-driven academic portfolio and lab website repository built with pure HTML, CSS, and JavaScript for PhD students, MSc students, postdocs, professors, research groups, and university faculty who want a polished online presence without frameworks or dependencies.

---

> **If this project is useful to you, please consider giving it a star.**
> Stars help others discover this project and motivate continued development.
>
> [![Star This Repo](https://img.shields.io/github/stars/riponcm/acadpro?style=for-the-badge&color=2d5a7b&labelColor=ffffff&label=Star%20This%20Repo)](https://github.com/riponcm/acadpro)

---

## What's New in V2.0.2

- All site content is now driven by a single `data.json` file — no more editing HTML
- Student and Professor modes are now supported with separate frontends
- New dedicated `professor.html` page for faculty and research lab websites
- Floating demo switcher now opens the Student or Professor page directly
- Student template keeps the portfolio-oriented homepage and no-map contact layout
- Professor page adds a lab-focused hero, collaboration section, lab overview, lab publications, and map-based contact layout
- Research Highlights & Interests now use a tabbed layout matching the existing theme
- Highlights and Interests can now render compact technical skill cards with icons and learning levels
- Optional Google Scholar integration to auto-update citation counts
- Two publication display styles — card grid or tabbed list — switchable via JSON
- Dynamic Publication sorting by "Year" or "Citations" with "Load More" pagination
- BibTeX Copy-to-Clipboard modal
- Every section (projects, publications, teaching, experience, education, awards, contact) is fully configurable from JSON
- Configurable Default Theme (`light`, `dark`, `blue`) directly controlled from `data.json`

---

## Overview

This is a complete, production-ready academic portfolio website. All content lives in `data.json` — edit that one file and the website updates automatically. No build tools, no package managers, no server-side code.

The design follows an editorial aesthetic with warm muted tones, refined typography, and subtle animations. It includes light and dark mode, responsive layout, and all interactive features built from scratch.

---
---

## Templates

Acadpro now supports two main academic website experiences:
- `index.html` for Student / Researcher portfolios
- `professor.html` for Professor / Lab frontends

### Student Template

Use this for:
- PhD students
- MSc / MS students
- Postdocs
- Early-career researchers

Main characteristics:
- Hero remains in the same visual style
- Simple `Open to Collaborate` banner
- Tabbed `Research Highlights & Interests` section
- Compact technical skill cards supported inside research tabs
- Existing publication system stays unchanged
- Existing project cards stay unchanged
- Existing teaching section stays unchanged
- Existing experience and education tabs stay unchanged
- Existing awards section stays unchanged
- `Contact Me` becomes two centered banner blocks with no map

### Professor Template

Use this for:
- Professors
- Teachers
- Senior faculty profiles
- Research labs
- Principal investigators

Main characteristics:
- Same visual theme and shared academic branding
- Dedicated `professor.html` page instead of forcing all logic into one homepage
- Lab-first hero with welcome message and research highlight slider
- Collaboration and open positions section for PhD, Master's, postdoc, and visiting researchers
- Large `About the Lab` section with tabs for overview, themes, facilities/methods, and team/culture
- Lab publications section reusing the shared publication engine
- Map-based `Contact Us` area with professor/lab details, CV, and academic profiles

### How To Change Template

In `data.json`:

```json
"settings": {
  "template": "phd",
  "templateLabel": "PhD Student"
}
```

Available values:
- `phd` for the student/researcher view
- `professor` for the professor/teacher view

You can also change the visible label:

```json
"templateLabel": "Postdoctoral Researcher"
```

### Which File To Open

- Use `index.html` for the student/researcher site
- Use `professor.html` for the professor/lab site
- Both pages read from the same `data.json`

### Demo Switcher

For demo purposes, the site can show a floating switch button on the middle-right side of the screen to open the Student or Professor page quickly.

Enable it in `data.json`:

```json
"settings": {
  "demoTemplateSwitcher": true
}
```

Hide it on a real published site:

```json
"settings": {
  "demoTemplateSwitcher": false
}
```

When hidden, visitors will only see the single template selected in `settings.template`.

---

## Page Structure

| # | Section | JSON Key | Description |
|:---:|:---|:---|:---|
| 01 | **Header** | `profile` | Sticky navigation with glass blur effect and theme toggle |
| 02 | **Hero** | `profile` & `projects` | Welcome text with auto-rotating photo carousel (combines profile pics + project pics) |
| 03 | **Hiring Banner** | `hiring` | Highlighted "Open to Work" section with animated pulse |
| 04 | **Research Highlights & Interests** | `researchProfile`, `expertise`, `lab` | Tabbed research overview, highlights, and interests |
| 05 | **Publications** | `publications` | Existing publication system with auto-fetch compatibility, sorting, BibTeX, sharing, and load more |
| 06 | **Projects** | `projects` | Existing project cards with images, GitHub links, and share dropdown |
| 07 | **Teaching** | `teaching` | Existing video tiles that open YouTube in a modal |
| 08 | **Experience** | `experience` | Existing tabbed work-history panel |
| 09 | **Education** | `education` | Existing tabbed degree panel |
| 10 | **Awards** | `awards` | Existing compact cards with external links |
| 11 | **Contact Me** | `contact`, `cv`, `settings.template` | Student view: two centered banners without map. Professor view: map layout with contact info |
| 12 | **Footer** | `footer` | Existing footer style with version and repo link |

### Professor Page Structure

| # | Section | JSON Key | Description |
|:---:|:---|:---|:---|
| 01 | **Header** | `profile` | Shared sticky header and branding |
| 02 | **Lab Hero** | `professorPage.hero`, `profile`, `lab` | Welcome to lab message with research highlight slider |
| 03 | **Collaboration & Open Positions** | `professorPage.collaboration` | PhD, Master's, postdoc, visiting researcher, and collaboration callout |
| 04 | **About the Lab** | `professorPage.aboutLab`, `lab` | Large tabbed lab section with overview, themes, methods, and people |
| 05 | **Lab Publications** | `publications` | Shared publication engine reused for the professor frontend |
| 06 | **Contact Us** | `contact`, `cv`, `lab`, `profile` | Map-based faculty/lab contact section |
| 07 | **Footer** | `footer` | Shared footer style |

---

## Installation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/riponcm/acadpro.git
cd acadpro
```

### Step 2 — Edit Your Data

Open `data.json` in any text editor (VS Code recommended) and replace the demo content with your own information. See the Customization Guide below for details on each section.

### Step 3 — Test Locally

Since the site loads `data.json` via JavaScript fetch, you need a local server to test:

```bash
# Using Python (recommended)
python3 -m http.server 8000

# Using Node.js
npx serve .
```

Then open `http://localhost:8000` in your browser.

**Note:** Opening `index.html` directly as a file will not work because browsers block `fetch()` requests from `file://` protocol. Always use a local server for testing.

### Step 4 (Optional) — Auto-Update from Google Scholar

```bash
pip install scholarly
python fetch_scholar.py --scholar-id YOUR_SCHOLAR_ID
```

Your Google Scholar ID is the value after `user=` in your profile URL:
`https://scholar.google.com/citations?user=YOUR_SCHOLAR_ID`

This updates citation counts for existing papers and adds new ones with placeholder images. Your manual edits (images, PDFs, descriptions) are never overwritten. A backup is saved as `data.backup.json` before each update.

---

## Deployment

### Option 1 — Netlify (Recommended)

1. Go to [app.netlify.com](https://app.netlify.com) and sign in.
2. Click **"Add new site"** then **"Deploy manually"**.
3. Drag your project folder (containing `index.html` and `data.json`) into the upload area.
4. Your site is live. Netlify provides a free URL and HTTPS.

To update: drag the updated folder into the re-deploy area on the **Deploys** tab.

### Option 2 — GitHub Pages

1. Push your repository to GitHub.
2. Go to repository **Settings** then **Pages**.
3. Under **Source**, select branch `main` and root folder `/`.
4. Click **Save**. Your site will be available at `https://username.github.io/repo-name`.
5. Any push to `main` will automatically redeploy.

### Option 3 — Vercel

1. Go to [vercel.com](https://vercel.com) and import your GitHub repository.
2. No build settings needed — it serves static files automatically.
3. Deploys on every push.

---

## File Structure

```
acadpro/
  |-- index.html              <- Main site (reads data.json, renders everything)
  |-- data.json               <- All site content (edit this file)
  |-- fetch_scholar.py        <- Optional: auto-pull from Google Scholar
  |-- LICENSE.txt             <- License terms
  |-- README.md               <- This file
  |-- .gitignore
  |-- screenshots/
       |-- light-mode.png
       |-- dark-mode.png
       |-- hero.png
       |-- banner.png
       |-- expertise.png
       |-- tabs.png
```

---

## Customization Guide

### How It Works

All site content is stored in `data.json`. The `index.html` file reads this JSON on page load and renders every section dynamically. You never need to touch the HTML — just edit the JSON and push.

### Profile and Hero Section

```json
"profile": {
  "name": "Dr. Your Name",
  "initials": "YN",
  "tagline": "Your Research Areas",
  "headline": "Your headline text",
  "bio": "Your bio with <strong>HTML</strong> allowed",
  "role": "Your Title",
  "affiliation": "Your University",
  "photos": [
    { "src": "https://your-photo-url.jpg", "alt": "Description" }
  ]
}
```

### Hiring Banner / Open To Collaborate

Toggle the banner on or off:

```json
"hiring": {
  "enabled": true,
  "title": "Open to Collaboration",
  "description": "Your hiring message here."
}
```

Set `enabled` to `false` to hide the banner completely.

You can also supply a cleaner opportunity list for student-style templates:

```json
"opportunities": {
  "title": "Open to Collaborate",
  "summary": "Open to PhD, MSc, postdoc, and collaborative research opportunities.",
  "positions": [
    "Seeking PhD position",
    "Seeking MSc position",
    "Seeking Postdoc position"
  ]
}
```

### Research Highlights & Interests

```json
"researchProfile": {
  "title": "Research Highlights & Interests",
  "summary": "Short overview of your research direction.",
  "interests": [
    "Geotechnical Engineering",
    "Ground Improvement",
    "Experimental Soil Mechanics"
  ],
  "metrics": [
    { "label": "Publications", "value": "8+" }
  ],
  "highlights": [
    {
      "title": "Area of Expertise",
      "description": "Your focus areas.",
      "items": [
        "Soft soil improvement",
        "Vacuum densification"
      ]
    }
  ]
}
```

### Contact And CV

```json
"contact": {
  "email": "your-email@university.edu",
  "phone": "+1 (000) 000-0000",
  "office": "Room 101, Building Name",
  "cvUrl": "https://example.edu/cv.pdf",
  "socials": [
    { "platform": "google-scholar", "url": "https://scholar.google.com/..." },
    { "platform": "github", "url": "https://github.com/..." },
    { "platform": "linkedin", "url": "https://linkedin.com/in/..." },
    { "platform": "orcid", "url": "https://orcid.org/..." }
  ]
},
"cv": {
  "title": "Academic CV",
  "buttonLabel": "View CV",
  "url": "https://example.edu/cv.pdf"
}
```

Template behavior:
- `phd` removes the map and shows two centered contact banners
- `professor` keeps the map contact layout

### Previous Lab Content

The previous lab-oriented data can still remain in `data.json`, and the research section can reuse it as supporting content when needed.

```json
"lab": {
  "directorName": "Dr. Your Name",
  "title": "Your Lab Name",
  "description": "Lab focus and descriptions go here."
}
```

### Real Site Setup

For a real site, these are the most common production settings:

```json
"settings": {
  "template": "phd",
  "templateLabel": "PhD Student",
  "demoTemplateSwitcher": false,
  "publicationStyle": "alt",
  "theme": "blue"
}
```

That keeps one stable template live and hides the floating demo switcher from visitors.

### Legacy Lab / About Section Data

If you still want to keep older lab-oriented content in the JSON, you can:

```json
"lab": {
  "directorName": "Dr. Your Name",
  "title": "Your Lab Name",
  "description": "Lab focus and descriptions go here. Explaining what you build.",
  "members": [
    {
      "roleGroup": "Postdoctoral Researchers",
      "people": [
        { "name": "Dr. Alice Smith", "role": "Postdoc, ML", "image": "img1.png" }
      ]
    },
    {
      "roleGroup": "Ph.D. Students",
      "people": [
        { "name": "Charlie Davis", "role": "Ph.D. Candidate", "image": "img2.png" }
      ]
    }
  ]
}
```

### Expertise Tags

Add or remove skills. Levels control visual size: `expert` (largest), `advanced`, `intermediate`.

```json
"expertise": [
  { "name": "Machine Learning", "level": "expert" },
  { "name": "Python", "level": "advanced" }
]
```

### Projects

```json
"projects": [
  {
    "title": "Project Name",
    "subtitle": "Short description",
    "year": "2024",
    "image": "https://your-image-url.jpg",
    "description": "Detailed description.",
    "github": "https://github.com/you/repo",
    "url": "https://project-url.com"
  }
]
```

### Publications

Each publication entry:

```json
{
  "title": "Paper Title",
  "authors": "A. You, B. Coauthor",
  "highlightAuthor": "A. You",
  "venue": "Journal Name, Vol. X",
  "year": 2024,
  "type": "journal",
  "image": "https://card-image.jpg",
  "thumbnail": "https://list-thumbnail.jpg",
  "description": "Paper abstract or summary.",
  "pdfUrl": "https://link-to-pdf.pdf",
  "url": "https://paper-url.com",
  "citations": 42,
  "bibtex": "@article{key,title={...},author={...},year={2024}}"
}
```

The `type` field accepts `journal`, `conference`, or `workshop` — this controls the filter tabs.

The `highlightAuthor` field is your name as it appears in the authors string — it gets bolded and color-highlighted automatically.

### Publication Display Style

In the `settings` section of `data.json`:

```json
"settings": {
  "publicationStyle": "alt"
}
```

Options: `"alt"` (tabbed list view), `"card"` (grid cards), or `"both"` (shows both styles).

### Teaching

```json
"teaching": [
  {
    "title": "Lecture 1 — Topic",
    "subtitle": "Short description",
    "videoUrl": "https://www.youtube.com/embed/VIDEO_ID",
    "bgColor": "#2d5a7b"
  }
]
```

### Experience and Education

Experience uses icon names. Education uses logo image URLs.

```json
"experience": [
  {
    "title": "Job Title",
    "organization": "Company or University",
    "description": "What you did.",
    "years": "2022 — Present",
    "icon": "monitor"
  }
],
"education": [
  {
    "title": "Ph.D. in Your Field",
    "organization": "University Name",
    "description": "Details about your degree.",
    "years": "2016 — 2020",
    "logo": "https://university-logo-url.png"
  }
]
```

Available icon names: `monitor`, `globe`, `pencil`, `code`, `shield`, `cap`, `star`, `award`.

### Awards

```json
"awards": [
  {
    "title": "Best Paper Award",
    "subtitle": "Conference Name, 2024",
    "url": "https://link-to-award.com",
    "icon": "award",
    "iconColor": "warm"
  }
]
```

Icon color options: `"warm"` (copper), `"accent"` (blue), `"sage"` (green).

### Contact and Socials

```json
"contact": {
  "email": "you@university.edu",
  "phone": "+1 (555) 000-0000",
  "office": "Room 100, Building Name",
  "mapEmbed": "https://www.google.com/maps/embed?pb=YOUR_EMBED_URL",
  "socials": [
    { "platform": "google-scholar", "url": "https://scholar.google.com/..." },
    { "platform": "github", "url": "https://github.com/you" },
    { "platform": "linkedin", "url": "https://linkedin.com/in/you" },
    { "platform": "orcid", "url": "https://orcid.org/0000-..." }
  ]
}
```

Supported social platforms: `google-scholar`, `github`, `linkedin`, `orcid`, `twitter`.

### Adjust Colors

All colors are CSS variables at the top of `index.html`. Edit `:root` for light mode and `[data-theme="dark"]` for dark mode.

You can also set the default appearance in `data.json` under `settings`:

```json
"settings": {
  "theme": "blue" // Available options: "light", "dark", "blue"
}
```
The "blue" theme uses a crisp white background with primary blue accents. Users will still be able to toggle to a dark mode via the UI button.

---

## Google Scholar Integration

The included `fetch_scholar.py` script connects to Google Scholar and updates your `data.json` automatically.

### Setup

```bash
pip install scholarly
```

### First Run

Add your Scholar ID to `data.json`:

```json
"settings": {
  "scholarId": "YOUR_SCHOLAR_ID"
}
```

Then run:

```bash
python fetch_scholar.py
```

### What It Does

- Fetches all your publications from Google Scholar
- For **existing papers** in `data.json`: updates citation count only
- For **new papers**: adds them with placeholder images (you replace later)
- **Never deletes or overwrites** your manual edits (images, PDFs, descriptions)
- Creates `data.backup.json` before every save

### Recommended Workflow

Run the script monthly to keep citations current:

```bash
python fetch_scholar.py
# Review data.json for new entries
# Replace placeholder images for new papers
# Add PDF URLs
git add data.json
git commit -m "Update publications from Scholar"
git push
```

### Important Notes

- Google Scholar has no official API — the script uses the `scholarly` library
- Google may rate-limit requests; if blocked, wait and try again later
- The script takes 30-60 seconds depending on your number of publications

---

## Features

### Design

- Clean editorial typography using Playfair Display and Source Sans 3
- Light and dark theme with smooth toggle and persistence via localStorage
- Warm muted color palette — slate blue, copper, sage green
- Subtle grain texture overlay for depth
- Glassmorphism header with backdrop blur
- Responsive layout — works on desktop, tablet, and mobile
- Print-friendly styles

### Interactive Elements

- Auto-rotating photo carousel with dot indicators and navigation arrows
- Scroll-triggered reveal animations with staggered timing
- Expertise cloud with hover tooltips showing proficiency levels
- Tabbed content panel for experience and education
- Tabbed professor lab section for overview, research themes, facilities, and team
- Share dropdown with Copy Link, Facebook, LinkedIn, and X support
- BibTeX download button that generates and saves citation files
- Publication filter tabs including Journal, Conference, Workshop, Poster, and Thesis / Dissertation
- Video tiles that open lectures in a YouTube modal
- Awards and certifications with popup detail support
- Project detail popups with tabs, screenshots, demo links, repository links, and video support

### Technical

- JSON-driven — all content in one file, zero HTML editing needed for content updates
- Dual static frontends: `index.html` and `professor.html`
- All icons are inline SVG — no icon library needed
- Google Fonts loaded via preconnect for performance
- Fully semantic HTML with ARIA labels
- Zero JavaScript frameworks — pure vanilla JS
- No cookies, no analytics, no tracking

---

## Custom Design Service

If you need a tailored version of this portfolio with custom branding, unique layout modifications, additional sections, or integration with a CMS or backend system, I am available for commissioned work.

**Contact for custom design inquiries:**

| | |
|:---|:---|
| **Author** | Ripon Chandra Malo |
| **LinkedIn** | *https://www.linkedin.com/in/engr-ripon/* |

Typical turnaround for custom modifications is 3 to 7 business days depending on scope.

---

## License

This project is released under the MIT License.

You can use, modify, publish, distribute, sublicense, and sell this project, as long as the copyright notice and license text are included in substantial copies of the software.

---

## Technical Notes

- Tested on Chrome, Firefox, Safari, and Edge (latest versions).
- Mobile responsive down to 320px viewport width.
- Lighthouse score: 95+ Performance, 100 Accessibility, 100 Best Practices, 100 SEO (when hosted over HTTPS).
- Total file size: approximately 55 KB HTML + 15 KB JSON uncompressed.
- No external JavaScript dependencies. No npm. No Webpack. No React.
- Requires a web server for local testing (uses `fetch()` to load JSON).

---

**AcadPro — An Academic Portfolio Template** — Version 2.0.2

Designed by **Ripon Chandra Malo**

---

> **If this project helped you, consider buying me a coffee.**
<div align="center">

[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-2d5a7b?style=for-the-badge&labelColor=ffffff&logo=buymeacoffee&logoColor=2d5a7b)](https://www.buymeacoffee.com/riponce)             [![Star This Repo](https://img.shields.io/badge/Give_a_Star-2d5a7b?style=for-the-badge&labelColor=ffffff&logo=github&logoColor=2d5a7b)](https://github.com/riponcm/acadpro)

</div>

<p align="center">
  <a href="#">
      <img src="https://api.visitorbadge.io/api/VisitorHit?user=riponcm&repo=acadpro-badge&countColor=%237B1E7A" />
   </a>
</p>
