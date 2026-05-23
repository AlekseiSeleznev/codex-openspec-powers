# AGENTS.md

This project is Codex OpenSpec Powers, a Codex-native OpenSpec workflow kit.

- Do not silently overwrite project-owned OpenSpec content. Preserve
  `openspec/changes/`, `openspec/specs/`, existing schema choices, source code,
  tests, and product documentation unless the user explicitly asks for changes.
- Treat `.codex/codex-openspec-powers/manifest.yaml` as the ownership model for
  overlay repair. Specific template-owned file entries override containing
  merge-review directories; user-added files in merge-review directories are
  preserved.
- For `/opsx:apply`, read proposal, specs, design, and tasks from the OpenSpec
  change before modifying code. Update `tasks.md` checkboxes only after the
  corresponding work is actually complete.
- Optional skills require recommendation and user consent. When one or more
  optional steps apply, show one grouped `**== РЕКОМЕНДАЦИЯ ==**` block with
  numbered items, `Что выполнить?`, and answer options `1`, comma-separated
  sequences such as `1,2`, `+`, and `-`. Ordinary skills use `Вызвать` and
  `Выполнить?`; Superpowers use `Использовать` and `Использовать?`. Keep
  `**Да / Нет**` compatibility visible.
- Superpowers are optional external accelerators, not vendored project skills.
  Run `superpowers:*` recommendations only when the Superpowers plugin is
  available; if it is unavailable, report that and continue the OpenSpec
  workflow without treating it as a blocker.
- End completed user-facing OpenSpec workflow steps with `**== УРОКИ ==**`
  followed by `**== СЛЕДУЮЩИЙ ШАГ ==**`.
- If a recommended skill, Superpowers step, or review tool is accepted and run
  inside an OpenSpec workflow, return to the active workflow afterward and still
  end the user-facing response with `**== УРОКИ ==**` followed by
  `**== СЛЕДУЮЩИЙ ШАГ ==**`.
- Use `/opsx:check-overlay` after `openspec init --tools codex`, OpenSpec
  upgrades, or suspected generated-file overwrites.
- Claude OpenSpec Review is OFF by default. It may run only through the
  `/opsx:claude-review` controls or workflow gates when enabled.
- Claude review must use an isolated temporary bundle containing only relevant
  OpenSpec markdown/config files. Never pass the repository root or broad globs
  to Claude by default.
- Show Claude budgets before review. Save outputs under
  `openspec/changes/<change>/reviews/`.
- Claude never writes project files directly. Codex may apply safe doc-only
  fixes only after policy checks and user consent when required.
- Unresolved Critical/High Claude findings block apply/archive. Turning Claude
  review OFF does not clear unresolved blockers.
