---
description: Verify implementation against OpenSpec artifacts
---

Verify implementation against proposal, specs, design, and tasks.

Steps:

1. Select the change.
2. Run `openspec instructions apply --change "<name>" --json`.
3. Read all context files.
4. Check task completion, requirement coverage, scenario coverage, design
   coherence, and relevant tests/checks.
5. If Claude OpenSpec Review is enabled, prepare archive-readiness review after
   local verification passes.

**== РЕВЬЮ CLAUDE ==**

If enabled and local verification has no critical blockers, run
`/opsx:claude-review run <change> archive-readiness`. Save review output and
preserve unresolved Critical/High findings as archive blockers.

Optional recommendations:

Recommendation selection rule:

- Evaluate all candidates as the workflow reaches their condition.
- Render at most one user-facing `**== РЕКОМЕНДАЦИЯ ==**` block for the current
  decision point; do not render one block per candidate.
- Treat candidates as complementary stages. If two candidates overlap, choose
  the earliest useful stage now and put later-stage work under `Позже`.
- Use `superpowers:verification-before-completion` before completion claims;
  use `grill-with-docs` for artifact/design ambiguity; use code review when a
  broad change needs a second pass before archive.
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

1. Вызвать `grill-with-docs` - use when verification finds design ambiguity or
   the change spans multiple OpenSpec capabilities.
2. Использовать `superpowers:verification-before-completion` - use before
   claiming the implementation is complete.
3. Использовать `superpowers:requesting-code-review` - use when the change is
   broad or should receive a second pass before archive.

If an optional recommendation is accepted and the recommended skill, Superpowers step, or review tool runs, return to this OpenSpec workflow after it finishes and still finish the user-facing response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the next OpenSpec step, accounting for selected or
skipped optional recommendations, Claude review status, and any outcome from
the selected steps.

```text
/opsx:archive <change>
```

Выполнить?

**Да / Нет**
