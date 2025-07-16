#!/bin/bash

# tools/init_topic.sh
# Usage: ./tools/init_topic.sh <topic-name>
# Must be run inside the submodule root (e.g., vault-pqc)

set -e

TOPIC="$1"
DATE=$(date '+%Y-%m-%d')

if [ -z "$TOPIC" ]; then
  echo "Usage: $0 <topic-name>"
  exit 1
fi

echo ">>> [vault-init] Initializing topic: $TOPIC"

# Define all 7 cycle phases
PHASES=(
  "01_context"
  "02_basics"
  "03_detections"
  "04_mappings"
  "05_response"
  "06_automation"
  "07_outputs"
)

# Scaffold the cycle/ folder structure
mkdir -p cycle
for PHASE in "${PHASES[@]}"; do
  mkdir -p "cycle/$PHASE"
  if [ ! -f "cycle/$PHASE/_index.yaml" ]; then
    echo "id: $PHASE" > "cycle/$PHASE/_index.yaml"
    echo "title: ${PHASE//_/ }" >> "cycle/$PHASE/_index.yaml"
    echo "description: Auto-generated phase index for $PHASE" >> "cycle/$PHASE/_index.yaml"
  fi
done

# Generate context file from template
TEMPLATE="cycle/01_context/context_template.yaml"
TARGET="cycle/01_context/${TOPIC}.yaml"

if [ -f "$TEMPLATE" ]; then
  cp "$TEMPLATE" "$TARGET"
else
  cat > "$TARGET" <<EOF
topic: $TOPIC
version: 1.0
status: draft
maintainer: ragverus
last_updated: $DATE

why_it_matters:
  - TODO: Fill in strategic importance of $TOPIC

objectives:
  - TODO: Define what this module aims to accomplish

target_audience:
  - TODO: Who is this for?

cycle_plan:
  basics: []
  detections: []
  mappings: []
  response: []
  automation: []
  outputs: []

tags:
  - #next
  - #flow
  - #ciso-track
EOF
fi

echo "✔ Created context file: $TARGET"

# Create meta/ folder and files
mkdir -p meta

cat > meta/meta.yaml <<EOF
topic: $TOPIC
description: $TOPIC module for CISO-cycle
maintainer: ragverus
status: draft
created: $DATE
EOF

cat > meta/tags.yaml <<EOF
tags:
  - "#next"
  - "#flow"
  - "#wrap"
  - "#vault"
  - "#ciso-track"
EOF

cat > meta/version.yaml <<EOF
version: 0.1.0
last_updated: $DATE
EOF

cat > meta/cycle_tracker.yaml <<EOF
$TOPIC:
  context: complete
  basics: pending
  detections: pending
  mappings: pending
  response: pending
  automation: pending
  outputs: pending
EOF

echo "✔ Meta folder initialized under meta/"

echo ">>> [vault-init] Topic scaffold complete. You may now populate content in cycle/*/"

