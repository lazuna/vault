#!/usr/bin/env python3

# tools/update_phase_index.py
# Auto-generates or updates _index.yaml files inside cycle/ folders

import os
import yaml

CYCLE_DIR = "cycle"


def phase_title(phase_folder):
    return phase_folder.replace("_", " ").title()


def ensure_index_file(phase_path):
    index_file = os.path.join(phase_path, "_index.yaml")
    phase_id = os.path.basename(phase_path)

    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            try:
                data = yaml.safe_load(f) or {}
            except Exception:
                data = {}
    else:
        data = {}

    updated = False

    if data.get("id") != phase_id:
        data["id"] = phase_id
        updated = True

    if data.get("title") != phase_title(phase_id):
        data["title"] = phase_title(phase_id)
        updated = True

    if updated:
        with open(index_file, "w") as f:
            yaml.dump(data, f, sort_keys=False)
        print(f"✔ Updated: {index_file}")
    else:
        print(f"✓ Already OK: {index_file}")


def main():
    if not os.path.isdir(CYCLE_DIR):
        print("❌ No cycle/ directory found.")
        return

    for phase in sorted(os.listdir(CYCLE_DIR)):
        phase_path = os.path.join(CYCLE_DIR, phase)
        if os.path.isdir(phase_path):
            ensure_index_file(phase_path)


if __name__ == "__main__":
    main()
