---
description: Archive multiple completed OpenSpec changes
---

Archive multiple completed changes after reviewing status, tasks, and spec sync
state for each selected change.

Steps:

1. Run `openspec list --json`.
2. Ask the user to select two or more completed changes.
3. Gather status, task completion, delta specs, and spec conflicts.
4. Show the batch archive plan and ask for explicit confirmation.
5. After confirmation, run `openspec archive "<name>"` for each selected change
   in the planned order. Use `--skip-specs` for a selected change only when the
   user explicitly chooses to skip spec update operations.
6. Stop before the next archive if OpenSpec reports a spec conflict or another
   archive error, then report the completed and remaining changes.

This utility prompt does not require optional skill consent unless git-sensitive
follow-up work is requested.

If the user requests git-sensitive follow-up work and an optional
recommendation is accepted, return to this OpenSpec workflow after the
recommended skill, Superpowers step, or review tool finishes and still finish
the user-facing response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the next OpenSpec step.

```text
/opsx:check-overlay
```

Выполнить?

**Да / Нет**
