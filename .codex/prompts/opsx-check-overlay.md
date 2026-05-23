---
description: Check and safely repair the Codex codex-openspec-powers overlay
---

Inspect the Codex-native overlay and propose safe repair when generated files or
upgrades removed template-owned behavior.

Steps:

1. Read `.codex/codex-openspec-powers/manifest.yaml`.
2. Classify files using manifest ownership before proposing any repair.
3. Check required prompts before marker validation.
4. Check required markers, snippets, forbidden paths, optional skill consent
   policy, Superpowers policy, Claude review policy, and documentation
   freshness.
5. Report healthy state without writing files.
6. When repair is needed, show affected files and exact intended changes, then
   ask for confirmation before editing.

Repair must modify only manifest-listed template-owned additions or explicitly
approved merge-review paths. If the bundled template source is unavailable,
report the missing source and ask the user to re-apply the template.

**== РЕКОМЕНДАЦИЯ ==**

Repair the listed template-owned overlay additions.

Use this only after showing the planned repair scope and confirming it will not
overwrite project-owned content silently.

Выполнить?

**Да / Нет**

If an optional recommendation is accepted and the recommended skill, Superpowers step, or review tool runs, return to this OpenSpec workflow after it finishes and still finish the user-facing response with the blocks below.

Finish successful output with:

**== УРОКИ ==**

- 3-4 concise lessons from this step.

**== СЛЕДУЮЩИЙ ШАГ ==**

One-line rationale for the repair confirmation when issues exist, or for the
appropriate next OpenSpec workflow command when the installation is healthy.
If the installation is healthy, do not suggest `/opsx:check-overlay` again
unless the user explicitly asked to re-run the healthcheck.

```text
/opsx:new <change>
```

Выполнить?

**Да / Нет**
