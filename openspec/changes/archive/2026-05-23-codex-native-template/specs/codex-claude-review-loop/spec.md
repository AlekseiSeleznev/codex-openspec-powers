## ADDED Requirements

### Requirement: Claude review loop is opt-in
The template SHALL provide an optional Claude OpenSpec Review mode that is OFF
by default and can be enabled, disabled, checked, or run explicitly from Codex.

#### Scenario: User checks default state
- **WHEN** a new chat or project starts without explicit Claude review
  activation
- **THEN** Claude OpenSpec Review is OFF and OpenSpec workflows run without
  invoking `claude -p`

#### Scenario: User controls Claude review mode
- **WHEN** the user invokes Claude review control commands
- **THEN** the overlay supports `/opsx:claude-review on`,
  `/opsx:claude-review off`, `/opsx:claude-review status`, and
  `/opsx:claude-review run <change> <stage>`

### Requirement: Claude receives only relevant OpenSpec files
The Claude review loop SHALL pass only relevant markdown/config files for the
current OpenSpec change. It SHALL enforce this scope at invocation time rather
than relying only on prompt wording.

#### Scenario: Claude review runs for a change
- **WHEN** Codex invokes Claude review for `<change>`
- **THEN** the file set is limited by default to
  `openspec/changes/<change>/proposal.md`,
  `openspec/changes/<change>/design.md`,
  `openspec/changes/<change>/tasks.md`,
  `openspec/changes/<change>/README.md`,
  `openspec/changes/<change>/specs/*/spec.md`, and `openspec/config.yaml`

#### Scenario: Codex builds an isolated review bundle
- **WHEN** Codex prepares Claude review input
- **THEN** Codex copies only whitelisted review files into a temporary review
  bundle, invokes `claude -p` from that bundle directory, and does not pass the
  repository root or absolute repository paths to Claude

#### Scenario: File-scope enforcement is unavailable
- **WHEN** Codex cannot create an isolated review bundle or cannot invoke
  Claude without repository-root access
- **THEN** Codex skips automated Claude review, emits a
  `**== РЕВЬЮ CLAUDE ==**` block explaining that file-scope isolation is
  unavailable, and treats the stage as externally unreviewed

#### Scenario: Isolated review bundle is removed
- **WHEN** Claude review finishes, fails, or is skipped after bundle creation
- **THEN** Codex removes the temporary review bundle unless the user explicitly
  asks to preserve it for debugging

#### Scenario: User requests extra review files
- **WHEN** the user explicitly requests extra files for Claude review
- **THEN** Codex accepts only named repository-relative files after explicit
  confirmation and rejects broad globs, directories, and full-repository scope

### Requirement: Claude review stages are enumerated
The Claude review loop SHALL accept only known stage names.

#### Scenario: Unknown stage is rejected
- **WHEN** the user invokes `/opsx:claude-review run <change> <stage>` with a
  stage other than `propose`, `apply-readiness`, or `archive-readiness`
- **THEN** Codex rejects the request, shows the valid stage names, and does not
  invoke Claude

### Requirement: Claude review stages are budgeted
The template SHALL define stage-specific Claude review budgets in USD.

#### Scenario: Propose review runs
- **WHEN** Claude review runs after `/opsx:propose`
- **THEN** the stage is `propose` and the maximum budget is `0.50 USD`

#### Scenario: Apply-readiness review runs
- **WHEN** Claude review runs before `/opsx:apply`
- **THEN** the stage is `apply-readiness` and the maximum budget is `1.50 USD`

#### Scenario: Archive-readiness review runs
- **WHEN** Claude review runs after `/opsx:verify` and before `/opsx:archive`
- **THEN** the stage is `archive-readiness` and the maximum budget is `1.00 USD`

#### Scenario: Budget limit is reached
- **WHEN** Claude review reaches or reports the configured stage budget limit
- **THEN** Codex stops the review when possible, emits a
  `**== РЕВЬЮ CLAUDE ==**` block with budget-limited status, limit, reported
  usage when available, and marks the stage as externally unreviewed or
  incomplete

#### Scenario: Bundle exceeds pre-call limits
- **WHEN** the isolated review bundle exceeds configured pre-call limits for the
  stage, such as maximum input bytes or maximum file count
- **THEN** Codex refuses to invoke Claude, emits a `**== РЕВЬЮ CLAUDE ==**`
  block explaining the pre-call limit, and marks the stage as externally
  unreviewed

### Requirement: Claude review configuration is overlay-owned
The Claude review loop SHALL store user-editable Claude review settings outside
`openspec/config.yaml` in an overlay-owned config file.

#### Scenario: User configures Claude review budget
- **WHEN** a user opens `.codex/codex-openspec-powers/claude-review.yaml`
- **THEN** the file contains the overlay-namespaced top-level key
  `claudeOpenSpecReview` with `enabled`, `maxBudgetUsd`,
  `autoApplySafeDocFixes`, `blockOnCriticalHigh`, `saveReviews`, `model`,
  `effort`, and pre-call limit settings beneath it

#### Scenario: User configures stage-specific Claude options
- **WHEN** a user opens `.codex/codex-openspec-powers/claude-review.yaml`
- **THEN** the file can define per-stage overrides for budget, model, and effort
  for the `propose`, `apply-readiness`, and `archive-readiness` stages using
  canonical camelCase YAML keys: `propose`, `applyReadiness`, and
  `archiveReadiness`

#### Scenario: Stage-specific Claude option shape is stable
- **WHEN** `.codex/codex-openspec-powers/claude-review.yaml` defines
  stage-specific Claude review settings
- **THEN** budgets are read from
  `claudeOpenSpecReview.maxBudgetUsd.<stage>` and model or effort overrides are
  read from `claudeOpenSpecReview.stageOptions.<stage>.model` and
  `claudeOpenSpecReview.stageOptions.<stage>.effort`

#### Scenario: YAML stage keys use camelCase
- **WHEN** Codex reads `.codex/codex-openspec-powers/claude-review.yaml`
- **THEN** the canonical YAML stage keys are `propose`, `applyReadiness`, and
  `archiveReadiness`, while CLI stage names remain `propose`,
  `apply-readiness`, and `archive-readiness`

#### Scenario: Kebab-case YAML stage keys are ignored with warning
- **WHEN** `.codex/codex-openspec-powers/claude-review.yaml` contains
  kebab-case stage override keys such as `apply-readiness` or
  `archive-readiness`
- **THEN** Codex treats those keys as unknown extras, preserves them, warns
  that they are ignored, and continues using the valid camelCase keys

#### Scenario: Claude review config contains unknown keys
- **WHEN** `.codex/codex-openspec-powers/claude-review.yaml` contains unknown
  extra keys
- **THEN** Codex preserves them, warns that they are ignored by the current
  overlay, and continues using the known keys when they remain valid

#### Scenario: OpenSpec config remains supported
- **WHEN** the overlay is installed
- **THEN** `openspec/config.yaml` does not receive custom
  `claudeOpenSpecReview` top-level keys

#### Scenario: Default model and effort are omitted
- **WHEN** `model` or `effort` is set to `default`
- **THEN** Codex treats the value as a sentinel meaning "inherit Claude CLI
  defaults" and does not pass a literal `default` override to Claude

### Requirement: Claude review artifacts are saved
The Claude review loop SHALL save review output and any Codex-applied summary
inside the current change directory.

#### Scenario: Claude review completes
- **WHEN** Claude returns review output for `<stage>`
- **THEN** Codex saves it to
  `openspec/changes/<change>/reviews/claude-<stage>-<timestamp>.md`

#### Scenario: Codex applies safe doc fixes
- **WHEN** Codex applies Claude recommendations as safe doc-only fixes
- **THEN** Codex saves an applied summary to
  `openspec/changes/<change>/reviews/claude-<stage>-applied.md` as an
  append-only canonical log

#### Scenario: Codex records blocker resolutions
- **WHEN** the user approves a manual resolution for a Critical or High finding
- **THEN** Codex records it in
  `openspec/changes/<change>/reviews/claude-<stage>-resolutions.md` with the
  finding ID, decision, rationale, timestamp, and user approval text

### Requirement: Claude review can only auto-apply safe doc-only fixes
Codex SHALL treat Claude as an external reviewer, not an editor. Claude never
writes project files directly, and Codex may only auto-apply safe doc-only
recommendations according to policy.

#### Scenario: Auto-apply is disabled
- **WHEN** `autoApplySafeDocFixes` is `false`
- **THEN** Codex displays safe doc-only recommendations in a
  `**== РЕВЬЮ CLAUDE ==**` block and asks `Выполнить?` before applying any
  documentation fix

#### Scenario: Auto-apply is enabled
- **WHEN** `autoApplySafeDocFixes` is `true`
- **THEN** Codex may apply safe doc-only recommendations only after internally
  classifying every recommendation as safe doc-only and showing one batch-level
  `Выполнить?` confirmation with a planned diff summary

#### Scenario: Finding is safe doc-only
- **WHEN** Claude recommends wording clarification, missing acceptance criteria,
  task/spec wording sync, verification note, broken link fix, or an unambiguous
  documentation correction that does not change scope
- **THEN** Codex may apply the recommendation only according to the
  `autoApplySafeDocFixes` policy and records the summary if applied

#### Scenario: Finding requires manual decision
- **WHEN** Claude recommends scope changes, requirement removal, new feature
  requirements, architecture changes, code changes, data model changes, security
  behavior changes, overwriting user changes, or archiving with unresolved
  Critical/High findings
- **THEN** Codex SHALL not auto-apply it and SHALL ask the user for a manual
  decision

### Requirement: Critical and High findings block gated steps
The Claude review loop SHALL block `/opsx:apply` and `/opsx:archive` when
unresolved Critical or High findings remain.

#### Scenario: Claude output uses severity rubric
- **WHEN** Codex prompts Claude for review
- **THEN** the prompt defines severity as `Critical`, `High`, `Medium`, or
  `Low`, where Critical means unsafe workflow, security/data-loss risk, or
  broken gate; High means a lifecycle-integrity or required-artifact issue that
  must be fixed before the next gated step; Medium means a non-blocking
  completeness, maintainability, or clarity issue; and Low means cosmetic
  wording or formatting feedback

#### Scenario: Claude output uses stable finding IDs
- **WHEN** Codex prompts Claude for review
- **THEN** the prompt requires every finding to include a stable finding ID that
  can be referenced by applied summaries and manual resolution records

#### Scenario: Finding is considered resolved
- **WHEN** a Critical or High finding has a matching entry in
  `claude-<stage>-applied.md` or `claude-<stage>-resolutions.md` that references
  the stable finding ID and records the doc fix or manual decision
- **THEN** that finding is considered resolved for the gated step

#### Scenario: Finding absence does not resolve blockers
- **WHEN** a later Claude review no longer mentions a previous Critical or High
  finding but no applied summary or manual resolution references its stable
  finding ID
- **THEN** the previous blocker remains unresolved

#### Scenario: Turning review off does not clear blockers
- **WHEN** Claude OpenSpec Review is turned OFF while saved unresolved
  Critical or High findings exist for the gated stage
- **THEN** those blockers continue to block `/opsx:apply` or `/opsx:archive`
  until explicitly resolved

#### Scenario: Propose blockers carry into apply
- **WHEN** a saved `propose` review contains unresolved Critical or High
  findings for the same change
- **THEN** `/opsx:apply` remains blocked until those finding IDs are resolved
  through the applied log or manual resolution record, even if a later
  `apply-readiness` review does not mention them

#### Scenario: Apply-readiness review finds blockers
- **WHEN** Claude returns unresolved Critical or High findings during
  `apply-readiness`
- **THEN** Codex blocks `/opsx:apply`, saves the review, and recommends fixing
  OpenSpec artifacts before implementation

#### Scenario: Archive-readiness review finds blockers
- **WHEN** Claude returns unresolved Critical or High findings during
  `archive-readiness`
- **THEN** Codex blocks `/opsx:archive`, saves the review, and recommends
  resolving drift before archive

### Requirement: Claude review is visible in chat and followed by footer blocks
The template SHALL make Claude review status visible in the Codex chat and
SHALL still end the overall OpenSpec response with `**== УРОКИ ==**` and
`**== СЛЕДУЮЩИЙ ШАГ ==**` blocks.

#### Scenario: Claude review starts
- **WHEN** Codex starts a Claude review
- **THEN** it emits a `**== РЕВЬЮ CLAUDE ==**` block with change, stage, file
  summary, budget, model, and effort

#### Scenario: Claude review is skipped
- **WHEN** Claude OpenSpec Review is OFF or `claude` is unavailable
- **THEN** Codex emits a `**== РЕВЬЮ CLAUDE ==**` block explaining the skip and
  continues the OpenSpec workflow when safe

#### Scenario: Claude review fails mid-call
- **WHEN** the Claude CLI exits non-zero, times out, or aborts during review
- **THEN** Codex emits a `**== РЕВЬЮ CLAUDE ==**` block with failed status,
  saves any available partial output, treats the stage as externally
  unreviewed, and does not treat review as completed

#### Scenario: Utility command completes
- **WHEN** the user invokes `/opsx:claude-review on`, `off`, or `status`
- **THEN** Codex emits the `**== РЕВЬЮ CLAUDE ==**` status block and also ends
  the response with `**== УРОКИ ==**` and `**== СЛЕДУЮЩИЙ ШАГ ==**`

#### Scenario: Status reports unresolved blockers while review is off
- **WHEN** the user invokes `/opsx:claude-review status` while Claude OpenSpec
  Review is OFF and unresolved Critical or High findings exist
- **THEN** Codex reports those unresolved blockers in the
  `**== РЕВЬЮ CLAUDE ==**` status block and states which gated OpenSpec steps
  remain blocked

#### Scenario: OpenSpec response completes after Claude review
- **WHEN** the Claude review substep finishes, whether successful, skipped,
  budget-limited, or blocking
- **THEN** Codex still ends the response with `**== УРОКИ ==**` and
  `**== СЛЕДУЮЩИЙ ШАГ ==**` blocks
