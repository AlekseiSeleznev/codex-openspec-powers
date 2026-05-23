## 1. Repository Foundation

- [x] 1.1 Confirm the repository is a standalone git repository with the
  expected OpenSpec/Codex foundation.
- [x] 1.2 Inventory the project foundation files and
  classify each file as keep, adapt, or drop for the Codex-native target.
- [x] 1.3 Confirm the design target tree still matches the project and local
  inventory before moving or rewriting template assets.
- [x] 1.4 Create an overlay manifest that classifies template-owned paths,
  required markers, required snippets, generated paths, merge-review paths, and
  never-overwrite paths, explicitly lists all required `opsx` prompt files, and
  documents that specific template-owned file matches take precedence over
  containing merge-review directories. Classify `INSTALL_CODEX_TEMPLATE.md` as
  template-owned and `README.md` / `AGENTS.md` as merge-review documentation.
- [x] 1.5 Add `.codex/codex-openspec-powers/claude-review.yaml` for
  user-editable Claude OpenSpec Review defaults, budgets, model, effort, and
  per-stage overrides without adding nonstandard custom top-level keys to
  `openspec/config.yaml`; use camelCase YAML stage keys such as
  `applyReadiness` and warn on ignored kebab-case variants.

## 2. Codex Workflow Prompts

- [x] 2.1 Create `.codex/prompts/` if it is absent.
- [x] 2.2 Add or adapt `opsx` prompt files for new, propose, continue,
  explore, apply, verify, sync, archive, fast-forward, bulk archive, and
  overlay check workflows.
- [x] 2.3 Use Codex-native command names and interaction language throughout
  the workflow prompts.
- [x] 2.4 Review prompts for OpenSpec artifact discipline and ensure apply
  workflows require reading proposal/spec/design/tasks context before code
  changes.
- [x] 2.5 Add an overlay healthcheck/repair prompt that checks fresh OpenSpec
  Codex installations and safely restores missing template-owned additions.
- [x] 2.6 Ensure every user-facing `opsx` workflow prompt ends completed steps
  with `**== УРОКИ ==**` and `**== СЛЕДУЮЩИЙ ШАГ ==**` blocks.
- [x] 2.7 Add `/opsx:claude-review` controls for on, off, status, and manual
  run of a named stage.
- [x] 2.8 Integrate optional Claude review substeps after propose, before apply,
  and after verify before archive.

## 3. Codex Skill Adaptation

- [x] 3.1 Review existing generated `.codex/skills/openspec-*` skills and keep
  the Codex-compatible lifecycle behavior as the foundation.
- [x] 3.2 Adapt ADR authoring guidance into
  `.codex/skills/architectural-decision-records/`.
- [x] 3.3 Adapt C4 diagram guidance into `.codex/skills/c4-diagrams/`.
- [x] 3.4 Adapt Gherkin authoring guidance into
  `.codex/skills/gherkin-authoring/`.
- [x] 3.5 Adapt rigorous design review guidance into an optional
  context-aware `.codex/skills/grill-with-docs/` skill.
- [x] 3.6 Adapt OpenSpec git discipline guidance into
  `.codex/skills/openspec-git-discipline/`.
- [x] 3.7 Ensure the target template contains only named project skills.
- [x] 3.8 Review every retained skill for Codex-compatible wording, paths,
  commands, and tool assumptions.
- [x] 3.9 Ensure optional skills are documented as lazy-loaded library skills,
  not mandatory context for every workflow.
- [x] 3.10 Add recommendation-and-consent wording to prompts before optional
  steps such as `grill-with-docs`, C4, ADR extraction, Gherkin refinement, and
  `openspec-git-discipline`, including `/opsx:apply` and `/opsx:archive` when
  they reach commit, branch, archive, or other git-sensitive work.
- [x] 3.11 Use Codex interactive user questions for optional skill consent when
  available, with a compact `**== РЕКОМЕНДАЦИЯ ==**` Markdown fallback.
- [x] 3.12 Add Superpowers recommendation policy for brainstorming,
  writing-plans, test-driven-development, systematic-debugging,
  verification-before-completion, requesting-code-review, and
  finishing-a-development-branch.
- [x] 3.13 Use `Вызвать` / `Выполнить?` for ordinary skills and
  `Использовать` / `Использовать?` for Superpowers.
- [x] 3.14 Ensure Claude review status uses `**== РЕВЬЮ CLAUDE ==**` and never
  replaces final `**== УРОКИ ==**` / `**== СЛЕДУЮЩИЙ ШАГ ==**` output.
- [x] 3.15 Ensure accepted ordinary skills, Superpowers steps, and review tools
  return to the active OpenSpec workflow and preserve final `**== УРОКИ ==**` /
  `**== СЛЕДУЮЩИЙ ШАГ ==**` output.

## 4. Overlay Installation Documentation

- [x] 4.1 Write `INSTALL_CODEX_TEMPLATE.md` for applying the template over an
  existing OpenSpec project, including the prerequisite OpenSpec Codex foundation
  from `openspec init --tools codex` or equivalent setup.
- [x] 4.2 Mark `.codex/`, `AGENTS.md`, and `openspec/config.yaml` as
  merge-review paths when they already exist in the target project.
- [x] 4.3 Document optional handling for project-specific OpenSpec schema support so
  existing project schemas are not silently replaced.
- [x] 4.4 Update `README.md` to describe the Codex-native template, the overlay
  use case, and the retained OpenSpec lifecycle.
- [x] 4.5 Add or update `AGENTS.md` with Codex-specific collaboration rules for
  the template.
- [x] 4.6 Document running the overlay healthcheck/repair prompt after
  `openspec init --tools codex`, OpenSpec upgrades, or suspected generated-file
  overwrites.
- [x] 4.7 Populate supported `openspec/config.yaml` `context` and `rules` with
  overlay methodology guidance without adding nonstandard custom top-level keys:
  overlay purpose, optional skill consent, Superpowers recommendation policy,
  and post-step footer output for proposal/specs/design/tasks.
- [x] 4.8 Document Claude OpenSpec Review mode, default OFF behavior, budgets,
  reviewed file set, saved review artifacts, and blocking behavior in
  `INSTALL_CODEX_TEMPLATE.md`, `README.md`, and `AGENTS.md`.
- [x] 4.9 Add manifest snippet anchors for `INSTALL_CODEX_TEMPLATE.md`,
  `README.md`, and `AGENTS.md` so `/opsx:check-overlay` can detect missing
  required documentation sections without replacing merge-review documents.

## 5. Verification

- [x] 5.1 Ensure the target template contains only project-owned Codex/OpenSpec
  assets.
- [x] 5.2 Run OpenSpec status/validation commands for the change and resolve
  malformed artifacts.
- [x] 5.3 Inspect the final file tree for duplicate lifecycle prompts or
  nonfunctional process artifacts.
- [x] 5.4 Summarize remaining manual installation caveats, if any, before the
  change is applied to other projects.
- [x] 5.5 Verify that the overlay healthcheck detects missing footer policy,
  optional skill consent policy, and missing template-owned skills without
  overwriting project-owned content silently.
- [x] 5.6 Verify that the overlay healthcheck detects missing Superpowers
  policy, missing manifest markers, and missing documentation sections.
- [x] 5.7 Create or document fixture-style broken overlay states for checking
  healthcheck behavior, including expected findings and repair prompts for
  missing footer, missing manifest, missing required prompt,
  missing consent wording, missing or malformed `claude-review.yaml`, missing
  Claude review substep marker, unresolved Critical/High blocker,
  Claude review budget limit reached, Claude review pre-call bundle limit
  exceeded, unavailable/failing Claude CLI, `opsx-check-overlay` missing its
  repair recommendation marker, utility-only prompt without consent wording,
  and user-added files inside merge-review directories.
- [x] 5.8 Verify Claude review behavior for OFF mode, unavailable `claude` CLI,
  budget limit, saved review output, safe doc-only fix summaries, and
  Critical/High blockers before apply/archive.
- [x] 5.9 Verify Claude review file-scope isolation using a temporary review
  bundle, unknown-stage rejection, autoApplySafeDocFixes=false consent behavior,
  and Critical/High resolution semantics.
- [x] 5.10 Verify unresolved Critical/High findings persist when Claude review
  is turned OFF, stable finding IDs are required, bundle pre-call limits are
  enforced, and mid-call Claude failures are marked externally unreviewed.
- [x] 5.11 Address external full-review findings for dead prompt references,
  OpenSpec CLI command consistency, manifest marker/snippet scope, Claude
  unknown-key handling, and repository hygiene.
- [x] 5.12 Split GitHub README into English `README.md` and Russian
  `README.ru.md` while keeping overlay healthcheck snippets for both files.
- [x] 5.13 Address release-readiness review findings for README heading
  structure, Russian README license parity, required snippet schema alignment,
  and target shape coverage.
- [x] 5.14 Address final Claude review findings for Claude stage option
  examples, camelCase stage-key wording, target shape drift, affected areas,
  `.gitignore` installation guidance, documentation protection, and onboarding
  skill visibility.
