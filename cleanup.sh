#!/bin/bash
# === MKUltra Repo Cleanup ===
# Generated: 2026-05-08 | Node: Rat Dev / Mause König
# Curation plan: PROJECT_KNOWLEDGE_CURATION_20260508.md
#
# What this script does:
#   1. Purges docs/_archive/ — reconciliation maps and stale SAPs
#      (superseded; actively misleading to any new node that reads them)
#      Exception: epistemic ownership evidence is NOT touched.
#   2. Purges drafts/draft_bibliography_md/ — entire directory
#      (superseded by docs/SERIES_BIBLIOGRAPHY.md v1.1)
#   3. Removes root-level assembled Paper[N]_Draft.md files
#      (superseded by paper[N]/Paper[N]_Rewrite.md or section files)
#   4. Removes drafts/Paper1_Compiled_Draft.md
#      (pre-rewrite compiled version; superseded by Paper1_Rewrite.md)
#   5. Removes drafts/SERIES_DRAFT_INDEX.md
#      (superseded by RUNBOOK.md and CHECKPOINT_20260508.md)
#   6. Removes drafts/P7_S5_Results_Placeholder.md root-level duplicate
#      (canonical copy is drafts/paper7/P7_S5_Results_Placeholder.md)
#
# What this script does NOT touch:
#   scripts/_archive/    — Jung/Tarot monoliths preserved (epistemic ownership)
#   seeds/_archive/      — seed provenance preserved
#   docs/_archive/       — directory kept but stale content removed
#   Paper2_Draft.md      — P2 rewrite is incomplete; assembled draft is still
#                          the reference until Paper2_Rewrite_v1.md is complete
#   Paper3_Draft.md      — P3 S1-S3 only; assembled draft is the working doc
#   Paper6_Draft.md      — no rewrite started; assembled draft is working doc
#   Paper7_Draft.md      — no rewrite started; assembled draft is working doc
#   Any .docx files      — already excluded by .gitignore; no action needed
#
# Safety: dry-run mode shows what would be deleted without deleting anything.
# Usage:
#   bash cleanup.sh --dry-run    # preview
#   bash cleanup.sh              # execute
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
  echo "🔍 DRY RUN — nothing will be deleted"
  echo ""
fi

REMOVED=0
SKIPPED=0

# Helpers
remove() {
  local target="$1"
  local reason="$2"
  if [[ -e "$target" ]]; then
    if $DRY_RUN; then
      echo "  [DRY] rm -rf $target"
      echo "        reason: $reason"
    else
      rm -rf "$target"
      echo "  ✅ removed: $target"
    fi
    REMOVED=$((REMOVED + 1))
  else
    echo "  ⏭  not found (already gone?): $target"
    SKIPPED=$((SKIPPED + 1))
  fi
}

# Confirm we're in the right place
if [[ ! -f "README.md" ]] || [[ ! -d "scripts" ]]; then
  echo "❌ Not in MKUltra repo root. Aborting."
  echo "   Expected README.md and scripts/ at current directory."
  echo "   Current: $(pwd)"
  exit 1
fi

echo "=== MKUltra cleanup — $(date '+%Y-%m-%d %H:%M') ==="
echo "Working directory: $(pwd)"
echo ""


# ── 1. docs/_archive/ — purge stale reconciliation maps and SAPs ──────────────
# Epistemic ownership note: these are process/state documents, not intellectual
# origin artifacts. Safe to purge. The reconciliation maps are actively
# misleading (mark resolved items as open). The SAP versions are superseded.

echo "--- 1. docs/_archive/ — stale process documents ---"

remove "docs/_archive/RECONCILIATION_MAP.md" \
  "marks P1 S3 as MISSING and data_dictionary as STUB — both false"

remove "docs/_archive/RECONCILIATION_MAP_v2.md" \
  "same stale state; superseded by RUNBOOK.md"

remove "docs/_archive/Statistical_Analysis_Plan.md" \
  "v1.0 — superseded by SAP v1.2 (docs/Statistical_Analysis_Plan_v1.2.md)"

remove "docs/_archive/Statistical_Analysis_Plan_v1.1.md" \
  "v1.1 — superseded by SAP v1.2; wrong analysis sequence references"

# Check if _archive is now empty; if so, remove the directory stub
if [[ -d "docs/_archive" ]] && [[ -z "$(ls -A docs/_archive 2>/dev/null)" ]]; then
  if $DRY_RUN; then
    echo "  [DRY] rmdir docs/_archive  (would be empty after above removals)"
  else
    rmdir "docs/_archive"
    echo "  ✅ removed empty: docs/_archive/"
  fi
fi

echo ""


# ── 2. drafts/draft_bibliography_md/ — entire directory ───────────────────────
# Superseded entirely by docs/SERIES_BIBLIOGRAPHY.md v1.1.
# Contains stale Hadnagy (2010), split-date errors, Anderson (1978) (removed),
# and references to RECONCILIATION_MAP_v2.md as a project artifact.

echo "--- 2. drafts/draft_bibliography_md/ — superseded by bibliography gem ---"

remove "drafts/draft_bibliography_md" \
  "entire directory superseded by docs/SERIES_BIBLIOGRAPHY.md v1.1"

echo ""


# ── 3. Root-level assembled Paper[N]_Draft.md files ───────────────────────────
# These are the initial assembly outputs at drafts/ root.
# P1 and P4 are superseded by their Rewrite.md files.
# P2: keep (rewrite is incomplete — Paper2_Rewrite_v1.md covers S1-S2 only)
# P3: keep (assembled draft is working doc; S4-S8 pending data)
# P5/P6/P7: keep (no rewrites started; assembled drafts are working docs)

echo "--- 3. Root-level assembled drafts — superseded by rewrites ---"

remove "drafts/Paper1_Draft.md" \
  "superseded by drafts/paper1/Paper1_Rewrite.md (clean, scaffolding-free)"

remove "drafts/Paper4_Draft.md" \
  "superseded by drafts/paper4/Paper4_Rewrite.md (clean, scaffolding-free)"

echo "  ⏭  keeping drafts/Paper2_Draft.md (P2 rewrite is incomplete)"
echo "  ⏭  keeping drafts/Paper3_Draft.md (assembled working doc; data pending)"
echo "  ⏭  keeping drafts/Paper5_Draft.md (no rewrite started)"
echo "  ⏭  keeping drafts/Paper6_Draft.md (no rewrite started)"
echo "  ⏭  keeping drafts/Paper7_Draft.md (no rewrite started)"

echo ""


# ── 4. drafts/paper1/Paper1_Compiled_Draft.md ────────────────────────────────
# Pre-rewrite compiled version. Superseded by Paper1_Rewrite.md.
# The rewrite is the canonical P1 text.

echo "--- 4. Pre-rewrite compiled draft ---"

remove "drafts/paper1/Paper1_Compiled_Draft.md" \
  "superseded by Paper1_Rewrite.md"

echo ""


# ── 5. drafts/SERIES_DRAFT_INDEX.md ──────────────────────────────────────────
# Assembly-pass index. Superseded by RUNBOOK.md and CHECKPOINT_20260508.md.
# Contains stale flags (C-10 CRITICAL — resolved; P1 S3 MISSING — resolved).

echo "--- 5. Stale series index ---"

remove "drafts/SERIES_DRAFT_INDEX.md" \
  "superseded by RUNBOOK.md; contains resolved flags marked as open"

echo ""


# ── 6. drafts/P7_S5_Results_Placeholder.md (root-level duplicate) ────────────
# Canonical copy is drafts/paper7/P7_S5_Results_Placeholder.md.
# The root-level copy is a leftover from the assembly session.

echo "--- 6. P7 S5 root-level duplicate ---"

remove "drafts/P7_S5_Results_Placeholder.md" \
  "duplicate — canonical copy is drafts/paper7/P7_S5_Results_Placeholder.md"

echo ""


# ── Summary ───────────────────────────────────────────────────────────────────

echo "================================================"
if $DRY_RUN; then
  echo " DRY RUN complete — no files were modified"
  echo " Re-run without --dry-run to execute"
else
  echo " Cleanup complete"
fi
echo ""
echo " Items actioned: $REMOVED"
echo " Items skipped (not found): $SKIPPED"
echo ""
echo " Preserved (epistemic ownership):"
echo "   scripts/_archive/     Jung/Tarot monoliths — provenance evidence"
echo "   seeds/_archive/       seed provenance"
echo ""
echo " Preserved (active working docs):"
echo "   drafts/Paper2_Draft.md     P2 rewrite incomplete"
echo "   drafts/Paper3_Draft.md     data pending"
echo "   drafts/Paper5_Draft.md     no rewrite started"
echo "   drafts/Paper6_Draft.md     no rewrite started"
echo "   drafts/Paper7_Draft.md     no rewrite started"
echo "================================================"

# Suggest a quick git status to see what changed
if ! $DRY_RUN; then
  echo ""
  echo "Next: git add -A && git status"
  echo "      Review the deletions, then: git commit -m 'cleanup: purge superseded docs'"
fi
