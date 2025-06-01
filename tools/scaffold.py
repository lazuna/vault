from pathlib import Path
import shutil

# === CONFIGURATION ===
base_path = Path("vault")  # This can be relative or absolute

# Folder and file structure to scaffold
structure = {
    "knowledge": {},
    "projects": {},
    "growth": {},
    "meta": {
        "changelog.md": "",
    },
    ".github": {
        "CONTRIBUTING.md": "# Contributing Guidelines\n\nPlease follow the rules.",
        "COMMIT_CONVENTIONS.md": "# Commit Conventions\n\nUse conventional commits.",
        "BRANCHING_STRATEGY.md": "# Branching Strategy\n\nFollow GitHub flow.",
        "PULL_REQUEST_TEMPLATE.md": "# Pull Request\n\n## Description\n\n<!-- Please include a summary -->",
        "ISSUE_TEMPLATE": {
            "bug_report.md": "# Bug Report\n\n## Describe the bug\nA clear description of the issue.",
            "feature_request.md": "# Feature Request\n\n## Proposal\nDescribe the new feature."
        },
        "workflows": {
            "ci.yml": """name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 .
"""
        }
    }
}

# Dotfile linter configs
dotfiles = {
    ".flake8": "[flake8]\nmax-line-length = 88\nexclude = .git,__pycache__,.venv",
    ".eslintrc.json": '{ "env": { "browser": true, "es2021": true }, "extends": "eslint:recommended" }',
    ".stylelintrc.json": '{ "extends": "stylelint-config-standard" }',
    ".yamllint.yml": "extends: default\nrules:\n  line-length: disable",
    ".clang-format": "BasedOnStyle: Google\nIndentWidth: 4"
}

# README and LICENSE
readme = """# 🧠 vault

A curated vault of technical knowledge, real-world projects, and personal growth insights — built for mastery, maintained for clarity.

## 📁 Structure

- `knowledge/` — Technical deep-dives on backend, frontend, cloud, system design, etc.
- `projects/` — Hands-on code examples and blueprints
- `growth/` — Communication, leadership, productivity, and career guides
- `meta/` — Templates, changelogs, contribution guidelines

## 🛡 License

- **Code and Templates**: MIT License (`LICENSE`)
- **Documentation and Notes**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

> Attribution required. Commercial use of notes not permitted without consent.
"""

license_text = """MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy...
"""

# === FUNCTIONS ===

def create_structure(base, struct):
    for name, contents in struct.items():
        path = base / name
        try:
            if isinstance(contents, dict):
                path.mkdir(parents=True, exist_ok=True)
                create_structure(path, contents)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists():
                    path.write_text(contents)
        except Exception as e:
            print(f"Error creating {path}: {e}")

# === EXECUTION ===
base_path.mkdir(parents=True, exist_ok=True)
create_structure(base_path, structure)

# Write dotfiles
for filename, content in dotfiles.items():
    path = base_path / filename
    if not path.exists():
        path.write_text(content)

# Write readme and license
(base_path / "README.md").write_text(readme)
(base_path / "LICENSE").write_text(license_text)

# Optional: zip output
shutil.make_archive("vault-foundation", "zip", base_path)

"✅ vault scaffold created and zipped successfully."

