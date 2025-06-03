# 🤝 Contributing to `vault`

Welcome — this repository is open to thoughtful, security-aligned contributions.

## 🧭 Principles

- Design with purpose: Security, maturity, and clarity
- Prefer strategy over speed: Think in terms of control and signal
- Respect identity: This repo models a future CISO path

## 🛠 Contribution Flow

1. Fork the repo
2. Create a branch:
    > git checkout -b feat/edr-dns-detection
3. Commit using our [Commit Conventions](./COMMIT_CONVENTIONS.md)
4. Push and open a Pull Request using our [PR Template](./PULL_REQUEST_TEMPLATE.md)
5. Add appropriate **labels**:
- `type:policy`, `area:edr`, `type:design`, `priority:high`

## 📌 What You Can Contribute

| Area        | Examples                                   |
|-------------|--------------------------------------------|
| **Security**| Detection logic, control designs           |
| **Docs**    | Design notes, architecture, meta content   |
| **Infra**   | CI/CD, workflows, linting                  |
| **Growth**  | Strategy, maturity models, roadmaps        |
| **Code**    | Actual implementations (e.g., notify tool) |

## ✅ Checklist

- [ ] Linted your code or YAML (`pre-commit` recommended)
- [ ] Used conventional commits
- [ ] Linked issues (where applicable)
- [ ] PR includes security or purpose notes (see below)

## 🧠 Guidance for Review

When reviewing or submitting code:
- Can this be explained to a future CISO?
- Is the risk posture better now than before?
- Will this make it easier to scale or delegate?
