#!/usr/bin/env python3
"""Unified CLI Entrypoint and Function Wrapper for Gemini SEO in Antigravity.

Enables running any SEO skill, tool, or script via CLI or direct Python function calls.
Supports automatic virtualenv resolution, SSRF-safe URL fetching, and structured JSON output.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

ROOT_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
VENV_PYTHON = ROOT_DIR / ".venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def get_python_executable() -> str:
    """Resolve the best Python executable (local .venv if available, else current interpreter)."""
    if VENV_PYTHON.is_file() and os.access(VENV_PYTHON, os.X_OK):
        return str(VENV_PYTHON)
    env_override = os.environ.get("GEMINI_SEO_PYTHON") or os.environ.get("CLAUDE_SEO_PYTHON")
    if env_override and Path(env_override).is_file():
        return env_override
    return sys.executable


def execute_script(script_name: str, args: List[str], capture_output: bool = True) -> Dict[str, Any]:
    """Execute a script from the scripts/ directory using the resolved Python interpreter."""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.is_file():
        return {"status": "error", "error": f"Script not found: {script_name}"}

    python_bin = get_python_executable()
    cmd = [python_bin, str(script_path)] + args

    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    if str(SCRIPTS_DIR) not in env.get("PYTHONPATH", ""):
        env["PYTHONPATH"] = f"{SCRIPTS_DIR}:{env.get('PYTHONPATH', '')}".strip(":")

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE if capture_output else None,
            stderr=subprocess.PIPE if capture_output else None,
            text=True,
            env=env,
            timeout=120,
        )
        stdout = proc.stdout.strip() if proc.stdout else ""
        stderr = proc.stderr.strip() if proc.stderr else ""

        # Attempt to parse as JSON if output appears to be JSON
        json_data = None
        if stdout.startswith(("{", "[")):
            try:
                json_data = json.loads(stdout)
            except Exception:
                pass

        return {
            "status": "success" if proc.returncode == 0 else "error",
            "returncode": proc.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "data": json_data if json_data is not None else stdout,
        }
    except subprocess.TimeoutExpired:
        return {"status": "error", "error": f"Execution of {script_name} timed out (120s)"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


# ---------------------------------------------------------------------------
# High-Level Skill Functions (Callable from Python or Terminal)
# ---------------------------------------------------------------------------

def run_doctor() -> Dict[str, Any]:
    """Check Python environment, dependency status, and configured API credentials."""
    python_bin = get_python_executable()
    has_venv = VENV_PYTHON.is_file()

    # Check key dependencies
    core_packages = [
        ("requests", "requests", "HTTP requests & API calls"),
        ("bs4", "beautifulsoup4", "HTML parsing"),
        ("lxml", "lxml", "Fast XML/HTML parsing"),
        ("playwright", "playwright", "Headless browser rendering"),
        ("trafilatura", "trafilatura", "Article text extraction"),
    ]
    optional_packages = [
        ("matplotlib", "matplotlib", "Report charts"),
        ("googleapiclient", "google-api-python-client", "Google Search Console & APIs"),
        ("weasyprint", "weasyprint", "PDF report generation (requires 'brew install pango')"),
    ]

    installed = {}
    missing_core = []
    missing_optional = []

    for import_name, pkg_name, desc in core_packages:
        res = subprocess.run(
            [python_bin, "-c", f"import {import_name}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if res.returncode == 0:
            installed[pkg_name] = {"status": "installed", "type": "core", "description": desc}
        else:
            missing_core.append(pkg_name)
            installed[pkg_name] = {"status": "missing", "type": "core", "description": desc}

    for import_name, pkg_name, desc in optional_packages:
        res = subprocess.run(
            [python_bin, "-c", f"import {import_name}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if res.returncode == 0:
            installed[pkg_name] = {"status": "installed", "type": "optional", "description": desc}
        else:
            missing_optional.append(pkg_name)
            installed[pkg_name] = {"status": "missing", "type": "optional", "description": desc}

    # Check API keys
    api_status = {
        "google_api": bool(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") or os.environ.get("GOOGLE_API_KEY")),
        "moz_api": bool(os.environ.get("MOZ_ACCESS_ID") and os.environ.get("MOZ_SECRET_KEY")),
        "bing_api": bool(os.environ.get("BING_API_KEY")),
        "dataforseo": bool(os.environ.get("DATAFORSEO_USERNAME") and os.environ.get("DATAFORSEO_PASSWORD")),
        "indexnow": bool(os.environ.get("INDEXNOW_KEY")),
    }

    return {
        "status": "ready" if not missing_core else "setup_required",
        "python_executable": python_bin,
        "virtualenv_active": has_venv,
        "packages": installed,
        "missing_core": missing_core,
        "missing_optional": missing_optional,
        "api_credentials": api_status,
    }


def run_setup() -> int:
    """Create local .venv and install requirements.txt."""
    print(f"Creating virtual environment in {ROOT_DIR / '.venv'}...")
    res = subprocess.run([sys.executable, "-m", "venv", str(ROOT_DIR / ".venv")])
    if res.returncode != 0:
        print("Failed to create virtual environment.", file=sys.stderr)
        return res.returncode

    pip_bin = ROOT_DIR / ".venv" / ("Scripts/pip.exe" if sys.platform == "win32" else "bin/pip")
    req_file = ROOT_DIR / "requirements.txt"
    if req_file.is_file():
        print(f"Installing dependencies from {req_file}...")
        res = subprocess.run([str(pip_bin), "install", "-r", str(req_file)])
        if res.returncode != 0:
            print("Failed to install pip dependencies.", file=sys.stderr)
            return res.returncode

    print("Setup completed successfully!")
    return 0


def run_page(url: str, json_output: bool = False) -> Dict[str, Any]:
    """Fetch and parse HTML for a single URL."""
    args = [url]
    if json_output:
        args.append("--json")
    return execute_script("parse_html.py", args)


def run_technical(url: str, json_output: bool = False) -> Dict[str, Any]:
    """Perform technical SEO audit on a URL."""
    args = [url]
    if json_output:
        args.append("--json")
    return execute_script("parse_html.py", args)


def run_content(url: str, text: Optional[str] = None) -> Dict[str, Any]:
    """Analyze content quality and E-E-A-T."""
    args = [url, "--json"]
    return execute_script("content_quality.py", args)


def run_schema(target: str, extra_args: Optional[List[str]] = None, json_output: bool = False) -> Dict[str, Any]:
    """Detect, validate or generate Schema.org JSON-LD."""
    if target.startswith(("http://", "https://")):
        args = [target]
        if json_output:
            args.append("--json")
        return execute_script("parse_html.py", args)
    else:
        args = [target] + (extra_args or [])
        return execute_script("schema_generate.py", args)


def run_sitemap(url: str, json_output: bool = False) -> Dict[str, Any]:
    """Discover and validate XML sitemaps for a website."""
    args = [url]
    if json_output:
        args.append("--json")
    return execute_script("sitemap_discovery.py", args)


def run_speed(url: str, json_output: bool = False) -> Dict[str, Any]:
    """Check PageSpeed Insights & CrUX metrics."""
    args = [url]
    if json_output:
        args.append("--json")
    return execute_script("pagespeed_check.py", args)


def run_geo(url: str, json_output: bool = False) -> Dict[str, Any]:
    """Audit AI Search (GEO) and Agent UX friendliness."""
    args = [url]
    if json_output:
        args.append("--json")
    return execute_script("agent_ux_check.py", args)


def run_drift(action: str, url: str, extra_args: Optional[List[str]] = None) -> Dict[str, Any]:
    """Manage SEO drift baselines and comparisons."""
    args = [url] + (extra_args or [])
    script_map = {
        "baseline": "drift_baseline.py",
        "compare": "drift_compare.py",
        "history": "drift_history.py",
        "report": "drift_report.py",
    }
    script = script_map.get(action.lower(), "drift_compare.py")
    return execute_script(script, args)


def run_backlinks(url: str, action: str = "verify") -> Dict[str, Any]:
    """Analyze or verify backlinks."""
    if action == "verify":
        return execute_script("verify_backlinks.py", [url])
    elif action == "moz":
        return execute_script("moz_api.py", [url])
    elif action == "bing":
        return execute_script("bing_webmaster.py", [url])
    elif action == "cc":
        return execute_script("commoncrawl_graph.py", [url])
    return execute_script("verify_backlinks.py", [url])


def run_google(cmd: str, args: List[str]) -> Dict[str, Any]:
    """Run Google SEO API commands (gsc, crux, indexing, ga4)."""
    script_map = {
        "query": "gsc_query.py",
        "inspect": "gsc_inspect.py",
        "notify": "indexing_notify.py",
        "ga4": "ga4_report.py",
        "report": "google_report.py",
    }
    script = script_map.get(cmd.lower(), "gsc_query.py")
    return execute_script(script, args)


def run_audit(url: str) -> Dict[str, Any]:
    """Orchestrate a multi-stage audit for a URL and aggregate findings."""
    results: Dict[str, Any] = {"url": url, "sections": {}}

    # 1. On-page & Technical
    results["sections"]["html_analysis"] = run_page(url, json_output=True).get("data")
    # 2. Sitemap Discovery
    results["sections"]["sitemap"] = run_sitemap(url, json_output=True).get("data")
    # 3. Agent UX / GEO
    results["sections"]["agent_ux"] = run_geo(url, json_output=True).get("data")
    # 4. Content Quality Check
    results["sections"]["content"] = run_content(url).get("data")

    return {
        "status": "success",
        "url": url,
        "audit_data": results,
    }


# ---------------------------------------------------------------------------
# CLI Argument Parser & Entrypoint
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="run_seo.py",
        description="Unified Antigravity SEO Runner & Tool Suite",
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="SEO Command to run")

    # doctor
    subparsers.add_parser("doctor", help="Inspect Python environment, dependencies and API status")

    # setup
    subparsers.add_parser("setup", help="Set up local .venv and install dependencies")

    # audit <url>
    p_audit = subparsers.add_parser("audit", help="Run comprehensive audit on a website")
    p_audit.add_argument("url", help="Target website URL")
    p_audit.add_argument("--json", action="store_true", help="Output as JSON")

    # page <url>
    p_page = subparsers.add_parser("page", help="Analyze on-page elements of a URL")
    p_page.add_argument("url", help="Target URL")
    p_page.add_argument("--json", action="store_true", help="Output as JSON")

    # technical <url>
    p_tech = subparsers.add_parser("technical", help="Audit technical SEO (crawlability, indexability, security)")
    p_tech.add_argument("url", help="Target URL")
    p_tech.add_argument("--json", action="store_true", help="Output as JSON")

    # content <url>
    p_content = subparsers.add_parser("content", help="Analyze content quality and E-E-A-T")
    p_content.add_argument("url", help="Target URL")

    # schema <url_or_type>
    p_schema = subparsers.add_parser("schema", help="Validate or generate Schema markup")
    p_schema.add_argument("target", help="URL to inspect or Schema type to generate (e.g., profile, discussion)")
    p_schema.add_argument("extra", nargs=argparse.REMAINDER, help="Extra arguments for schema generation")
    p_schema.add_argument("--json", action="store_true", help="Output as JSON")

    # sitemap <url>
    p_sitemap = subparsers.add_parser("sitemap", help="Discover and validate XML sitemaps")
    p_sitemap.add_argument("url", help="Target website URL")
    p_sitemap.add_argument("--json", action="store_true", help="Output as JSON")

    # speed <url>
    p_speed = subparsers.add_parser("speed", help="Audit Core Web Vitals and PageSpeed")
    p_speed.add_argument("url", help="Target URL")
    p_speed.add_argument("--json", action="store_true", help="Output as JSON")

    # geo <url>
    p_geo = subparsers.add_parser("geo", help="Audit AI search visibility (GEO / Agent UX)")
    p_geo.add_argument("url", help="Target URL")
    p_geo.add_argument("--json", action="store_true", help="Output as JSON")

    # drift <action> <url>
    p_drift = subparsers.add_parser("drift", help="SEO drift monitoring (baseline, compare, history, report)")
    p_drift.add_argument("action", choices=["baseline", "compare", "history", "report"], help="Drift action")
    p_drift.add_argument("url", help="Target URL")
    p_drift.add_argument("extra", nargs=argparse.REMAINDER, help="Extra arguments for drift")

    # backlinks <url>
    p_backlinks = subparsers.add_parser("backlinks", help="Analyze or verify backlinks")
    p_backlinks.add_argument("url", help="Target URL")
    p_backlinks.add_argument("--action", default="verify", choices=["verify", "moz", "bing", "cc"], help="Source/Action")

    # google <cmd>
    p_google = subparsers.add_parser("google", help="Interact with Google SEO APIs")
    p_google.add_argument("cmd", choices=["query", "inspect", "notify", "ga4", "report"], help="Google API command")
    p_google.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for Google command")

    # script <script_name.py> [args...]
    p_script = subparsers.add_parser("script", help="Run any script from scripts/ directly")
    p_script.add_argument("script_name", help="Script filename (e.g., fetch_page.py)")
    p_script.add_argument("args", nargs=argparse.REMAINDER, help="Arguments passed to script")

    return parser


def main() -> int:
    parser = build_parser()
    args, unknown = parser.parse_known_args()

    if not args.subcommand:
        parser.print_help()
        return 1

    def print_result(res: Dict[str, Any]) -> int:
        out = res.get("stdout") or ""
        err = res.get("stderr") or ""
        if out:
            print(out)
        if err and res.get("returncode", 0) != 0:
            print(err, file=sys.stderr)
        return res.get("returncode", 0)

    if args.subcommand == "doctor":
        res = run_doctor()
        print(json.dumps(res, indent=2))
        return 0 if res["status"] == "ready" else 2

    elif args.subcommand == "setup":
        return run_setup()

    elif args.subcommand == "audit":
        res = run_audit(args.url)
        print(json.dumps(res, indent=2) if args.json else res)
        return 0

    elif args.subcommand == "page":
        res = run_page(args.url, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "technical":
        res = run_technical(args.url, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "content":
        res = run_content(args.url)
        return print_result(res)

    elif args.subcommand == "schema":
        res = run_schema(args.target, extra_args=args.extra + unknown, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "sitemap":
        res = run_sitemap(args.url, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "speed":
        res = run_speed(args.url, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "geo":
        res = run_geo(args.url, json_output=args.json)
        return print_result(res)

    elif args.subcommand == "drift":
        res = run_drift(args.action, args.url, args.extra + unknown)
        return print_result(res)

    elif args.subcommand == "backlinks":
        res = run_backlinks(args.url, action=args.action)
        return print_result(res)

    elif args.subcommand == "google":
        res = run_google(args.cmd, args.args + unknown)
        return print_result(res)

    elif args.subcommand == "script":
        res = execute_script(args.script_name, args.args + unknown, capture_output=False)
        return res.get("returncode", 0)

    return 0


if __name__ == "__main__":
    sys.exit(main())
