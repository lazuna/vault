---
name: "🐞 Bug Report"
about: Report a defect or unexpected behavior in the system
title: "[BUG] <short summary>"
labels: [bug, triage-needed]
assignees: ''

---

# 🐞 Bug Report

## 1. Summary
> Provide a clear and concise description of the issue, unexpected behavior, or failure.

## 2. Environment
> Specify the context where the bug was found. Helps reproduce and isolate impact.

- **Component/Module**: [e.g., `auth`, `scanner`, `policy-parser`]
- **Environment**: [e.g., `local`, `CI`, `prod-mirror`]
- **OS/Platform**: [e.g., Ubuntu 22.04, macOS 14, GitHub Actions]
- **Python/Node/Go Version**: [as applicable]

## 3. Steps to Reproduce
> List the steps required to consistently reproduce the issue.

```bash
# Example
1. Run `python vault/tools/scaffold.py`
2. Observe the output error stack

> ^^^ Suggested Labels:
- `area:infra`, `area:ci`, `area:security`, `area:notify`, etc.
- `type:code`, `type:automation`, `type:policy`, `type:config`
- `priority:high` (if it blocks core functions or security)
- `type:reflection` (if found during a retrospective or audit)
