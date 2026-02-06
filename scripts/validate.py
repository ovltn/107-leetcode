#!/usr/bin/env python3
"""
Validate problem markdown files.
Checks structure, member presence, and valid status symbols.
"""

import sys
import json
import re
from pathlib import Path


def load_members():
    """Load members from members.json"""
    members_file = Path(__file__).parent.parent / "members.json"
    with open(members_file) as f:
        return json.load(f)


def validate_problem_file(filepath: Path, members: list):
    """Validate a single problem file."""
    errors = []
    
    # Read content
    with open(filepath) as f:
        content = f.read()
    
    # Check for submissions table
    if "## Submissions" not in content:
        errors.append(f"{filepath.name}: Missing '## Submissions' section")
    
    # Extract table rows
    table_pattern = r"\| ([^|]+) \| ([^|]+) \| ([^|]*) \| ([^|]*) \|"
    matches = re.findall(table_pattern, content)
    
    # Skip header row
    data_rows = [m for m in matches if m[0].strip() != "Member"]
    
    # Check each member has a row
    found_members = {row[0].strip() for row in data_rows}
    for member in members:
        if member not in found_members:
            errors.append(f"{filepath.name}: Missing row for member '{member}'")
    
    # Check for duplicate members
    if len(found_members) != len(data_rows):
        errors.append(f"{filepath.name}: Duplicate member rows detected")
    
    # Check valid status symbols
    valid_statuses = {"⬜", "✅"}
    for row in data_rows:
        status = row[1].strip()
        if status not in valid_statuses:
            errors.append(f"{filepath.name}: Invalid status '{status}' for {row[0].strip()}")
    
    # Check only valid members
    for member in found_members:
        if member not in members:
            errors.append(f"{filepath.name}: Unknown member '{member}'")
    
    return errors


def validate_all_problems():
    """Validate all problem files."""
    members = load_members()
    problems_dir = Path(__file__).parent.parent / "problems"
    
    if not problems_dir.exists():
        print("No problems directory found")
        return True
    
    all_errors = []
    # Recursively find all .md files in month subdirectories
    problem_files = sorted(problems_dir.rglob("*.md"))
    
    if not problem_files:
        print("No problem files to validate")
        return True
    
    for filepath in problem_files:
        errors = validate_problem_file(filepath, members)
        all_errors.extend(errors)
    
    if all_errors:
        print("Validation errors found:")
        for error in all_errors:
            print(f"  ❌ {error}")
        return False
    else:
        print(f"✅ All {len(problem_files)} problem files are valid")
        return True


if __name__ == "__main__":
    success = validate_all_problems()
    sys.exit(0 if success else 1)
