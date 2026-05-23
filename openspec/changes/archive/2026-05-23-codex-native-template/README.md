# codex-native-template

Implement Codex OpenSpec Powers as a Codex-native workflow kit for existing
OpenSpec projects.

Kept OpenSpec artifacts:

- `.openspec.yaml`: OpenSpec-generated change metadata; kept as tool state, not
  as a template overlay artifact.
- `proposal.md`: change purpose and scope.
- `design.md`: design decisions and ownership model.
- `tasks.md`: implementation checklist.
- `specs/*/spec.md`: delta requirements for the Codex overlay, prompts, skills,
  healthcheck, Superpowers policy, installation, and Claude review loop.

Process-only reviewer prompts were removed after implementation so the finished
repository contains only functional template files and the OpenSpec artifacts
needed to explain the implemented change.
