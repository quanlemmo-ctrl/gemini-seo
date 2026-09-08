#!/usr/bin/env python3
"""
Automated Editorial Banner Generator for Gemini SEO & SmartCartVouchers
Accurately generates category-specific, branded 1200x630 vector banners.
Handles:
- Product Reviews (with Lab Test badges, rating scores, benchmark metrics)
- Savings Hacks (with Verified Strategy badges, discount highlights, NO fake rating scores)
- Buying Guides (with Comparison badges, buyer tiers)
"""

import argparse
import html
import re
import sys
from pathlib import Path


def wrap_text(text: str, max_chars_per_line: int = 30, max_lines: int = 2) -> list:
    # Clean redundant punctuation
    text = text.replace("&amp;", "&")
    # Simplify long subtitles if separated by colon
    parts = text.split(":")
    main_title = parts[0].strip()
    sub_title = parts[1].strip() if len(parts) > 1 else ""

    # If main title is descriptive enough, use it; otherwise use full text
    target_text = main_title if len(main_title) >= 20 else text

    words = target_text.split()
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(word) + 1 <= max_chars_per_line:
            current_line.append(word)
            current_len += len(word) + 1
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)
        if len(lines) >= max_lines:
            break

    if current_line and len(lines) < max_lines:
        lines.append(" ".join(current_line))

    # Add ellipsis if truncated
    if len(lines) == max_lines and len(lines[max_lines - 1].split()) < len(words) - sum(len(l.split()) for l in lines[:-1]):
        if not lines[-1].endswith("..."):
            lines[-1] = lines[-1].rstrip(".,- ") + "..."

    return lines, sub_title


def generate_banner_svg(
    title: str,
    store: str = "EDITORIAL",
    category: str = "Product Reviews",
    metric_label: str = None,
    metric_value: str = None,
    subtitle: str = None,
    rating: float = None,
    brand_name: str = "SMARTCARTVOUCHERS",
) -> str:
    # Category-specific theming and copywriting
    if category == "Savings Hacks":
        theme = "amber"
        top_pill_text = f"{store.upper()} SAVINGS HACK"
        trust_badge_text = "VERIFIED SHOPPING SECRETS"
        metric_label = metric_label or "MAXIMUM DISCOUNT & SAVINGS STRATEGY"
        metric_value = metric_value or "Save 30% to 50% With Verified Stacking"
        rating_score = None  # Savings hacks should NEVER have a fake rating score!
    elif category == "Buying Guides":
        theme = "blue"
        top_pill_text = f"{store.upper()} BUYING GUIDE"
        trust_badge_text = "HEAD-TO-HEAD COMPARISON"
        metric_label = metric_label or "HEAD-TO-HEAD BENCHMARKS & VALUE VERDICT"
        metric_value = metric_value or "Multi-Model Comparison & Price Analysis"
        rating_score = None  # Comparison buying guides compare multiple models; no single score!
    else:  # Product Reviews
        theme = "purple"
        top_pill_text = f"{store.upper()} LAB REVIEW"
        trust_badge_text = "100% HAND-TESTED IN CART"
        metric_label = metric_label or "CORE BENCHMARK & DURABILITY METRIC"
        metric_value = metric_value or "Lab Tested Suction, Ergonomics & Value"
        rating_score = rating

    # Theme color palettes
    themes = {
        "purple": {
            "accent1": "#7C3AED",
            "accent2": "#A855F7",
            "badge_bg": "#581C87",
            "highlight": "#BEF264",
            "orb1": "#7C3AED",
            "orb2": "#A855F7",
        },
        "emerald": {
            "accent1": "#059669",
            "accent2": "#10B981",
            "badge_bg": "#064E3B",
            "highlight": "#FACC15",
            "orb1": "#059669",
            "orb2": "#34D399",
        },
        "blue": {
            "accent1": "#2563EB",
            "accent2": "#3B82F6",
            "badge_bg": "#1E3A8A",
            "highlight": "#38BDF8",
            "orb1": "#2563EB",
            "orb2": "#60A5FA",
        },
        "amber": {
            "accent1": "#D97706",
            "accent2": "#F59E0B",
            "badge_bg": "#78350F",
            "highlight": "#FDE047",
            "orb1": "#D97706",
            "orb2": "#FBBF24",
        },
    }

    t = themes.get(theme, themes["purple"])

    # Clean text wrapping
    title_lines, auto_sub = wrap_text(title, max_chars_per_line=30, max_lines=2)
    effective_sub = subtitle or auto_sub or f"{store} Independent Analysis & Discount Verification (2026)"

    esc_store = html.escape(store.upper())
    esc_pill = html.escape(top_pill_text)
    esc_trust = html.escape(trust_badge_text)
    esc_metric_lbl = html.escape(metric_label.upper())
    esc_metric_val = html.escape(metric_value)
    esc_subtitle = html.escape(effective_sub[:75])
    esc_brand = html.escape(brand_name.upper())

    escaped_title_lines = [html.escape(l.upper()) for l in title_lines]

    title_y = 145 if len(escaped_title_lines) == 1 else 130
    line_height = 44

    title_tspans = ""
    for i, line in enumerate(escaped_title_lines):
        y_pos = title_y + (i * line_height)
        title_tspans += f'<text x="50" y="{y_pos}" font-family="\'Arial Black\', \'Helvetica Neue\', sans-serif" font-size="32" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">{line}</text>\n  '

    # Rating badge: Only show if rating_score exists (Product Reviews & some Guides)
    rating_markup = ""
    if rating_score:
        rating_markup = f"""
    <!-- Rating Badge -->
    <rect x="520" y="0" width="180" height="30" rx="15" fill="#18181B" stroke="{t['accent1']}" stroke-width="1.5"/>
    <text x="610" y="19" font-family="'Helvetica Neue', Arial, sans-serif" font-size="11" font-weight="900" fill="{t['highlight']}" text-anchor="middle" letter-spacing="1">★ {rating_score:.1f}/10 SCORE</text>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="1200" height="675">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090B"/>
      <stop offset="60%" stop-color="#18181B"/>
      <stop offset="100%" stop-color="#27272A"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{t['accent1']}"/>
      <stop offset="100%" stop-color="{t['accent2']}"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#27272A" stroke-width="1" stroke-opacity="0.6"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bgGrad)"/>
  <rect width="100%" height="100%" fill="url(#grid)"/>

  <!-- Glowing Accent Orbs -->
  <circle cx="700" cy="90" r="220" fill="{t['orb1']}" opacity="0.16" filter="blur(45px)"/>
  <circle cx="100" cy="380" r="160" fill="{t['orb2']}" opacity="0.12" filter="blur(35px)"/>

  <!-- Top Badges -->
  <g transform="translate(50, 42)">
    <!-- Category Pill Badge -->
    <rect x="0" y="0" width="200" height="30" rx="15" fill="{t['badge_bg']}"/>
    <text x="100" y="19" font-family="'Helvetica Neue', Arial, sans-serif" font-size="11" font-weight="900" fill="{t['highlight']}" text-anchor="middle" letter-spacing="1">{esc_pill}</text>

    <!-- Trust Badge -->
    <rect x="212" y="0" width="220" height="30" rx="15" fill="#18181B" stroke="#3F3F46" stroke-width="1.5"/>
    <circle cx="228" cy="15" r="4" fill="#10B981"/>
    <text x="328" y="19" font-family="'Helvetica Neue', Arial, sans-serif" font-size="11" font-weight="700" fill="#E4E4E7" text-anchor="middle" letter-spacing="0.5">{esc_trust}</text>

    {rating_markup}
  </g>

  <!-- Title Section -->
  {title_tspans}

  <!-- Stat Highlight Box -->
  <g transform="translate(50, 195)">
    <rect x="0" y="0" width="700" height="95" rx="20" fill="#18181B" stroke="#3F3F46" stroke-width="1.5"/>
    <rect x="0" y="0" width="6" height="95" rx="3" fill="url(#accentGrad)"/>

    <text x="30" y="38" font-family="'Helvetica Neue', Arial, sans-serif" font-size="12" font-weight="800" fill="#A1A1AA" letter-spacing="1.5">{esc_metric_lbl}</text>
    <text x="30" y="72" font-family="'Arial Black', sans-serif" font-size="22" font-weight="900" fill="{t['highlight']}" letter-spacing="-0.5">{esc_metric_val}</text>
  </g>

  <!-- Subtitle Description -->
  <text x="50" y="335" font-family="'Helvetica Neue', Arial, sans-serif" font-size="15" font-weight="500" fill="#D4D4D8">
    {esc_subtitle}
  </text>

  <!-- Footer Watermark & Brand -->
  <g transform="translate(50, 400)">
    <line x1="0" y1="-20" x2="700" y2="-20" stroke="#27272A" stroke-width="1.5"/>
    <text x="0" y="8" font-family="'Helvetica Neue', Arial, sans-serif" font-size="13" font-weight="900" fill="{t['highlight']}" letter-spacing="0.5">{esc_brand}</text>
    <text x="180" y="8" font-family="'Helvetica Neue', Arial, sans-serif" font-size="12" font-weight="500" fill="#71717A">• Editorial Research Desk • Independent Verification</text>
  </g>
</svg>"""
    return svg


def batch_generate_from_blog_data(output_dir: Path, blog_data_file: Path):
    if not blog_data_file.exists():
        print(f"[-] Error: {blog_data_file} not found", file=sys.stderr)
        return

    content = blog_data_file.read_text(encoding="utf-8")

    # Accurate block-by-block parsing: Split by 'id: \'post-'
    blocks = content.split("id: 'post-")[1:]
    print(f"[*] Found {len(blocks)} distinct blog posts in {blog_data_file.name}")
    output_dir.mkdir(parents=True, exist_ok=True)

    generated = 0
    for idx, block in enumerate(blocks):
        slug_m = re.search(r"slug:\s*'([^']+)'", block)
        title_m = re.search(r"title:\s*'([^']+)'", block)
        cat_m = re.search(r"category:\s*'([^']+)'", block)
        store_m = re.search(r"storeName:\s*'([^']+)'", block)
        score_m = re.search(r"score:\s*([0-9.]+)", block)
        excerpt_m = re.search(r"excerpt:\s*[\r\n\s]*'([^']+)'", block)

        if not slug_m or not title_m:
            continue

        slug = slug_m.group(1)
        title = title_m.group(1)
        category = cat_m.group(1) if cat_m else "Product Reviews"
        store = store_m.group(1) if store_m else "EDITORIAL"
        rating = float(score_m.group(1)) if score_m else None
        excerpt = excerpt_m.group(1) if excerpt_m else ""

        # Smart extraction of discount or metric from title/excerpt
        metric_val = None
        if category == "Savings Hacks":
            if "save" in title.lower() or "off" in title.lower():
                discount_match = re.search(r"save\s+([0-9%$]+(?:\s+to\s+[0-9%$]+)?)", title, re.IGNORECASE)
                if discount_match:
                    metric_val = f"Save {discount_match.group(1)} With Verified Insider Hacks"
                else:
                    metric_val = "Verified Stacking, Open-Box & Rebate Secrets"
            else:
                metric_val = "Authorized Insider Savings Strategy"
        elif category == "Buying Guides":
            metric_val = "Multi-Model Benchmarks & Value Comparison"

        svg_content = generate_banner_svg(
            title=title,
            store=store,
            category=category,
            metric_value=metric_val,
            rating=rating,
        )

        svg_file = output_dir / f"{slug}.svg"
        svg_file.write_text(svg_content, encoding="utf-8")
        generated += 1

        rating_str = f"★ {rating}/10" if rating else "No Rating (Guide)"
        print(f"  [{idx+1:02d}] {slug[:32]:<34} | {category:<16} | {rating_str:<15} -> {svg_file.name}")

    print(f"\n[SUCCESS] Successfully generated {generated} category-calibrated vector banners in {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate automated high-converting editorial banners")
    parser.add_argument("--title", help="Banner title text")
    parser.add_argument("--store", default="BRAND", help="Store or Brand name")
    parser.add_argument("--category", choices=["Product Reviews", "Savings Hacks", "Buying Guides"], default="Product Reviews")
    parser.add_argument("--metric-label", help="Stat box header")
    parser.add_argument("--metric-val", help="Stat box value")
    parser.add_argument("--subtitle", help="Subtitle text")
    parser.add_argument("--rating", type=float, default=None, help="Rating score")
    parser.add_argument("--brand", default="SmartCartVouchers", help="Website brand name")
    parser.add_argument("--output", help="Target output file path (.svg)")
    parser.add_argument("--from-blog-data", action="store_true", help="Batch generate for all posts in SmartCartVouchers blog-data.ts")

    args = parser.parse_args()
    root_dir = Path(__file__).resolve().parent.parent

    if args.from_blog_data:
        blog_data = root_dir / "sites" / "SmartCartVouchers" / "src" / "lib" / "data" / "blog-data.ts"
        out_dir = root_dir / "sites" / "SmartCartVouchers" / "public" / "images" / "blog"
        batch_generate_from_blog_data(out_dir, blog_data)
        return

    if not args.title or not args.output:
        print("[-] Error: --title and --output are required unless --from-blog-data is used.", file=sys.stderr)
        sys.exit(1)

    svg_content = generate_banner_svg(
        title=args.title,
        store=args.store,
        category=args.category,
        metric_label=args.metric_label,
        metric_value=args.metric_val,
        subtitle=args.subtitle,
        rating=args.rating,
        brand_name=args.brand,
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(svg_content, encoding="utf-8")
    print(f"[+] Banner successfully created: {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
