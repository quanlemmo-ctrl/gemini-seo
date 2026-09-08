#!/usr/bin/env python3
"""
Web Scaffold Script for Gemini SEO - Affiliate Website Factory
Scaffolds a new high-converting Astro Affiliate website into `sites/<site_name>`.
Each website is initialized as an independent Git repository ready for GitHub & Cloudflare Pages.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def scaffold_site(site_name: str, domain: str = None, title: str = None):
    root_dir = Path(__file__).resolve().parent.parent
    template_dir = root_dir / "templates" / "astro-affiliate"
    target_dir = root_dir / "sites" / site_name

    if not template_dir.exists():
        print(f"[-] Error: Template directory not found at {template_dir}", file=sys.stderr)
        sys.exit(1)

    if target_dir.exists():
        print(f"[-] Error: Target directory already exists at {target_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Scaffolding new affiliate website '{site_name}'...")
    print(f"    Source template: {template_dir}")
    print(f"    Target directory: {target_dir}")

    # Copy template to target, ignoring node_modules and .astro
    def ignore_patterns(path, names):
        ignored = set()
        for name in names:
            if name in {"node_modules", ".astro", "dist", ".git"}:
                ignored.add(name)
        return ignored

    shutil.copytree(template_dir, target_dir, ignore=ignore_patterns)

    # Customize package.json
    pkg_file = target_dir / "package.json"
    if pkg_file.exists():
        content = pkg_file.read_text(encoding="utf-8")
        content = content.replace('"astro-affiliate-template"', f'"{site_name}"')
        pkg_file.write_text(content, encoding="utf-8")

    # Customize astro.config.mjs
    if domain:
        cfg_file = target_dir / "astro.config.mjs"
        if cfg_file.exists():
            clean_domain = domain.rstrip("/")
            if not clean_domain.startswith("http"):
                clean_domain = f"https://{clean_domain}"
            content = cfg_file.read_text(encoding="utf-8")
            content = content.replace("https://example.com", clean_domain)
            cfg_file.write_text(content, encoding="utf-8")

    # Initialize independent Git repository
    print(f"[*] Initializing independent Git repository in {target_dir}...")
    try:
        subprocess.run(["git", "init", "-b", "main"], cwd=target_dir, check=True, capture_output=True)
        # Create site-specific .gitignore
        site_gitignore = target_dir / ".gitignore"
        site_gitignore.write_text("node_modules/\n.astro/\ndist/\n.env\n.env.*\n*.log\n.DS_Store\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=target_dir, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"Initial commit: {site_name} affiliate website (Astro 5 + Tailwind)"], cwd=target_dir, check=True, capture_output=True)
        print("[+] Git repository initialized and initial commit created!")
    except Exception as e:
        print(f"[!] Warning: Git initialization encountered an issue: {e}", file=sys.stderr)

    print("\n" + "=" * 60)
    print(f" SUCCESS: Website created successfully at sites/{site_name}")
    print("=" * 60)
    print("Next steps:")
    print(f"  1. cd sites/{site_name}")
    print("  2. npm install")
    print("  3. npm run dev")
    print("\nTo connect with your GitHub repository:")
    print(f"  cd sites/{site_name}")
    print(f"  git remote add origin git@github.com:YOUR_USERNAME/{site_name}.git")
    print("  git push -u origin main")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Astro Affiliate website")
    parser.add_argument("site_name", help="Directory name for the new site (e.g. hotbuycoupon, techreview)")
    parser.add_argument("--domain", help="Production domain (e.g. https://hotbuycoupon.com)")
    parser.add_argument("--title", help="Site title/brand name")

    args = parser.parse_args()
    scaffold_site(args.site_name, domain=args.domain, title=args.title)


if __name__ == "__main__":
    main()
