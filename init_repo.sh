#!/bin/bash
# === MKUltra Git Init Script ===
# Remotes: local GitLab (origin) → public GitLab → GitHub
# Branch:  patient0
# Enhanced: 2026-05-08 | Rat Dev / Mause König
#
# Enhancements over v1:
#   1. --dry-run flag: shows what would be staged without committing
#   2. Push order: local → public GitLab → GitHub last
#      (GitHub requires repo to exist first; if it doesn't, the
#       local and GitLab pushes still succeed independently)
#   3. Per-remote error handling: one remote failing doesn't kill the others
#   4. Pre-flight checks: git binary, working directory, remote reachability hint
#   5. Staged file count reported before commit
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

# === CONFIG ===
REPO_NAME="MKUltra"
LOCAL_GITLAB_URL="http://192.168.0.15/scp-localhost/$REPO_NAME.git"
GITHUB_URL="git@github.com:scp-localhost/$REPO_NAME.git"
GITLAB_PUBLIC_URL="https://gitlab.com/scp-localhost/$REPO_NAME.git"
DEFAULT_BRANCH="patient0"
COMMIT_MESSAGE="Initial commit (automated)"

# === FLAGS ===
DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
  echo "🔍 DRY RUN — no commits or pushes will occur"
fi

# === PRE-FLIGHT ===
echo ""
echo "=== MKUltra init: pre-flight ==="

# Confirm we're in the right directory
if [[ ! -f "README.md" ]]; then
  echo "⚠️  WARNING: No README.md found. Are you in the repo root?"
  echo "   Expected: ~/git/$REPO_NAME"
  echo "   Current:  $(pwd)"
  read -p "   Continue anyway? [y/N] " confirm
  [[ "$confirm" =~ ^[Yy]$ ]] || { echo "Aborted."; exit 1; }
fi

# Confirm .gitignore is present
if [[ ! -f ".gitignore" ]]; then
  echo "❌ .gitignore not found. Place it at repo root before init."
  exit 1
fi
echo "✅ .gitignore present"

# === INIT ===
echo ""
echo "=== Git init ==="
if [ ! -d .git ]; then
  echo "🌀 Initializing Git repo on branch: $DEFAULT_BRANCH"
  git init -b "$DEFAULT_BRANCH"
else
  echo "✅ Git repo already initialized"
  CURRENT_BRANCH=$(git branch --show-current)
  echo "   Current branch: $CURRENT_BRANCH"
fi

# === DRY RUN: show what would be staged ===
if $DRY_RUN; then
  echo ""
  echo "=== Dry run: files that would be staged ==="
  git add --dry-run -A
  echo ""
  echo "=== Dry run: files that would be EXCLUDED (via .gitignore) ==="
  git ls-files --others --ignored --exclude-standard | head -30
  echo ""
  echo "🔍 Dry run complete. Re-run without --dry-run to commit and push."
  exit 0
fi

# === REMOTE SETUP ===
echo ""
echo "=== Remote setup ==="
git remote remove origin        2>/dev/null && echo "  removed: origin"        || true
git remote remove github        2>/dev/null && echo "  removed: github"        || true
git remote remove gitlab-public 2>/dev/null && echo "  removed: gitlab-public" || true

git remote add origin        "$LOCAL_GITLAB_URL"
git remote add github        "$GITHUB_URL"
git remote add gitlab-public "$GITLAB_PUBLIC_URL"

echo "  added: origin        → $LOCAL_GITLAB_URL"
echo "  added: github        → $GITHUB_URL"
echo "  added: gitlab-public → $GITLAB_PUBLIC_URL"

# === STAGE + COMMIT ===
echo ""
echo "=== Stage and commit ==="

if [ -z "$(git status --porcelain)" ]; then
  echo "✅ Nothing to commit — working tree clean."
else
  STAGED_COUNT=$(git diff --cached --numstat 2>/dev/null | wc -l || echo "0")
  git add .
  STAGED_COUNT=$(git diff --cached --numstat | wc -l)
  echo "📦 Staging $STAGED_COUNT file(s)..."
  git commit -m "$COMMIT_MESSAGE"
  echo "✅ Committed: \"$COMMIT_MESSAGE\""
fi

# === PUSH — order matters ===
# Push local GitLab first (always available, no pre-existence requirement).
# Push public GitLab second (may require project creation but tolerant).
# Push GitHub last — GitHub SSH remote requires the repo to exist on
# github.com before the first push. If it doesn't exist yet:
#   1. Create it at https://github.com/new (empty, no README, no .gitignore)
#   2. Re-run this script (local and GitLab pushes will be no-ops; GitHub push will land)
# Each remote is independent — one failure does not abort the others.

echo ""
echo "=== Push to remotes ==="

push_remote() {
  local name="$1"
  local label="$2"
  echo ""
  echo "🚀 Pushing to $label..."
  if git push -u "$name" "$DEFAULT_BRANCH"; then
    echo "✅ $label push succeeded"
  else
    echo "❌ $label push FAILED"
    echo "   Remote: $(git remote get-url "$name")"
    if [[ "$name" == "github" ]]; then
      echo ""
      echo "   ── GitHub pre-existence note ──────────────────────────────"
      echo "   GitHub requires the remote repo to exist before first push."
      echo "   If you haven't created it yet:"
      echo "     1. Go to https://github.com/new"
      echo "     2. Name: $REPO_NAME"
      echo "     3. Visibility: Private (or Public — your call)"
      echo "     4. ⚠️  Do NOT initialise with README, .gitignore, or licence"
      echo "            (empty repo only — local content takes precedence)"
      echo "     5. Re-run: bash init_repo.sh"
      echo "   ────────────────────────────────────────────────────────────"
    fi
    echo "   Other remotes are unaffected. Continuing..."
  fi
}

push_remote "origin"        "local GitLab (origin)"
push_remote "gitlab-public" "public GitLab"
push_remote "github"        "GitHub"

# === SUMMARY ===
echo ""
echo "================================================"
echo " MKUltra init complete"
echo "================================================"
echo " Branch:       $DEFAULT_BRANCH"
echo " Remotes:"
git remote -v | grep "(push)" | awk '{printf "   %-16s %s\n", $1, $2}'
echo ""
echo " To verify what landed:"
echo "   git log --oneline"
echo "   git remote show origin"
echo "================================================"
