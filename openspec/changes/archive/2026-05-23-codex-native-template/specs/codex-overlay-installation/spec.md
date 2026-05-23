## ADDED Requirements

### Requirement: Overlay installs over existing OpenSpec projects
The template SHALL provide a Codex-native overlay installation path that can be
applied to an existing OpenSpec project without silently replacing project-owned
OpenSpec changes, specs, or configuration choices.

#### Scenario: Existing OpenSpec project receives the Codex overlay
- **WHEN** a user applies the template to a project that already contains an
  `openspec/` directory
- **THEN** the installation guidance preserves existing `openspec/changes/`,
  `openspec/specs/`, and project-specific schema configuration unless the user
  explicitly chooses to replace them

#### Scenario: Empty project is prepared as a Codex-native template repository
- **WHEN** a user applies the template in an empty project directory
- **THEN** the project contains the minimal OpenSpec and Codex files required to
  operate the Codex OpenSpec Powers workflow as a reusable template

### Requirement: Target file set is explicit
The template SHALL define the Codex/OpenSpec files that belong to the reusable
overlay.

#### Scenario: User inspects the target template
- **WHEN** a user reviews the generated template files
- **THEN** the template-owned paths are limited to `.codex/`, `openspec/`,
  `README.md`, `INSTALL_CODEX_TEMPLATE.md`, `AGENTS.md`, and documented
  repository metadata needed for the workflow

### Requirement: Installation guidance identifies conflict points
The template SHALL document which files are safe to add, which files require
merge review, and which files must not overwrite project-owned content.

#### Scenario: Existing project has custom Codex or OpenSpec files
- **WHEN** an existing project already contains `.codex/`, `AGENTS.md`, or
  `openspec/config.yaml`
- **THEN** the installation guidance identifies those paths as merge-review
  points rather than unconditional replacements

### Requirement: Installation documentation has required sections
The template SHALL document the minimum installation and merge guidance needed
to apply the overlay safely.

#### Scenario: User reads installation prerequisites
- **WHEN** a user opens `INSTALL_CODEX_TEMPLATE.md`
- **THEN** it states that the target project should already have an OpenSpec
  Codex foundation from `openspec init --tools codex` or an equivalent setup
  before applying the overlay

#### Scenario: User reads installation documentation
- **WHEN** a user opens `INSTALL_CODEX_TEMPLATE.md`
- **THEN** it lists safe-to-add paths, merge-review paths, never-overwrite
  paths, optional project-specific schema handling, and the instruction to run
  `/opsx:check-overlay` after OpenSpec updates

#### Scenario: User reads Claude review installation guidance
- **WHEN** a user opens `INSTALL_CODEX_TEMPLATE.md`
- **THEN** it describes Claude OpenSpec Review as OFF by default, lists the
  per-stage budgets, names `.codex/codex-openspec-powers/claude-review.yaml` as
  the user-editable config path, lists the default files sent to Claude,
  explains that Claude review runs from an isolated bundle and does not receive
  the full repository, names the saved review artifact paths under
  `openspec/changes/<change>/reviews/`, and explains Critical/High blocking
  behavior

#### Scenario: User reads project README
- **WHEN** a user opens `README.md`
- **THEN** it describes the Codex-native overlay purpose, supported `opsx`
  workflow prompts, retained skills, optional skill consent policy, and
  OpenSpec lifecycle

#### Scenario: User reads Claude review overview
- **WHEN** a user opens `README.md`
- **THEN** it describes Claude OpenSpec Review as an optional external review
  loop, its OFF-by-default behavior, the `/opsx:claude-review` controls, and
  the reviewed file set, and mentions that Claude review consumes API credits
  subject to the configured per-stage budgets

#### Scenario: Codex reads project instructions
- **WHEN** Codex reads `AGENTS.md`
- **THEN** it receives project-level rules for safe overlay work, no silent
  overwrites, optional skill consent, post-step footer output, and
  `/opsx:check-overlay`

#### Scenario: Codex reads Claude review guardrails
- **WHEN** Codex reads `AGENTS.md`
- **THEN** it receives project-level guardrails for Claude review file-scope
  isolation, default OFF behavior, budget display, safe doc-only fixes, and
  Critical/High blocker handling, including that turning review OFF does not
  clear unresolved blockers and Claude never writes project files directly

### Requirement: OpenSpec config carries supported overlay guidance
The template SHALL populate `openspec/config.yaml` using supported OpenSpec
fields only, so artifact generation sees the overlay methodology without
depending on custom top-level keys.

#### Scenario: User reviews OpenSpec config
- **WHEN** a user opens `openspec/config.yaml`
- **THEN** it contains `context` and `rules` guidance for Codex overlay purpose,
  optional skill consent, Superpowers recommendation policy, and post-step
  footer output

#### Scenario: Existing project has its own config
- **WHEN** the overlay is applied to a project with an existing
  `openspec/config.yaml`
- **THEN** the install guidance treats config changes as merge-review content
  rather than unconditional replacement
