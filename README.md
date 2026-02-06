# 🚀 LeetCode Team Progress Tracker

A **GitHub-only** system for tracking team LeetCode progress using Python scripts, GitHub Actions, and markdown storage. No external APIs, no local tools required for members—everything runs in GitHub Actions.

## 🎯 Features

- ✅ **Submit progress via GitHub UI** (no git/terminal needed)
- 👥 **Automatic member detection** (uses GitHub actor, no manual setup)
- 🏷️ **Tag-based problem organization** (Array, Hash Table, etc.)
- 🔗 **Submission link tracking** (link your LeetCode submissions)
- 📊 **Automated dashboard generation**
- 🔄 **CI/CD validation** of submissions
- 📝 **Markdown-based storage** (problems organized by week)
- 🤖 **Fully automated** via GitHub Actions

## 📁 Project Structure

```
.
├── problems/           # Weekly folders (YYYY-week-XX) containing problem files
│   ├── 2026-week-05/  # Week 5 of 2026 problems
│   └── 2026-week-06/  # Week 6 of 2026 problems
├── scripts/            # Python automation scripts
├── DASHBOARD.md        # Auto-generated leaderboard
└── .github/workflows/  # GitHub Actions CI/CD
```

## 👥 For Team Members

### How to Submit Your Progress

**NO git commands needed! Use GitHub Actions UI only:**

1. Go to **Actions** tab in GitHub
2. Select **"Submit Progress"** workflow
3. Click **"Run workflow"**
4. Fill in the form:
   - **Problem slug**: e.g., `two-sum`
   - **Status**: `solved` (only option)
   - **Submission URL**: Your LeetCode submission link (e.g., `https://leetcode.com/submissions/detail/123456/`)
   - **Notes**: Optional (e.g., "Used hash map approach")
5. Click **"Run workflow"**

**Your GitHub username will be automatically detected!**

That's it! The system will:
- ✅ Update your row in the problem file
- ✅ Link your LeetCode submission
- ✅ Validate the submission
- ✅ Regenerate the team dashboard
- ✅ Commit and push changes automatically

### Important Notes

- **Automatic member detection**: The system uses your GitHub username automatically
- **First-time submission**: You'll be automatically added to all problems when you submit for the first time
- **Submission URL is required** for all submissions
- Get your submission URL from LeetCode after submitting your solution
- The URL format is: `https://leetcode.com/submissions/detail/[submission-id]/`

## 🔧 For Admins

### Adding a New Problem

**Option 1: Manual via GitHub Actions**

1. Go to **Actions** → **"Daily Problem"**
2. Click **"Run workflow"**
3. Fill in:
   - **slug**: `two-sum`
   - **title**: `Two Sum`
   - **url**: `https://leetcode.com/problems/two-sum/`
   - **tags**: `Array, Hash Table`
4. Click **"Run workflow"**

**Option 2: Automatic Daily**

The workflow runs automatically every day at 9 AM UTC (creates placeholder problem).

### Adding a New Member

**No manual setup needed!** Members are automatically added when they:
- Trigger the "Submit Progress" workflow (their GitHub username is used)
- Make their first submission to any problem

Optional: You can pre-populate members by adding them to `members.json`, but this is not required.

### Viewing the Dashboard

Check `DASHBOARD.md` for the auto-generated leaderboard showing:
- Member names
- Solved count (✅)
- Sorted by solved count

## 🛠️ Technical Details

### Scripts

| Script | Purpose |
|--------|---------|
| `create_problem.py` | Generate daily problem markdown template with tags |
| `submit.py` | Update member progress with submission URL |
| `validate.py` | Validate problem markdown structure |
| `dashboard.py` | Generate team leaderboard |

### Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `submit.yml` | Manual (workflow_dispatch) | Member progress submission |
| `dashboard.yml` | Push to `problems/**` | Auto-rebuild dashboard |
| `daily-problem.yml` | Daily cron + manual | Create new problem file |

### Problem File Format

Problems are organized in weekly folders (`YYYY-week-XX/`) and include tags:

```markdown
# Two Sum

**Link**: https://leetcode.com/problems/two-sum/  
**Date**: 2026-02-06  
**Tags**: Array, Hash Table

## Submissions

| Member | Status | Submission Link | Notes |
|--------|--------|-----------------|-------|
| alice | ✅ | [link](https-submission-url) | Used hash map |
| bob | ❌ |  | TLE on last case |
| charlie | ⬜ |  |  |
```

**Status Symbols:**
- ⬜ = Not solved
- ✅ = Solved

## 🚀 Getting Started

1. **Fork this repository**
2. **Enable GitHub Actions** in your fork settings
3. **Give team members write access** to the repository
4. **Create your first problem** using the Daily Problem workflow
5. **Start tracking progress!** (members are added automatically)

## 📊 Example Workflow

```
Day 1: Admin creates "Two Sum" problem with tags "Array, Hash Table"
       → Problem saved in problems/2026-week-06/2026-02-06-two-sum.md
       → All members see empty rows with ⬜

Day 2: Alice submits "solved" with submission URL via GitHub Actions
       → Her row shows ✅ with link to her LeetCode submission
       → Dashboard updates automatically

Day 3: Check DASHBOARD.md to see team standings!
```

## 🔒 Requirements

- Python 3.11 (handled by GitHub Actions)
- GitHub Free plan (all features work)
- No external dependencies
- No local tools needed for members

## 📝 License

Open source - use freely for your team!

---

**Made with ❤️ for LeetCode teams who want simple, automated progress tracking**
