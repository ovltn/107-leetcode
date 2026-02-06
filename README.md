# 🚀 LeetCode Team Progress Tracker

Track team LeetCode progress using GitHub Actions. No git commands needed—everything runs through GitHub UI.

## 📌 Quick Start

### Adding a New Problem

1. Go to **Actions** → **"Daily Problem"** workflow
2. Click **"Run workflow"**
3. Fill in the form:
   - **slug**: `two-sum` (from URL)
   - **title**: `Two Sum`
   - **url**: `https://leetcode.com/problems/two-sum/`
   - **tags**: `Array, Hash Table`
4. Click **"Run workflow"**

Done! Problem file created in `problems/week-XX-YYYY/YYYY-MM-DD-slug.md`

### Submitting Your Solution

1. Go to **Actions** → **"Submit Progress"** workflow
2. Click **"Run workflow"**
3. Fill in the form:
   - **Problem slug**: `two-sum` (must match the problem file)
   - **Status**: `solved`
   - **Submission URL**: `https://leetcode.com/submissions/detail/123456/`
   - **Notes**: (optional) `Used hash map`
4. Click **"Run workflow"**

Done! Your submission is recorded and dashboard updates automatically.

## 📊 Dashboard

Check [DASHBOARD.md](DASHBOARD.md) to see team leaderboard (auto-updated).

## 🔑 Key Features

- ✅ No git/terminal needed—use GitHub UI only
- 👥 Automatic member detection (uses your GitHub username)
- 📊 Auto-generated dashboard
- 🔄 Automatic validation

## 📁 Structure

```
problems/
  week-06-2026/
    2026-02-06-two-sum.md
    2026-02-06-longest-substring.md
scripts/          # Python automation
DASHBOARD.md      # Auto-generated leaderboard
```

## ⚙️ Setup

1. Fork this repository
2. Enable GitHub Actions in Settings
3. Give team members **write access**
4. Start adding problems and submitting!

---

**Note**: The system automatically adds members when they first submit. No manual member management needed.
