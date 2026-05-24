# codex-overlay-healthcheck Specification

## Purpose
Define how the overlay healthcheck detects missing or overwritten Codex
OpenSpec Powers behavior, classifies ownership through the manifest, and
repairs only approved template-owned additions while preserving project-owned
content.

## Requirements
### Requirement: Overlay healthcheck detects overwritten template behavior
The template SHALL provide a Codex prompt that checks a fresh or updated
OpenSpec Codex installation for missing or overwritten codex-openspec-powers overlay
behavior.

#### Scenario: OpenSpec update overwrote overlay prompt behavior
- **WHEN** the user runs the overlay healthcheck after updating OpenSpec
- **THEN** Codex detects missing recommendation prompts, missing post-step
  footer rules, missing optional skill consent rules, and missing template-owned
  skills

#### Scenario: Installation is already healthy
- **WHEN** the user runs the overlay healthcheck and all expected overlay files
  and markers are present
- **THEN** Codex reports that no repair is needed and does not modify files

### Requirement: Overlay repair is safe and reviewable
The overlay repair prompt SHALL inspect existing files before writing and SHALL
show the planned repair scope before modifying files.

#### Scenario: Repair requires file changes
- **WHEN** the healthcheck finds missing or overwritten overlay content
- **THEN** Codex reports the affected files, explains the intended repair, and
  asks the user for confirmation before applying changes

#### Scenario: Repair could overwrite project-owned content
- **WHEN** a planned repair would replace or conflict with project-owned content
- **THEN** Codex stops and asks the user to choose a merge strategy instead of
  overwriting silently

### Requirement: Overlay repair preserves OpenSpec updates
The overlay repair prompt SHALL preserve newly updated OpenSpec-generated
behavior where possible and re-apply only template-owned additions.

#### Scenario: Generated OpenSpec files changed in a newer foundation
- **WHEN** OpenSpec-generated prompts or skills differ from the previous overlay
  foundation
- **THEN** Codex treats the generated changes as authoritative unless they
  conflict with required overlay behavior

#### Scenario: Template-owned additions are missing
- **WHEN** template-owned snippets, skills, or markers are absent after an
  OpenSpec update
- **THEN** Codex restores only those missing additions and leaves unrelated
  generated content intact

#### Scenario: Template-owned prompt was regenerated
- **WHEN** `openspec init --tools codex` or an OpenSpec upgrade overwrites a
  manifest-listed `/opsx` prompt
- **THEN** Codex detects the missing markers and prepares a repair plan that
  restores the prompt from the bundled repair source after user confirmation

#### Scenario: Command-line repair restores regenerated prompt
- **WHEN** the command-line auto-repair runs after `openspec init --tools codex`
  or `openspec update` overwrote a manifest-listed `/opsx` prompt
- **THEN** it restores the prompt from the bundled repair source without
  requiring a manual `/opsx:check-overlay` step

#### Scenario: Manual command-line repair uses the installed bundle
- **WHEN** a project already contains `.codex/codex-openspec-powers/template/`
  and the user runs `opsx repair --yes` from that project
- **THEN** the repair uses the project's installed bundle as the source instead
  of comparing the damaged live prompt to itself

#### Scenario: Template-owned file source is unavailable
- **WHEN** a template-owned prompt, config, documentation file, or skill is
  missing and the bundled template source for that file is unavailable in the
  current installation
- **THEN** Codex reports the missing file and instructs the user to re-apply the
  template instead of inventing replacement content

### Requirement: Overlay ownership is manifest-driven
The template SHALL include a manifest that enumerates template-owned paths,
required markers, required snippets, generated paths, merge-review paths, and
the bundled repair source root. Healthcheck and repair SHALL use this manifest
instead of guessing ownership.

#### Scenario: Manifest has minimum structure
- **WHEN** a user opens `.codex/codex-openspec-powers/manifest.yaml`
- **THEN** it contains version, template, template-owned paths, generated paths,
  merge-review paths, never-overwrite paths, required markers, required
  snippets, required prompts, forbidden paths, and `repairSources.root`

#### Scenario: Bundled repair source path is deterministic
- **WHEN** the healthcheck needs to repair a template-owned target
- **THEN** it derives the source path from `repairSources.root` plus the target
  path and excludes the source bundle itself from recursive repair source
  lookup

#### Scenario: CLI and prompt repair use the same ownership model
- **WHEN** `/opsx:check-overlay` or `opsx repair --yes` repairs an overlay
- **THEN** both use the same manifest `templateOwnedPaths`, precedence rules,
  and bundled repair source root

#### Scenario: Missing required prompt is detected
- **WHEN** the healthcheck runs and a prompt listed in the manifest's required
  prompts is absent
- **THEN** Codex reports the missing prompt as a broken overlay installation
  before checking markers inside existing prompts

#### Scenario: Healthcheck classifies files before repair
- **WHEN** the healthcheck inspects the current repository
- **THEN** it classifies files using the overlay manifest before proposing any
  repair action

#### Scenario: Specific template-owned files override broader classifications
- **WHEN** a file path is listed in `templateOwnedPaths` and also matches a
  broader `mergeReviewPaths` or `generatedPaths` entry
- **THEN** Codex treats the specific file as template-owned while leaving other
  files in the broader classified directory as merge-reviewed, generated, or
  user-owned according to the manifest

#### Scenario: User-added files in merge-review directories are preserved
- **WHEN** `.codex/prompts/` or another merge-review directory contains a
  user-added file that is not listed in the overlay manifest
- **THEN** Codex leaves that file untouched and reports it, if needed, as
  informational rather than broken overlay content

#### Scenario: Documentation paths are classified
- **WHEN** a user opens `.codex/codex-openspec-powers/manifest.yaml`
- **THEN** `INSTALL_CODEX_TEMPLATE.md` is listed as a template-owned path,
  `README.md`, `README.en.md`, and `AGENTS.md` are listed as merge-review paths,
  and these documentation paths can be checked without overwriting existing
  project documentation silently

#### Scenario: Prompt marker scopes are manifest-specific
- **WHEN** the healthcheck validates prompt markers or snippets
- **THEN** it applies each marker or snippet rule only to the specific `path` or
  `paths` listed for that rule, not to every `opsx` prompt by default

#### Scenario: Repair recommendation marker is checked
- **WHEN** the healthcheck validates `/opsx:check-overlay`
- **THEN** it verifies that repair recommendations use the
  `**== РЕКОМЕНДАЦИЯ ==**` marker when a repair action is proposed

#### Scenario: Utility-only prompts do not require optional consent wording
- **WHEN** the healthcheck validates utility prompts such as `/opsx:sync`,
  `/opsx:bulk-archive`, `/opsx:check-overlay`, or `/opsx:claude-review`
- **THEN** it does not require ordinary skill or Superpowers consent wording
  unless the manifest explicitly lists that prompt for the matching snippet

#### Scenario: Documentation snippets are checked
- **WHEN** the healthcheck validates overlay documentation
- **THEN** it checks manifest-listed documentation snippets for
  `INSTALL_CODEX_TEMPLATE.md`, `README.md`, `README.en.md`, and `AGENTS.md` so
  missing Claude review guidance, install guidance, or agent guardrails are
  reported

#### Scenario: Repair targets template-owned additions
- **WHEN** a repair is approved
- **THEN** Codex modifies only manifest-listed template-owned additions or
  explicitly approved merge-review paths

#### Scenario: Repair source bundle is preserved
- **WHEN** a path is under `.codex/codex-openspec-powers/template/`
- **THEN** Codex treats it as template-owned repair source content and does not
  classify files inside it as live prompts or user prompt additions

#### Scenario: Automatic repair is limited to template-owned paths
- **WHEN** `opsx repair --yes` runs non-interactively
- **THEN** it writes only manifest-listed template-owned files from bundled
  sources and does not modify project-owned changes, specs, source code, tests,
  package files, or documentation

### Requirement: Healthcheck enforces MUST criteria
The overlay healthcheck SHALL treat missing core overlay behavior as a broken
installation.

#### Scenario: MUST criteria are checked
- **WHEN** the healthcheck runs
- **THEN** it verifies the post-step footer policy, optional skill consent
  policy, `grill-with-docs`, Codex command syntax, overlay manifest, required
  prompt presence, and repair confirmation-before-write behavior

### Requirement: Healthcheck reports SHOULD criteria
The overlay healthcheck SHALL report non-blocking overlay quality and freshness
issues separately from broken installation criteria.

#### Scenario: SHOULD criteria are checked
- **WHEN** the healthcheck runs
- **THEN** it reports retained extra skills, `openspec/config.yaml`
  context/rules presence, Superpowers policy presence, Claude review policy
  presence, manifest freshness, and overlay documentation freshness

### Requirement: Overlay command name is canonical
The overlay healthcheck prompt SHALL be exposed as `/opsx:check-overlay`.

#### Scenario: User runs overlay healthcheck
- **WHEN** the user invokes `/opsx:check-overlay`
- **THEN** Codex checks first, reports findings, and only performs repair after
  explicit confirmation

### Requirement: Repair conflict is narrowly defined
The overlay repair SHALL define a conflict as a generated or project-owned file
lacking, removing, omitting, altering, or contradicting a manifest-required
marker, required snippet, canonical command syntax, or consent wording.

#### Scenario: Generated update does not conflict
- **WHEN** an OpenSpec-generated file changes but preserves manifest-required
  overlay behavior
- **THEN** Codex preserves the generated update

#### Scenario: Generated update conflicts with overlay behavior
- **WHEN** an OpenSpec-generated file lacks, removes, omits, or alters a
  manifest-required footer marker, consent marker, command syntax, or required
  snippet
- **THEN** Codex reports the conflict and asks for confirmation before repair

#### Scenario: Unclassified paths are left untouched
- **WHEN** a path is not matched by `templateOwnedPaths`, `generatedPaths`,
  `mergeReviewPaths`, `neverOverwritePaths`, or `forbiddenPaths`
- **THEN** Codex does not modify it during repair and may report it only as
  informational context

### Requirement: Healthcheck verification uses broken overlay fixtures
The template SHALL define fixture-style broken overlay states or documented
sample trees that make healthcheck behavior verifiable.

#### Scenario: Missing footer fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay missing footer
  markers
- **THEN** the expected output identifies the missing `**== УРОКИ ==**` and
  `**== СЛЕДУЮЩИЙ ШАГ ==**` policy

#### Scenario: Missing manifest fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay missing
  `.codex/codex-openspec-powers/manifest.yaml`
- **THEN** the expected output identifies the missing overlay manifest as a
  broken installation

#### Scenario: Missing required prompt fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay missing a prompt
  listed in required prompts
- **THEN** the expected output identifies the missing prompt before marker
  validation

#### Scenario: Overwritten prompt repair-source fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay whose
  `.codex/prompts/opsx-apply.md` was regenerated without required overlay
  markers while its bundled repair source exists
- **THEN** the expected output identifies the prompt as repairable from
  `.codex/codex-openspec-powers/template/.codex/prompts/opsx-apply.md`

#### Scenario: Missing repair-source bundle fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay with overwritten
  template-owned prompts and no `.codex/codex-openspec-powers/template/` source
  bundle
- **THEN** the expected output instructs the user to re-apply the template
  rather than inventing replacement prompt content

#### Scenario: Missing consent wording fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay missing
  `Выполнить?`, `Использовать?`, or `**Да / Нет**` consent wording
- **THEN** the expected output identifies the missing optional skill consent
  policy

#### Scenario: Missing Claude review config fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay missing
  `.codex/codex-openspec-powers/claude-review.yaml`
- **THEN** the expected output identifies the missing Claude review config as
  an overlay documentation or policy issue

#### Scenario: Malformed Claude review config fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay whose
  `claude-review.yaml` is missing required keys such as
  `maxBudgetUsd.applyReadiness`
- **THEN** the expected output identifies the malformed Claude review config

#### Scenario: Missing Claude substep marker fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay whose
  `/opsx:apply` prompt lacks the `apply-readiness` Claude review substep marker
- **THEN** the expected output identifies missing Claude review substep
  integration

#### Scenario: Unresolved blocker fixture is checked
- **WHEN** the healthcheck is verified against a sample change with unresolved
  Critical or High Claude findings and no matching applied or resolution record
- **THEN** the expected output identifies the gated OpenSpec step as blocked

#### Scenario: Pre-call limit fixture is checked
- **WHEN** the healthcheck is verified against a sample Claude review bundle
  that exceeds configured pre-call limits
- **THEN** the expected output identifies that Claude must not be invoked and
  the stage must be externally unreviewed

#### Scenario: Budget-limit fixture is checked
- **WHEN** the healthcheck is verified against a sample Claude review run whose
  reported usage reaches the configured stage budget
- **THEN** the expected output identifies the budget-limited status, the
  configured limit, and that the stage is externally unreviewed or incomplete

#### Scenario: Missing repair recommendation marker fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay whose
  `/opsx:check-overlay` prompt lacks the `**== РЕКОМЕНДАЦИЯ ==**` marker used
  for repair recommendations
- **THEN** the expected output identifies the missing repair recommendation
  marker as a broken overlay state and recommends restoring the marker

#### Scenario: Failing Claude CLI fixture is checked
- **WHEN** the healthcheck is verified against a sample run where Claude is
  unavailable, exits non-zero, times out, or aborts
- **THEN** the expected output identifies the Claude review as failed or skipped
  without marking the stage reviewed

#### Scenario: User-added prompt fixture is checked
- **WHEN** the healthcheck is verified against a sample overlay containing a
  user-added prompt inside `.codex/prompts/` that is not listed in the manifest
- **THEN** the expected output leaves that prompt untouched while still checking
  manifest-listed prompt files

#### Scenario: Utility-only prompt fixture is checked
- **WHEN** the healthcheck is verified against a utility-only prompt that lacks
  optional skill consent wording and is not listed for an optional consent
  snippet in the manifest
- **THEN** the expected output does not flag that prompt as broken
