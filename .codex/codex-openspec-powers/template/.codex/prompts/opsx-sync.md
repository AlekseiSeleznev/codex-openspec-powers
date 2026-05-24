---
description: Sync delta specs from an active change to main specs
---

Sync delta specs from `openspec/changes/<change>/specs/*/spec.md` into
`openspec/specs/*/spec.md` without archiving the change.

Steps:

1. Select a change with delta specs.
2. Read each delta spec and corresponding main spec.
3. Apply ADDED, MODIFIED, REMOVED, and RENAMED requirements intelligently.
4. Preserve main-spec content not mentioned by the delta.
5. Summarize updated capabilities.

This utility prompt does not require optional skill consent unless the user asks
for a broader git-sensitive operation.

If the user requests a broader follow-up and an optional recommendation is
accepted, return to this OpenSpec workflow after the recommended skill,
Superpowers step, or review tool finishes and still finish the user-facing
response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the next OpenSpec step.

```text
/opsx:archive <change>
```

Выполнить?

**Да / Нет**
