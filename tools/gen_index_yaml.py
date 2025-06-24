#!/usr/bin/env python3
import os
import yaml
from datetime import date

# === Settings ===
IGNORE_DIRS = {".git", ".github", ".venv", "__pycache__", "tools"}
VALID_EXTS = {".yaml", ".yml", ".md", ".py", ".sh", ".ts", ".js"}
DEFAULT_DESCRIPTIONS = {
    "growth": "Tracks personal growth, CISO track planning, and progress metrics.",
    "projects": "Hands-on tools, experiments, and PoC implementations.",
    "meta": "System-wide metadata, changelogs, and philosophy of Vault.",
    "knowledge": "Primary knowledge base, organized by technical domain.",
    "certifications": "Certification notes, references, and coverage mapping.",
}


# === Helpers ===
def infer_title(folder_name):
    return folder_name.replace("_", " ").title()


def infer_description(path):
    base = os.path.basename(path)
    if base in DEFAULT_DESCRIPTIONS:
        return DEFAULT_DESCRIPTIONS[base]
    elif "cloud" in base:
        return "Cloud-native security and DevOps tools."
    elif "linux" in base:
        return "Linux usage, hardening, and system operations."
    elif "network" in base:
        return "Networking essentials, tunneling, and debugging techniques."
    elif "threat" in base:
        return "Threat intel, offensive tooling, and red-team notes."
    else:
        return "Technical artifacts and documentation."


def get_relevant_files(path):
    return sorted(
        [
            f
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
            and os.path.splitext(f)[1] in VALID_EXTS
            and not f.startswith("_")
        ]
    )


def generate_index_yaml(dir_path):
    base = os.path.basename(dir_path)
    index = {
        "title": infer_title(base),
        "description": infer_description(dir_path),
        "tags": ["vault", "index", base],
        "updated": str(date.today()),
        "contents": get_relevant_files(dir_path),
    }
    return index


# === Main ===
def main():
    root = os.getcwd()
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip ignored directories
        if any(ignored in dirpath.split(os.sep) for ignored in IGNORE_DIRS):
            continue

        index_path = os.path.join(dirpath, "_index.yaml")
        index_data = generate_index_yaml(dirpath)
        with open(index_path, "w") as f:
            yaml.dump(index_data, f, sort_keys=False, allow_unicode=True)
            print(f"[+] Updated: {index_path}")


if __name__ == "__main__":
    main()
