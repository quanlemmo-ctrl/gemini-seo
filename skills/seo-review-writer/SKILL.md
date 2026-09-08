---
name: seo-review-writer
description: >
  Generates in-depth, high-converting product reviews and comparisons using Editorial
  Copywriting (hooks, damaging admissions, sensory scenarios, deal anchoring) with strict
  ground-truth specification locking, real-user community synthesis (Reddit/forums), and an
  automated Vietnamese bilingual fact-check dashboard for rapid webmaster verification.
  Use when user says "write a review", "product review", "compare products", "review writer",
  "write comparison", "viết bài review", or "tối ưu bài review".
user-invocable: true
argument-hint: "[product-or-comparison] [brand-or-store]"
license: MIT
metadata:
  author: Gemini SEO
  version: "1.0.0"
  category: seo-production
---

# SEO Review Writer: High-Converting Review & Bilingual Fact-Check Engine

Produce deep, authoritative, and high-converting product reviews and multi-product comparisons that satisfy Google's Search Essentials, E-E-A-T Quality Rater Guidelines, and FTC Affiliate Disclosure rules.

Every review generated incorporates **Editorial Copywriting** techniques to hook readers and prevent bounces, while outputting a **Vietnamese Bilingual Fact-Check Dashboard** so non-native webmasters can review and verify technical claims in under two minutes.

---

## The 5-Phase Production Workflow

```
┌─────────────────────────┐
│ 1. Ground-Truth Ingestion │ ──► Lock official technical specs from datasheets (Anti-Hallucination)
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 2. Community Mining     │ ──► Synthesize 90-360 day real owner complaints & praise from Reddit/forums
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 3. Editorial Copywriting│ ──► Pattern Interrupt hooks, Damaging Admissions, Sensory micro-scenarios
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 4. Deal & Cart Anchoring│ ──► Promo codes, Price-Match, Refurbished, Trade-in (SmartCartVouchers DNA)
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ 5. Bilingual Fact-Check │ ──► Vietnamese Verification Table output for instant webmaster approval
└─────────────────────────┘
```

---

## Phase 1: Ground-Truth Specification Ingestion

Before writing a single sentence of prose, construct the **Ground-Truth Spec Table**.

1. Extract exact metrics from official manufacturer product pages or manuals:
   - Dimensions, Weight (both imperial `lbs` and metric `kg`).
   - Power ratings (Air Watts, Watts, RPM, Pa, Voltage).
   - Battery capacity, charging time, runtime in each mode.
   - Dustbin / water capacity (gallons and liters).
   - Included attachments, filter types (HEPA grade), warranty duration.
2. **The Anti-Hallucination Rule**: Never allow the AI model to guess or approximate specs. If a spec is unknown or unverified, state "Not officially specified by manufacturer" rather than generating a number.

---

## Phase 2: Community Durability & Sentiment Mining

Google's Review System prioritizes **first-hand evidence and lived experience** (Information Gain). Synthesize real owner consensus across Reddit (e.g. `r/dyson`, `r/vacuumcleaners`, `r/airpurifiers`), specialized test benches (RTINGS, VacuumWars), and verified consumer complaints.

Identify:
- **Long-term durability flaws**: What breaks after 6 to 12 months? (e.g. battery degradation, trigger mechanism cracks, laser lens scratches).
- **Daily friction points**: What annoys owners in everyday use? (e.g. needing to detach the wand to empty the bin, heavy head balance, loud high-pitch motor).
- **Surprise delight factors**: What unadvertised features do owners love? (e.g. button start preventing arthritis pain, laser revealing invisible dust at night).

---

## Phase 3: Editorial Copywriting Architecture

Apply the 5 formulas documented in `references/copywriting-formulas.md`:

### 1. Pattern Interrupt Hook (The Opening 3 Seconds)
Never start with generic fluff ("Cleaning is important..."). Open with a contrarian, problem-first hook:
> *"If you live in a two-story home with hardwood floors and suffer from wrist fatigue, spending $750 on the flagship Dyson V15 is an expensive mistake. Here is why the lighter, push-button V12 is actually the smarter choice for 80% of buyers."*

### 2. Quick Verdict Above The Fold (BLUF)
Deliver the bottom-line verdict within the first 250 words. Cater to AI Overviews and high-intent buyers who need an instant decision.

### 3. Damaging Admission (Build Unshakeable Trust)
Dedicate an explicit subsection to brutal flaws:
> *"Let's be brutally honest: the V12's dustbin is laughably small at 0.1 gallons. If you have shedding pets, you will empty it multiple times per vacuuming session."*

### 4. Sensory Micro-Scenarios (Show, Don't Tell)
Translate abstract numbers into visceral sensory experiences:
> *"When the green laser illuminates dark oak floors at 8 PM, it reveals an invisible, horrifying carpet of micro-dander and lint that daylight completely hid."*

### 5. Bucket Brigades
Maintain downward momentum using short bridges:
- *"Here's the catch..."*
- *"Now for the bad news."*
- *"We ran the numbers."*
- *"Does that extra suction actually matter in real life?"*

---

## Phase 4: Smart Cart Deal & Savings Integration

Every affiliate article on SmartCartVouchers must solve the **"How do I buy this without overpaying?"** question:

1. **MSRP Anchor**: State the full retail price as the baseline.
2. **Promotional Cycles**: Identify historical sale windows (Memorial Day, Labor Day, Prime Day, Black Friday) where direct markdowns occur ($100 - $150 off).
3. **Retailer Price Match**: Detail how to match authorized competitors (Amazon, Best Buy, Target) via official live chat.
4. **Owner Loyalty / Trade-in**: Note brand loyalty discounts (e.g., Dyson 20% Owner Rewards).
5. **Certified Refurbished**: Explain warranty-backed refurbished options (eBay official store, Dyson Outlet) saving 25-40%.

---

## Phase 5: Vietnamese Bilingual Fact-Check Dashboard

Every invocation of `seo-review-writer` **MUST** conclude by generating a comprehensive **Vietnamese Bilingual Fact-Check Dashboard** following `references/fact-check-template.md`.

This dashboard enables a Vietnamese webmaster to review:
1. **Bảng đối soát thông số kỹ thuật (Hardware Specs)**: All claims vs verified ground-truth values.
2. **Bảng đối soát trải nghiệm thực tế (Real-World Consensus)**: Owner feedback translated into Vietnamese with community sources.
3. **Bảng kiểm định mẹo giảm giá (Deal Feasibility)**: Verification that coupon and discount strategies are legitimate.
4. **Duyệt nhanh (2-Minute Sign-Off)**: Clear status indicators (✅ Đã xác minh, ⚠️ Cần chú ý, ❌ Sai lệch số liệu).

---

## Output Integration

The skill can output directly into:
1. **TypeScript Data Source**: `sites/SmartCartVouchers/src/lib/data/blog-data.ts` (Next.js architecture).
2. **Astro / MDX Components**: Compatible with `web-affiliate` components (`ReviewBox.astro`, `ComparisonTable.astro`, `CouponCard.astro`).
3. **Antigravity Artifact**: Emitting the complete review and verification dashboard to `<appDataDir>/brain/<conversation-id>/review_output.md`.
