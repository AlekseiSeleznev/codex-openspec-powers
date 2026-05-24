# Codex OpenSpec Powers

<p align="center">
  <strong>Codex-native workflow kit for OpenSpec projects.</strong>
</p>

<p align="center">
  <a href="README.md">Русский</a> | <strong>English</strong>
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v0.1.2-blue">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-green"></a>
  <img alt="OpenSpec" src="https://img.shields.io/badge/OpenSpec-ready-2f6fed">
  <img alt="Codex" src="https://img.shields.io/badge/Codex-native-111827">
</p>

Codex OpenSpec Powers adds a Codex-oriented layer on top of OpenSpec:
`/opsx:*` commands, local skills, safe installation rules, an overlay manifest,
a healthcheck, Superpowers recommendations, and optional Claude OpenSpec
Review.

OpenSpec remains the source of truth. Proposals, specs, designs, task lists,
implementation, verification, sync, and archive all move through OpenSpec
artifacts.

## Highlights

- Codex-native `/opsx:*` prompts for the full OpenSpec lifecycle.
- Manifest-driven overlay checks that preserve project-owned files.
- Optional skills loaded only after explicit recommendation and consent.
- When several optional actions fit a step, Codex shows one grouped
  recommendation block and accepts `1`, `1,2`, `+`, or `-`; the next suggested
  step accounts for the selected or skipped actions.
- Superpowers plugin integration as an optional methodology accelerator set.
- Claude OpenSpec Review with isolated reviewed file set handling and
  Critical/High blockers.
- Completed user-facing OpenSpec workflow steps end with `УРОКИ` and
  `СЛЕДУЮЩИЙ ШАГ` blocks.
- Published OpenSpec specs for the overlay behavior itself.

## Commands

Prompt files live in `.codex/prompts`.

| Command | Purpose |
| --- | --- |
| `/opsx:init` | Initialize a new project from Codex: run `opsx init`, restore the overlay, and check health. |
| `/opsx:new` | Create an OpenSpec change. |
| `/opsx:propose` | Prepare proposal, specs, design, and tasks. |
| `/opsx:continue` | Continue an existing change. |
| `/opsx:explore` | Explore without implementation. |
| `/opsx:apply` | Implement a change from OpenSpec artifacts. |
| `/opsx:verify` | Verify the implementation. |
| `/opsx:sync` | Sync spec deltas. |
| `/opsx:archive` | Archive a completed change. |
| `/opsx:ff` | Fast-forward OpenSpec artifact preparation. |
| `/opsx:bulk-archive` | Archive multiple changes. |
| `/opsx:check-overlay` | Check the overlay. |
| `/opsx:claude-review` | Control Claude review: `on`, `off`, `status`, `run`. |

## Skills

`.codex/skills` contains skills that extend the OpenSpec workflow in Codex.
They help carry a change from idea to archive, refine requirements, record
architecture decisions, and review project artifacts before implementation.

### OpenSpec Lifecycle Skills

These skills support the main OpenSpec lifecycle:

- `openspec-new-change` prepares a new change.
- `openspec-propose` creates proposal, specs, design, and tasks in one pass.
- `openspec-continue-change` continues an existing change and creates the next artifact.
- `openspec-explore` investigates a problem without moving into implementation.
- `openspec-apply-change` implements tasks described by an OpenSpec change.
- `openspec-verify-change` checks implementation against proposal, specs, design, and tasks.
- `openspec-sync-specs` moves delta specs into the main specs.
- `openspec-archive-change` archives a completed change.
- `openspec-bulk-archive-change` archives several completed changes.
- `openspec-ff-change` fast-forwards OpenSpec artifacts to an apply-ready state.
- `openspec-onboard` walks through the OpenSpec workflow on a real task.

### Additional Engineering Skills

These skills do not replace OpenSpec. They add structure where a change needs
clearer design artifacts, sharper acceptance criteria, or stronger engineering
discipline:

- `architectural-decision-records` captures one architecturally significant decision at a time, including rationale, tradeoffs, alternatives, consequences, status, and history.
- `c4-diagrams` maps architecture boundaries, responsibilities, actors, dependencies, and data flow, then draws only the C4 level that answers the current question.
- `gherkin-authoring` turns behavior into concrete Gherkin/BDD examples with clear initial state, one meaningful event, and observable outcomes.
- `grill-with-docs` stress-tests a proposal, design, or plan against OpenSpec artifacts, architecture decision records, project documentation, and relevant code, then asks focused questions about the highest-risk uncertainties and provides recommended answers.
- `openspec-git-discipline` enforces Git timing around the OpenSpec lifecycle: proposal state reaches `main` before apply, archive runs from merged `main`, and commits or merges happen only when explicitly requested.

Additional skills are loaded only after recommendation and explicit user
consent. Superpowers are not part of this bundled skill set: they are not
vendored into the repository and require the separate Superpowers plugin in the
Codex environment.

When several optional actions apply at the same stage, `/opsx:*` commands show
one grouped `РЕКОМЕНДАЦИЯ` block with numbered items. The user can choose one
item, an ordered sequence, all items, or nothing: `1`, `1,2`, `+`, `-`. After
the selected actions run, Codex returns to the active OpenSpec step and chooses
the next suggestion from the outcome.

## Claude OpenSpec Review

Claude OpenSpec Review is disabled by default:

```text
/opsx:claude-review on
/opsx:claude-review off
/opsx:claude-review status
/opsx:claude-review run <change> <stage>
```

Stages: `propose`, `apply-readiness`, `archive-readiness`.
Config: `.codex/codex-openspec-powers/claude-review.yaml`.
Outputs: `openspec/changes/<change>/reviews/`.

Claude receives a reviewed file set limited by default to the named change's
`proposal.md`, `design.md`, `tasks.md`, `README.md`, `specs/*/spec.md`, and
`openspec/config.yaml` from an isolated temporary bundle. Review can consume API
credits and is subject to configured per-stage budgets. Unresolved
Critical/High findings block `/opsx:apply` and `/opsx:archive` until an applied
summary or manual resolution records the finding ID.

## Installation

Recommended automatic setup:

```bash
bin/opsx install-auto-repair
```

Then initialize a new project with:

```bash
opsx init /path/to/project
```

or from the project root:

```bash
opsx init
```

The command runs `openspec init --tools codex`, applies the overlay, and checks
that `/opsx` commands were not overwritten. The installed wrapper also catches a
plain call to:

```bash
openspec init --tools codex
```

and automatically runs overlay repair after a successful `init`.

When starting a project directly from Codex, use:

```text
/opsx:init
```

It runs `opsx init`, then `opsx doctor`, and suggests `/opsx:explore` for the
first project idea.

Manual overlay contents:

```text
.codex/codex-openspec-powers/
.codex/prompts/opsx-*.md
.codex/skills/architectural-decision-records/
.codex/skills/c4-diagrams/
.codex/skills/gherkin-authoring/
.codex/skills/grill-with-docs/
.codex/skills/openspec-git-discipline/
INSTALL_CODEX_TEMPLATE.md
```

If `.codex`, `AGENTS.md`, `openspec/config.yaml`, or `openspec/schemas`
already exist, merge-review them instead of replacing them. Do not overwrite
`openspec/changes/`, `openspec/specs/`, source code, tests, package/build/config
files, or product documentation without an explicit user decision.

For a manual post-installation check, run:

```text
/opsx:check-overlay
```

If `openspec init --tools codex` or an OpenSpec upgrade overwrites `/opsx`
commands, automatic repair restores template-owned files from the bundled
repair source set in `.codex/codex-openspec-powers/template/`.
`/opsx:check-overlay` remains the manual verification and safe repair-plan view.

Detailed installation notes are in
[INSTALL_CODEX_TEMPLATE.md](INSTALL_CODEX_TEMPLATE.md).

## Repository Layout

```text
bin/                              `opsx` CLI and automatic repair wrapper
.codex/
  prompts/                         Codex slash-command prompts
  skills/                          OpenSpec lifecycle and optional skills
  codex-openspec-powers/           Overlay manifest, Claude config, and bundled repair source set
openspec/
  config.yaml                       OpenSpec context and rules for the overlay
  specs/                           Published overlay requirements
  changes/archive/                 Archived implementation change
README.md                          Russian README and main GitHub page
README.en.md                       English README
```

## Validation

```bash
openspec validate --all --strict
openspec list --specs
```

## Version

Current release: `v0.1.2`.

## License

MIT. See [`LICENSE`](LICENSE).
