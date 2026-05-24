---
description: Initialize a project with OpenSpec Codex and Codex OpenSpec Powers
---

Initialize the current project for Codex OpenSpec Powers.

Input may be empty or a target path. If empty, use the current workspace root.

Steps:

1. Run `opsx init` for the current workspace, or `opsx init "<path>"` when the
   user supplied an explicit path.
2. Confirm that the command completed successfully. It runs
   `openspec init --tools codex` and then non-interactive overlay repair.
3. Run `opsx doctor` in the initialized project to verify that template-owned
   prompts, skills, manifest files, and bundled repair sources are healthy.
4. Report what was initialized and whether auto-repair is active through the
   installed `openspec` shim.

Guardrails:

- Do not overwrite `openspec/changes/`, `openspec/specs/`, source code, tests,
  package files, or documentation outside the `opsx init`/repair ownership
  model.
- If `opsx init` or `opsx doctor` fails, stop and show the exact failing command
  and output. Do not continue into `/opsx:explore`.
- If the user supplied a path, make the next suggested command include that
  project context only when Codex can continue in that workspace.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this initialization step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for starting exploration now that the OpenSpec/Codex
foundation and overlay are installed.

```text
/opsx:explore <идея проекта>
```

Выполнить?

**Да / Нет**
