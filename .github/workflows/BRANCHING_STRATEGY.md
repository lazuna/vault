# 🪢 Branching Strategy

This repository follows a strategic Git model focused on traceability, risk isolation, and audit clarity.

## 🧭 Main Branches

| Branch     | Purpose                                  |
|------------|------------------------------------------|
| `main`     | Stable, production-ready code            |
| `develop`  | Integration branch for features/patches  |

## 🌱 Feature & Topic Branches

Use the following format: <type>/<area>-<short-summary>

### Examples
- `feat/notify-alert-throttling`
- `fix/lint-prettier-config`
- `docs/meta-contribution-guide`
- `policy/edr-file-modification`

Use these **prefixes**:
- `feat/` – New features
- `fix/` – Bug fixes
- `docs/` – Documentation changes
- `policy/` – Security or governance logic
- `infra/` – Tooling, automation, CI/CD

## 🔁 Merging Rules

- PRs to `main`: Reviewed, tested, changelog included
- PRs to `develop`: Staging zone for QA/stability checks
- Fast-forward merges only (default, enforced via GitHub settings)
- Feature branches deleted post-merge

## 🏷 Suggested Labels for PRs
- `type:code`, `type:design`, `type:automation`, `type:policy`
- `area:<component>` for traceability

