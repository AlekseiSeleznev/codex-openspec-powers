## ADDED Requirements

### Requirement: Codex prompts cover the OpenSpec lifecycle
The template SHALL provide Codex prompt files for the core OpenSpec lifecycle so
users can drive proposal, exploration, continuation, implementation, validation,
synchronization, fast-forward artifact creation, archive, and bulk archive
flows from Codex.

#### Scenario: User installs Codex workflow prompts
- **WHEN** the Codex overlay is installed
- **THEN** the project contains Codex prompt definitions for `/opsx:new`,
  `/opsx:propose`, `/opsx:continue`, `/opsx:explore`, `/opsx:apply`,
  `/opsx:verify`, `/opsx:sync`, and `/opsx:archive`

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
  OpenSpec step, a fenced ready-to-run Codex command using `/opsx:<name>`, the
  question `Выполнить?`, and `**Да / Нет**` choices

### Requirement: Prompt UX strings are Russian in v1
The template SHALL emit the footer and recommendation UX markers as exact
Russian strings in v1. Localization is out of scope for this change.

#### Scenario: Healthcheck validates prompt markers
- **WHEN** the overlay healthcheck checks workflow prompt output rules
- **THEN** it treats `**== УРОКИ ==**`, `**== СЛЕДУЮЩИЙ ШАГ ==**`,
  `**== РЕКОМЕНДАЦИЯ ==**`, `**== РЕВЬЮ CLAUDE ==**`, `Выполнить?`,
  `Использовать?`, and `**Да / Нет**` as the canonical markers
