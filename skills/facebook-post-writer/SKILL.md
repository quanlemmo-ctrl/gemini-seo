---
name: facebook-post-writer
description: >
  Generates algorithm-optimized, high-converting Facebook posts from blog articles, product deals, and smart shopping guides. Implements Meta algorithmic link-distribution strategies (Direct-in-Caption, First-Comment, Comment-to-DM), mobile-first Pattern Interrupt hooks, visual asset prompts, and first-comment templates to maximize organic reach and affiliate conversions.
user-invocable: true
argument-hint: "[topic-or-blog-slug] [post-archetype: engagement|deal|lead]"
license: MIT
metadata:
  author: Gemini SEO
  version: "1.0.0"
  category: social-production
---

# Facebook Post Writer: Algorithm-Optimized Social Copywriting Engine

Turn technical website reviews, hardware teardowns, and savings guides into viral, high-converting Facebook posts tailored for the Meta Newsfeed algorithm.

---

## 1. The Core Meta Algorithmic Dilemma: Reach vs. Conversion

Meta's core advertising-driven business model penalizes outbound links:
- **External link in caption**: Algorithmic penalty reduces organic reach by **40% to 70%**, but provides zero-friction 1-click conversion.
- **Link in first comment**: Preserves 100% of organic distribution, but users must open comments to find the link.
- **Comment-to-DM trigger**: Highest algorithmic distribution boost (comments signal high engagement to Meta), opening direct Messenger nurturing.

---

## 2. The 3 Post Archetypes & Link-Routing Matrix

Every Facebook post must be explicitly routed into one of the following 3 archetypes:

```
                                  FACEBOOK POST LINK-ROUTING MATRIX
                                                  │
         ┌────────────────────────────────────────┼────────────────────────────────────────┐
         ▼                                        ▼                                        ▼
┌─────────────────────────────────┐      ┌─────────────────────────────────┐      ┌─────────────────────────────────┐
│ Archetype A: Engagement & Story │      │ Archetype B: Flash Deal / Coupon│      │ Archetype C: Lead Magnet Funnel │
│ (Mẹo mua sắm / Bóc phốt chi phí)│      │ (Mã độc quyền / Giảm giá sâu)   │      │ (Checklist PDF / Bảng tính TCO) │
├─────────────────────────────────┤      ├─────────────────────────────────┤      ├─────────────────────────────────┤
│ • Primary Goal: Max Reach       │      │ • Primary Goal: Max 1-Click CTR │      │ • Primary Goal: Lead Gen & Chat │
│ • Format: Native Media + Story  │      │ • Format: Scannable Offer Box   │      │ • Format: Value Teaser + Action │
│ • Link Strategy: FIRST COMMENT  │      │ • Link Strategy: DIRECT CAPTION │      │ • Link Strategy: COMMENT-TO-DM  │
│   (Ghim bình luận số 1)         │      │   (Chấp nhận reach thấp)        │      │   (Keyword trigger tự động)     │
└─────────────────────────────────┘      └─────────────────────────────────┘      └─────────────────────────────────┘
```

### Archetype A: Engagement & Practical Hacks (`type: 'engagement'`)
* **When to use**: Educating readers, sharing maintenance teardowns, counter-intuitive financial tips (TCO breakdowns, seasonal sales calendars).
* **Link Execution**:
  - **In Caption**: Absolutely ZERO outbound URLs in the caption body. Include a clear closing CTA:
    > *"📌 I’ve pinned the full 36-month hardware breakdown and verified care pack link in the FIRST COMMENT below!"*
  - **First Comment Output**: Always provide the exact copy for the first comment:
    > *"🔗 Full 36-Month TCO Hardware Teardown & Maintenance Guide: [Link] (Verified coupon codes included!)"*

### Archetype B: Exclusive Deals & Flash Markdowns (`type: 'deal'`)
* **When to use**: Time-sensitive discounts (e.g. "Roborock S8 MaxV $200 OFF this weekend only"), promo codes with expiration dates, or sponsored paid ads.
* **Link Execution**:
  - **In Caption**: Place a clean, UTM-tagged, branded short link directly in the caption:
    > *"Grab the verified $200 OFF voucher before it expires Sunday: 👉 [Link]"*
  - **Rationale**: Buyers in this mode are high-intent. A friction drop-off in comments will kill more conversions than algorithmic reach loss.

### Archetype C: Lead Magnet & Viral Automation (`type: 'lead'`)
* **When to use**: Offering downloadable assets (e.g. 15-Point Open-Box Inspection Checklist PDF, TCO Calculator Google Sheets).
* **Link Execution**:
  - **In Caption**: No outbound URLs. Include an automation keyword trigger:
    > *"Comment 'TCO' below and our automated assistant will instantly DM you the free printable 36-month checklist + verified parts coupon sheet!"*
  - **Rationale**: High comment volume triggers Meta's virality algorithm, multiplying organic impressions by 3x - 5x.

---

## 3. The 5-Step Editorial Copywriting Framework

1. **The Scroll-Stopping Hook (First 2 Lines)**:
   - Challenge conventional wisdom or highlight a painful financial blind spot.
   - Example: *"That $350 robot vacuum you snagged on flash sale? It might be the most deceptive financial leak in your home right now. 📉👇"*
2. **The Damaging Admission / Industry Secret**:
   - Reveal the unadvertised business model (e.g. Razor-and-blade consumables).
3. **The Visceral Contrast (The Numbers)**:
   - Break down abstract concepts into tangible line items with intuitive emojis (📦, 🌪️, 🔄, 🧼, 🔋).
4. **Actionable Value-First Solutions**:
   - Provide 3-4 bullet-point takeaways that give standalone value even if the user never clicks the link.
5. **Interactive Engagement Booster**:
   - Close with an open-ended debate question to encourage comments.

---

## 4. Standard Output Structure

Every run of `facebook-post-writer` must generate:
1. **Target Archetype & Link Strategy Rationale**
2. **Main Caption Copy** (with appropriate formatting and spacing)
3. **First-Comment Copy** (if Archetype A) OR **Keyword Automation Rule** (if Archetype C)
4. **Visual Asset Recommendation** (Infographic prompt / photo description, 1:1 aspect ratio)
5. **Vietnamese Fact-Check & Verification Summary** for webmaster sign-off.
