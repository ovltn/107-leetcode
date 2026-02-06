#!/usr/bin/env python3
"""
Generate team dashboard from all problem files.
Creates DASHBOARD.md with member statistics and leaderboard.
"""

import re
from pathlib import Path


def parse_problem_file(filepath: Path):
    """Parse a problem file and extract member statuses."""
    with open(filepath) as f:
        content = f.read()
    
    # Extract table rows
    table_pattern = r"\| ([^|]+) \| ([^|]+) \| ([^|]*) \| ([^|]*) \|"
    matches = re.findall(table_pattern, content)
    
    # Skip header row and parse data
    data_rows = [m for m in matches if m[0].strip() != "Member"]
    
    result = {}
    for row in data_rows:
        member = row[0].strip()
        status = row[1].strip()
        result[member] = status
    
    return result


def generate_dashboard():
    """Generate dashboard from all problem files."""
    problems_dir = Path(__file__).parent.parent / "problems"
    
    # Collect all unique members from problem files
    all_members = set()
    
    # Process all problem files in all week folders
    problem_files = []
    if problems_dir.exists():
        # Recursively find all .md files in week subdirectories
        problem_files = sorted(problems_dir.rglob("*.md"))
    
    # First pass: collect all unique members
    for filepath in problem_files:
        statuses = parse_problem_file(filepath)
        all_members.update(statuses.keys())
    
    # Initialize stats for all members found
    stats = {member: {"solved": 0} for member in all_members}
    
    # Second pass: count solved problems
    for filepath in problem_files:
        statuses = parse_problem_file(filepath)
        for member, status in statuses.items():
            if member in stats:
                if status == "✅":
                    stats[member]["solved"] += 1
    
    # Sort members by solved (descending)
    sorted_members = sorted(
        all_members,
        key=lambda m: stats[m]["solved"],
        reverse=True
    )
    
    # Generate dashboard content
    lines = [
        "# 🚀 Team Dashboard",
        "",
        "| Member | Solved |",
        "|---------|-----------|"
    ]
    
    for member in sorted_members:
        solved = stats[member]["solved"]
        lines.append(f"| {member} | {solved} |")
    
    lines.append("")
    lines.append(f"**Total problems**: {len(problem_files)}")
    lines.append("")
    
    # Write dashboard
    dashboard_path = Path(__file__).parent.parent / "DASHBOARD.md"
    with open(dashboard_path, 'w') as f:
        f.write("\n".join(lines) + "\n")
    
    print(f"✅ Dashboard generated with {len(problem_files)} problems")


if __name__ == "__main__":
    generate_dashboard()
