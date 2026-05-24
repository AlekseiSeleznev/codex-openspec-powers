# codex-workflow-prompts Specification

## Purpose
Define the Codex-native `/opsx:*` prompt layer for the OpenSpec lifecycle,
including artifact discipline, grouped optional recommendations, and required
post-step footer blocks.

## Requirements
### Requirement: Codex prompts cover the OpenSpec lifecycle
The template SHALL provide Codex prompt files for the core OpenSpec lifecycle so
users can drive initialization, proposal, exploration, continuation,
implementation, validation, synchronization, fast-forward artifact creation,
archive, and bulk archive flows from Codex.

#### Scenario: User installs Codex workflow prompts
- **WHEN** the Codex overlay is installed
- **THEN** the project contains Codex prompt definitions for `/opsx:init`,
  `/opsx:new`, `/opsx:propose`, `/opsx:continue`, `/opsx:explore`,
  `/opsx:apply`, `/opsx:verify`, `/opsx:sync`, and `/opsx:archive`

#### Scenario: User initializes a project from Codex
- **WHEN** a user invokes `/opsx:init`
- **THEN** Codex runs `opsx init` for the current project or supplied path,
  verifies the result with `opsx doctor`, and suggests `/opsx:explore` as the
  first OpenSpec workflow command

#### Scenario: User installs auxiliary lifecycle prompts
- **WHEN** the Codex overlay is installed
- **THEN** the project contains Codex prompt definitions for fast-forwarding
  artifact creation with `/opsx:ff` and bulk archiving with
  `/opsx:bulk-archive`

#### Scenario: User installs overlay healthcheck prompt
- **WHEN** the Codex overlay is installed
- **THEN** the project contains a Codex prompt definition for
  `/opsx:check-overlay`

#### Scenario: User installs Claude review control prompt
- **WHEN** the Codex overlay is installed
- **THEN** the project contains a Codex prompt definition for
  `/opsx:claude-review`

### Requirement: Prompt syntax is Codex-native
The prompt layer SHALL use Codex slash-command naming and Codex-oriented
instructions.

#### Scenario: User reads a workflow prompt
- **WHEN** a user opens any `opsx` workflow prompt
- **THEN** the prompt refers to Codex command forms such as `/opsx:new` and
  `/opsx:apply` consistently

#### Scenario: Workflow prompt makes optional recommendations visible
- **WHEN** a user runs an `opsx` workflow prompt that lists optional
  recommendations
- **THEN** the prompt tells Codex not to replace applicable recommendations
  with an internal decision or after-the-fact summary, and to show one grouped
  recommendation choice with numbered items before loading any optional skill,
  Superpowers step, or review tool

#### Scenario: Grouped recommendation choices are compact
- **WHEN** a workflow prompt shows a grouped optional recommendation block
- **THEN** it asks `Что выполнить?`, renders `Ответьте одним из вариантов:`,
  uses circle-bullet choices such as ○ 1, ○ 1,3, ○ +, and ○ -, and treats + as
  all recommended steps and - as no optional steps

#### Scenario: Workflow prompts share one recommendation block shape
- **WHEN** a workflow prompt lists optional recommendations
- **THEN** it includes the same rendered grouped recommendation shape with
  numbered items, `Позже` for premature candidates when relevant, a recommended
  order line when order matters, circle-bullet choices, and `**Да / Нет**`
  compatibility guidance

#### Scenario: Grouped recommendation answer changes workflow continuation
- **WHEN** the user selects one or more optional recommendation items from a
  grouped block
- **THEN** Codex runs only those selected items in the requested order, returns
  to the active OpenSpec workflow, and chooses the next suggested command based
  on the selected items' result instead of blindly using the default next step

#### Scenario: Codex executes a workflow prompt
- **WHEN** Codex follows a workflow prompt
- **THEN** the prompt instructions use Codex-compatible interaction language and
  tool assumptions

### Requirement: Prompts preserve OpenSpec artifact discipline
The prompt layer SHALL preserve the artifact-driven workflow where proposals,
specs, designs, and tasks are created or read before implementation work starts.

#### Scenario: User asks Codex to implement a change
- **WHEN** a user invokes the apply workflow for an OpenSpec change
- **THEN** Codex is instructed to read the OpenSpec context files and task list
  before modifying application code

### Requirement: Workflow prompts end with post-step footer blocks
Every user-facing `opsx` workflow prompt SHALL instruct Codex to end completed
steps with `**== УРОКИ ==**` and `**== СЛЕДУЮЩИЙ ШАГ ==**` blocks.

#### Scenario: Codex completes an OpenSpec lifecycle step
- **WHEN** Codex finishes a user-visible OpenSpec lifecycle step
- **THEN** the response ends with a `**== УРОКИ ==**` block followed by a
  `**== СЛЕДУЮЩИЙ ШАГ ==**` block

#### Scenario: Codex runs an accepted recommended step
- **WHEN** a user accepts a recommended ordinary skill, Superpowers step, or
  review tool from inside an `opsx` workflow
- **THEN** Codex returns to the active OpenSpec workflow after the recommended
  step completes and still ends the user-facing response with a `**== УРОКИ ==**`
  block followed by a `**== СЛЕДУЮЩИЙ ШАГ ==**` block

#### Scenario: Codex completes overlay healthcheck
- **WHEN** Codex finishes `/opsx:check-overlay`
- **THEN** the response also ends with a `**== УРОКИ ==**` block followed by a
  `**== СЛЕДУЮЩИЙ ШАГ ==**` block, where the next step is either the proposed
  repair confirmation when issues exist or the appropriate next OpenSpec
  workflow command when the installation is healthy

#### Scenario: Lessons block is rendered
- **WHEN** Codex renders the `**== УРОКИ ==**` block
- **THEN** the block contains 3-4 concise lessons learned from the completed
  step

#### Scenario: Next step block is rendered
- **WHEN** Codex renders the `**== СЛЕДУЮЩИЙ ШАГ ==**` block
- **THEN** the block contains a one-line rationale for the recommended next
  OpenSpec step that accounts for selected or skipped optional recommendations
  and any blockers or outcomes they produced, a fenced ready-to-run Codex
  command using `/opsx:<name>`, the question `Выполнить?`, and `**Да / Нет**`
  choices

### Requirement: Prompt UX strings are Russian in v1
The template SHALL emit the footer and recommendation UX markers as exact
Russian strings in v1. Localization is out of scope for this change.

#### Scenario: Healthcheck validates prompt markers
- **WHEN** the overlay healthcheck checks workflow prompt output rules
- **THEN** it treats `**== УРОКИ ==**`, `**== СЛЕДУЮЩИЙ ШАГ ==**`,
  `**== РЕКОМЕНДАЦИЯ ==**`, `**== РЕВЬЮ CLAUDE ==**`, `Выполнить?`,
  `Использовать?`, and `**Да / Нет**` as the canonical markers
