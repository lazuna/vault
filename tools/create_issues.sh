i#!/bin/bash
# Script to batch-create GitHub issues using GitHub CLI (`gh`)
# Run this from inside the vault repository root

# Exit on error
set -e

echo "Creating issues..."

gh issue create --title "Refine folder-level README.md files" --body "Refine README.md in knowledge/, projects/, growth/, and meta/" --label "area:infra,type:documentation"
gh issue create --title "Document file/folder naming conventions" --body "Define standards in meta/structure.md" --label "area:infra,type:standard"

gh issue create --title "Add Python test workflow" --body "Create .github/workflows/test-python.yml for pytest or unittest integration" --label "area:ci,type:automation,priority:high"
gh issue create --title "Add Go test workflow" --body "Create .github/workflows/test-go.yml for Go test runner" --label "area:ci,type:automation"
gh issue create --title "Add release pipeline" --body "Setup release automation in .github/workflows/release.yml including changelog generation" --label "area:ci,type:release"
gh issue create --title "Add PR/Issue auto-labeler" --body "Use .github/workflows/auto-label.yml to label PRs and issues based on file paths or content" --label "area:ci,type:workflow"

gh issue create --title "Add pre-commit hook config" --body "Setup .pre-commit-config.yaml for all linters" --label "area:lint,type:devx"
gh issue create --title "Add commit linting config" --body "Add commitlint.config.js to enforce conventional commits" --label "area:git,type:standard"
gh issue create --title "Setup changelog generator" --body "Configure cz or standard-version for automated changelog" --label "area:git,type:release"

gh issue create --title "Write growth roadmap" --body "Document growth/roadmap.md outlining skills, goals, and trajectory" --label "area:growth,type:reflection"
gh issue create --title "Write strategic visibility doc" --body "Create growth/strategy.md reflecting long-term public goals" --label "area:growth,type:strategy"
gh issue create --title "Document vault identity posture" --body "Write meta/identity.md for tone, intent, and narrative posture" --label "area:meta,type:vision"

gh issue create --title "Write alert evaluator scaffold" --body "Implement evaluator.py in notify/ for rule interpretation" --label "area:notify,type:code"
gh issue create --title "Create dynamic rule patterns" --body "Write example alerting rules in notify/alerts.md" --label "area:notify,type:example"
gh issue create --title "Design modal config" --body "Draft modal_config.yaml to define alert UI subscriptions" --label "area:notify,type:config"

gh issue create --title "Create detection-control template" --body "Write edr_template.yaml to define rule/control relationships" --label "area:edr,type:template"
gh issue create --title "Draft matrix design doc" --body "Create edr_matrix/matrix.md to outline detection mapping approach" --label "area:edr,type:design"
gh issue create --title "Add initial detection rules" --body "Write base Sigma-style rules in edr_matrix/rules/" --label "area:edr,type:detection"

gh issue create --title "Write maturity matrix doc" --body "Define levels and scoring axes in maturity_model/matrix.md" --label "area:maturity,type:strategy"
gh issue create --title "Create scoring template" --body "Build scoring_template.json or .xlsx for self-assessment" --label "area:maturity,type:template"

gh issue create --title "Add SECURITY.md" --body "Draft security policy and responsible disclosure info" --label "area:security,type:policy"
gh issue create --title "Add vuln scanner config" --body "Include Tenable or Mend config samples" --label "area:security,type:integration"
gh issue create --title "Create detection rule template" --body "Write first Sigma-style detection rule for vault" --label "area:security,type:detection"

gh issue create --title "Add public visibility doc" --body "Write vault-public.md to declare what is visible, what is not" --label "area:meta,type:policy"
gh issue create --title "Create contributor docs" --body "Add CONTRIBUTING.md and CODE_OF_CONDUCT.md" --label "area:infra,type:community"
gh issue create --title "List open source targets" --body "Create a list of repos for external contributions (Sigma, osv, Trivy)" --label "area:meta,type:visibility"

echo "All issues created successfully."

