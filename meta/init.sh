#!/bin/bash
# vault/meta/init.sh
# One-time setup for label scaffolding in the vault repo

set -e

echo ">>> Initializing vault metadata..."

## Define labels
declare -A labels=(
  ["area:infra"]="Infra and repo scaffolding"
  ["area:ci"]="CI/CD pipelines and workflows"
  ["area:lint"]="Linter setup and configuration"
  ["area:git"]="Git standards, commit style, changelog"
  ["area:growth"]="Growth, trajectory, strategic notes"
  ["area:meta"]="Vault identity, tone, visibility"
  ["area:notify"]="Notify tool development"
  ["area:edr"]="EDR detection-control architecture"
  ["area:maturity"]="Security maturity model design"
  ["area:security"]="Security rules, policy, tooling"
  ["type:documentation"]="README or documentation tasks"
  ["type:standard"]="Naming, formatting, guideline standards"
  ["type:automation"]="Workflow and CI automation"
  ["type:release"]="Release process and changelog"
  ["type:devx"]="Developer experience enhancements"
  ["type:reflection"]="Growth and self-reflection tasks"
  ["type:strategy"]="Strategic or directional items"
  ["type:code"]="Implementation and dev work"
  ["type:example"]="Sample configurations or use cases"
  ["type:config"]="YAML or tool config files"
  ["type:template"]="Starter scaffolds (YAML/JSON/etc.)"
  ["type:design"]="Design notes or decisions"
  ["type:detection"]="Detection logic, rules, mapping"
  ["type:policy"]="Security policy or process"
  ["type:integration"]="Tool or platform integrations"
  ["type:community"]="Contributing and community onboarding"
  ["type:visibility"]="External visibility or positioning"
  ["priority:high"]="High impact or time-sensitive"
)

## Create labels using GitHub CLI
for label in "${!labels[@]}"; do
  desc="${labels[$label]}"
  echo "Creating label: $label"
  gh label create "$label" --description "$desc" --color "ededed" 2>/dev/null || echo "↳ Label $label already exists."
done

echo ">>> Vault labels initialized."

