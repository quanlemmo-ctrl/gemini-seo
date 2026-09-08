---
name: web-scaffold
description: >
  Scaffold a new high-converting Affiliate website (Astro 5 + Tailwind) inside
  `sites/<site-name>`. Configures independent Git repository, sets domain and
  metadata, and prepares the site for deployment to Cloudflare Pages or Vercel.
  Use when the user asks to "tạo website mới", "scaffold site", "dựng web affiliate",
  or "tạo site review/coupon".
user-invocable: true
argument-hint: "<site-name> [--domain <url>] [--title <name>]"
license: MIT
metadata:
  author: Gemini SEO
  version: "1.0.0"
  category: web-builder
---

# Web Scaffold: Affiliate Website Generator

Scaffold modern, fast, and SEO-engineered affiliate websites (Astro 5 + Tailwind CSS) with independent Git repositories inside `sites/<site-name>`.

## Workflow

1. **Collect Requirements**:
   - Site folder name (e.g. `hotbuycoupon`, `gear-reviews`)
   - Production domain (e.g. `https://hotbuycoupon.com`)
   - Brand name / Title (e.g. `HotBuyCoupon - Daily Verified Promo Codes`)
   - Niche type: Coupon/Deal, Product Review Blog, or Hybrid

2. **Execute Scaffolding**:
   Run the scaffold script:
   ```bash
   python3 scripts/web_scaffold.py <site-name> --domain <https://example.com> --title "<Brand Name>"
   ```

3. **Install Dependencies in Target Site**:
   ```bash
   cd sites/<site-name> && npm install
   ```

4. **Verify Independent Git Repository**:
   Each site inside `sites/` is completely ignored by the parent `gemini-seo` repository and has its own `git init` on branch `main`.
   To connect to GitHub:
   ```bash
   cd sites/<site-name>
   git remote add origin git@github.com:YOUR_USERNAME/<site-name>.git
   git push -u origin main
   ```

5. **Local Preview**:
   ```bash
   npm run dev
   ```
