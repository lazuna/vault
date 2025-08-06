#!/bin/bash

set -euo pipefail

echo "==> Starting repo restructure based on 'cycle/' directory philosophy..."

move_dir_contents() {
  local src=$1
  local dest=$2

  mkdir -p "$dest"

  if [ -d "$src" ]; then
    echo "→ Moving contents of $src to $dest"
    shopt -s dotglob nullglob
    for item in "$src"/*; do
      git mv "$item" "$dest/" 2>/dev/null || mv "$item" "$dest/"
    done
    rmdir "$src" 2>/dev/null || true
  fi
}

move_single_file() {
  local src=$1
  local dest=$2
  mkdir -p "$(dirname "$dest")"
  if [ -f "$src" ]; then
    git mv "$src" "$dest" 2>/dev/null || mv "$src" "$dest"
    echo "✔ Moved '$src' → '$dest'"
  fi
}

# Move knowledge under 02_basics
move_dir_contents "knowledge" "cycle/02_basics/knowledge"

# Move recon-lab project
move_dir_contents "projects/recon-lab" "cycle/03_detections/labs/recon-lab"

# Move evaluator project
move_dir_contents "projects/evaluator" "cycle/05_response/tools/evaluator"

# Move soft-systems
move_dir_contents "soft-systems" "cycle/01_context/soft_systems"

# Move architecture
move_dir_contents "meta/architecture" "cycle/01_context/architecture"

# Move scaffold_recon.py
move_single_file "tools/scaffold_recon.py" "cycle/03_detections/tools/scaffold_recon.py"

# Move init_*.sh scripts
for script in tools/init_*.sh; do
  [ -e "$script" ] || continue
  move_single_file "$script" "tools/init/$(basename "$script")"
done

echo "==> Restructure complete. Review with 'git status' or 'git diff --name-status'"

