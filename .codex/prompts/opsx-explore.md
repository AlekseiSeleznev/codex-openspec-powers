---
description: Explore ideas, problems, and requirements without implementation
---

Enter exploration mode. Think with the user, inspect files when useful, and do
not implement application changes.

Allowed work:

- Read code and OpenSpec artifacts.
- Compare options and tradeoffs.
- Draw ASCII or Mermaid diagrams.
- Create or update OpenSpec artifacts only when the user asks to capture the
  exploration.

Optional recommendations:

Recommendation selection rule:

- Evaluate all candidates as the workflow reaches their condition.
- Render at most one user-facing `**== РЕКОМЕНДАЦИЯ ==**` block for the current
  decision point; do not render one block per candidate.
- Treat candidates as complementary stages. If two candidates overlap, choose
  the earliest useful stage now and put later-stage work under `Позже`.
- Use `superpowers:brainstorming` for unclear ideas before OpenSpec artifacts
  exist, `c4-diagrams` for boundaries or runtime relationships, and
  `grill-with-docs` only after proposal, design, documentation, or code context
  exists.
- Do not silently omit listed recommendations. Include applicable candidates as
  numbered items; include relevant but premature candidates under `Позже` with
  one concise reason; omit truly irrelevant candidates only with a concise skip
  reason.
- When applicability is uncertain, include the candidate as a numbered item.
- The grouped block must begin with `Есть необязательные шаги, которые могут
  помочь на этом этапе:`.
- The user-facing block must ask `Что выполнить?` and then render
  `Ответьте одним из вариантов:`.
- Render answer choices with circle bullets. For one candidate show 1, +,
  and -; for two candidates show 1, 2, 1,2, +, and -; for three or
  more candidates show 1, 2, 3, one sequence example such as 1,3, +,
  and -.
- The visible answer list must use labels like ○ 1, ○ 1,2, ○ +, and ○ -.
- Use + as the canonical answer for all recommended steps and - as the
  canonical answer for no optional steps. For compatibility, Да means +,
  Нет means -, всё means +, and ничего means -.
- Use `Вызвать` / `Выполнить?` wording for ordinary skills and `Использовать` /
  `Использовать?` wording for Superpowers. Keep `**Да / Нет**` visible in the
  grouped block.
- Use this rendered shape. Adapt numbered items to currently applicable
  candidates; do not render sample text as a real recommendation:

```text
**== РЕКОМЕНДАЦИЯ ==**

Есть необязательные шаги, которые могут помочь на этом этапе:

1. Использовать `superpowers:brainstorming` - уточнить идею, выбрать подход и
   сузить срез работы.
2. Вызвать `c4-diagrams` - разобрать границы, компоненты, связи и потоки данных.

Позже:
- Вызвать `grill-with-docs` - вернуться после появления proposal/design/docs.

Рекомендуемый порядок: 1 -> 2.

Что выполнить? (`Выполнить?` / `Использовать?`)
Ответьте одним из вариантов:

○ 1: выполнить только первый шаг
○ 2: выполнить только второй шаг
○ 1,2: выполнить выбранные шаги в указанном порядке
○ +: выполнить все рекомендованные шаги
○ -: ничего не выполнять

Совместимость с **Да / Нет**: Да = +, Нет = -.
```

Recommendation response handling rule:

- Wait for the user's answer before loading any optional skill, Superpowers
  step, or review tool from the grouped recommendation block.
- Interpret +, всё, and Да as all currently numbered recommended steps in the
  recommended order.
- Interpret -, ничего, and Нет as skipping all optional steps at this decision
  point.
- Interpret a single number as only that numbered step.
- Interpret comma-separated numbers as exactly those numbered steps in the
  user-provided order.
- Do not run items listed under `Позже` unless they are later shown as numbered
  recommendations at a new decision point.
- After selected steps finish, return to this OpenSpec workflow, do not repeat
  the same recommendation block unless new information changes the candidate
  set, and make `**== СЛЕДУЮЩИЙ ШАГ ==**` account for the user's choice and any
  outcome from the selected steps.

Explore-specific guidance:

- A new feature idea, unclear scope, or multiple plausible implementation
  directions counts as ambiguous enough to recommend
  `superpowers:brainstorming`.
- Runtime structure, UI-to-state boundaries, rendering loops, data flow, input
  handling, or component relationships count as runtime relationships for
  `c4-diagrams`.
- `grill-with-docs` requires useful proposal, design, project documentation, or
  code context. If those artifacts are absent, state that it is not recommended
  yet instead of silently omitting it.

Recommendation candidates:

1. Вызвать `c4-diagrams` - use when the exploration is about architecture
   boundaries or runtime relationships.
2. Вызвать `grill-with-docs` - use when a proposal or design needs focused
   stress-testing against project documents.
3. Использовать `superpowers:brainstorming` - use when the problem is ambiguous
   and divergent thinking would help.

If an optional recommendation is accepted and the recommended skill, Superpowers step, or review tool runs, return to this OpenSpec workflow after it finishes and still finish the user-facing response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the next OpenSpec step, accounting for selected or
skipped optional recommendations and any outcome from the selected steps.

```text
/opsx:new <change>
```

Выполнить?

**Да / Нет**
