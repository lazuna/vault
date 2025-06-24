#!/bin/bash
# Auto-format Python using black, then run flake8

echo "[*] Formatting with black..."
black ./projects ./tools

echo "[*] Running flake8..."
flake8 ./projects ./tools

