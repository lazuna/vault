#!/bin/sh

# List of labels and their descriptions (flat list: label1 desc1 label2 desc2 ...)
labels=(
  "area:infra" "Infra and scaffolding tasks"
  "area:ci" "CI/CD-related issues"
  "area:lint" "Linter setup/config"
  "area:git" "Git conventions, commit style, changelog"
  "area:growth" "Career, roadmap, strategy docs"
  "area:meta" "Vault philosophy, visibility, policy"
  "area:notify" "Notify tool development"
  "area:edr" "Detection control and EDR mapping"
  "area:maturity" "Maturity model design and scoring"
  "area:security" "Security policy, rules, and tooling"

  "type:documentation" "README, scaffolding, docs"
  "type:standard" "Guidelines, lint, naming"
  "type:automation" "CI/CD or workflow automation"
  "type:release" "Release config or changelog automation"
  "type:devx" "Developer experience improvements"
  "type:reflection" "Growth, introspection tasks"
  "type:strategy" "Vision, narrative, roadmap"
  "type:code" "Actual implementation tasks"
  "type:example" "Sample configs, illustrative code"
  "type:config" "Configuration files"
  "type:template" "YAML/JSON scaffolds, starter formats"
  "type:design" "Design-oriented issues"
  "type:detection" "Detection logic or rules"
  "type:policy" "Policy and governance-related work"
  "type:integration" "External tool integration"
  "type:community" "CONTRIBUTING.md, CODE_OF_CONDUCT.md"
  "type:visibility" "Open source presence, contributor targeting"

  "priority:high" "Must-do/high-impact"
)

i=0
while [ $i -lt ${#labels[@]} ]; do
  label="${labels[$i]}"
  desc="${labels[$((i + 1))]}"

  if gh label list | grep -q "^$label"; then
    echo "↳ Label '$label' already exists, skipping."
  else
    if gh label create "$label" --description "$desc" --color "ededed"; then
      echo "✓ Created label: $label"
    else
      echo "✗ Failed to create: $label"
    fi
  fi

  i=$((i + 2))
done

