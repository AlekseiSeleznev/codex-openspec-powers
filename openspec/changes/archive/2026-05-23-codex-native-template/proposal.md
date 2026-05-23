## Why

Codex OpenSpec Powers needs a compact Codex-native workflow kit for OpenSpec
projects. The template should provide repeatable prompts, optional skills,
manifest-driven overlay checks, Superpowers recommendations, and an opt-in
external review loop while preserving existing project OpenSpec content.

This matters because the target workflow should preserve the Codex OpenSpec
Powers lifecycle while making the day-to-day commands, skills, and guidance
natural for Codex.

## What Changes

- Create a Codex-native template shape for Codex OpenSpec Powers usage.
- Adapt the useful OpenSpec workflow commands into `.codex/prompts`
  using Codex slash-command names and Codex tool language.
- Adapt reusable engineering skills into `.codex/skills` where they remain
  valuable for Codex:
  - OpenSpec lifecycle skills.
  - ADR authoring.
  - Optional C4 diagram guidance.
  - Gherkin-style requirement authoring.
  - OpenSpec git discipline.
  - Optional rigorous design review with project documents
    (`grill-with-docs`).
- Add optional Superpowers recommendation policy for methodology accelerators
  such as brainstorming, writing plans, TDD, debugging, verification, code
  review, and branch finishing.
- Add an opt-in Claude OpenSpec review loop that can run external `claude -p`
  reviews at key workflow gates, save review artifacts, and block apply/archive
  on unresolved Critical/High findings.
- Add installation guidance for applying this template over an existing
  OpenSpec project without overwriting unrelated project files.
- Add a Codex overlay healthcheck/repair prompt that verifies a fresh or updated
  OpenSpec Codex installation and restores template-owned additions only after
  checking that the repair is safe.
- Keep OpenSpec schema/config assets only when they support the Codex overlay
  use case.

## Capabilities

### New Capabilities

- `codex-overlay-installation`: Defines how the template can be applied over an
  existing OpenSpec project while preserving project-specific OpenSpec content.
- `codex-workflow-prompts`: Defines the Codex slash-command prompt layer for the
  OpenSpec lifecycle.
- `codex-skill-adaptation`: Defines how reusable workflow and engineering skills
  are adapted from agent-generic form into Codex-native skills.
- `codex-overlay-healthcheck`: Defines a Codex prompt that checks whether an
  OpenSpec update overwrote overlay behavior and safely restores missing
  template-owned additions.
- `codex-superpowers-policy`: Defines when Codex recommends Superpowers
  methodology skills and how those recommendations differ from normal skill
  recommendations.
- `codex-claude-review-loop`: Defines the optional Claude external review loop,
  review stages, budgets, saved outputs, auto-apply limits, and blocking
  behavior.

### Modified Capabilities

- None. This repository has no existing archived OpenSpec capabilities yet.

## Impact

- Affected repository areas:
  - `.codex/prompts/`
  - `.codex/skills/`
  - `.codex/codex-openspec-powers/manifest.yaml`
  - `.codex/codex-openspec-powers/claude-review.yaml`
  - `openspec/`
  - `README.md`
  - `README.ru.md`
  - `INSTALL_CODEX_TEMPLATE.md`
  - `AGENTS.md`
  - `.gitignore`
  - `LICENSE`
- External inputs:
  - Project identity `AlekseiSeleznev/codex-openspec-powers`.
  - Existing generated OpenSpec Codex prompt/skill conventions from
    `openspec init --tools codex`.
- Compatibility constraints:
  - The resulting template must be safe to apply to an existing OpenSpec
    project.
  - Existing project specs, changes, and schema choices must not be overwritten
    silently.
  - Optional skills must be installed as a library and loaded only when the
    workflow needs them.
  - Overlay repair must inspect the current installation and report planned
    changes before modifying files.
  - Claude OpenSpec Review must be disabled by default and must never send the
    full repository to Claude unless the user explicitly expands scope.
