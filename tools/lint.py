#!/usr/bin/env python3
"""
ACCOUNT.md Linter — validates ACCOUNT.md files against the spec.

Usage:
    python lint.py path/to/ACCOUNT.md
    python lint.py path/to/accounts/          # lint all .md files in directory
"""

import sys
import os
import re
import yaml


REQUIRED_FIELDS = ["version", "name", "slug", "health", "tier", "privacy"]
VALID_HEALTH = ["green", "yellow", "red"]
VALID_PRIVACY = ["full", "masked", "ids-only"]
VALID_CONTACT_ROLES = ["decision-maker", "champion", "day-to-day", "executive", "technical"]
VALID_THREAD_STATUSES = ["Not started", "In progress", "Waiting", "Resolved"]
VALID_CONFIDENCE = ["single-source", "corroborated", "verified"]
REQUIRED_SECTIONS = ["HEAD", "BODY", "FOOTER"]
CONTENT_LINE_CAP = 300


def lint_file(filepath):
    """Lint a single ACCOUNT.md file. Returns list of (level, message) tuples."""
    issues = []

    with open(filepath, "r") as f:
        content = f.read()

    # Parse YAML front matter
    front_matter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not front_matter_match:
        issues.append(("error", "No YAML front matter found"))
        return issues

    try:
        meta = yaml.safe_load(front_matter_match.group(1))
    except yaml.YAMLError as e:
        issues.append(("error", f"Invalid YAML front matter: {e}"))
        return issues

    if not isinstance(meta, dict):
        issues.append(("error", "YAML front matter is not a mapping"))
        return issues

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in meta:
            issues.append(("warn", f"Missing required field: {field}"))

    # Validate health enum
    if "health" in meta and meta["health"] not in VALID_HEALTH:
        issues.append(("error", f"Invalid health value: '{meta['health']}'. Must be one of: {', '.join(VALID_HEALTH)}"))

    # Validate privacy enum
    if "privacy" in meta and meta["privacy"] not in VALID_PRIVACY:
        issues.append(("warn", f"Unknown privacy mode: '{meta['privacy']}'. Standard values: {', '.join(VALID_PRIVACY)}"))

    # Validate contacts
    contacts = meta.get("contacts", [])
    if contacts:
        for i, contact in enumerate(contacts):
            if not isinstance(contact, dict):
                issues.append(("warn", f"Contact {i + 1} is not a mapping"))
                continue
            if "name" not in contact and meta.get("privacy") == "full":
                issues.append(("warn", f"Contact {i + 1} missing name (privacy mode is full)"))
            if "role" not in contact:
                issues.append(("warn", f"Contact {i + 1} missing role"))
            elif contact["role"] not in VALID_CONTACT_ROLES:
                issues.append(("info", f"Contact {i + 1} uses custom role: '{contact['role']}'"))

    # Validate parent/children types
    if "parent" in meta and meta["parent"] is not None and not isinstance(meta["parent"], str):
        issues.append(("warn", f"parent field should be a string (slug) or null"))

    if "children" in meta and not isinstance(meta.get("children"), list):
        issues.append(("warn", f"children field should be a list of slugs"))

    # Check markdown body sections
    body = content[front_matter_match.end():]
    sections_found = re.findall(r"^## (\w+)", body, re.MULTILINE)

    for section in REQUIRED_SECTIONS:
        if section not in sections_found:
            issues.append(("warn", f"Missing section: ## {section}"))

    # Check section order
    section_positions = {}
    for section in REQUIRED_SECTIONS:
        if section in sections_found:
            section_positions[section] = sections_found.index(section)

    if len(section_positions) >= 2:
        ordered = sorted(section_positions.keys(), key=lambda s: section_positions[s])
        expected = [s for s in REQUIRED_SECTIONS if s in ordered]
        if ordered != expected:
            issues.append(("error", f"Sections out of order. Expected: {' → '.join(expected)}. Found: {' → '.join(ordered)}"))

    # Check for duplicate sections
    for section in REQUIRED_SECTIONS:
        count = sections_found.count(section)
        if count > 1:
            issues.append(("error", f"Duplicate section: ## {section} (found {count} times)"))

    # Count content lines (excluding references blocks)
    content_lines = body.split("\n")
    in_references = False
    content_line_count = 0
    for line in content_lines:
        if line.strip() == "### References":
            in_references = True
            continue
        if in_references and line.startswith("## "):
            in_references = False
        if not in_references and line.strip():
            content_line_count += 1

    yaml_lines = front_matter_match.group(0).count("\n")
    total_content = yaml_lines + content_line_count

    if total_content > CONTENT_LINE_CAP:
        issues.append(("warn", f"File has ~{total_content} content lines (guideline: {CONTENT_LINE_CAP}). Consider archiving older entries."))

    # Check signal log confidence tiers (5-column tables under "Signal Log" heading)
    in_signal_log = False
    for line in body.split("\n"):
        stripped = line.strip()
        if "Signal Log" in stripped and stripped.startswith("#"):
            in_signal_log = True
            continue
        if in_signal_log and stripped.startswith("#") and "Signal Log" not in stripped:
            in_signal_log = False
            continue
        if in_signal_log and stripped.startswith("|"):
            cells = [c.strip() for c in line.split("|") if c.strip()]
            if len(cells) == 5:
                confidence = cells[-1].lower()
                if confidence in ["confidence", "---"]:
                    continue
                if confidence not in VALID_CONFIDENCE:
                    issues.append(("info", f"Unknown confidence tier: '{confidence}'"))

    return issues


def print_results(filepath, issues):
    """Print lint results for a file."""
    basename = os.path.basename(filepath)
    if not issues:
        print(f"  ✓ {basename} — no issues")
        return 0

    errors = [i for i in issues if i[0] == "error"]
    warns = [i for i in issues if i[0] == "warn"]
    infos = [i for i in issues if i[0] == "info"]

    print(f"\n  {basename}")
    for level, msg in issues:
        symbol = {"error": "✗", "warn": "!", "info": "·"}[level]
        print(f"    {symbol} [{level}] {msg}")

    print(f"    — {len(errors)} error(s), {len(warns)} warning(s), {len(infos)} info")
    return len(errors)


def main():
    if len(sys.argv) < 2:
        print("Usage: python lint.py <file.md or directory>")
        sys.exit(1)

    target = sys.argv[1]
    files = []

    if os.path.isdir(target):
        for root, dirs, filenames in os.walk(target):
            for f in filenames:
                if f.endswith(".md") and f != "ACCOUNT.config.md":
                    filepath = os.path.join(root, f)
                    with open(filepath) as fh:
                        first_line = fh.readline()
                        if first_line.strip() == "---":
                            files.append(filepath)
    elif os.path.isfile(target):
        files.append(target)
    else:
        print(f"Not found: {target}")
        sys.exit(1)

    if not files:
        print("No ACCOUNT.md files found.")
        sys.exit(0)

    print(f"\nACCOUNT.md Lint — checking {len(files)} file(s)\n")

    total_errors = 0
    for filepath in sorted(files):
        issues = lint_file(filepath)
        total_errors += print_results(filepath, issues)

    print(f"\n{'—' * 40}")
    if total_errors == 0:
        print("All files passed.")
    else:
        print(f"{total_errors} error(s) found.")
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
