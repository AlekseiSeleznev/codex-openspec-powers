# codex-skill-adaptation Specification

## Purpose
Define the Codex-adapted OpenSpec skill layer, optional engineering skills,
recommendation consent UX, and lifecycle-specific rules for when additional
skills and Superpowers may be suggested.

## Requirements
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

#### Scenario: Recommendation selection gate is explicit
- **WHEN** an `opsx` workflow prompt lists optional recommendations
- **THEN** the prompt instructs Codex to evaluate each listed recommendation
  candidate as its condition is reached, render at most one grouped
  `**== РЕКОМЕНДАЦИЯ ==**` block for the current decision point, number the
  applicable choices, render answer options under `Ответьте одним из
  вариантов:` with circle bullets, accept responses such as 1, 1,2, +,
  and -, avoid silently omitting listed candidates, state a concise skip
  reason for omitted items, and put relevant but premature candidates under
  `Позже`

#### Scenario: Recommendation answer options are compact
- **WHEN** a grouped recommendation block has one candidate
- **THEN** the answer options include ○ 1, ○ +, and ○ -

#### Scenario: Recommendation answer options support ordered subsets
- **WHEN** a grouped recommendation block has two or more candidates
- **THEN** the answer options include single numbers, one comma-separated
  ordered sequence example such as 1,2 or 1,3, ○ + for all recommended steps,
  and ○ - for no optional steps

#### Scenario: Recommendation response controls selected steps
- **WHEN** the user answers a grouped recommendation with +, -, a single number,
  or comma-separated numbers
- **THEN** Codex interprets +, всё, and Да as all currently numbered
  recommended steps in the recommended order; interprets -, ничего, and Нет as
  skipping optional steps at that decision point; interprets a single number as
  only that numbered step; and interprets comma-separated numbers as exactly
  those numbered steps in the user-provided order

#### Scenario: Selected recommendation outcome affects next step
- **WHEN** selected optional recommendation steps finish inside an `opsx`
  workflow
- **THEN** Codex returns to the active OpenSpec workflow, does not repeat the
  same recommendation block unless new information changes the candidate set,
  and makes the final `**== СЛЕДУЮЩИЙ ШАГ ==**` account for the user's selected
  or skipped recommendations and any blockers, questions, artifact updates, or
  conclusions produced by the selected steps

#### Scenario: Ordinary skill recommendation uses canonical wording
- **WHEN** Codex recommends an ordinary optional skill such as
  `gherkin-authoring`, `c4-diagrams`, `architectural-decision-records`,
  `openspec-git-discipline`, or `grill-with-docs`
- **THEN** Codex includes the ordinary skill as a numbered item in the grouped
  `**== РЕКОМЕНДАЦИЯ ==**` block using `Вызвать <skill>`, preserves
  `Выполнить?` compatibility wording, and shows `**Да / Нет**` where `Да`
  means the recommended set and `Нет` means nothing

#### Scenario: Git discipline is recommended near git-sensitive steps
- **WHEN** `/opsx:apply` or `/opsx:archive` reaches commit, branch, archive, or
  other git-sensitive work
- **THEN** Codex can recommend `openspec-git-discipline` as an ordinary optional
  skill using the same grouped recommendation and `Вызвать` / `Выполнить?`
  consent wording

#### Scenario: Interactive user question is available
- **WHEN** the current Codex environment exposes an interactive user-question
  mechanism, such as a `request_user_input`-style tool or equivalent UI control
- **THEN** Codex presents the optional skill choice as a user question with
  `Да` and `Нет` choices and includes the recommendation and reason in the
  prompt text while preserving the same canonical wording

#### Scenario: Interactive user question is unavailable
- **WHEN** no interactive user-question mechanism is available in the current
  Codex environment
- **THEN** Codex renders the recommendation as a compact grouped Markdown block
  with the `**== РЕКОМЕНДАЦИЯ ==**` heading, numbered choices, +, -, and
  `**Да / Нет**` compatibility choices where Да maps to + and Нет maps to -

### Requirement: Optional recommendation map matches OpenSpec lifecycle stages
The template SHALL recommend optional skills and Superpowers only at lifecycle
stages where their scope is distinct and useful.

#### Scenario: Explore recommendations are staged
- **WHEN** `/opsx:explore` considers optional recommendations
- **THEN** it uses `superpowers:brainstorming` for unclear ideas before
  OpenSpec artifacts exist, `c4-diagrams` for boundaries or runtime
  relationships, and `grill-with-docs` only later after proposal, design,
  documentation, or code context exists

#### Scenario: New change recommendations are limited
- **WHEN** `/opsx:new` considers optional recommendations
- **THEN** it can recommend `openspec-git-discipline` for git-sensitive
  lifecycle starts and `superpowers:brainstorming` for vague, high-impact, or
  multi-direction requests

#### Scenario: Continue recommendations follow the next artifact
- **WHEN** `/opsx:continue` considers optional recommendations
- **THEN** it can recommend `gherkin-authoring` for behavior examples or BDD
  acceptance criteria, `c4-diagrams` for design boundaries or runtime flows, and
  `superpowers:writing-plans` only when the next artifact exposes a complex
  implementation sequence

#### Scenario: Propose and fast-forward recommendations use completed context
- **WHEN** `/opsx:propose` or `/opsx:ff` considers optional recommendations
- **THEN** it can recommend `grill-with-docs` only after enough proposal,
  design, specs, docs, or code context exists, `architectural-decision-records`
  when a durable decision should be recorded, and `superpowers:writing-plans`
  when implementation sequencing is the current problem

#### Scenario: Apply recommendations separate implementation and debugging
- **WHEN** `/opsx:apply` considers optional recommendations
- **THEN** it can recommend `openspec-git-discipline` before apply when git
  timing affects correctness, `superpowers:test-driven-development` before
  planned user-facing or risky implementation, and
  `superpowers:systematic-debugging` only after a failing check, bug, or
  unexpected behavior appears

#### Scenario: Verify and archive recommendations are stage-specific
- **WHEN** `/opsx:verify` or `/opsx:archive` considers optional recommendations
- **THEN** verify can recommend `superpowers:verification-before-completion`
  before completion claims, `grill-with-docs` for remaining design ambiguity,
  and `superpowers:requesting-code-review` for broad changes; archive can
  recommend `openspec-git-discipline` for archive timing and
  `superpowers:finishing-a-development-branch` for final branch cleanup, checks,
  review, merge, or branch housekeeping

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
