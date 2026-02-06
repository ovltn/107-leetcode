#!/usr/bin/env python3
"""
Create a new problem markdown file with template structure.
Usage: create_problem.py <slug> <title> <url> <tags>
"""

import sys
import json
from pathlib import Path
from datetime import datetime


def load_members():
    """Load members from members.json"""
    members_file = Path(__file__).parent.parent / "members.json"
    with open(members_file) as f:
        return json.load(f)


def get_all_members():
    """Get all unique members from existing problem files."""
    problems_dir = Path(__file__).parent.parent / "problems"
    members = set()
    
    if problems_dir.exists():
        # Scan all problem files to find unique members
        for problem_file in problems_dir.rglob("*.md"):
            try:
                with open(problem_file) as f:
                    content = f.read()
                    # Extract member names from table rows
                    import re
                    pattern = r"^\| ([^|]+) \|"
                    matches = re.findall(pattern, content, re.MULTILINE)
                    for match in matches:
                        member = match.strip()
                        if member and member != "Member":
                            members.add(member)
            except Exception:
                continue
    
    return sorted(list(members)) if members else []


def create_problem(slug: str, title: str, url: str, tags: str):
    """Create a new problem markdown file."""
    # Get today's date and week
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    # Get ISO week number (e.g., "2026-week-06")
    year, week, _ = today.isocalendar()
    week_str = f"week-{week:02d}-{year}"
    
    # Create week directory
    problems_dir = Path(__file__).parent.parent / "problems" / week_str
    problems_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename
    filename = f"{date_str}-{slug}.md"
    filepath = problems_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Problem file already exists: {filepath}")
        return
    
    # Get members from existing problems (or use default if none exist)
    members = get_all_members()
    if not members:
        # Fallback: try to load from members.json if it exists
        try:
            members = load_members()
        except Exception:
            # If no members found anywhere, create empty problem
            members = []
    
    # Create table rows
    rows = []
    for member in members:
        rows.append(f"| {member} | ⬜ |  |  |")
    
    # Create markdown content
    content = f"""# {title}

**Link**: {url}  
**Date**: {date_str}  
**Tags**: {tags}

## Submissions

| Member | Status | Submission Link | Notes |
|--------|--------|-----------------|-------|
{chr(10).join(rows) if rows else ""}
"""
    
    # Write file
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created problem file: {filepath}")
    if members:
        print(f"Included {len(members)} existing members")
    else:
        print("No existing members found - new members will be added on first submission")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: create_problem.py <slug> <title> <url> <tags>")
        print("Example: create_problem.py two-sum 'Two Sum' 'https://leetcode.com/problems/two-sum/' 'Array, Hash Table'")
        sys.exit(1)
    
    slug = sys.argv[1]
    title = sys.argv[2]
    url = sys.argv[3]
    tags = sys.argv[4]
    
    create_problem(slug, title, url, tags)
