## ADDED Requirements

### Requirement: Superpowers are optional methodology accelerators
The template SHALL treat Superpowers as optional methodology accelerators that
support OpenSpec work without replacing OpenSpec artifacts as the source of
truth.

#### Scenario: Superpower is considered during an OpenSpec workflow
- **WHEN** Codex identifies that a Superpower could improve the current step
- **THEN** Codex presents it as optional help and keeps proposal, specs, design,
  and tasks as the authoritative workflow artifacts

### Requirement: Supported Superpowers are named explicitly
The template SHALL document the supported Superpowers recommendation targets.

#### Scenario: User reviews the Superpowers policy
- **WHEN** a user reads the Codex overlay policy
- **THEN** the supported targets include `superpowers:brainstorming`,
  `superpowers:writing-plans`, `superpowers:test-driven-development`,
  `superpowers:systematic-debugging`,
  `superpowers:verification-before-completion`,
  `superpowers:requesting-code-review`, and
  `superpowers:finishing-a-development-branch`

### Requirement: Superpowers use distinct recommendation wording
The template SHALL use `Использовать` wording for Superpowers recommendations
instead of the `Вызвать` wording used for ordinary skills.

#### Scenario: Codex recommends a Superpower
- **WHEN** Codex recommends a supported Superpower
- **THEN** the recommendation renders a `**== РЕКОМЕНДАЦИЯ ==**` block, uses
  `Использовать <superpower>`, and asks `Использовать?` with `**Да / Нет**`
  choices

#### Scenario: Codex recommends an ordinary skill
- **WHEN** Codex recommends a non-Superpowers skill
- **THEN** the recommendation uses `Вызвать <skill>` and asks `Выполнить?` with
  `**Да / Нет**` choices

#### Scenario: User accepts recommended Superpower
- **WHEN** the user accepts a recommended Superpowers step inside an OpenSpec
  workflow
- **THEN** Codex runs the Superpowers step, returns to the active OpenSpec workflow
  after the step finishes, and preserves the workflow's final
  `**== УРОКИ ==**` / `**== СЛЕДУЮЩИЙ ШАГ ==**` footer output
