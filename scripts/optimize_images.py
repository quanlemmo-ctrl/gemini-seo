#!/usr/bin/env python3
"""
Image Optimization Script for Gemini SEO
Recursively compresses, resizes, and optimizes images in web projects to achieve 100/100 Core Web Vitals.
Reduces multi-megabyte images to clean, web-ready files (<150KB) while preserving high visual fidelity.
"""

import argparse
import os
import sys
from pathlib import Path
from PIL import Image


def optimize_image(
    file_path: Path,
    max_dimension: int = 1400,
    quality: int = 82,
    create_webp: bool = True,
    in_place: bool = True,
) -> dict:
    original_size = file_path.stat().st_size
    rel_name = file_path.name

    try:
        with Image.open(file_path) as img:
            orig_width, orig_height = img.size
            orig_format = img.format or "JPEG"

            # Convert RGBA/palette to RGB if saving to JPEG
            target_img = img.copy()
            if target_img.mode in ("RGBA", "LA", "P") and file_path.suffix.lower() in [".jpg", ".jpeg"]:
                bg = Image.new("RGB", target_img.size, (255, 255, 255))
                if target_img.mode == "P":
                    target_img = target_img.convert("RGBA")
                bg.paste(target_img, mask=target_img.split()[-1] if target_img.mode == "RGBA" else None)
                target_img = bg
            elif target_img.mode not in ("RGB", "RGBA"):
                target_img = target_img.convert("RGB")

            # Resize if dimensions exceed max_dimension
            width, height = target_img.size
            if width > max_dimension or height > max_dimension:
                if width >= height:
                    new_width = max_dimension
                    new_height = int(height * (max_dimension / width))
                else:
                    new_height = max_dimension
                    new_width = int(width * (max_dimension / height))
                target_img = target_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            else:
                new_width, new_height = width, height

            # Save in-place optimized version
            if in_place:
                if file_path.suffix.lower() in [".jpg", ".jpeg"]:
                    target_img.save(file_path, "JPEG", quality=quality, optimize=True, progressive=True)
                elif file_path.suffix.lower() == ".png":
                    target_img.save(file_path, "PNG", optimize=True)
                elif file_path.suffix.lower() == ".webp":
                    target_img.save(file_path, "WEBP", quality=quality, method=6)

            new_size = file_path.stat().st_size
            saved_bytes = original_size - new_size
            ratio = (saved_bytes / original_size * 100) if original_size > 0 else 0

            # Also create .webp copy if requested
            webp_size = 0
            if create_webp and file_path.suffix.lower() != ".webp":
                webp_path = file_path.with_suffix(".webp")
                target_img.save(webp_path, "WEBP", quality=quality, method=6)
                webp_size = webp_path.stat().st_size

            return {
                "file": rel_name,
                "orig_size": original_size,
                "new_size": new_size,
                "webp_size": webp_size,
                "orig_res": f"{orig_width}x{orig_height}",
                "new_res": f"{new_width}x{new_height}",
                "ratio": ratio,
                "success": True,
            }

    except Exception as e:
        return {
            "file": rel_name,
            "orig_size": original_size,
            "new_size": original_size,
            "ratio": 0,
            "success": False,
            "error": str(e),
        }


def process_directory(directory: Path, max_dimension: int = 1400, quality: int = 82):
    if not directory.exists():
        print(f"[-] Error: Directory {directory} does not exist", file=sys.stderr)
        sys.exit(1)

    image_files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
        image_files.extend(directory.rglob(ext))

    image_files = sorted(set(image_files))
    if not image_files:
        print(f"[*] No images found in {directory}")
        return

    print(f"[*] Found {len(image_files)} images in {directory}")
    print("=" * 80)
    print(f"{'File':<32} {'Original':<12} {'Optimized':<12} {'Saved':<10} {'Resolution':<14}")
    print("-" * 80)

    total_orig = 0
    total_new = 0

    for img_path in image_files:
        orig_s = img_path.stat().st_size
        total_orig += orig_s

        res = optimize_image(img_path, max_dimension=max_dimension, quality=quality)
        if res["success"]:
            total_new += res["new_size"]
            orig_str = f"{res['orig_size']/1024:.1f} KB"
            new_str = f"{res['new_size']/1024:.1f} KB"
            pct_str = f"-{res['ratio']:.1f}%"
            res_str = f"{res['new_res']}"
            print(f"{res['file'][:30]:<32} {orig_str:<12} {new_str:<12} {pct_str:<10} {res_str:<14}")
        else:
            total_new += orig_s
            print(f"{res['file'][:30]:<32} FAILED: {res.get('error')}")

    print("=" * 80)
    total_saved = total_orig - total_new
    total_pct = (total_saved / total_orig * 100) if total_orig > 0 else 0
    print(f"SUMMARY:")
    print(f"  Total Original:  {total_orig / (1024*1024):.2f} MB")
    print(f"  Total Optimized: {total_new / (1024*1024):.2f} MB")
    print(f"  Bandwidth Saved: {total_saved / (1024*1024):.2f} MB ({total_pct:.1f}% reduction!)")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Optimize web images for 100/100 Core Web Vitals")
    parser.add_argument("directory", help="Target directory containing images")
    parser.add_argument("--max-dim", type=int, default=1400, help="Max width/height dimension in px (default: 1400)")
    parser.add_argument("--quality", type=int, default=82, help="Compression quality 1-100 (default: 82)")

    args = parser.parse_args()
    process_directory(Path(args.directory), max_dimension=args.max_dim, quality=args.quality)


if __name__ == "__main__":
    main()
