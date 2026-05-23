---
name: openspec-git-discipline
description: Use when OpenSpec propose, continue, apply, verify, archive, branch, merge, or worktree timing affects git history.
license: MIT
compatibility: Codex lazy-loaded skill for git-backed OpenSpec projects.
---

# OpenSpec Git Discipline

Use this optional skill only after recommendation and user consent.

Core rule: every OpenSpec state change must cross `main` before the next
lifecycle phase depends on it.

- Proposal artifacts may be drafted on a branch, but must be committed and
  merged to `main` before apply starts.
- Apply may run on `main`, a branch, or a worktree only if that exact proposal
  state is already available on `main`.
- Archive should run from `main` after implementation is merged back.
- Never create commits, branches, merges, or archives unless the user explicitly
  asks.

## Gates

- Before propose: prefer `main`; otherwise warn and ask whether to continue.
- During continue: ask about committing completed artifact changes before the
  next artifact when the change is git-sensitive.
- Before apply: run `git status --short` and verify proposal artifacts are not
  only local uncommitted state.
- Before archive: run `git branch --show-current` and `git status --short`;
  stop if not on `main` or implementation has not been merged.
- After archive: ask the user whether to commit archive/spec sync changes.

## Required Language

If proposal state has not reached `main`:

> I should not apply this yet because the proposal change has not reached
> `main`. A proposal can be drafted on a branch, but apply must start only after
> that proposal state is available on `main`.

If archive is not running from merged `main`:

> I should not archive this yet because archive must run from `main` after
> implementation is merged back. Verify makes a change eligible to merge; it
> does not replace the merge.
