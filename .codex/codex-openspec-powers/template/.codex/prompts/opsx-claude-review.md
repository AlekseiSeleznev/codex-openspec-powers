---
description: Control and run optional Claude OpenSpec Review
---

Control Claude OpenSpec Review.

Supported commands:

- `/opsx:claude-review on`
- `/opsx:claude-review off`
- `/opsx:claude-review status`
- `/opsx:claude-review run <change> <stage>`

Valid stages are `propose`, `apply-readiness`, and `archive-readiness`.
Canonical YAML stage keys are `propose`, `applyReadiness`, and
`archiveReadiness`; warn and ignore kebab-case YAML override keys.
Preserve and warn on any unknown extra config key instead of deleting or acting
on it silently.
Reject any unknown stage before building a bundle or invoking Claude.

For control commands:

- `on`: set `claudeOpenSpecReview.enabled: true` in
  `.codex/codex-openspec-powers/claude-review.yaml`.
- `off`: set `claudeOpenSpecReview.enabled: false`; do not delete saved review
  artifacts and do not clear unresolved blockers.
- `status`: read the config and saved review/applied/resolution files, report
  enabled state and unresolved Critical/High blockers, and do not write files.

When updating the config, preserve known settings and unknown extra keys. Warn
about unknown extras and ignored kebab-case stage keys instead of deleting them
or treating them as active overrides.

**== РЕВЬЮ CLAUDE ==**

Rules:

- Default state is OFF.
- Read `.codex/codex-openspec-powers/claude-review.yaml`.
- Before invoking Claude, emit this block with the change name, stage,
  whitelisted file summary, resolved budget, model, effort, and pre-call limits.
- Treat `model: default` and `effort: default` as sentinels that inherit Claude
  CLI defaults; do not pass literal `default` overrides to Claude.
- Enforce pre-call `maxInputBytes` and `maxFiles` before invocation.
- Build a temporary isolated bundle containing only whitelisted files for the
  selected change plus `openspec/config.yaml`.
- Invoke `claude -p` from the bundle directory only.
- Do not pass repository root, broad globs, or absolute repository paths.
- Accept extra review files only when the user explicitly names repository
  relative files and confirms them. Reject directories and broad globs.
- Remove the temporary review bundle after completion, failure, or skip unless
  the user explicitly asks to preserve it for debugging.
- Save review output under
  `openspec/changes/<change>/reviews/claude-<stage>-<timestamp>.md`.
- Save any available partial output when the Claude CLI exits non-zero, times
  out, or aborts.
- Require stable finding IDs and severity values `Critical`, `High`, `Medium`,
  or `Low`.
- Define severity as: `Critical` means unsafe workflow, security/data-loss risk,
  or broken gate; `High` means a lifecycle-integrity or required-artifact issue
  that must be fixed before the next gated step; `Medium` means a non-blocking
  completeness, maintainability, or clarity issue; `Low` means cosmetic wording
  or formatting feedback.
- Critical/High findings block apply/archive until an applied summary or manual
  resolution references the finding ID.
- `/opsx:claude-review status` reports unresolved Critical/High blockers even
  when review is OFF and states which gated steps remain blocked.
- Claude never writes project files directly.
- With `autoApplySafeDocFixes: false`, ask `Выполнить?` before applying any
  safe doc-only fix.

If `claude` is unavailable, budget is reached, pre-call limits fail, isolation
cannot be created, or the mid-call fails, mark the stage externally unreviewed
or incomplete and report the reason.

If an optional recommendation is accepted and the recommended skill, Superpowers step, or review tool runs, return to this OpenSpec workflow after it finishes and still finish the user-facing response with the blocks below.

Finish user-visible output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

Pick the next command based on the invoked sub-command or stage:

- For `run <change> propose` or `run <change> apply-readiness`, return to the
  caller when this is a workflow substep; otherwise select the apply command if
  no unresolved blocker remains.
- For `run <change> archive-readiness`, return to the caller when this is a
  workflow substep; otherwise select the archive command if no unresolved
  blocker remains.
- For `on`, `off`, or `status`, suggest the caller's active OpenSpec command
  when known; otherwise suggest `/opsx:check-overlay` as a safe follow-up.

Render the selected command as a ready-to-run Codex command. Choose a concrete
command for the current branch; never render an angle-bracket placeholder.

```text
/opsx:check-overlay
```

Выполнить?

**Да / Нет**
