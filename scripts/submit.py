#!/usr/bin/env python3
"""
Update a member's progress in a problem file.
Usage: submit.py <member> <slug> <status> <submission_url> <notes>
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def find_problem_file(slug: str):
    """Find problem file by slug in current week's folder."""
    today = datetime.now()
    # Get ISO week number (e.g., "2026-week-06")
    year, week, _ = today.isocalendar()
    week_str = f"week-{week:02d}-{year}"
    date_str = today.strftime("%Y-%m-%d")
    
    filename = f"{date_str}-{slug}.md"
    problems_dir = Path(__file__).parent.parent / "problems" / week_str
    filepath = problems_dir / filename
    
    if not filepath.exists():
        print(f"Error: Problem file not found: {filepath}")
        sys.exit(1)
    
    return filepath


def get_status_symbol(status: str):
    """Map status string to emoji."""
    mapping = {
        "solved": "✅",
        "pending": "⬜"
    }
    return mapping.get(status.lower(), "⬜")


def update_submission(filepath: Path, member: str, status: str, submission_url: str, notes: str):
    """Update the member's row in the problem file."""
    # Read current content
    with open(filepath) as f:
        content = f.read()
    
    # Get status symbol
    status_symbol = get_status_symbol(status)
    
    # Format submission link
    submission_link = ""
    if submission_url and submission_url.strip():
        submission_link = f"[link]({submission_url})"
    
    # Escape notes for markdown
    notes = notes.replace("|", "\\|")
    
    # Create new row
    new_row = f"| {member} | {status_symbol} | {submission_link} | {notes} |"
    
    # Pattern to match the member's row
    pattern = rf"^\| {re.escape(member)} \|.*\|.*\|.*\|$"
    
    # Check if member exists
    if re.search(pattern, content, re.MULTILINE):
        # Replace existing row
        updated_content = re.sub(pattern, new_row, content, flags=re.MULTILINE)
    else:
        # Member doesn't exist - add new row to the table
        # Strategy: Insert the row right after the header separator line
        header_separator = "|--------|--------|-----------------|-------|"
        
        if header_separator in content:
            # Split content at the header separator
            parts = content.split(header_separator, 1)
            if len(parts) == 2:
                # Reconstruct with the new row added after the separator
                updated_content = parts[0] + header_separator + "\n" + new_row + "\n" + parts[1].lstrip("\n")
                print(f"✨ Added new member '{member}' to the problem")
            else:
                print(f"Error: Could not parse table in {filepath}")
                sys.exit(1)
        else:
            print(f"Error: Could not find table header in {filepath}")
            sys.exit(1)
    
    # Write updated content
    with open(filepath, 'w') as f:
        f.write(updated_content)
    
    slug = filepath.stem.split('-', 3)[3]  # Extract slug from filename
    print(f"Updated {member}'s status to {status_symbol} for {slug}")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: submit.py <member> <slug> <status> <submission_url> <notes>")
        print("Example: submit.py alice two-sum solved 'https://leetcode.com/submissions/detail/123456/' 'Used hash map'")
        sys.exit(1)
    
    member = sys.argv[1]
    slug = sys.argv[2]
    status = sys.argv[3]
    submission_url = sys.argv[4]
    notes = sys.argv[5]
    
    filepath = find_problem_file(slug)
    update_submission(filepath, member, status, submission_url, notes)
