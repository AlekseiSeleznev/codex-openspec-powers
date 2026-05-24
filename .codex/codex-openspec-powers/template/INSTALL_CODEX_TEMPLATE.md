# Install Codex OpenSpec Powers

This guide applies Codex OpenSpec Powers to an existing OpenSpec project
without silently replacing project-owned OpenSpec content.

## Recommended automatic setup

From this repository, install the local `opsx` CLI and the OpenSpec auto-repair
shim:

```bash
bin/opsx install-auto-repair
```

After that, initialize each new project with:

```bash
opsx init /path/to/project
```

or from the project root:

```bash
opsx init
```

`opsx init` runs `openspec init --tools codex`, applies the overlay, and runs
`opsx repair --yes` automatically. The installed shim also keeps the normal
OpenSpec command usable: when a user runs `openspec init --tools codex` or
`openspec update`, the real OpenSpec CLI runs first and the overlay repair runs
after the OpenSpec command succeeds.

## Manual prerequisite

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
- `.codex/codex-openspec-powers/template/`
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

## Bundled repair sources

The overlay carries bundled repair sources under
`.codex/codex-openspec-powers/template/`. The source path mirrors the target
path. For example:

```text
.codex/codex-openspec-powers/template/.codex/prompts/opsx-apply.md
```

is the repair source for:

```text
.codex/prompts/opsx-apply.md
```

If `openspec init --tools codex` or an OpenSpec upgrade regenerates `/opsx`
prompts, automatic repair restores template-owned files from the bundled repair
sources. `/opsx:check-overlay` remains the manual, reviewable repair-plan view.
If the source bundle itself is missing, re-apply this template instead of
inventing replacement content.

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
upgrades, or suspected generated-file overwrites when you want a manual report.
The healthcheck reads the manifest, reports missing template-owned additions,
checks documentation snippets, compares damaged template-owned files with
bundled repair sources, and asks for confirmation before repairing anything.
The command-line auto-repair path uses the same ownership model but runs
non-interactively only after `opsx init`, `openspec init --tools codex`, or
`openspec update` succeeds.

## Verification

After installation, run:

```bash
git status --short
opsx doctor
openspec status --change <change> --json
```

If OpenSpec or Codex tooling is unavailable, report that clearly and leave the
installed files for manual review.
