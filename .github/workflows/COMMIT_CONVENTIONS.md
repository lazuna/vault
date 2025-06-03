# 🧬 Commit Conventions

This repo uses **Conventional Commits** with scope labels to power changelogs, traceability, and security audits.

## Format
<type>(<scope>): <message>


### Examples
feat(notify): add alert filter for file changes
fix(ci): resolve YAML indent error in linter workflow
docs(meta): clarify vault mission and persona strategy
policy(edr): restrict script-based file writes


## Types

| Type    | Purpose                            |
|---------|------------------------------------|
| `feat`  | New functionality                  |
| `fix`   | Bug fix                            |
| `docs`  | Markdown/docs-only change          |
| `style` | Formatting, linting (no logic)     |
| `refactor` | Code change without behavior change |
| `test`  | Adding or fixing tests             |
| `chore` | Non-code task (e.g., deps, infra)  |
| `policy`| Security rules, control logic      |

## Scope

Use **component-level or strategic** scopes:
- `notify`, `ci`, `infra`, `meta`, `lint`, `edr`, `growth`, `maturity`

## Rules

- Use imperative mood: “Add”, not “Added”
- Wrap lines at 72 chars (body only)
- Include references in footer when needed:
    - Closes #42
    - Related to #99

## Tools
- Optional: Use `commitlint` with `husky` for local enforcement
-
