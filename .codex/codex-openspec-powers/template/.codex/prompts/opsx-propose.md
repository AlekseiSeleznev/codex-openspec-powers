---
description: Create proposal, specs, design, and tasks in one guided pass
---

Create a complete OpenSpec artifact set for a new change.

Steps:

1. Resolve the change name or description.
2. Create the change with `openspec new change "<name>"`.
3. Repeatedly run `openspec status --change "<name>" --json` and
   `openspec instructions <artifact-id> --change "<name>" --json`.
4. Read dependency artifacts before creating the next artifact.
5. Create artifacts until `applyRequires` are complete.
6. If Claude OpenSpec Review is enabled, run the `propose` stage after artifact
   creation.

Do not add OpenSpec `context` or `rules` blocks into artifacts. Apply them as
constraints.

Optional recommendations:

Recommendation selection rule:

- Evaluate all candidates as the workflow reaches their condition.
- Render at most one user-facing `**== РЕКОМЕНДАЦИЯ ==**` block for the current
  decision point; do not render one block per candidate.
- Treat candidates as complementary stages. If two candidates overlap, choose
  the earliest useful stage now and put later-stage work under `Позже`.
- Use `grill-with-docs` after proposal/design context exists; use
  `superpowers:writing-plans` when execution sequencing is the current problem,
  not as a replacement for document-aware review.
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
- The visible answer list must use labels like ○ 1, ○ 1,3, ○ +, and ○ -.
- Use + as the canonical answer for all recommended steps and - as the
  canonical answer for no optional steps. For compatibility, Да means +,
  Нет means -, всё means +, and ничего means -.
- Use `Вызвать` / `Выполнить?` wording for ordinary skills and `Использовать` /
  `Использовать?` wording for Superpowers. Keep `**Да / Нет**` visible in the
  grouped block.
- Use this rendered shape. Replace the sample items with currently applicable
  candidates; do not render sample text as a real recommendation:

```text
**== РЕКОМЕНДАЦИЯ ==**

Есть необязательные шаги, которые могут помочь на этом этапе:

1. Вызвать `c4-diagrams` - пример обычного навыка.
2. Использовать `superpowers:brainstorming` - пример Superpowers.

Позже:
- Вызвать `grill-with-docs` - пример шага для более позднего момента.

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

Recommendation candidates:

1. Вызвать `grill-with-docs` - use when the proposal changes prompts, skills,
   installation behavior, multiple capabilities, or durable architecture
   decisions.
2. Вызвать `architectural-decision-records` - use when the design records a
   durable architecture or workflow decision.
3. Использовать `superpowers:writing-plans` - use when artifact creation spans
   prompts, skills, docs, config, and verification work.

Claude gate:

**== РЕВЬЮ CLAUDE ==**

If enabled, run `/opsx:claude-review run <change> propose`. Save review output,
handle budget/pre-call failures, and resolve or record Critical/High findings
before presenting the next step.

If an optional recommendation is accepted and the recommended skill, Superpowers step, or review tool runs, return to this OpenSpec workflow after it finishes and still finish the user-facing response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the next OpenSpec step, accounting for selected or
skipped optional recommendations, Claude review status, and any outcome from
the selected steps.

```text
/opsx:apply <change>
```

Выполнить?

**Да / Нет**
