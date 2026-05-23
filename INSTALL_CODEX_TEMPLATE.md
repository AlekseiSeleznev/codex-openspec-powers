# Install Codex OpenSpec Powers

This guide applies Codex OpenSpec Powers to an existing OpenSpec project
without silently replacing project-owned OpenSpec content.

## Prerequisite

Prepare the target project with an OpenSpec Codex foundation first:

```bash
openspec init --tools codex
```

An equivalent existing setup is fine when it already provides `openspec/`,
`openspec/config.yaml`, and `.codex/skills/openspec-*`.

Superpowers integration is optional but external. If users want the
`superpowers:*` recommendations to run, enable the Superpowers plugin in the
Codex environment. This template does not vendor Superpowers into
`.codex/skills`; when the plugin is unavailable, Codex should skip that
accelerator and continue the OpenSpec workflow.

Optional recommendations are grouped at each decision point. Codex should show
one `**== РЕКОМЕНДАЦИЯ ==**` block, number applicable steps, and accept `1`,
comma-separated sequences such as `1,2`, `+` for all recommended steps, and `-`
for no optional steps. After selected steps finish, Codex returns to the active
OpenSpec workflow and makes the next suggested step account for that choice.

## Safe To Add

Add these paths when they are absent:

- `.codex/codex-openspec-powers/manifest.yaml`
- `.codex/codex-openspec-powers/claude-review.yaml`
- `.codex/prompts/opsx-*.md`
- `.codex/skills/architectural-decision-records/`
- `.codex/skills/c4-diagrams/`
- `.codex/skills/gherkin-authoring/`
- `.codex/skills/grill-with-docs/`
- `.codex/skills/openspec-git-discipline/`
- `INSTALL_CODEX_TEMPLATE.md`

If a target project has a `.gitignore`, merge-review it instead of replacing it.

## Merge Review

Treat these paths as merge-review content when they already exist:

- `.codex/`
- `.codex/prompts/`
- `.codex/skills/`
- `.gitignore`
- `AGENTS.md`
- `README.md`
- `README.en.md`
- `openspec/config.yaml`
- `openspec/schemas/`

Specific files listed as template-owned in
`.codex/codex-openspec-powers/manifest.yaml` take precedence over a containing
merge-review directory. Other files in those directories remain project-owned.

## Never Overwrite Silently

Do not replace these paths during overlay installation:

- `openspec/changes/`
- `openspec/specs/`
- project source code, package files, tests, `docs/`, and product documentation

If a project already uses a custom OpenSpec schema, keep it. Any optional
project-specific schema support may be added only after explicit user approval
and must not replace the active schema in `openspec/config.yaml` silently.

## Claude OpenSpec Review

Claude OpenSpec Review is OFF by default. The user-editable configuration lives
at `.codex/codex-openspec-powers/claude-review.yaml`.

Controls:

- `/opsx:claude-review on`
- `/opsx:claude-review off`
- `/opsx:claude-review status`
- `/opsx:claude-review run <change> <stage>`

Default budgets:

- `propose`: 0.50 USD
- `apply-readiness`: 1.50 USD
- `archive-readiness`: 1.00 USD

Codex sends Claude only an isolated temporary bundle containing relevant
OpenSpec markdown/config files for the named change: `proposal.md`,
`design.md`, `tasks.md`, `README.md`, `specs/*/spec.md`, and
`openspec/config.yaml`. The repository root and broad globs are not passed to
Claude unless the user explicitly expands scope with named files.

Review output is saved under
`openspec/changes/<change>/reviews/claude-<stage>-<timestamp>.md`. Applied
doc-only summaries and manual blocker resolutions are append-only logs in the
same `reviews/` directory. Unresolved Critical or High findings block
`/opsx:apply` and `/opsx:archive`; turning review OFF does not clear blockers.

## Healthcheck

Run `/opsx:check-overlay` after `openspec init --tools codex`, OpenSpec
upgrades, or suspected generated-file overwrites. The healthcheck reads the
manifest, reports missing template-owned additions, checks documentation
snippets, and asks for confirmation before repairing anything.

## Verification

After installation, run:

```bash
git status --short
openspec status --change <change> --json
```

If OpenSpec or Codex tooling is unavailable, report that clearly and leave the
installed files for manual review.
