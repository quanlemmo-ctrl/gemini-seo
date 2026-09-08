---
name: web-predeploy
description: >
  Pre-deployment SEO Quality Gate and Verification for affiliate websites.
  Audits static build output (dist/) for broken internal links, missing alt tags,
  unprotected affiliate links (missing sponsored/nofollow), schema validity, and Core Web Vitals readiness.
  Use when user says "kiểm tra trước khi deploy", "predeploy audit", "kiểm tra web", or before pushing to production.
user-invocable: true
argument-hint: "<sites/site-name>"
license: MIT
metadata:
  author: Gemini SEO
  version: "1.0.0"
  category: web-builder
---

# Web Pre-deploy: SEO Quality Gate & Launch Readiness

Run an exhaustive local audit on static build files before deploying to production.

## Pre-deploy Workflow

### 1. Build Static Output
In the target site directory:
```bash
cd sites/<site-name>
npm run build
```
Verify exit code `0` and check that all expected routes are generated in `dist/`.

### 2. Pre-deploy SEO Checklist
Inspect the generated HTML files in `dist/`:

| Check Category | Verification Item | Standard |
|---|---|---|
| **Core Metadata** | `<title>`, `<meta name="description">` | Present on 100% of pages, non-empty, title $\le$ 60 chars |
| **Canonical Links** | `<link rel="canonical" href="...">` | Self-referencing or points to authoritative target URL |
| **Robots Control** | Meta robots tag | `index, follow` on content pages; `noindex, nofollow` on `/go/*` links |
| **Affiliate Links** | Commercial outbound links | Must have `rel="sponsored nofollow"` (or routed via `/go/*`) |
| **Structured Data** | JSON-LD Scripts | Valid `@type: Review`, `@type: Article`, or `@type: FAQPage` |
| **AI Citability** | GEO & Robots.txt | `robots.txt` explicitly allows GPTBot, ClaudeBot, PerplexityBot |
| **FTC Compliance** | Affiliate Disclosure | Visible at top of page before any commercial CTA |

### 3. Automated HTML Validation via Gemini SEO Tools
Run the built-in HTML parser to inspect the output:
```bash
python3 run_seo.py page file://$(pwd)/dist/index.html
```

### 4. Git & Production Push
Once all checks pass:
```bash
cd sites/<site-name>
git status
git add .
git commit -m "feat: content updates and SEO optimizations"
git push origin main
```
Cloudflare Pages or Vercel will automatically build and publish the live site.
