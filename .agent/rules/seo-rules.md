# Workspace Rule: Antigravity SEO Execution Standards

This rule governs how the Antigravity agent executes SEO tasks, audits, and content evaluations within this workspace.

## 1. Execution Protocol
- Always run bundled scripts via `python3 run_seo.py <command>` or direct `python3 scripts/<script.py>`.
- Use the `--json` flag when programmatic parsing of the results is required.
- Do not run bare network fetch requests without using `scripts/url_safety.py` or `run_seo.py` to ensure SSRF/DNS-rebinding protection.

## 2. Decision Tree for User Inquiries
- **Full site / domain check**: Execute `run_seo.py audit <url>` or run multi-step checks (technical, content, schema, speed, geo) and synthesize into an Antigravity Artifact.
- **Single URL inspection**: Run `run_seo.py page <url>` and check specific on-page signals.
- **Technical issues / Core Web Vitals**: Run `run_seo.py technical <url>` and `run_seo.py speed <url>`.
- **Content audit / E-E-A-T**: Run `run_seo.py content <url>` and check claims / citations.
- **Schema markup**: Run `run_seo.py schema <url>` to audit existing JSON-LD or generate missing schema.
- **Before/After deployments**: Run `run_seo.py drift compare <url>` against stored baselines.

## 3. Artifact Standards
- Analysis reports must be formatted in GitHub-flavored Markdown with standard headers, priority tables, and actionable remediation steps.
- Present major deliverables as Antigravity Artifacts rather than raw console dumps.
