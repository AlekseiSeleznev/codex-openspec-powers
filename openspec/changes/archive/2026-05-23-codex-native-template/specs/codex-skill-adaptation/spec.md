## ADDED Requirements

### Requirement: Reusable skills are adapted for Codex
The template SHALL adapt useful reusable workflow and engineering skills into
`.codex/skills` with Codex-compatible wording, file paths, and tool references.

#### Scenario: User installs the Codex skill layer
- **WHEN** the Codex overlay is installed
- **THEN** reusable OpenSpec lifecycle, ADR, optional C4, Gherkin,
  OpenSpec git discipline, and optional `grill-with-docs` review skills are
  available under `.codex/skills`

### Requirement: Skills are Codex-compatible
Each adapted skill SHALL use Codex command names, configuration paths, and tool
references.

#### Scenario: User reads an adapted skill
- **WHEN** a user opens an adapted `SKILL.md`
- **THEN** the skill describes Codex-compatible behavior and points to the
  project-owned Codex/OpenSpec files

### Requirement: Skill adaptation is selective
The template SHALL only include skills that support the Codex/OpenSpec overlay
goal.

#### Scenario: Skill layer is reviewed
- **WHEN** the template skill layer is reviewed
- **THEN** only Codex-relevant workflow and engineering skills are retained in
  the target template

#### Scenario: Project skill set is explicit
- **WHEN** the Codex overlay is installed
- **THEN** `.codex/skills` contains the named project skills documented by the
  overlay manifest

### Requirement: Review skills are context-aware and optional
The template SHALL provide rigorous design review as an optional
`grill-with-docs` skill that reads relevant OpenSpec artifacts and project
documents before asking review questions.

#### Scenario: Proposal has been drafted
- **WHEN** Codex drafts a proposal for a change that affects multiple
  capabilities, changes installation behavior, changes reusable skills, changes
  workflow prompts, or introduces a durable architecture decision
- **THEN** the workflow may recommend `grill-with-docs` as a model-judged
  optional review step before continuing

#### Scenario: Review is accepted
- **WHEN** the user chooses to run `grill-with-docs`
- **THEN** the skill reviews relevant proposal, specs, design, ADRs, and project
  context before asking focused questions

#### Scenario: Review is skipped
- **WHEN** the user skips `grill-with-docs` for a simple or low-risk change
- **THEN** the workflow continues without loading the review skill into context

### Requirement: Optional skills require explicit recommendation and consent
The template SHALL make optional skill usage explicit by announcing the
recommendation, explaining the reason, and asking the user before loading the
optional skill.

#### Scenario: Optional skill is recommended
- **WHEN** a workflow detects that an optional skill is useful for the current
  change
- **THEN** Codex states the recommendation, gives the specific reason, and asks
  whether to run or skip the skill

#### Scenario: Ordinary skill recommendation uses canonical wording
- **WHEN** Codex recommends an ordinary optional skill such as
  `gherkin-authoring`, `c4-diagrams`, `architectural-decision-records`,
  `openspec-git-discipline`, or `grill-with-docs`
- **THEN** Codex renders a `**== РЕКОМЕНДАЦИЯ ==**` block using
  `Вызвать <skill>`, asks `Выполнить?`, and shows `**Да / Нет**`

#### Scenario: Git discipline is recommended near git-sensitive steps
- **WHEN** `/opsx:apply` or `/opsx:archive` reaches commit, branch, archive, or
  other git-sensitive work
- **THEN** Codex can recommend `openspec-git-discipline` as an ordinary optional
  skill using the same `Вызвать` / `Выполнить?` consent wording

#### Scenario: Interactive user question is available
- **WHEN** the current Codex environment exposes an interactive user-question
  mechanism, such as a `request_user_input`-style tool or equivalent UI control
- **THEN** Codex presents the optional skill choice as a user question with
  `Да` and `Нет` choices and includes the recommendation and reason in the
  prompt text while preserving the same canonical wording

#### Scenario: Interactive user question is unavailable
- **WHEN** no interactive user-question mechanism is available in the current
  Codex environment
- **THEN** Codex renders the recommendation as a compact Markdown block with the
  `**== РЕКОМЕНДАЦИЯ ==**` heading and `**Да / Нет**` choices

#### Scenario: Optional skill is not recommended
- **WHEN** a workflow detects that an optional skill is unnecessary for the
  current change
- **THEN** Codex can state that the step is being skipped and continue without
  asking for extra confirmation

#### Scenario: User declines recommended optional skill
- **WHEN** the user declines a recommended optional skill
- **THEN** Codex continues the workflow without loading that skill and does not
  repeat the same prompt unless new risk or complexity appears

#### Scenario: User accepts recommended optional skill
- **WHEN** the user accepts a recommended ordinary optional skill
- **THEN** Codex runs the skill, returns to the active OpenSpec workflow after
  the skill finishes, and preserves the workflow's final `**== УРОКИ ==**` /
  `**== СЛЕДУЮЩИЙ ШАГ ==**` footer output
