---
name: web-affiliate
description: >
  Guide and generate high-converting Affiliate Marketing components and content
  (Blog reviews, Coupon & Deal cards, Comparison Tables, Pros & Cons, and E-E-A-T badges).
  Ensures FTC and Google compliance (rel="sponsored nofollow", affiliate disclosures,
  valid Schema.org Review & Offer markup). Use when creating or optimizing affiliate content.
user-invocable: true
argument-hint: "[review | coupon | comparison | schema]"
license: MIT
metadata:
  author: Gemini SEO
  version: "1.0.0"
  category: web-builder
---

# Web Affiliate: High-Converting UX & Content Specialist

Design, write, and optimize affiliate assets that maximize Click-Through Rate (CTR) while strictly following Google Search Essentials and FTC guidelines.

## Core Conversion Principles

1. **Quick Verdict Above The Fold**:
   - Provide a 2-3 sentence definitive answer ("Quick Verdict") within the top 30% of the page.
   - *Why*: Powers Google AI Overviews and Perplexity citations while answering high-intent searchers instantly.

2. **Dual-Action Coupon UX**:
   - Every coupon code button must perform two simultaneous actions on click:
     1. Copy the discount code to the user's clipboard.
     2. Open the merchant's store via the affiliate tracking URL in a new browser tab.

3. **Google & FTC Compliance**:
   - All commercial affiliate links must include `rel="sponsored nofollow"`.
   - The top of every page must feature an explicit Affiliate Disclosure.

## UI Component Reference

### 1. Wirecutter-Style Review Box (`ReviewBox.astro`)
```astro
---
import ReviewBox from '@/components/affiliate/ReviewBox.astro';
---

<ReviewBox
  title="Sony WH-1000XM5 Wireless Headphones"
  badge="Editor's Choice"
  rating={9.4}
  quickVerdict="Unrivaled active noise cancellation, lightweight comfort, and 30-hour battery life make the XM5 the premier travel headphone."
  pros={["Industry-leading ANC", "Superb microphone clarity", "Multipoint Bluetooth"]}
  cons={["Earcups do not fold inwards", "Premium price tag"]}
  price="$398.00"
  affiliateUrl="/go/sony-xm5"
  affiliateText="Check Price on Amazon"
/>
```

### 2. Multi-Product Comparison Matrix (`ComparisonTable.astro`)
```astro
---
import ComparisonTable from '@/components/affiliate/ComparisonTable.astro';

const items = [
  {
    name: "Sony XM5",
    badge: "Best Overall",
    rating: 9.4,
    specs: { "Battery": "30 hrs", "ANC": "10/10", "Weight": "250g" },
    price: "$398",
    affiliateUrl: "/go/sony-xm5"
  },
  {
    name: "Bose QC Ultra",
    badge: "Most Comfortable",
    rating: 9.1,
    specs: { "Battery": "24 hrs", "ANC": "9.5/10", "Weight": "252g" },
    price: "$429",
    affiliateUrl: "/go/bose-qc-ultra"
  }
];
---

<ComparisonTable
  title="Headphone Comparison Matrix"
  items={items}
  specKeys={["Battery", "ANC", "Weight"]}
/>
```

### 3. Click-to-Reveal Coupon Card (`CouponCard.astro`)
```astro
---
import CouponCard from '@/components/affiliate/CouponCard.astro';
---

<CouponCard
  title="Get 80% Off NordVPN 2-Year Plan + 3 Months Free"
  store="NordVPN"
  discount="80% OFF"
  code="BIGDEAL2026"
  affiliateUrl="/go/nordvpn-special"
  verified={true}
  exclusive={true}
  usedCount={3490}
/>
```

## Schema.org Rich Results Checklist

- **Review Posts**: Must include `@type: "Review"` with `reviewRating` (`ratingValue`, `bestRating: 10`), `itemReviewed` (`Product`), and `author`.
- **FAQ Sections**: Must include `@type: "FAQPage"` containing array of `Question` and `acceptedAnswer`.
